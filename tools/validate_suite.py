#!/usr/bin/env python3
"""Check suite structure and parity; does not validate generated RTL or UVM."""
import ast
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def validate_metadata(path, name):
    """Validate this suite's deliberately restricted interface-only YAML format.

    This is not a general YAML parser. Reject unsupported forms rather than
    accepting partially parsed metadata. Extend the schema before adding policy
    or dependency fields to the suite.
    """
    try:
        lines = path.read_text(encoding='utf-8').splitlines()
        if not lines or lines[0] != 'interface:':
            raise ValueError('expected interface mapping')
        fields = {}
        for line in lines[1:]:
            if not line.strip():
                continue
            match = re.fullmatch(r'  ([a-z_]+): (.+)', line)
            if not match or match[1] in fields:
                raise ValueError('invalid or duplicate interface field')
            value = json.loads(match[2])
            if not isinstance(value, str) or not value.strip():
                raise ValueError('expected nonempty quoted string')
            fields[match[1]] = value
        if set(fields) != {'display_name', 'short_description', 'default_prompt'}:
            raise ValueError('unexpected or missing interface fields')
        if not 25 <= len(fields['short_description']) <= 64:
            raise ValueError('short_description must be 25-64 characters')
        if '$' + name not in fields['default_prompt']:
            raise ValueError('default_prompt must mention the skill')
    except (OSError, ValueError) as exc:
        return f'{name}: invalid UI metadata: {exc}'
    return None

def validate(root):
    root = Path(root)
    errors = []
    a, b = root / '.agents/skills', root / '.claude/skills'
    def inventory(tree):
        return {p.relative_to(tree): p.read_bytes() for p in tree.rglob('*')
                if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
    left, right = inventory(a), inventory(b)
    if not left or left != right:
        errors.append('Paired skill trees are empty or differ')
    skills = sorted(a.glob('*/SKILL.md'))
    try:
        catalog = json.loads((root / 'tools/skill_catalog.json').read_text(encoding='utf-8'))
        names = catalog['skills']
        if (catalog.get('schema_version') != 1 or not isinstance(names, list)
                or not all(isinstance(n, str) for n in names)
                or len(names) != len(set(names)) or not names):
            raise ValueError('invalid catalog schema or duplicate skills')
        if set(names) != {p.parent.name for p in skills}:
            errors.append('Discovered skills do not match tools/skill_catalog.json')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'Invalid skill catalog: {exc}')
    rules = set()
    for path in skills:
        text = path.read_text(encoding='utf-8')
        parts = text.split('---', 2)
        if len(parts) != 3 or parts[0] != '':
            errors.append(f'{path.parent.name}: invalid frontmatter')
            continue
        header = {}
        for line in parts[1].strip().splitlines():
            key, sep, value = line.partition(':')
            if not sep or key in header:
                errors.append(f'{path.parent.name}: invalid header field')
                continue
            header[key] = value.strip()
        name = header.get('name', '')
        if set(header) != {'name', 'description'} or name != path.parent.name or not re.fullmatch(r'[a-z0-9-]{1,64}', name):
            errors.append(f'{path.parent.name}: invalid name/fields')
        try:
            description = json.loads(header.get('description', ''))
            if not isinstance(description, str) or not description.strip():
                raise ValueError('empty description')
        except ValueError:
            errors.append(f'{name}: expected nonempty JSON-quoted YAML description')
        if '[TODO' in text or len(text.splitlines()) >= 500:
            errors.append(f'{name}: unfinished or oversized instructions')
        for doc in path.parent.rglob('*.md'):
            for label, target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', doc.read_text(encoding='utf-8')):
                if not target.startswith(('https://', 'http://', '#', 'mailto:')):
                    target_path = (doc.parent / target.split('#', 1)[0]).resolve()
                    if not target_path.is_file():
                        errors.append(f'{name}: broken link in {doc.name}: {target}')
        rule = path.parent / 'references/DV_RULES.md'
        if rule.exists():
            content = rule.read_bytes()
            rules.add(content)
            ids = re.findall(rb'^(DV-\d{3}) MUST', content, re.M)
            if sorted(ids) != [f'DV-{i:03}'.encode() for i in range(1, 21)]:
                errors.append(f'{name}: expected unique rules DV-001 through DV-020')
        else:
            errors.append(f'{name}: missing DV rules')
        metadata = path.parent / 'agents/openai.yaml'
        metadata_error = validate_metadata(metadata, name)
        if metadata_error:
            errors.append(metadata_error)
    if len(rules) != 1:
        errors.append('Bundled rule versions differ')
    for path in root.rglob('*.py'):
        try:
            ast.parse(path.read_text(), filename=str(path))
        except SyntaxError as exc:
            errors.append(str(exc))
    return errors, len(skills), len(left)

if __name__ == '__main__':
    errors, count, files = validate(ROOT)
    for error in errors:
        print('ERROR:', error)
    print(f'{count} skills per tool; {files} files per tree; {len(errors)} structural errors.')
    sys.exit(bool(errors))

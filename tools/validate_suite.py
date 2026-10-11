#!/usr/bin/env python3
"""Check suite structure and parity; does not validate generated RTL or UVM."""
import ast
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def validate(root):
    errors = []
    a, b = root / '.agents/skills', root / '.claude/skills'
    def inventory(tree):
        return {p.relative_to(tree): p.read_bytes() for p in tree.rglob('*')
                if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
    left, right = inventory(a), inventory(b)
    if not left or left != right:
        errors.append('Paired skill trees are empty or differ')
    skills = sorted(a.glob('*/SKILL.md'))
    if len(skills) != 11:
        errors.append(f'Expected 11 skills, found {len(skills)}')
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
        for label, target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text):
            if not target.startswith(('https://', 'http://', '#')):
                if not (path.parent / target).is_file():
                    errors.append(f'{name}: broken link {target}')
        rule = path.parent / 'references/DV_RULES.md'
        if rule.exists():
            content = rule.read_bytes()
            rules.add(content)
            if len(re.findall(rb'^DV-\d{3} MUST', content, re.M)) != 20:
                errors.append(f'{name}: expected 20 normative DV rules')
        metadata = path.parent / 'agents/openai.yaml'
        if not metadata.exists() or '$' + name not in metadata.read_text():
            errors.append(f'{name}: missing/inconsistent UI metadata')
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

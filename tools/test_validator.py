#!/usr/bin/env python3
"""Mutation tests for structural checks; no hardware or model behavior claims."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from validate_suite import ROOT, validate


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'suite'
        shutil.copytree(ROOT, self.root,
                        ignore=shutil.ignore_patterns('.git', '__pycache__', '*.pyc'))

    def mutate_both(self, relative, text):
        for tree in ('.agents', '.claude'):
            (self.root / tree / 'skills/vlsit-dv-debug' / relative).write_text(text, encoding='utf-8')

    def test_baseline(self):
        self.assertEqual(validate(self.root)[0], [])

    def test_broken_nested_reference(self):
        self.mutate_both('references/task.md', '[missing](absent.md)\n')
        self.assertTrue(any('broken link' in e for e in validate(self.root)[0]))

    def test_invalid_metadata_with_valid_skill_token(self):
        self.mutate_both('agents/openai.yaml', 'broken [ $vlsit-dv-debug\n')
        self.assertTrue(any('invalid UI metadata' in e for e in validate(self.root)[0]))

    def test_tree_drift(self):
        (self.root / '.claude/skills/vlsit-dv-debug/references/task.md').write_text('drift\n')
        self.assertTrue(any('trees' in e for e in validate(self.root)[0]))

    def test_catalog_mismatch(self):
        p = self.root / 'tools/skill_catalog.json'
        data = json.loads(p.read_text())
        data['skills'].append('vlsit-dv-missing')
        p.write_text(json.dumps(data))
        self.assertTrue(any('catalog' in e for e in validate(self.root)[0]))

    def test_missing_rules_without_link(self):
        for tree in ('.agents', '.claude'):
            p = self.root / tree / 'skills/vlsit-dv-debug'
            (p / 'references/DV_RULES.md').unlink()
            skill = p / 'SKILL.md'
            skill.write_text(skill.read_text().replace('[DV rules](references/DV_RULES.md)', 'DV rules'))
        self.assertTrue(any('missing DV rules' in e for e in validate(self.root)[0]))


if __name__ == '__main__':
    unittest.main(verbosity=2)

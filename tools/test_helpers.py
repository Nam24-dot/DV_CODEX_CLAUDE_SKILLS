#!/usr/bin/env python3
"""Synthetic contract tests; no simulator required."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / '.agents/skills/vlsit-dv-regression/scripts/summarize_runs.py'
spec = importlib.util.spec_from_file_location('summarize_runs', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class SummaryTests(unittest.TestCase):
    def setUp(self):
        self.row = dict(run_id='test_1', test='smoke', seed=1, configuration='default',
                        status='PASS', command=['sim', '+seed=1'], tool_version='fixture',
                        exit_code=0, log='fixture.log', reason='Synthetic fixture')
    def test_pass_and_nonpass(self):
        rows = [dict(self.row, run_id=str(i), status=status, reason='Synthetic reason')
                for i, status in enumerate(module.STATUSES)]
        result = module.summarize(rows)
        self.assertEqual(result['total_records'], 6)
        self.assertEqual(result['counts']['PASS'], 1)
        self.assertFalse(result['all_records_pass'])
        self.assertTrue(module.summarize([self.row])['all_records_pass'])
    def test_reject_invalid(self):
        invalid = [[], {}, [self.row, self.row]]
        for key, value in [('seed', True), ('seed', -1), ('command', 'sim'),
                           ('status', 'PASSED'), ('exit_code', True),
                           ('exit_code', 1), ('log', ''), ('command', []),
                           ('test', ''), ('reason', None)]:
            invalid.append([dict(self.row, **{key: value})])
        missing = copy.deepcopy(self.row)
        del missing['configuration']
        invalid.extend([[missing], [dict(self.row, status='FAIL', reason='')]])
        for case in invalid:
            with self.subTest(case=case), self.assertRaises(ValueError):
                module.summarize(case)
    def test_cli_roundtrip_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, target = Path(tmp)/'input.json', Path(tmp)/'out.json'
            source.write_text(json.dumps([self.row]))
            command = [sys.executable, str(SCRIPT), str(source), '--out', str(target)]
            first = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            original = target.read_bytes()
            second = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(second.returncode, 2)
            self.assertEqual(target.read_bytes(), original)
            source.write_text('{malformed')
            bad = subprocess.run([sys.executable, str(SCRIPT), str(source), '--out', str(Path(tmp)/'bad.json')], capture_output=True)
            self.assertEqual(bad.returncode, 2)
            self.assertFalse((Path(tmp)/'bad.json').exists())

if __name__ == '__main__':
    unittest.main(verbosity=2)

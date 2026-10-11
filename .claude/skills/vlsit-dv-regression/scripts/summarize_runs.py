#!/usr/bin/env python3
"""Validate normalized records, not simulator logs; aggregate recorded claims."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys

STATUSES = ('PASS', 'FAIL', 'NOT_RUN', 'UNSUPPORTED', 'INCONCLUSIVE', 'N/A')
REQUIRED = {'run_id', 'test', 'seed', 'configuration', 'status', 'command',
            'tool_version', 'exit_code', 'log', 'reason'}

def summarize(rows):
    if not isinstance(rows, list) or not rows:
        raise ValueError('Input must be a nonempty JSON array of run records')
    seen = set()
    for index, row in enumerate(rows):
        prefix = f'row {index}'
        if not isinstance(row, dict) or not REQUIRED.issubset(row):
            raise ValueError(f'{prefix}: missing required fields or not an object')
        for field in ('run_id', 'test', 'configuration', 'status', 'tool_version'):
            if not isinstance(row[field], str) or not row[field].strip():
                raise ValueError(f'{prefix}: {field} must be a nonempty string')
        if row['run_id'] in seen:
            raise ValueError(f'{prefix}: duplicate run_id {row["run_id"]}')
        seen.add(row['run_id'])
        if row['status'] not in STATUSES:
            raise ValueError(f'{prefix}: unknown status')
        if type(row['seed']) is not int or row['seed'] < 0:
            raise ValueError(f'{prefix}: seed must be a nonnegative integer')
        if not isinstance(row['command'], list) or any(not isinstance(x, str) or not x for x in row['command']):
            raise ValueError(f'{prefix}: command must be an array of nonempty strings')
        if row['exit_code'] is not None and type(row['exit_code']) is not int:
            raise ValueError(f'{prefix}: exit_code must be an integer or null')
        if not isinstance(row['log'], str) or not isinstance(row['reason'], str):
            raise ValueError(f'{prefix}: log and reason must be strings')
        if row['status'] == 'PASS':
            if row['exit_code'] != 0 or not row['log'].strip() or not row['command']:
                raise ValueError(f'{prefix}: PASS needs exit_code 0, log and command')
        elif not row['reason'].strip():
            raise ValueError(f'{prefix}: non-PASS status needs a reason')
    counts = Counter(row['status'] for row in rows)
    return {
        'schema_version': 1,
        'scope': 'Normalized claims only; logs and checker activity are not verified by this script.',
        'total_records': len(rows),
        'counts': {s: counts[s] for s in STATUSES},
        'all_records_pass': all(row['status'] == 'PASS' for row in rows),
        'non_pass_run_ids': [r['run_id'] for r in rows if r['status'] != 'PASS'],
        'runs': rows,
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = summarize(json.loads(args.input.read_text(encoding='utf-8')))
        with args.out.open('x', encoding='utf-8') as stream:
            json.dump(result, stream, indent=2)
            stream.write('\n')
    except (OSError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2
    print(f'Validated {result["total_records"]} recorded claims; not a sign-off decision.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

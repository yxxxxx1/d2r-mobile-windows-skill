#!/usr/bin/env python3
"""Read-only verifier for local D2R save backup manifests; Python 3.11+."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath, PureWindowsPath
import re
import sys


def verify_backup(manifest_path):
    manifest_path = Path(manifest_path).resolve(strict=True)
    root = manifest_path.parent
    manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
    if not isinstance(manifest, dict):
        raise ValueError('Manifest must be a JSON object')
    saves = manifest.get('saves')
    if not isinstance(saves, list) or not saves:
        raise ValueError('A nonempty saves list is required')
    seen = set()
    total = 0
    for item in saves:
        if not isinstance(item, dict):
            raise ValueError('Each save record must be an object')
        name = item.get('path')
        if not isinstance(name, str) or not name or '\\' in name:
            raise ValueError('Save paths must be relative and use forward slashes')
        relative = PurePosixPath(name)
        windows = PureWindowsPath(name)
        if (relative.is_absolute() or windows.drive or ':' in name
                or '..' in relative.parts or len(relative.parts) < 2
                or relative.parts[0] != 'save'
                or any(part in ('', '.', '..') for part in name.split('/'))):
            raise ValueError('Save path must stay within save/: ' + name)
        key = name.casefold()
        if key in seen:
            raise ValueError('Duplicate save path: ' + name)
        seen.add(key)
        size = item.get('bytes')
        sha = item.get('sha256')
        if type(size) is not int or size < 0:
            raise ValueError('Invalid byte count: ' + name)
        if not isinstance(sha, str) or re.fullmatch(r'[0-9a-fA-F]{64}', sha) is None:
            raise ValueError('Invalid SHA-256: ' + name)
        path = root.joinpath(*relative.parts).resolve(strict=True)
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError('Save resolves outside the backup or is not a file: ' + name)
        if path.stat().st_size != size:
            raise ValueError('Byte count mismatch: ' + name)
        with path.open('rb') as source:
            actual = hashlib.file_digest(source, 'sha256').hexdigest()
        if actual != sha.lower():
            raise ValueError('SHA-256 mismatch: ' + name)
        total += size
    return {'status': 'verified', 'save_files': len(saves), 'save_bytes': total}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path, help='Backup manifest next to the save/ folder')
    args = parser.parse_args()
    try:
        result = verify_backup(args.manifest)
    except (OSError, ValueError) as error:
        print(json.dumps({'status': 'failed', 'reason': str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

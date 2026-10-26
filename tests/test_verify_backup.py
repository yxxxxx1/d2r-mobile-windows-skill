import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / 'skills/d2r-mobile-windows/scripts/verify_backup.py'
spec = importlib.util.spec_from_file_location('verify_backup', MODULE)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class BackupChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = b'example local save\x00\x01'
        self.relative = 'save/角色/角色.d2s'
        self.file = self.root / self.relative
        self.file.parent.mkdir(parents=True)
        self.file.write_bytes(self.data)
        self.record = {'path': self.relative, 'bytes': len(self.data),
                       'sha256': hashlib.sha256(self.data).hexdigest()}
        self.manifest = self.root / 'backup-manifest.json'

    def write(self, records):
        self.manifest.write_text(json.dumps({'saves': records}, ensure_ascii=False), encoding='utf-8-sig')

    def test_valid_unicode_backup_is_unchanged(self):
        self.write([self.record])
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        result = checker.verify_backup(self.manifest)
        self.assertEqual(result['save_files'], 1)
        self.assertEqual(result['save_bytes'], len(self.data))
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_same_length_corruption_is_detected(self):
        self.write([self.record])
        self.file.write_bytes(b'X' * len(self.data))
        with self.assertRaisesRegex(ValueError, 'SHA-256 mismatch'):
            checker.verify_backup(self.manifest)

    def test_wrong_size_is_detected(self):
        self.write([{**self.record, 'bytes': len(self.data) + 1}])
        with self.assertRaisesRegex(ValueError, 'Byte count mismatch'):
            checker.verify_backup(self.manifest)

    def test_missing_file_is_detected(self):
        self.write([self.record])
        self.file.unlink()
        with self.assertRaises(FileNotFoundError):
            checker.verify_backup(self.manifest)

    def test_unsafe_paths_are_rejected(self):
        for path in ['../outside.d2s', 'save/../../outside.d2s', '/save/a.d2s',
                     'C:/save/a.d2s', 'save\\a.d2s', 'save/a.d2s:stream',
                     'save//a.d2s', 'save/./a.d2s']:
            with self.subTest(path=path):
                self.write([{**self.record, 'path': path}])
                with self.assertRaises(ValueError):
                    checker.verify_backup(self.manifest)

    def test_case_insensitive_duplicate_is_rejected(self):
        self.write([self.record, {**self.record, 'path': 'save/' + self.relative[5:].upper()}])
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            checker.verify_backup(self.manifest)

    def test_empty_or_invalid_records_are_rejected(self):
        for records in [[], [None], [{**self.record, 'bytes': True}],
                        [{**self.record, 'sha256': 'not-a-sha'}]]:
            with self.subTest(records=records):
                self.write(records)
                with self.assertRaises(ValueError):
                    checker.verify_backup(self.manifest)

    def test_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as other:
            outside = Path(other) / 'outside.d2s'
            outside.write_bytes(self.data)
            link = self.root / 'save/link.d2s'
            try:
                link.symlink_to(outside)
            except OSError:
                self.skipTest('Creating symlinks is unavailable for this Windows user')
            self.write([{**self.record, 'path': 'save/link.d2s'}])
            with self.assertRaisesRegex(ValueError, 'outside'):
                checker.verify_backup(self.manifest)


if __name__ == '__main__':
    unittest.main()

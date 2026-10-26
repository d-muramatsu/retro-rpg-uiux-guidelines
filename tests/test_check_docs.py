"""Regression fixtures ensure broken docs do not silently pass the checker."""
from pathlib import Path
import importlib.util
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('check_docs', ROOT / 'scripts/check_docs.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class DocumentChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in checker.REQUIRED:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)

    def edit(self, name, before, after):
        path = self.root / name
        path.write_text(path.read_text(encoding='utf-8').replace(before, after), encoding='utf-8')

    def errors(self):
        return '\n'.join(checker.validate(self.root)[0])

    def test_valid_documents(self):
        self.assertEqual(self.errors(), '')

    def test_broken_link(self):
        self.edit('README.md', '(docs/battle.md)', '(docs/missing.md)')
        self.assertIn('broken local link', self.errors())

    def test_missing_field(self):
        self.edit('docs/battle.md', '**理由:**', '**目的:**')
        self.assertIn('missing 理由', self.errors())

    def test_missing_review_rule(self):
        self.edit('checklists/review.md', '- [ ] BAT-01:', '- BAT-01:')
        self.assertIn('exactly one entry: BAT-01', self.errors())

    def test_priority_mismatch(self):
        self.edit('docs/battle.md', 'BAT-01 — MUST / P0', 'BAT-01 — SHOULD / P1')
        self.assertIn('priority mismatch: BAT-01', self.errors())

    def test_duplicate_rule(self):
        self.edit('docs/battle.md', 'BAT-02 —', 'BAT-01 —')
        self.assertIn('Duplicate rule: BAT-01', self.errors())

    def test_missing_file(self):
        (self.root / 'docs/battle.md').unlink()
        self.assertIn('Missing required file: docs/battle.md', self.errors())

    def test_link_outside_repo(self):
        self.edit('README.md', '(docs/battle.md)', '(../outside.md)')
        self.assertIn('link outside repository', self.errors())


if __name__ == '__main__':
    unittest.main()

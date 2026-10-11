import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


class DistributionTests(unittest.TestCase):
    def profile(self):
        data = json.loads((ROOT / 'skills/notion-project-memory/profile.example.json').read_text(encoding='utf-8'))
        data.update(homepage_url='https://www.notion.so/sample-homepage', timezone='UTC')
        return data

    def test_credential_field_and_foreign_url_rejected(self):
        validate = module('configure').validate_profile
        for change in ({'password': 'do-not-store'}, {'homepage_url': 'https://example.org/page'}, {'homepage_url': 'https://user:password' + '@www.notion.so/page'}, {'auto_create_projects': 'true'}):
            data = self.profile()
            data.update(change)
            with self.assertRaises(ValueError):
                validate(data)
        validate(self.profile())

    def test_existing_profile_not_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'profile.local.json'
            cmd = [sys.executable, str(ROOT / 'scripts/configure.py'), '--name', 'Example', '--homepage', 'https://www.notion.so/sample-homepage', '--timezone', 'UTC', '--output', str(output)]
            first = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            original = output.read_bytes()
            second = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(original, output.read_bytes())

    def test_release_rejects_private_ids_paths_and_credentials(self):
        validate = module('package').validate_public_content
        for value in (uuid.uuid4().hex, str(uuid.uuid4()),
                      'C:' + chr(92) + 'Users' + chr(92) + 'Example',
                      '/home/' + 'example/private', 'ntn_' + 'x' * 20,
                      'github_pat_' + 'x' * 20,
                      '-----BEGIN ' + 'PRIVATE KEY-----'):
            with self.subTest(kind=value[:8]):
                with self.assertRaises(ValueError) as caught:
                    validate(value, 'fixture.md')
                self.assertNotIn(value, str(caught.exception))
        validate('https://www.notion.so/your-homepage and generic instructions', 'example.md')

    def test_release_excludes_private_profile_and_runtime(self):
        package = module('package')
        with tempfile.TemporaryDirectory() as tmp:
            test_root = Path(tmp)
            import shutil
            for file in package.public_files():
                target = test_root / file.relative_to(ROOT)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(file, target)
            private = test_root / 'skills/notion-project-memory/profile.local.json'
            marker = uuid.uuid4().hex.encode('ascii')
            private.write_text(json.dumps({'private': marker.decode('ascii')}), encoding='utf-8')
            (test_root / 'skills/notion-project-memory/references/homepage.local.md').write_bytes(marker)
            package.ROOT = test_root
            artifacts = package.build()
            for artifact in artifacts:
                with zipfile.ZipFile(artifact) as archive:
                    self.assertFalse(any('local.' in name or 'runtime/' in name for name in archive.namelist()))
                    self.assertFalse(any(marker in archive.read(name) for name in archive.namelist()))
            with zipfile.ZipFile(artifacts[0]) as archive:
                self.assertIn('plugin.json', archive.namelist())
                self.assertIn('skills/notion-homepage-setup/SKILL.md', archive.namelist())
            with zipfile.ZipFile(artifacts[1]) as archive:
                self.assertIn('notion-project-memory/SKILL.md', archive.namelist())
            with zipfile.ZipFile(artifacts[2]) as archive:
                self.assertEqual(set(archive.namelist()), {'gpt-instructions.md', 'gpt-skill.md'})
                for name in archive.namelist():
                    self.assertEqual(archive.read(name), (test_root / 'docs' / name).read_bytes())


if __name__ == '__main__':
    unittest.main()

"""Build public skill/plugin ZIPs using an explicit allowlist; private files stay local."""
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate_public_content(content, label):
    # Both Notion URL IDs and dashed UUIDs must remain user-local.
    patterns = {
        'page ID': r'(?i)(?<![0-9a-f])[0-9a-f]{32}(?![0-9a-f])|\b[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}\b',
        'credential': r'(?:secret_|ntn_|gh[pousr]_|github_pat_|sk-proj-)[A-Za-z0-9_-]{12,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
        'machine path': r'(?i)(?<![A-Za-z0-9])(?:[A-Z]:[\\/]|/Users/|/home/)[A-Za-z0-9_.-]+',
    }
    for category, pattern in patterns.items():
        if re.search(pattern, content):
            # Do not echo the matched private value into logs.
            raise ValueError(f'Possible private {category} in {label}')


def public_files():
    files = [ROOT / 'plugin.json', ROOT / 'README.md', ROOT / '.gitignore', ROOT / 'requirements.txt']
    files += [ROOT / 'docs' / name for name in ('chatgpt.md', 'publishing.md', 'evaluation.md', 'learning.md')]
    files += [ROOT / 'scripts/configure.py', ROOT / 'scripts/package.py', ROOT / 'tests/test_distribution.py']
    for skill in ('notion-project-memory', 'notion-homepage-setup'):
        base = ROOT / 'skills' / skill
        files += [base / 'SKILL.md', base / 'agents/openai.yaml']
        if skill == 'notion-project-memory':
            files += [base / 'profile.example.json'] + [base / 'references' / name for name in ('setup.md', 'homepage.md', 'project-workflow.md', 'note-format.md', 'knowledge.md', 'learning.md', 'consolidation.md', 'platforms.md')]
    for file in files:
        if not file.is_file() or file.is_symlink():
            raise ValueError(f'Missing or linked public file: {file.relative_to(ROOT)}')
        content = file.read_text(encoding='utf-8')
        validate_public_content(content, file.relative_to(ROOT))
    return sorted(files)


def build():
    files = public_files()
    dest = ROOT / 'dist'
    dest.mkdir(exist_ok=True)
    outputs = []
    plugin_zip = dest / 'notion-homepage-kit-plugin.zip'
    with zipfile.ZipFile(plugin_zip, 'w', zipfile.ZIP_DEFLATED) as archive:
        for file in files:
            archive.write(file, file.relative_to(ROOT).as_posix())
    outputs.append(plugin_zip)
    for name in ('notion-project-memory',):
        out = dest / f'{name}.zip'
        with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as archive:
            for file in files:
                relative = file.relative_to(ROOT)
                if relative.parts[:2] == ('skills', name):
                    archive.write(file, Path(*relative.parts[1:]).as_posix())
        outputs.append(out)
    return outputs


if __name__ == '__main__':
    for artifact in build():
        print(artifact)

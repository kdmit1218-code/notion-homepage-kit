"""Create a local profile; no credentials, network calls or Notion writes."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

ROOT = Path(__file__).resolve().parents[1]


def validate_profile(data):
    allowed = set(json.loads((ROOT / 'skills/notion-project-memory/profile.example.json').read_text(encoding='utf-8')))
    if set(data) - allowed:
        raise ValueError('Unknown profile keys; do not put credentials in a profile')
    for key in ('display_name', 'homepage_title', 'language', 'timezone'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'{key} must be a non-empty string')
    url = urlparse(data.get('homepage_url', ''))
    host = (url.hostname or '').lower()
    if url.scheme != 'https' or url.username or url.password or not (host in ('notion.so', 'www.notion.so', 'app.notion.com', 'notion.com', 'www.notion.com') or host.endswith('.notion.site')):
        raise ValueError('homepage_url must be an HTTPS Notion URL without credentials')
    if data.get('sync_mode') not in ('manual', 'on_decision'):
        raise ValueError('sync_mode must be manual or on_decision')
    if type(data.get('auto_create_projects')) is not bool:
        raise ValueError('auto_create_projects must be a boolean')
    if data.get('homepage_layout') not in ('preserve', 'starter'):
        raise ValueError('homepage_layout must be preserve or starter')
    if not isinstance(data.get('sections'), dict) or not data['sections'].get('projects') or any(not isinstance(v, str) or not v.strip() for v in data['sections'].values()):
        raise ValueError('sections must contain heading names')
    if not isinstance(data.get('project_aliases'), dict):
        raise ValueError('project_aliases must be an object')
    for alias, target in data['project_aliases'].items():
        if not isinstance(alias, str) or not alias.strip() or not isinstance(target, str):
            raise ValueError('project_aliases must map non-empty names to Notion URLs')
        alias_data = dict(data, project_aliases={}, homepage_url=target)
        validate_profile(alias_data)
    try:
        ZoneInfo(data['timezone'])
    except ZoneInfoNotFoundError:
        raise ValueError('Unknown IANA timezone or missing OS timezone data; on Windows install tzdata') from None
    return data


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--name', required=True)
    p.add_argument('--homepage', required=True)
    p.add_argument('--timezone', default='UTC')
    p.add_argument('--language', default='zh-CN')
    p.add_argument('--sync-mode', choices=['manual', 'on_decision'], default='manual')
    p.add_argument('--auto-create-projects', action='store_true')
    p.add_argument('--output', type=Path, default=ROOT / 'skills/notion-project-memory/profile.local.json')
    args = p.parse_args()
    data = json.loads((ROOT / 'skills/notion-project-memory/profile.example.json').read_text(encoding='utf-8'))
    data.update(display_name=args.name, homepage_title=f'{args.name}’s Homepage', homepage_url=args.homepage,
                timezone=args.timezone, language=args.language, sync_mode=args.sync_mode,
                auto_create_projects=args.auto_create_projects)
    validate_profile(data)
    if args.output.exists():
        p.error('Output exists; preserve it and update it deliberately instead of overwriting')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Local profile saved: {args.output}. Verify the Homepage through Notion before writing.')


if __name__ == '__main__':
    main()

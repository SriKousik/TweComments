"""Refresh only the English progress column in BLOCKED-SITES.md."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'tools/blocked-english-status.json'


def main():
    results = json.loads(RESULTS.read_text()) if RESULTS.exists() else {}
    latest = {}
    audit = ROOT / 'tools/blocked-english.jsonl'
    if audit.exists():
        for line in audit.read_text().splitlines():
            row = json.loads(line)
            latest[row['home']] = row
    by_home = {r['home']: r for r in results.values()}
    path = ROOT / 'BLOCKED-SITES.md'
    text = path.read_text()
    before, english = text.split('### English (', 1)
    english, after = english.split('\n### ', 1)
    lines = []
    for line in english.splitlines():
        if line.startswith('| Extension |'):
            line = '| Extension | Site | Original reason | Rule | Latest check |'
        elif line.startswith('|---'):
            line = '|---|---|---|---|---|'
        elif line.startswith('| ') and 'https://' in line:
            columns = [c.strip() for c in line.strip('|').split('|')]
            name, home, reason = columns[:3]
            verified = by_home.get(home)
            evidence = latest.get(home)
            rule, note = '', 'Pending'
            if verified:
                rule = f"[{verified['rule']}](rules/{verified['rule']}.json)" if verified.get('rule') else ''
                note = verified['note']
                if verified.get('url'):
                    note += f" · [sample]({verified['url']})"
            elif evidence:
                status = evidence['status']
                note = {
                    'blocked': '⛔ Still blocked after service retry' if evidence.get('service') else '⏳ Access blocked; service retry queued',
                    'error': '⛔ Request failed; unresolved',
                    'unreachable': '⛔ Site returned an HTTP error',
                    'comments-found': '🔎 Widget found; rule/read verification pending',
                    'inspect': '🔎 Pages checked; custom/dynamic comments need inspection',
                    'no-title': '🔎 Home checked; title discovery needs follow-up',
                }.get(status, status)
            line = f'| {name} | {home} | {reason} | {rule} | {note} |'
        lines.append(line)
    text = before + '### English (' + '\n'.join(lines) + '\n### ' + after
    path.write_text(text)


if __name__ == '__main__':
    main()

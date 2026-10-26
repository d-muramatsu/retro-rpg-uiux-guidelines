"""Validate this repository's deliberately small Markdown convention; no network."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

REQUIRED = (
    'README.md', 'CONTRIBUTING.md', 'LICENSE-STATUS.md',
    'docs/principles.md', 'docs/navigation.md', 'docs/exploration-dialogue.md',
    'docs/battle.md', 'docs/inventory-progression.md', 'docs/save-state.md',
    'docs/accessibility-input.md', 'docs/extensions.md', 'docs/sources.md',
    'checklists/review.md', 'templates/playtest.md',
)
RULE = re.compile(r'^## ([A-Z]+-\d{2}) — (MUST / P0|SHOULD / P1|MAY / P2):', re.M)
FIELDS = ('理由', '推奨', '悪い例', '良い例', '例外・トレードオフ', '確認')


def validate(root):
    root = Path(root).resolve()
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f'Missing required file: {name}')
    files = sorted(root.rglob('*.md'))
    rules = {}
    for path in files:
        content = path.read_text(encoding='utf-8')
        rel = path.relative_to(root)
        if not content.endswith('\n'):
            errors.append(f'{rel}: missing final newline')
        if '\ufffd' in content:
            errors.append(f'{rel}: replacement character')
        if content.count('```') % 2:
            errors.append(f'{rel}: unclosed fenced block')
        for dest in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', content):
            url = urlsplit(dest)
            if url.scheme or dest.startswith('//'):
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(root):
                errors.append(f'{rel}: link outside repository: {dest}')
            elif not target.is_file():
                errors.append(f'{rel}: broken local link: {dest}')
            elif url.fragment:
                # Explicit anchors only; automatic heading slugs are intentionally unused.
                anchor = unquote(url.fragment)
                if f'id="{anchor}"' not in target.read_text(encoding='utf-8'):
                    errors.append(f'{rel}: missing explicit anchor: {dest}')
        matches = list(RULE.finditer(content))
        for idx, match in enumerate(matches):
            rule_id, level = match.groups()
            if rule_id in rules:
                errors.append(f'Duplicate rule: {rule_id}')
            rules[rule_id] = level
            end = matches[idx + 1].start() if idx + 1 < len(matches) else len(content)
            block = content[match.end():end]
            for field in FIELDS:
                if f'**{field}:**' not in block:
                    errors.append(f'{rel}: {rule_id} missing {field}')
    checklist = root / 'checklists/review.md'
    if checklist.exists():
        content = checklist.read_text(encoding='utf-8')
        entries = re.findall(r'^- \[ \] ([A-Z]+-\d{2}):', content, re.M)
        for rule_id in rules:
            if entries.count(rule_id) != 1:
                errors.append(f'Checklist needs exactly one entry: {rule_id}')
        for rule_id in entries:
            if rule_id not in rules:
                errors.append(f'Checklist unknown rule: {rule_id}')
        section = None
        for line in content.splitlines():
            if line.startswith('## P'):
                section = line[3:5]
            item = re.match(r'- \[ \] ([A-Z]+-\d{2}):', line)
            if item and item[1] in rules and not rules[item[1]].endswith(section or '?'):
                errors.append(f'Checklist priority mismatch: {item[1]}')
    return errors, len(files), len(rules)


if __name__ == '__main__':
    errors, documents, rules = validate(Path(__file__).resolve().parents[1])
    for error in errors:
        print(f'ERROR: {error}')
    print(f'{documents} Markdown files; {rules} rules; {len(errors)} errors')
    sys.exit(bool(errors))

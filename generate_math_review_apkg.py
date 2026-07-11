# -*- coding: utf-8 -*-
"""按《数学回顾要点.md》+ 大观例题生成 Anki .apkg 与 Markdown 记忆卡。"""
import genanki
import random
import os
import re
from collections import Counter, defaultdict

from cards_reading import register_reading
from cards_content import register_practice

ANKI_CSS = (
    '.card { font-family: "Microsoft YaHei", "SimHei", sans-serif; font-size: 17px; '
    'line-height: 1.7; text-align: left; color: #222; }'
    'table { border-collapse: collapse; margin: 8px 0; width: 100%; font-size: 15px; }'
    'td, th { border: 1px solid #ccc; padding: 6px 10px; vertical-align: middle; }'
    'b { font-weight: bold; color: #1a5276; }'
    'hr#answer { border: none; border-top: 2px solid #ccc; margin: 16px 0; }'
)

model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    '数学回顾问答',
    fields=[{'name': 'Front'}, {'name': 'Back'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '{{Front}}',
        'afmt': '{{FrontSide}}{{#Back}}<hr id="answer">{{Back}}{{/Back}}',
    }],
    css=ANKI_CSS,
)

decks = {}
cards_data = []


def get_deck(path):
    if path not in decks:
        decks[path] = genanki.Deck(random.randrange(1 << 30, 1 << 31), path)
    return decks[path]


def add(deck_path, front, back, tag=None):
    cards_data.append((deck_path, front, back, tag or 'card'))


def html_to_md(text):
    s = text
    s = re.sub(r'<br\s*/?>', '\n', s, flags=re.IGNORECASE)
    s = re.sub(r'<b>(.*?)</b>', r'**\1**', s, flags=re.IGNORECASE | re.DOTALL)
    s = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', s, flags=re.IGNORECASE | re.DOTALL)
    s = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', s, flags=re.DOTALL)
    s = re.sub(r'\\\((.*?)\\\)', r'$\1$', s, flags=re.DOTALL)
    return s.strip()


DECK_ORDER = [
    '记忆', '常用公式速查', '函数', '连续与间断点', '函数极限',
    '数列极限', '渐近线', '极限等式', '无穷小', '无穷大', '泰勒多项式',
]


def deck_to_heading(deck_path):
    parts = deck_path.split('::')
    if parts and parts[0] == '数学回顾':
        parts = parts[1:]
    return parts


def deck_sort_key(deck_path):
    parts = deck_to_heading(deck_path)
    if not parts:
        return (999, deck_path)
    try:
        i = DECK_ORDER.index(parts[0])
    except ValueError:
        i = 999
    return (i, deck_path)


def write_markdown(cards, out_path):
    grouped = defaultdict(list)
    for deck_path, front, back, tag in cards:
        grouped[deck_path].append((tag, front, back))

    lines = [
        '# 数学回顾要点 · 记忆卡',
        '',
        '> 与 `数学回顾要点-Anki.apkg` 同步生成。',
        '> **阅读卡**：要点通读；**速记卡**（`memo-*`）：只背原理/判定/方法，不挂具体小题。',
        f'> 共 **{len(cards)}** 张。运行 `python generate_math_review_apkg.py` 可重新导出。',
        '',
        '---',
        '',
    ]

    last_h2 = last_h3 = None
    for deck_path in sorted(grouped.keys(), key=deck_sort_key):
        parts = deck_to_heading(deck_path)
        if not parts:
            continue

        h2 = parts[0]
        h3 = ' · '.join(parts[1:]) if len(parts) > 1 else None

        if h2 != last_h2:
            lines.append(f'## {h2}')
            lines.append('')
            last_h2, last_h3 = h2, None

        if h3 and h3 != last_h3:
            lines.append(f'### {h3}')
            lines.append('')
            last_h3 = h3

        for i, (tag, front, back) in enumerate(grouped[deck_path], 1):
            if tag.startswith('read-'):
                kind = '阅读'
            elif tag.startswith('memo-'):
                kind = '速记'
            elif tag.startswith('disc-'):
                kind = '辨析'
            elif tag.startswith('ask-'):
                kind = '提问'
            else:
                kind = '练习'
            lines.append(f'#### {kind} {i} `{tag}`')
            lines.append('')
            if kind == '阅读':
                lines.append('**内容**')
                lines.append('')
                lines.append(html_to_md(front))
            elif kind == '速记':
                lines.append('**问**')
                lines.append('')
                lines.append(html_to_md(front))
                lines.append('')
                lines.append('**答**')
                lines.append('')
                lines.append(html_to_md(back))
            elif kind == '辨析':
                lines.append('**要点 · 大观题**')
                lines.append('')
                lines.append(html_to_md(front))
                lines.append('')
                lines.append('**处理方法**')
                lines.append('')
                lines.append(html_to_md(back))
            elif kind == '提问':
                lines.append('**大观题 · 问**')
                lines.append('')
                lines.append(html_to_md(front))
                lines.append('')
                lines.append('**方法**')
                lines.append('')
                lines.append(html_to_md(back))
            else:
                lines.append('**问**')
                lines.append('')
                lines.append(html_to_md(front))
                lines.append('')
                lines.append('**答**')
                lines.append('')
                lines.append(html_to_md(back))
            lines.append('')
            lines.append('---')
            lines.append('')

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


register_reading(add)
register_practice(add)

for deck_path, front, back, tag in cards_data:
    note = genanki.Note(model=model, fields=[front, back], tags=[tag])
    get_deck(deck_path).add_note(note)

base = os.path.dirname(os.path.abspath(__file__))
apkg_path = os.path.join(base, '数学回顾要点-Anki.apkg')
md_path = os.path.join(base, '数学回顾要点-记忆卡.md')

genanki.Package(list(decks.values())).write_to_file(apkg_path)
write_markdown(cards_data, md_path)

read_n = sum(1 for _, _, _, t in cards_data if t.startswith('read-'))
memo_n = sum(1 for _, _, _, t in cards_data if t.startswith('memo-'))
print(f'已生成 {len(cards_data)} 张（阅读 {read_n} + 速记 {memo_n}）')
print(f'  Anki: {apkg_path}')
print(f'  Markdown: {md_path}')
print('\n章节分布：')
for path, n in sorted(Counter(d for d, _, _, _ in cards_data).items()):
    print(f'  {path}: {n} 张')

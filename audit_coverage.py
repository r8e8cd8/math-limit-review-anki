# -*- coding: utf-8 -*-
"""核对《数学回顾要点.md》各小节是否都有阅读卡 + 速记卡。"""
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cards_reading import register_reading
from cards_content import register_practice

# 笔记小节 → 期望的 deck 路径前缀（与 cards_* 中一致）
EXPECTED = [
    '数学回顾::记忆',
    '数学回顾::常用公式速查::代数与三角',
    '数学回顾::常用公式速查::绝对值三角不等式',
    '数学回顾::函数::奇偶性',
    '数学回顾::函数::周期性',
    '数学回顾::函数::有界性',
    '数学回顾::连续与间断点::四则运算',
    '数学回顾::连续与间断点::间断点分类',
    '数学回顾::函数极限::概念题',
    '数学回顾::函数极限::重要极限',
    '数学回顾::函数极限::0/0型',
    '数学回顾::函数极限::∞/∞型',
    '数学回顾::函数极限::∞-∞型',
    '数学回顾::函数极限::0^0与∞^0',
    '数学回顾::函数极限::1^∞型',
    '数学回顾::函数极限::含e与绝对值',
    '数学回顾::函数极限::导数定义求极限',
    '数学回顾::函数极限::三角处理',
    '数学回顾::函数极限::积分形式极限',
    '数学回顾::数列极限::积分形式',
    '数学回顾::数列极限::积分形式::一看就别积分',
    '数学回顾::数列极限::n项和::经典极限与不等式',
    '数学回顾::数列极限::n项和::黎曼和',
    '数学回顾::数列极限::n项和::夹逼定理',
    '数学回顾::数列极限::n项和::二重积分',
    '数学回顾::数列极限::n次根号或乘积',
    '数学回顾::数列极限::递推数列',
    '数学回顾::数列极限::暂不深入',
    '数学回顾::渐近线::基本方法',
    '数学回顾::渐近线::垂直渐近线',
    '数学回顾::渐近线::水平渐近线',
    '数学回顾::渐近线::斜渐近线特殊方法',
    '数学回顾::极限等式',
    '数学回顾::无穷小',
    '数学回顾::无穷大',
    '数学回顾::泰勒多项式',
    '数学回顾::泰勒多项式::使用条件',
    '数学回顾::泰勒多项式::求极限常用',  # 阅读卡补充常用展开
]


def collect():
    cards = []

    def add(deck, front, back, tag):
        cards.append((deck, tag))

    register_reading(add)
    register_practice(add)
    return cards


def main():
    cards = collect()
    by_deck = {}
    for deck, tag in cards:
        by_deck.setdefault(deck, {'read': 0, 'memo': 0})
        if tag.startswith('read-'):
            by_deck[deck]['read'] += 1
        elif tag.startswith('memo-'):
            by_deck[deck]['memo'] += 1

    missing_read = []
    missing_memo = []
    ok = []

    for path in EXPECTED:
        info = by_deck.get(path, {'read': 0, 'memo': 0})
        if info['read'] == 0:
            missing_read.append(path)
        if info['memo'] == 0:
            missing_memo.append(path)
        if info['read'] and info['memo']:
            ok.append((path, info['read'], info['memo']))

    read_n = sum(1 for _, t in cards if t.startswith('read-'))
    memo_n = sum(1 for _, t in cards if t.startswith('memo-'))
    print(f'总计 {len(cards)} 张（阅读 {read_n} + 速记 {memo_n}）\n')

    if missing_read:
        print('[!] 缺阅读卡：')
        for p in missing_read:
            print(f'  - {p}')
        print()

    if missing_memo:
        print('[!] 缺速记卡：')
        for p in missing_memo:
            print(f'  - {p}')
        print()

    print(f'OK 双轨齐全 {len(ok)}/{len(EXPECTED)} 个小节：')
    for p, r, m in ok:
        print(f'  {p}: 阅读{r} + 速记{m}')

    return 1 if (missing_read or missing_memo) else 0


if __name__ == '__main__':
    raise SystemExit(main())

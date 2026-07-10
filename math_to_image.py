# -*- coding: utf-8 -*-
"""将卡片 HTML 中所有 LaTeX 渲染为 PNG（整行混排，适配墨墨等客户端）。"""
import hashlib
import os
import re

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

_DISPLAY = re.compile(r'\\\[(.+?)\\\]', re.DOTALL)
_INLINE = re.compile(r'\\\((.+?)\\\)', re.DOTALL)
_BR = re.compile(r'<br\s*/?>', re.IGNORECASE)
_HTML_TAG = re.compile(r'<[^>]+>')
_CJK = re.compile(r'[\u4e00-\u9fff]')
_MATH_HINT = re.compile(
    r'\\(?:frac|dfrac|lim|sum|int|sqrt|sin|cos|tan|ln|exp|alpha|beta|xi|eta|'
    r'pi|infty|to|geq|leq|neq|Leftrightarrow|nearrow|left|right|text|prod|'
    r'partial|cdot|cdots|quad|displaystyle|iint|oint|sinh|cosh|arcsin|arctan|tanh)'
)

_media_paths = set()
_render_errors = []


def reset():
    global _media_paths, _render_errors
    _media_paths = set()
    _render_errors = []


def get_media_files():
    return sorted(_media_paths)


def get_render_errors():
    return list(_render_errors)


def _get_font(size=20):
    families = ['Microsoft YaHei', 'SimHei', 'Noto Sans CJK SC', 'Arial Unicode MS', 'DejaVu Sans']
    for fam in families:
        try:
            return font_manager.FontProperties(family=fam, size=size)
        except Exception:
            continue
    return font_manager.FontProperties(size=size)


def normalize_latex(latex):
    s = latex.strip()
    s = re.sub(r'\\sqrt\[([^\]]+)\]\{([^}]+)\}', r'(\2)^{1/\1}', s)
    # \frac1n、\frac1{n^2}、\frac\pi2 等补全花括号
    s = re.sub(r'\\frac([0-9]+)(\{)', r'\\frac{\1}\2', s)
    s = re.sub(r'\\frac([0-9]+)([0-9a-zA-Z]+)', r'\\frac{\1}{\2}', s)
    s = re.sub(
        r'\\frac\\([a-zA-Z]+)([0-9]+)',
        lambda m: f'\\frac{{\\{m.group(1)}}}{{{m.group(2)}}}',
        s,
    )
    s = s.replace(r'\iff', r'\Leftrightarrow')
    s = s.replace(r'\dfrac', r'\frac')
    s = re.sub(r'\\displaystyle\s*', '', s)
    s = s.replace(r'\!', ' ')
    s = re.sub(r'\\text\{([^}]*)\}', r'\1', s)
    s = s.replace(r'\bigl', r'\left').replace(r'\bigr', r'\right')
    s = s.replace(r'\Bigl', r'\left').replace(r'\Bigr', r'\right')
    s = s.replace(r'\iint', r'\int\!\int')
    s = s.replace(r'\nearrow', r'\uparrow')
    return s


def _math_wrapped(latex):
    latex = normalize_latex(latex)
    if not latex:
        return ''
    if _CJK.search(latex):
        return latex
    return f'${latex}$'


def _strip_html(text):
    text = text.replace('&nbsp;', ' ')
    text = _HTML_TAG.sub('', text)
    return text.strip()


def _has_math(text):
    if r'\(' in text or r'\[' in text:
        return True
    return bool(_MATH_HINT.search(text))


def _to_mathtext_line(text):
    text = _strip_html(text)

    def repl(m):
        return _math_wrapped(m.group(1))

    text = _DISPLAY.sub(repl, text)
    text = _INLINE.sub(repl, text)
    return text


def _cache_name(content, display):
    key = hashlib.sha256((('D' if display else 'L') + content).encode('utf-8')).hexdigest()[:16]
    return f'ml2_{"d" if display else "l"}_{key}.png'


def _render_png(mathtext, media_dir, display=False):
    mathtext = mathtext.strip()
    if not mathtext:
        return None

    fname = _cache_name(mathtext, display)
    path = os.path.join(media_dir, fname)
    if os.path.isfile(path):
        _media_paths.add(os.path.abspath(path))
        return fname

    fontsize = 26 if display else (18 if len(mathtext) > 90 else 22)
    dpi = 240
    font_prop = _get_font(size=fontsize)

    fig = plt.figure(dpi=dpi)
    fig.patch.set_alpha(0.0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')

    try:
        text_obj = ax.text(
            0.02 if not display else 0.5,
            0.5,
            mathtext,
            fontproperties=font_prop,
            fontsize=fontsize,
            va='center',
            ha='left' if not display else 'center',
        )
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
        bbox = text_obj.get_window_extent(renderer=renderer)
        pad_x, pad_y = 20, 14
        width_px = bbox.width + pad_x * 2
        height_px = max(bbox.height + pad_y * 2, fontsize * 2.0)
        fig.set_size_inches(width_px / dpi, height_px / dpi)

        ax.set_xlim(0, width_px)
        ax.set_ylim(0, height_px)
        text_obj.set_position((
            pad_x if not display else width_px / 2,
            height_px / 2,
        ))
        text_obj.set_ha('left' if not display else 'center')

        fig.savefig(path, dpi=dpi, transparent=True, pad_inches=0)
    except Exception as exc:
        plt.close(fig)
        _render_errors.append((mathtext[:80], str(exc)))
        return None
    finally:
        if plt.fignum_exists(fig.number):
            plt.close(fig)

    _media_paths.add(os.path.abspath(path))
    return fname


def _img_tag(fname, display=False):
    if display:
        return f'<div class="math-block"><img class="math-display" src="{fname}"></div>'
    return f'<div class="math-line"><img class="math-line-img" src="{fname}"></div>'


def _render_line_html(line, media_dir):
    raw = line.strip()
    if not raw or not _has_math(raw):
        return raw

    only_display = re.fullmatch(r'\\\[(.+?)\\\]\s*', raw, flags=re.DOTALL)
    if only_display:
        mathtext = _math_wrapped(only_display.group(1))
        fname = _render_png(mathtext, media_dir, display=True)
        if fname:
            return _img_tag(fname, display=True)

    mathtext = _to_mathtext_line(raw)
    fname = _render_png(mathtext, media_dir, display=False)
    if fname:
        return _img_tag(fname, display=False)

    return f'<div class="math-fallback">{_strip_html(raw)}</div>'


def replace_math(html, media_dir):
    if not html or not _has_math(html):
        return html

    parts = _BR.split(html)
    out = []
    for part in parts:
        if _has_math(part):
            out.append(_render_line_html(part, media_dir))
        else:
            out.append(part)
    return '<br>'.join(out)

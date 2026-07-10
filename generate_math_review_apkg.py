# -*- coding: utf-8 -*-
"""按《数学回顾要点.md》生成 Anki .apkg（LaTeX 由 Anki MathJax 渲染）。"""
import genanki
import random
import os
from collections import Counter

DECK_ROOT = '数学回顾'

ANKI_CSS = (
    '.card { font-family: "Microsoft YaHei", "SimHei", sans-serif; font-size: 18px; '
    'line-height: 1.65; text-align: left; color: #222; }'
    'table { border-collapse: collapse; margin: 8px 0; width: 100%; font-size: 16px; }'
    'td, th { border: 1px solid #ccc; padding: 6px 10px; vertical-align: middle; }'
    'b { font-weight: bold; }'
)

model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    '数学回顾填空',
    fields=[{'name': 'Front'}, {'name': 'Back'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '{{Front}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Back}}',
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
    cards_data.append((deck_path, front, back, tag or deck_path.split('::')[-1]))


def add_group(deck_path, title, front_body, back_body, tag=None, method_example=None):
    """同类内容合并为一张卡。method_example 仅用于方法/概念类卡片，公式类不传。"""
    back = back_body
    if method_example:
        back += '<br><br><b>例（方法）</b><br>' + method_example
    add(deck_path, f'【{title}】<br>{front_body}', back, tag or title)


# ========== 记忆 ==========
add('数学回顾::记忆',
    '【记忆】知识点是______的，题是______的。真正要掌握的不是题，而是______。',
    '知识点是<b>有限</b>的，题是<b>无限</b>的。真正要掌握的不是题，而是<b>一般方法</b>。<br><br>'
    '<b>例（方法）</b><br>'
    '0/0 型形式各异，固定套路是「泰勒 / 等价无穷小 / 洛必达」。')

# ========== 常用公式速查（纯公式，直接记忆）==========
add_group('数学回顾::常用公式速查::代数与三角', '立方差与立方和',
    r'立方差：\( a^3 - b^3 = \) ______<br>'
    r'立方和：\( a^3 + b^3 = \) ______<br>'
    r'立方和（特例）：\( x^3 + 1 = \) ______',
    r'\[ a^3 - b^3 = (a-b)(a^2 + ab + b^2) \]<br>'
    r'\[ a^3 + b^3 = (a+b)(a^2 - ab + b^2) \]<br>'
    r'\[ x^3 + 1 = (x+1)(x^2 - x + 1) \]')

add_group('数学回顾::常用公式速查::代数与三角', '二倍角公式',
    r'\( \sin 2\alpha = \) ______<br>'
    r'\( \cos 2\alpha = \) ______ \( = \) ______ \( = \) ______<br>'
    r'\( \tan 2\alpha = \) ______',
    r'\[ \sin 2\alpha = 2\sin\alpha\cos\alpha \]<br>'
    r'\[ \cos 2\alpha = \cos^2\alpha - \sin^2\alpha = 2\cos^2\alpha - 1 = 1 - 2\sin^2\alpha \]<br>'
    r'\[ \tan 2\alpha = \dfrac{2\tan\alpha}{1 - \tan^2\alpha} \]')

add_group('数学回顾::常用公式速查::代数与三角', '降幂公式',
    r'\( \sin^2\alpha = \) ______<br>'
    r'\( \cos^2\alpha = \) ______',
    r'\[ \sin^2\alpha = \dfrac{1 - \cos 2\alpha}{2} \]<br>'
    r'\[ \cos^2\alpha = \dfrac{1 + \cos 2\alpha}{2} \]')

add('数学回顾::常用公式速查::绝对值三角不等式',
    r'【绝对值三角不等式】\[ \bigl| |a_n| - |a| \bigr| \leq \] ______<br>'
    r'（若另有 \( |a_n-a| < \dfrac{|a|}{2} \)，可进一步估计 \( |a_n| \) 与 \( |a| \)）',
    r'\[ \bigl| |a_n| - |a| \bigr| \leq |a_n - a| \]<br>'
    r'（常用于数列收敛证明；右端 \( <\dfrac{|a|}{2} \) 仅在已知 \( a_n \) 接近 \( a \) 时使用。）')

# ========== 函数::奇偶性 ==========
add_group('数学回顾::函数::奇偶性', '奇偶性要点',
    r'①【原函数奇偶】偶函数的原函数______；只有积分区间为 ______ 时才是奇函数。（速记：哦!飞机）<br>'
    r'②【含积分求导】可通过______处理含积分的函数，但原函数符号与预期______。<br>'
    r'③【无从下手】分析奇偶性时，应______。',
    r'① 原函数<b>不一定是奇函数</b>；\( [0, x] \)<br>'
    r'② 求导；与预期<b>相反</b><br>'
    r'③ 回到<b>奇偶性的定义</b>来分析。',
    method_example=
    r'\( f(x)=x^2 \) 偶，\( \int_0^x t^2\,dt \) 才是奇函数；\( \int_{-1}^x t^2\,dt \) 一般不是。')

# ========== 函数::周期性 ==========
add_group('数学回顾::函数::周期性', '周期性要点',
    r'①【周期与原函数】若 \( f \) 以 \( T \) 为周期且可积，则 \( \displaystyle\int_0^T f = 0 \Leftrightarrow \) 其原函数也以 ______ 为周期。<br>'
    r'②【嵌套函数】嵌套分段函数，应先分析______：内层取不同值，对应外层______。<br>'
    r'③【图像平移】周期内图像相同、整体平移，可用 ______ 理解。<br>'
    r'④【计算困难】分析周期性时，应______。',
    r'① \( T \)（相同周期）<br>'
    r'② 外层函数；不同分段<br>'
    r'③ \( y = f(ax) \)<br>'
    r'④ 回到<b>周期函数的定义</b>。',
    method_example=
    r'嵌套 \( f(x)=|x-1|+|x-2| \) 先拆外层；\( \sin x \) 周期 \( 2\pi \)，\( \int_0^{2\pi}\sin x\,dx=0 \)，原函数同周期。')

# ========== 函数::有界性 ==========
add_group('数学回顾::函数::有界性', '有界性要点',
    r'①【端点取不到】判断区间端点有界性，应______。<br>'
    r'②【子列判无界】存在子列使函数值趋于无穷 \( \Rightarrow \) 该点附近函数______。<br>'
    r'③【易错·极限不存在】仅知极限不存在，能否直接断定函数无界？答：______。<br>'
    r'&nbsp;&nbsp;&nbsp;（反例：\( \sin\dfrac{1}{x} \) 在 \( x \to 0 \) 极限不存在，但在去心邻域内有界）',
    r'① 必须考察<b>端点的极限</b>。<br>'
    r'② <b>无界</b>。<br>'
    r'③ <b>不能</b>，不能直接判定无界。',
    method_example=
    r'\( \frac{1}{x} \) 在 \( x=0 \) 无界（子列 \( x_n=\frac1n \)）；\( \sin\frac{1}{x} \) 极限不存在但有界。')

# ========== 连续与间断点::四则运算 ==========
add_group('数学回顾::连续与间断点::四则运算', '连续函数四则运算',
    r'\( f(x) \pm g(x) \) 连续：______<br>'
    r'\( f(x) \cdot g(x) \) 连续：______<br>'
    r'\( \dfrac{f(x)}{g(x)} \) 连续：______（注意：______）<br>'
    r'\( C \cdot f(x) \) 连续：______',
    r'连续<br>连续<br>连续，要求 \( g(x_0) \neq 0 \)<br>连续（\( C \) 为常数）')

# ========== 连续与间断点::间断点分类（识别方法）==========
add_group('数学回顾::连续与间断点::间断点分类', '间断点分类',
    r'可去间断点（断桥）：______<br>'
    r'跳跃间断点（台阶/断层）：______<br>'
    r'无穷间断点（万丈深渊）：______<br>'
    r'振荡间断点（暴风吊桥）：______',
    r'左右极限相等，但不等于函数值<br>'
    r'左右极限不等<br>'
    r'极限为 \( \pm\infty \)<br>'
    r'极限不存在，也不趋于无穷',
    method_example=
    r'可去 \( \frac{x^2-1}{x-1} \) @ \( x=1 \)；跳跃 \( \frac{|x|}{x} \) @ \( x=0 \)；'
    r'无穷 \( \frac{1}{x} \) @ \( x=0 \)；振荡 \( \sin\frac{1}{x} \) @ \( x=0 \)')

# ========== 函数极限::概念题（方法/概念）==========
add_group('数学回顾::函数极限::概念题', '连续与极限前提',
    r'①【连续定义】\( f(x) \) 在 \( x_0 \) 连续：\( \displaystyle\lim_{x \to x_0} f(x) = \) ______，'
    r'且 \( f(x_0) \) 存在，且极限存在并______。<br>'
    r'②【极限存在前提】极限存在的前提：______。',
    r'① \[ \lim_{x \to x_0} f(x) = f(x_0) \]；相等<br>'
    r'② 在某个<b>去心邻域</b>内，函数必须处处有定义。<br>'
    r'（连续<b>只保证在 \( x_0 \) 这一点</b>，不保证周围点也连续；可联系<b>可去间断点</b>理解。）',
    method_example=
    r'\( \frac{x^2-1}{x-1} \) 在 \( x=1 \) 无定义，补 \( f(1)=2 \) 后可连续。')

add_group('数学回顾::函数极限::概念题', '保号性',
    r'（设 \( \displaystyle\lim_{x \to x_0} f(x) = A \)，同理可推广到 \( x \to \infty \)）<br>'
    r'①【正向保号】\( A > 0 \) \( \Rightarrow \) 存在 \( \delta>0 \)，去心邻域内 \( f(x) \) 应满足______。<br>'
    r'②【逆向保号】邻域内 \( f(x) \geq 0 \) 且极限存在 \( \Rightarrow A \) 满足______。<br>'
    r'③【易错·严格正】\( f(x)>0 \) 严格成立，关于极限 \( A \) 的符号能推出什么？答：______。',
    r'① 恒有 \( f(x) > 0 \)（或 \( f(x) < 0 \)）<br>'
    r'② \( A \geq 0 \)（或 \( A \leq 0 \)）<br>'
    r'③ 只能得 \( A \geq 0 \)，<b>不能</b>推出 \( A > 0 \)',
    method_example=
    r'\( f(x)=(x-1)^2\geq 0 \)，\( \lim_{x\to 1}=0 \)：只能得 \( A\geq 0 \)，不能得 \( A>0 \)。')

add_group('数学回顾::函数极限::概念题', '其他要点',
    r'①【极限含义】极限反映"______"的行为，不是某点值或区间值。<br>'
    r'②【极限大】"极限大" \( \Rightarrow \) 去心邻域内函数值大（依据______）。<br>'
    r'③【邻域大≠极限大】"邻域内函数值大" \( \Rightarrow \) 关于极限符号能推出什么？答：______。<br>'
    r'④【未给极限值】题目未说明极限等于某数时，关于极限存在性：______。<br>'
    r'⑤【数列收敛】判断 \( a_n \) 与 \( a \) 是否相等，应______，构造 \( \varepsilon \)。',
    r'① 趋近时的行为<br>② 保号性<br>③ 只能推出极限 \( \geq \)<br>'
    r'④ 不一定极限存在<br>⑤ 常用定义式',
    method_example=
    r'\( a_n=(-1)^n \) 无极限；判断 \( |a_n-a| \) 用 \( \varepsilon \)-N 定义。')

# ========== 函数极限::重要极限（纯公式）==========
add_group('数学回顾::函数极限::重要极限', '重要极限',
    r'\[ \lim_{n \to \infty} \left(1 + \frac{a}{n}\right)^n = \] ______（\( a=1 \) 时得 \( e \)）<br>'
    r'\[ \lim_{x \to 0} \frac{\sin x}{x} = \] ______<br>'
    r'\[ \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = \] ______<br>'
    r'\[ \lim_{x \to 0} (1 + x)^{\frac{1}{x}} = \] ______',
    r'\[ \lim_{n \to \infty} \left(1 + \frac{a}{n}\right)^n = e^a \]<br>'
    r'\[ \lim_{x \to 0} \frac{\sin x}{x} = 1 \]<br>'
    r'\( e \)<br>\( e \)')

# ========== 函数极限::0/0型（方法）==========
add_group('数学回顾::函数极限::0/0型', '0/0型方法速查',
    r'主要工具：______ 和 ______<br><br>'
    r'| 情形 | 方法 |<br>'
    r'| 分母简单（如 \( 2x \)） | ______ |<br>'
    r'| 根号减根号 | ______；根号减无根号项也可尝试 |<br>'
    r'| \( \ln(1+f(x)) \) 展开 | ______ |<br>'
    r'| \( x^x \) 型 | 先提 \( x \)，再用 ______ 代换 |<br>'
    r'| 反三角函数 | ______ |<br>'
    r'| 拉格朗日中值定理型 | ______ |',
    r'泰勒公式、等价无穷小<br><br>'
    r'洛必达；导数难求用对数求导<br>'
    r'乘以共轭<br>'
    r'至少展开到 \( \dfrac{f(x)^2}{2} \)，否则可能丢精度<br>'
    r'\( e^{x\ln x} \)<br>'
    r'记住常用展开公式<br>'
    r'夹住两个函数确定中值项大小；能代入则代入，否则等价替换',
    method_example=
    r'\( \frac{\sqrt{x+1}-1}{x} \) → 乘共轭；\( \ln(1+x)-x \) → 展开到 \( -\frac{x^2}{2} \)。')

add_group('数学回顾::函数极限::∞/∞型', '∞/∞型要点',
    r'①【抓大头】\( e^x \) 类不能简单抓大头——底数微小扰动会______。<br>'
    r'②【其他工具】也可用______（可能给 \( f(0) \) 等具体值让你自己找）。倒代换：令 ______。<br>'
    r'③【海涅定理】令 \( x=\frac1n \)（______），则 \( n\to\infty \) 时 \( x\to 0^+ \)，'
    r'\( \displaystyle\lim_{n\to\infty} f\!\left(\frac1n\right) = \) ______。<br>'
    r'④【符号】\( \sqrt{x^2} = \) ______，注意符号。',
    r'① 非线性放大<br>② 拉格朗日中值定理；\( t=\frac1x \)<br>'
    r'③ 必须如此；\( \displaystyle\lim_{x\to 0^+} f(x) \)<br>④ \( |x| \)',
    method_example=
    r'\( \frac{2x^2+1}{3x^2-1}\to\frac23 \) 抓最高次；\( \frac{e^{1.001x}}{e^x}\to 1 \) 指数放大差异。')

add_group('数学回顾::函数极限::不定式', '其他不定式',
    r'∞−∞型：______、根式有理化、通分；可能需______（提出根号内分子，或处理无分母情形）<br>'
    r'\( 0^0 \)/\( \infty^0 \)：恒等变形 \( u^v = \) ______<br>'
    r'\( 1^\infty \)：化为 ______（指数乘上"底数减 1"）<br>'
    r'含绝对值：______',
    r'代换<br>提项<br>\( e^{v\ln u} \)<br>\( e^{v(u-1)} \)<br>分情况讨论',
    method_example=
    r'\( \sqrt{x^2+x}-x \) 有理化；\( x^x=e^{x\ln x} \)；\( \frac{|x|}{x} \) 在 \( x=0 \) 分左右。')

add_group('数学回顾::函数极限::导数定义求极限', '导数定义求极限',
    r'常见形 \( \frac{f(x+a)-f(x)}{a} \) 中，\( a \) 可能起______作用。<br>'
    r'①【标准形】应凑______，解 \( f\'(x) \)。<br>'
    r'②【两点差】\( f(x+a)-f(x+b) \)：应______配凑；或除以 \( f(\text{某式}) \) 再右边______。<br>'
    r'③【易错·局部凑】能否单独对小部分用？答：______。<br>'
    r'④【可导】左右导数存在且相等，极限须从______逼近且结果一致。',
    r'迷惑<br>① 导数定义<br>② 分开；乘回<br>③ 不能，必须整体凑定义<br>④ 双侧',
    method_example=
    r'\( \lim_{h\to 0}\frac{f(1+h)-f(1)}{h}=f\'(1) \)；\( |x| \) 在 0 处左右导数不等。')

# ========== 函数极限::三角处理（纯公式）==========
add_group('数学回顾::函数极限::三角处理', '三角平移公式',
    r'\( \sin(x - n\pi) = \) ______<br>'
    r'\( \cos(x - n\pi) = \) ______<br>'
    r'\( \tan(x - n\pi) = \) ______',
    r'\( (-1)^n \sin x \)<br>\( (-1)^n \cos x \)<br>\( \tan x \)')

add_group('数学回顾::函数极限::积分形式极限', '积分形式极限要点',
    r'①【多参数换元】换元时 \( x \) ______，变换______。<br>'
    r'②【化简技巧】尝试______，或直接在积分内部代入。<br>'
    r'③【中值代入】被夹住的中值 \( \xi \)，记得代入如 ______、\( \cos 0 \) 等。<br>'
    r'④【积分中值定理】\( \displaystyle\int_a^b f(x)\,dx = \) ______（此处掌握需加强）<br>'
    r'⑤【等价】积分上限趋于 0，被积函数在 0 附近等价 \( \Rightarrow \) 积分也______。<br>'
    r'⑥【二重变限】______，把最内层变量提出来。<br>'
    r'⑦【二重中值】\( \displaystyle\iint_D f = \) ______',
    r'① 不变；上下限<br>② 提出 \( e^x \)<br>③ \( e^0 \)<br>'
    r'④ \( f(\xi)(b-a) \)<br>⑤ 等价<br>⑥ 交换积分次序<br>⑦ \( f(\xi,\eta)\cdot S_D \)',
    method_example=
    r'\( \int_0^x\sin t\,dt \sim \frac{x^2}{2} \)（\( x\to 0 \)）；含参 \( \int_0^1 e^{tx}\,dt \) 令 \( u=tx \) 变限。')

# ========== 数列极限::积分形式 ==========
add_group('数学回顾::数列极限::积分形式', '积分形式数列极限',
    r'①【可积可化简】直接______后求极限。<br>'
    r'②【不可积不可化简】采用______，并用上下限逼近（\( n \to +\infty \)，或构造积分上下限对应的______）。',
    r'① 化简<br>② 积分中值定理；放缩',
    method_example=
    r'可积直接算；\( \lim\int_0^1\frac{x^n}{1+x}\,dx \) 用积分中值定理，别硬积。')

add_group('数学回顾::数列极限::积分形式::一看就别积分', '一看就别积分速查表',
    r'| 判定特征 | 典型例题 | 正确操作（❌ 别积分） |<br>'
    r'| 含 \( x^n \) | \( \int_0^1 \frac{x^n}{1+x}\,dx \) | ______ |<br>'
    r'| 含 \( e^{\pm nx} \) | \( \int_0^1 e^{-nx}\cos x\,dx \) | ______ |<br>'
    r'| 含 \( \sin^n x \) | \( \int_0^{\pi/2} \sin^n x\,dx \) | ______ |<br>'
    r'| 根号 + 幂次 | \( \int_0^1 \frac{x^n}{\sqrt{1+x^2}}\,dx \) | ______ |<br>'
    r'| 参数嵌分母 | \( \int_0^1 \frac{\ln(1+x)}{1+x^n}\,dx \) | ______ |',
    r'积分中值定理：\( \dfrac{\xi^n}{1+\xi} \to 0 \)<br>'
    r'积分中值定理：\( e^{-n\xi}\cos\xi \to 0 \)<br>'
    r'积分中值定理：\( \sin^n\xi \cdot \dfrac{\pi}{2} \to 0 \)<br>'
    r'放缩：\( 0 \leq \cdots \leq \int_0^1 x^n\,dx = \dfrac{1}{n+1} \to 0 \)<br>'
    r'放缩 + 分段估计（极限 \( = \ln 2 \)）',
    method_example=
    r'见笔记典型题：\( \int_0^1\frac{x^n}{1+x} \)、\( \int_0^1\frac{\ln(1+x)}{1+x^n} \) 等。')

# ========== 数列极限::经典极限与不等式（纯公式）==========
add_group('数学回顾::数列极限::n项和::经典极限与不等式', '经典数列极限',
    r'\[ \lim_{n \to \infty} \sqrt[n]{a} = \] ______（\( a > 0 \)）<br>'
    r'\[ \lim_{n \to \infty} \sqrt[n]{n} = \] ______',
    r'\( 1 \)<br>\( 1 \)')

add_group('数学回顾::数列极限::n项和::经典极限与不等式', '常用不等式',
    r'\( \sin x \) ______ \( x \) ______ \( \tan x \)（\( 0 < x < \dfrac{\pi}{2} \)）<br>'
    r'\( \dfrac{2}{\pi}x \) ______ \( \sin x \) ______ \( x \) ______ \( \dfrac{\pi}{2}\sin x \)（\( 0 < x < \dfrac{\pi}{2} \)）<br>'
    r'\( e^x \) ______ \( 1 + x \)（\( x \neq 0 \)）<br>'
    r'\( \dfrac{x}{1+x} \) ______ \( \ln(1+x) \) ______ \( x \)（\( x > -1,\ x \neq 0 \)）',
    r'\( < \) \( < \) \( < \)<br>\( < \) \( < \) \( < \) \( < \)<br>\( > \)<br>\( < \) \( < \) \( < \)')

# ========== 数列极限::黎曼和/夹逼（方法）==========
add_group('数学回顾::数列极限::n项和::黎曼和', '黎曼和步骤与取点',
    r'步骤：① 凑 ______（\( i=1,2,\ldots,n \)）  ② 起止换 ______、______（有限项不影响极限）'
    r'  ③ 最后的 \( \dfrac{x}{n} \) 是区间 \( [a,b] \) 的每一小段<br><br>'
    r'| 取点 \( \xi_i \) | Riemann 和 | 分割 |<br>'
    r'| \( \dfrac{i}{n} \) | \( \sum f\!\left(\dfrac{i}{n}\right)\cdot\dfrac{1}{n} \) | ______ |<br>'
    r'| \( \dfrac{i-1}{n} \) | \( \sum f\!\left(\dfrac{i-1}{n}\right)\cdot\dfrac{1}{n} \) | 左端点 |<br>'
    r'| \( \dfrac{2i-1}{2n} \) | \( \sum f\!\left(\dfrac{2i-1}{2n}\right)\cdot\dfrac{1}{n} \) | 中点 |<br><br>'
    r'关键：\( f \) 在 \( [a,b] \) 上可积（通常连续即可），三种取点极限______，都等于 ______。<br>'
    r'需要 \( \dfrac{i}{n} \) 的系数为 ______ 才能保证一一对应。',
    r'① \( \dfrac{i}{n} \)；\( 1 \)；\( m \)<br>'
    r'右端点，\( [0,1] \) 等分<br><br>'
    r'完全相同；\( \displaystyle\int_a^b f(x)\,dx \)；\( 1 \)',
    method_example=
    r'\( \sum\frac{i}{n}\cdot\frac1n \to \int_0^1 x\,dx=\frac12 \)；'
    r'\( \sum\left(\frac{i}{n}\right)^2\frac1n \to \frac13 \)。')

add_group('数学回顾::数列极限::n项和::夹逼定理', '夹逼定理',
    r'先______，再用上述黎曼和处理<br>'
    r'在 \( i^2 \) 前配 \( c_n \)（______），令 \( \dfrac{i}{n^2+n+c_n i^2} = k_n \cdot \dfrac{i}{n^2+i^2} \)<br>'
    r'或变成 \( i+a \) 消去 \( \dfrac{i+k}{n} \) 中的无关系数 ______',
    r'放缩<br>不能动 \( n^2 \)，积分值会变<br>\( k \)',
    method_example=
    r'\( \sum\frac{1}{n^2+i^2} \) 先放缩，再化为 \( \int_0^1\frac{1}{1+x^2}\,dx \)。')

add_group('数学回顾::数列极限::n项和::夹逼定理', '主动构造',
    r'\( 1 = \) ______<br>'
    r'\( 1 - \dfrac{1}{n+1} = \) ______<br>'
    r'\( \dfrac{1}{3} = \) ______',
    r'\[ 1 = \sum_{k=1}^{n} \frac{1}{n} \]<br>'
    r'\[ 1 - \frac{1}{n+1} = \sum_{k=1}^{n} \frac{1}{k(k+1)} \]<br>'
    r'\[ \frac{1}{3} = \sum_{k=1}^{n} \left(\frac{k}{n}\right)^2 \cdot \frac{1}{n} \]')

add('数学回顾::数列极限::n项和::二重积分',
    '【变成二重积分】提出 ______，积分区间变化后得到 \( j \) 和 \( i \) 的等式，'
    '把 \( y \) 代入 ______、\( x \) 代入 ______，得到 \( x \) 与 \( y \) 的关系（积分区域）。',
    r'\( \dfrac{1}{n^2} \)；\( \dfrac{j}{n} \)；\( \dfrac{i}{n} \)<br><br>'
    r'<b>例（方法）</b><br>'
    r'提出 \( \frac1{n^2} \)，令 \( x=\frac{i}{n}, y=\frac{j}{n} \) 确定区域再积分。')

add_group('数学回顾::数列极限::n次根号或乘积', 'n次根号或乘积',
    r'\( n \) 次根号下 \( n \) 次方的值 \( \to \) ______；无穷多项时也找最大值，可能用______。<br>'
    r'乘积取对数 \( \to \) 变成______',
    r'最大值<br>单调性<br>求和',
    method_example=
    r'\( \sqrt[n]{1^n+2^n+3^n}\to 3 \) 取最大底；\( \prod(1+\frac1k) \) 取对数变求和。')

# ========== 数列极限::递推（公式+方法）==========
add_group('数学回顾::数列极限::递推数列', '等价代换与施托尔兹',
    r'\( n! \sim \sqrt{2\pi n}\left(\dfrac{n}{e}\right)^n \sim \) ______<br>'
    r'\( (\sqrt{2\pi n})^{1/n} \to \) ______（\( n \to \infty \)）<br>'
    r'施托尔兹（数列版洛必达，\( b_n \) ______）：'
    r'\( \displaystyle\lim\frac{a_n}{b_n} = \lim\frac{a_{n+1}-a_n}{b_{n+1}-b_n} \)<br>'
    r'推广（\( x_n>0 \)，右端极限存在）：\( \displaystyle\lim\sqrt[n]{x_n} = \lim \) ______',
    r'\( \dfrac{\sqrt{2\pi n}}{e^n}\cdot n^n \)<br>\( 1 \)<br>'
    r'\( \nearrow +\infty \)<br>\( \displaystyle\lim\frac{x_{n+1}}{x_n} \)')

add_group('数学回顾::数列极限::递推数列', '单调有界与存在性',
    r'①【存在性】______必存在（单调性若求导不好证，可用______证明）。<br>'
    r'②【极限方程】对 \( x_{n+1}=f(x_n) \)，若收敛，极限 \( a \) 必满足 \( a=f(a) \)，'
    r'解方程并结合______筛选。<br>'
    r'③【例】\( x_{n+1}=\sqrt{6+x_n} \)：\( a=\sqrt{6+a} \) 得 \( a=3 \) 或 \( -2 \)，由根号非负舍去 ______，极限 = ______。',
    r'① 单调有界；定义<br>② 实际意义<br>③ \( -2 \)；\( 3 \)',
    method_example=
    r'\( x_1=1, x_{n+1}=\sqrt{6+x_n} \)：证单调有界 → 令 \( a=\sqrt{6+a} \) 得 \( a=3 \) 或 \( -2 \)，舍 \( -2 \)。')

add('数学回顾::数列极限::暂不深入',
    '【暂不深入】以下题型目前不花时间研究：<br>'
    '① 数列收敛/发散/有界/无界（构造交错 ______ 或 \( \sin n \) 等即可）<br>'
    '② 数列极限的______问题<br>'
    '③ 数列无穷小______<br>'
    '④ ______',
    r'① \( 1,-1,1,-1 \)<br>② 最值<br>③ 比阶<br>④ 证明题<br><br>'
    r'<b>例（方法）</b><br>'
    r'\( a_n=(-1)^n \) 发散；\( \sin n \) 有界无极限——构造反例即可。')

add_group('数学回顾::渐近线', '渐近线基本方法',
    r'【斜率】\( k = \displaystyle\lim_{x\to\infty}\frac{f(x)}{x} \)（把函数"拉平"成一次函数，一次项系数 = ______）<br>'
    r'【截距】\( b = \displaystyle\lim_{x\to\infty}[f(x)-kx] \)，斜渐近线 \( y = \) ______<br>'
    r'【垂直渐近线】找图像在垂直方向"无限逼近但不接触"的直线；口诀：找无定义点 → 极限是否为 ______（可能从左右两侧逼近）<br>'
    r'【水平渐近线】分别看 \( x\to\pm\infty \) 的极限是否为有限数（如 \( e^x \) 两侧不同）<br>'
    r'已有水平渐近线（同侧 \( x\to\infty \)），则通常______斜渐近线',
    r'斜率<br>\( kx+b \)<br>\( \infty \)<br>无斜渐近线',
    method_example=
    r'\( f(x)=\frac{2x^2+1}{x} \) 斜渐近线 \( y=2x \)；\( \frac1x \) 垂直渐近线 \( x=0 \)。')

add_group('数学回顾::渐近线::斜渐近线特殊方法', '斜渐近线拆分法',
    r'①【证明】用______（斜率为 0 或不存在则无斜渐近线）；已知存在时用拆分法<br>'
    r'②【拆分】强行拆成"直线部分 + 无穷小部分"：\( f=\alpha x+\beta+\gamma(x) \)，\( \gamma\to 0 \)，则 \( y= \) ______<br>'
    r'③【展开对象】______（如 \( \dfrac{1}{x} \)、\( x-a \) 等）<br>'
    r'④【\( x\to\infty \) 代换】\( (1+x)^\alpha = x^\alpha\left(1+\dfrac{1}{x}\right)^\alpha \)，遇 \( x\to\infty \) 时先做______<br>'
    r'⑤【有理函数】做______，拆成「一次多项式 + 趋于 0 的余项」，______即得斜渐近线',
    r'① 定义法<br>② \( \alpha x+\beta \)<br>③ 趋于 0 的小量<br>④ 代换<br>⑤ 多项式长除法；丢掉余项',
    method_example=
    r'\( \frac{x^2+1}{x}=x+\frac1x \)，斜渐近线 \( y=x \)；长除法丢余项。')

add('数学回顾::极限等式',
    '【极限等式】若极限存在，则 \( A \) 是______，可用于反推未知参数。',
    '一个<b>确定的实数</b><br><br>'
    '<b>例（方法）</b><br>'
    r'\( \lim_{x\to 1}(ax+b)=2 \Rightarrow a+b=2 \)，联立求参数。')

add_group('数学回顾::无穷小', '无穷小',
    r'\( f(x) = o(x^k) \)（\( x \to 0 \)）\( \iff \lim\frac{f}{x^k} = \) ______<br>'
    r'（要严格用此式证明，否则______）<br>'
    r'\( \lim\frac{\beta}{\alpha}=0 \Rightarrow \) ______是______的______'
    r'（记忆：\( x^3/x^2 \to 0 \)，\( x^3 \) 是 \( x^2 \) 的______）<br>'
    r'极限为 0 的数列/函数称为______（常数列 0 是无穷小）',
    r'\( 0 \)<br>容易出错<br>\( \beta \)；\( \alpha \)；高阶无穷小；高阶无穷小<br>无穷小',
    method_example=
    r'证 \( x^2=o(x) \)：算 \( \lim\frac{x^2}{x}=0 \)；\( x^3 \) 是 \( x^2 \) 的高阶无穷小。')

add_group('数学回顾::无穷大', '无穷大',
    r'\( x\sin x \)："______"（可取特殊数列说明无界或极限不存在）<br>'
    r'\( \dfrac{\sin x}{x} \)："______"（有界；\( x\to\infty \) 时极限为 0）<br>'
    r'对 \( x\sin x \)：取特殊数列经过 \( \sin x = 0 \) 的点，从而说明______或极限不存在',
    r'扩音器<br>缩音器<br>无界',
    method_example=
    r'取 \( x_n=n\pi \) 使 \( x_n\sin x_n=0 \)，再取 \( y_n=n\pi+\frac\pi2 \) 使趋于无穷 → 无界。')

# ========== 泰勒（公式直接记；使用条件属方法）==========
add_group('数学回顾::泰勒多项式', '泰勒多项式概念',
    r'泰勒级数：\( f(x) = \sum\frac{f^{(n)}(a)}{n!}(x-a)^n \)<br>'
    r'\( f^{(n)}(a) \) = ______，\( n! \) = ______<br>'
    r'常说的泰勒展开大多是______（在 ______ 处）',
    r'n 阶导数；n 的阶乘<br>麦克劳林；\( x=0 \)')

add_group('数学回顾::泰勒多项式::使用条件', '泰勒使用条件',
    r'①【麦克劳林前提】变量趋于 ______，只能在______上使用。<br>'
    r'②【ln 展开精度】\( \ln(1+f(x)) \) 至少展开到 ______，否则将______。<br>'
    r'③【易错·x→∞】\( (1+x)^{1/x} \) 当 \( x\to\infty \) 时，能否直接套用麦克劳林？答：______。'
    r'（\( x \) 不是无穷小，______中也含 \( x \)）<br>'
    r'④【正确做法】先取对数化为 ______，把 ______ 视为无穷小量展开，再还原指数。',
    r'① \( 0 \)；无穷小量<br>② \( \frac{f(x)^2}{2} \)；丢精度<br>③ 不能；指数<br>'
    r'④ \( \exp\!\left(\frac{\ln(1+x)}{x}\right) \)；\( \frac{1}{x} \)',
    method_example=
    r'\( (1+x)^{1/x} \) 当 \( x\to\infty \)：不能直套；先取对数，令 \( t=\frac1x\to 0 \) 再展开。')

add_group('数学回顾::泰勒多项式::一般形式', '泰勒一般形式',
    r'佩亚诺余项：\( f=\cdots + \) ______<br>'
    r'拉格朗日余项：\( R_n = \) ______，\( \xi \) ______',
    r'\( o\bigl((x-a)^n\bigr) \)<br>'
    r'\( \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1} \)；介于 a 与 x 之间')

taylor_sections = {
    '指数与对数': [
        (r'e^x', r'e^x = 1 + x + \frac{x^2}{2!} + \cdots + \frac{x^n}{n!} + o(x^n)'),
        (r'a^x', r'a^x = e^{x\ln a} = 1 + x\ln a + \frac{(x\ln a)^2}{2!} + \cdots + o(x^n)'),
        (r'\ln(1+x)', r'\ln(1+x) = x - \frac{x^2}{2} + \cdots + (-1)^{n-1}\frac{x^n}{n} + o(x^n)'),
        (r'\ln(1-x)', r'\ln(1-x) = -\left(x + \frac{x^2}{2} + \cdots\right) + o(x^n)'),
    ],
    '三角函数': [
        (r'\sin x', r'\sin x = x - \frac{x^3}{3!} + \cdots + (-1)^n\frac{x^{2n+1}}{(2n+1)!} + o(x^{2n+1})'),
        (r'\cos x', r'\cos x = 1 - \frac{x^2}{2!} + \cdots + (-1)^n\frac{x^{2n}}{(2n)!} + o(x^{2n})'),
        (r'\tan x', r'\tan x = x + \frac{x^3}{3} + \frac{2x^5}{15} + o(x^5)'),
        (r'\arcsin x', r'\arcsin x = x + \frac{x^3}{6} + \frac{3x^5}{40} + o(x^5)'),
        (r'\arctan x', r'\arctan x = x - \frac{x^3}{3} + \cdots + (-1)^n\frac{x^{2n+1}}{2n+1} + o(x^{2n+1})'),
    ],
    '幂函数与二项式': [
        (r'(1+x)^\alpha', r'(1+x)^\alpha = 1 + \alpha x + \cdots + \frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}x^n + o(x^n)'),
        (r'\frac{1}{1+x}', r'\frac{1}{1+x} = 1 - x + x^2 + \cdots + (-1)^n x^n + o(x^n)'),
        (r'\frac{1}{1-x}', r'\frac{1}{1-x} = 1 + x + x^2 + \cdots + x^n + o(x^n)'),
        (r'\sqrt{1+x}', r'\sqrt{1+x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \frac{x^3}{16} + o(x^3)'),
        (r'\frac{1}{\sqrt{1+x}}', r'\frac{1}{\sqrt{1+x}} = 1 - \frac{x}{2} + \frac{3x^2}{8} - \frac{5x^3}{16} + o(x^3)'),
    ],
    '双曲函数': [
        (r'\sinh x', r'\sinh x = x + \frac{x^3}{3!} + \cdots + o(x^{2n+1})'),
        (r'\cosh x', r'\cosh x = 1 + \frac{x^2}{2!} + \cdots + o(x^{2n})'),
    ],
}
for section, items in taylor_sections.items():
    front_lines = [rf'\( {name} \) = ______' for name, _ in items]
    back_lines = [rf'\[ {formula} \]' for _, formula in items]
    add_group(f'数学回顾::泰勒多项式::{section}', f'{section}麦克劳林展开',
              '<br>'.join(front_lines), '<br>'.join(back_lines))

add_group('数学回顾::泰勒多项式::求极限常用', '求极限常用泰勒（二阶/三阶）',
    r'\( e^x \) = ______ + \( o(x^2) \)<br>'
    r'\( \ln(1+x) \) = ______ + \( o(x^2) \)<br>'
    r'\( \sin x \) = ______ + \( o(x^3) \)<br>'
    r'\( \cos x \) = ______ + \( o(x^2) \)<br>'
    r'\( \tan x \) = ______ + \( o(x^3) \)<br>'
    r'\( (1+x)^\alpha \) = ______ + \( o(x^2) \)<br>'
    r'\( \arcsin x \) = ______ + \( o(x^3) \)<br>'
    r'\( \arctan x \) = ______ + \( o(x^3) \)',
    r'\( 1 + x + \dfrac{x^2}{2} \)<br>'
    r'\( x - \dfrac{x^2}{2} \)<br>'
    r'\( x - \dfrac{x^3}{6} \)<br>'
    r'\( 1 - \dfrac{x^2}{2} \)<br>'
    r'\( x + \dfrac{x^3}{3} \)<br>'
    r'\( 1 + \alpha x + \dfrac{\alpha(\alpha-1)}{2}x^2 \)<br>'
    r'\( x + \dfrac{x^3}{6} \)<br>'
    r'\( x - \dfrac{x^3}{3} \)')

# ========== 写入 apkg ==========
for deck_path, front, back, tag in cards_data:
    note = genanki.Note(model=model, fields=[front, back], tags=[tag.replace(' ', '_')])
    get_deck(deck_path).add_note(note)

base = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(base, '数学回顾要点-Anki.apkg')
genanki.Package(list(decks.values())).write_to_file(out_path)

counts = Counter(d for d, _, _, _ in cards_data)
print(f'已生成 {len(cards_data)} 张卡片 -> {out_path}')
print('公式：\\( ... \\) / \\[ ... \\]，Anki 2.1+ 自动 MathJax 渲染')
print('\n章节分布：')
for path in sorted(counts.keys()):
    print(f'  {path}: {counts[path]} 张')

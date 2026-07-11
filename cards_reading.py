# -*- coding: utf-8 -*-
"""阅读卡：完整呈现笔记要点，供理解记忆（非填空）。"""


def register_reading(read):
    """read(deck_path, section_title, html_body, tag)"""

    def R(deck, title, body, tag):
        front = f'<b>{title}</b><br><br>{body}'
        read(deck, front, '', f'read-{tag}')

    # ---------- 记忆 ----------
    R('数学回顾::记忆', '记忆',
      r'知识点是<b>有限</b>的，题是<b>无限</b>的。<br>'
      r'真正要掌握的，不是题，而是<b>一般方法</b>（定题型 → 选工具）。',
      'mem')

    # ---------- 常用公式 ----------
    R('数学回顾::常用公式速查::代数与三角', '代数与三角公式表',
      r'<table><tr><th>名称</th><th>公式</th></tr>'
      r'<tr><td>立方差</td><td>\( a^3-b^3=(a-b)(a^2+ab+b^2) \)</td></tr>'
      r'<tr><td>立方和</td><td>\( a^3+b^3=(a+b)(a^2-ab+b^2) \)</td></tr>'
      r'<tr><td>立方和特例</td><td>\( x^3+1=(x+1)(x^2-x+1) \)</td></tr>'
      r'<tr><td>正弦二倍角</td><td>\( \sin2\alpha=2\sin\alpha\cos\alpha \)</td></tr>'
      r'<tr><td>余弦二倍角</td><td>\( \cos2\alpha=\cos^2\alpha-\sin^2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha \)</td></tr>'
      r'<tr><td>正切二倍角</td><td>\( \tan2\alpha=\dfrac{2\tan\alpha}{1-\tan^2\alpha} \)</td></tr>'
      r'<tr><td>降幂</td><td>\( \sin^2\alpha=\dfrac{1-\cos2\alpha}{2} \)，\( \cos^2\alpha=\dfrac{1+\cos2\alpha}{2} \)</td></tr>'
      r'</table>',
      'alg')

    R('数学回顾::常用公式速查::绝对值三角不等式', '绝对值三角不等式',
      r'\[ \bigl| |a_n| - |a| \bigr| \leq |a_n - a| \]<br>'
      r'常用于数列收敛证明。若另有 \( |a_n-a| \lt \dfrac{|a|}{2} \)，才可进一步估计 \( |a_n| \) 与 \( |a| \) 的差。',
      'tri')

    # ---------- 函数 ----------
    R('数学回顾::函数::奇偶性', '奇偶性',
      r'• 偶函数的原函数<b>不一定是</b>奇函数；只有积分区间为 \( [0,x] \) 时，偶函数的原函数才是奇函数。（哦!飞机）<br>'
      r'• 可通过求导处理含积分的函数，但原函数符号与预期<b>相反</b>。<br>'
      r'• 无从下手时，回到奇偶性的定义来分析。',
      'odd')

    R('数学回顾::函数::周期性', '周期性',
      r'• 若 \( f \) 以 \( T \) 为周期且可积，则 \( \int_0^T f=0 \Leftrightarrow \) 其原函数也以 \( T \) 为周期。<br>'
      r'• 嵌套分段函数：先分析<b>外层</b>，内层不同值对应外层不同分段。<br>'
      r'• 周期内图像相同、整体平移，可用 \( y=f(ax) \) 理解。<br>'
      r'• 计算困难时，回到周期函数的定义。',
      'per')

    R('数学回顾::函数::有界性', '有界性',
      '• 区间端点<b>取不到</b>时，必须考察端点的极限。<br>'
      '• 存在子列使函数值趋于无穷 → 该点附近<b>无界</b>。<br>'
      r'• 极限不存在<b>不能</b>直接判无界。例：\( \sin\dfrac{1}{x} \) 在 \( x\to0 \) 极限不存在，但在去心邻域内有界。',
      'bnd')

    # ---------- 连续与间断 ----------
    R('数学回顾::连续与间断点::四则运算', '连续函数四则运算',
      r'<table><tr><th>运算</th><th>结论</th><th>注意</th></tr>'
      r'<tr><td>加减</td><td>\( f\pm g \) 连续</td><td>✅</td></tr>'
      r'<tr><td>乘法</td><td>\( f\cdot g \) 连续</td><td>✅</td></tr>'
      r'<tr><td>除法</td><td>\( f/g \) 连续</td><td>⚠️ \( g(x_0)\neq0 \)</td></tr>'
      r'<tr><td>常数倍</td><td>\( Cf \) 连续</td><td>✅</td></tr></table>',
      'cont')

    R('数学回顾::连续与间断点::间断点分类', '间断点分类',
      r'<table><tr><th>类型</th><th>比喻</th><th>特征</th></tr>'
      r'<tr><td>可去</td><td>断桥</td><td>左右极限相等 ≠ 函数值</td></tr>'
      r'<tr><td>跳跃</td><td>台阶</td><td>左右极限不等</td></tr>'
      r'<tr><td>无穷</td><td>深渊</td><td>极限 \( \pm\infty \)</td></tr>'
      r'<tr><td>振荡</td><td>吊桥</td><td>极限不存在，也不趋于无穷</td></tr></table>',
      'disc')

    # ---------- 函数极限 ----------
    D = '数学回顾::函数极限::概念题'
    R(D, '连续的定义',
      r'\( \lim_{x\to x_0}f(x)=f(x_0) \)，且 \( f(x_0) \) 存在，极限存在并相等。<br>'
      r'连续<b>只保证在 \( x_0 \) 这一点</b>，不保证周围点也连续（可去间断点）。',
      'con-def')
    R(D, '极限存在的前提',
      '在某个<b>去心邻域</b>内，函数必须处处有定义。',
      'con-pre')
    R(D, '保号性',
      r'<table><tr><th>方向</th><th>条件</th><th>结论</th></tr>'
      r'<tr><td>正向</td><td>\( A\gt 0 \)（或 \( A\lt 0 \)）</td><td>去心邻域内 \( f(x)\gt 0 \)（或 \( \lt 0 \)）</td></tr>'
      r'<tr><td>逆向</td><td>邻域内 \( f\geq0 \)（或 \( \leq0 \)），极限存在</td><td>\( A\geq0 \)（或 \( \leq0 \)）</td></tr></table>'
      r'<br>⚠️ \( f(x)\gt 0 \) 严格成立也只能得 \( A\geq0 \)，不能得 \( A\gt 0 \)。可推广到 \( x\to\infty \)。',
      'sgn')
    R(D, '其他要点',
      r'• 极限反映趋近时的行为，不是点值或区间值。<br>'
      r'• 「极限大」→ 去心邻域内函数值大（保号性）。<br>'
      r'• 「邻域内大」→ 只能得极限 \( \geq \)，不能得 \( > \)。<br>'
      r'• 未说明极限等于某数 → 不一定极限存在。<br>'
      r'• 判 \( a_n \) 与 \( a \)：用 \( \varepsilon \)-N 定义。',
      'con-oth')

    R('数学回顾::函数极限::重要极限', '重要极限',
      r'\[ \lim_{n\to\infty}\left(1+\frac{a}{n}\right)^n=e^a \quad (a=1 \Rightarrow e) \]<br>'
      r'\[ \lim_{x\to0}\frac{\sin x}{x}=1 \]<br>'
      r'\[ \lim_{x\to0}(1+x)^{1/x}=e,\quad \lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n=e \]',
      'imp')

    R('数学回顾::函数极限::0/0型', '0/0 型方法速查',
      r'主工具：<b>泰勒</b>、<b>等价无穷小</b>。<br><table>'
      r'<tr><th>情形</th><th>方法</th></tr>'
      r'<tr><td>分母简单（如 \( 2x \)）</td><td>洛必达；导数难求用对数求导</td></tr>'
      r'<tr><td>根号减根号</td><td>乘共轭；根号减无根号项也可试</td></tr>'
      r'<tr><td>\( \ln(1+f(x)) \)</td><td>至少展到 \( \dfrac{f^2}{2} \)</td></tr>'
      r'<tr><td>\( x^x \)</td><td>先提 \( x \)，再 \( e^{x\ln x} \)</td></tr>'
      r'<tr><td>反三角</td><td>记常用展开</td></tr>'
      r'<tr><td>拉格朗日型</td><td>夹住中值项；能代入则代入</td></tr></table>',
      'z0')

    R('数学回顾::函数极限::∞/∞型', '∞/∞ 型',
      r'• <b>抓大头</b>：不能对 \( e^x \) 简单抓大头（指数非线性放大）。<br>'
      r'• 可用拉格朗日（可能给 \( f(0) \) 让你自己找）。<br>'
      r'• <b>倒代换</b>：\( t=\dfrac{1}{x} \)。<br>'
      r'• <b>海涅</b>：\( x=\dfrac{1}{n} \)（必须），\( n\to\infty \Leftrightarrow x\to0^+ \)。<br>'
      r'• \( \sqrt{x^2}=|x| \)，注意符号。',
      'zi')

    R('数学回顾::函数极限::∞-∞型', '∞−∞ 型',
      r'主要：代换、根式有理化、<b>通分</b>。可能需<b>提项</b>（提出根号内分子等）。',
      'zm')

    R('数学回顾::函数极限::0^0与∞^0', '0^0 与 ∞^0',
      r'恒等变形：\( u^v=e^{v\ln u} \)。',
      'zp')

    R('数学回顾::函数极限::1^∞型', '1^∞ 型',
      r'化为 \( e^{v(u-1)} \)（指数乘「底数减 1」）。',
      'z1')

    R('数学回顾::函数极限::含e与绝对值', '含 e 与绝对值',
      r'• 绝对值：<b>分情况</b>讨论左右。<br>'
      r'• 经典：\( \left(1+\dfrac{1}{n}\right)^n\to e \)，\( (1+x)^{1/x}\to e \)。',
      'ze')

    R('数学回顾::函数极限::导数定义求极限', '导数定义求极限',
      r'常见 \( \dfrac{f(x+a)-f(x)}{a} \) 中 \( a \) 可能起<b>迷惑</b>作用。<br>'
      r'• 凑导数定义解 \( f\'(x) \)。<br>'
      r'• \( f(x+a)-f(x+b) \) 分开配凑；或除以 \( f \) 某式再乘回。<br>'
      r'• <b>不能</b>只对局部凑，必须整体。<br>'
      r'• 可导：左右导数存在且相等，双侧逼近一致。',
      'der')

    R('数学回顾::函数极限::三角处理', '三角平移',
      r'\( \sin(x-n\pi)=(-1)^n\sin x \)，\( \cos(x-n\pi)=(-1)^n\cos x \)，\( \tan(x-n\pi)=\tan x \)',
      'trig')

    R('数学回顾::函数极限::积分形式极限', '积分形式极限',
      r'• 多参数换元：\( x \) 不变，变上下限。<br>'
      r'• 可提 \( e^x \)；中值 \( \xi \) 代入 \( e^0,\cos0 \)。<br>'
      r'• 积分中值：\( \int_a^b f=f(\xi)(b-a) \)。<br>'
      r'• 上限 \( \to0 \) 时被积函数等价 → 积分等价。<br>'
      r'• 二重变限：交换次序，提出最内层。<br>'
      r'• 二重中值：\( \iint_D f=f(\xi,\eta)\cdot S_D \)。',
      'intl')

    # ---------- 数列极限 ----------
    R('数学回顾::数列极限::积分形式', '以积分形式给出',
      r'<b>可积可化简</b>：直接化简后求极限。<br>'
      r'<b>不可积</b>：积分中值定理 + 上下限放缩（\( n\to+\infty \)）。',
      'seqi')

    R('数学回顾::数列极限::积分形式::一看就别积分', '一看就别积分速查表',
      '<table><tr><th>特征</th><th>典型例题</th><th>操作</th></tr>'
      r'<tr><td>\( x^n \)</td><td>\( \int_0^1\dfrac{x^n}{1+x} \)</td><td>中值 \( \dfrac{\xi^n}{1+\xi}\to0 \)</td></tr>'
      r'<tr><td>\( e^{\pm nx} \)</td><td>\( \int_0^1 e^{-nx}\cos x \)</td><td>中值 \( e^{-n\xi}\cos\xi\to0 \)</td></tr>'
      r'<tr><td>\( \sin^n x \)</td><td>\( \int_0^{\pi/2}\sin^n x \)</td><td>中值 \( \sin^n\xi\cdot\dfrac{\pi}{2}\to0 \)</td></tr>'
      r'<tr><td>根号+幂次</td><td>\( \int_0^1\dfrac{x^n}{\sqrt{1+x^2}} \)</td><td>放缩至 \( \int_0^1 x^n\to0 \)</td></tr>'
      r'<tr><td>参数分母</td><td>\( \int_0^1\dfrac{\ln(1+x)}{1+x^n} \)</td><td>放缩+分段 → \( \ln2 \)</td></tr></table>',
      'noint')

    R('数学回顾::数列极限::n项和::经典极限与不等式', '经典极限与不等式',
      r'\( \lim\sqrt[n]{a}=1,\ \lim\sqrt[n]{n}=1 \)（\( a>0 \)）<br>'
      r'\( \sin x\lt x\lt \tan x \)，\( \dfrac{2}{\pi}x\lt\sin x\lt x\lt \dfrac{\pi}{2}\sin x \)（\( 0\lt x\lt \dfrac{\pi}{2} \)）<br>'
      r'\( e^x\gt 1+x \)，\( \dfrac{x}{1+x}\lt\ln(1+x)\lt x \)（\( x\gt -1,x\neq0 \)）',
      'ineq')

    R('数学回顾::数列极限::n项和::黎曼和', '黎曼和',
      r'1. 凑 \( \dfrac{i}{n} \)　2. 起止改 \( 1,m \)（有限项不影响）　3. \( \dfrac{1}{n} \) 为小区间长度<br>'
      r'<table><tr><th>取点</th><th>和式</th><th>分割</th></tr>'
      r'<tr><td>\( i/n \)</td><td>\( \sum f(i/n)\cdot 1/n \)</td><td>右端点 [0,1]</td></tr>'
      r'<tr><td>\( (i-1)/n \)</td><td>\( \sum f((i-1)/n)\cdot 1/n \)</td><td>左端点</td></tr>'
      r'<tr><td>\( (2i-1)/2n \)</td><td>\( \sum f((2i-1)/2n)\cdot 1/n \)</td><td>中点</td></tr></table>'
      r'<br>左/右/中点极限相同 \( =\int_a^b f \)；\( i/n \) 系数须为 <b>1</b>。',
      'rim')

    R('数学回顾::数列极限::n项和::夹逼定理', '夹逼定理',
      r'先放缩，再黎曼和。<br>'
      r'• \( i^2 \) 前配 \( c_n \)（<b>不能动 \( n^2 \)</b>）。<br>'
      r'• 或变成 \( i+a \) 消去 \( \dfrac{i+k}{n} \) 中的 \( k \)。<br>'
      r'主动构造：\( 1=\sum\dfrac{1}{n} \)，\( 1-\dfrac{1}{n+1}=\sum\dfrac{1}{k(k+1)} \)，\( \dfrac{1}{3}=\sum\left(\dfrac{k}{n}\right)^2\dfrac{1}{n} \)。',
      'sqz')

    R('数学回顾::数列极限::n项和::二重积分', '二重积分定义',
      r'提出 \( \dfrac{1}{n^2} \)；\( x=\dfrac{i}{n},\,y=\dfrac{j}{n} \) 确定积分区域。',
      'dbl')

    R('数学回顾::数列极限::n次根号或乘积', 'n 次根号或乘积',
      r'\( n \) 次根下 \( n \) 次方的和 → <b>最大值</b>；无穷多项也抓最大，可用单调性。<br>'
      '乘积 → 取对数变求和。',
      'root')

    R('数学回顾::数列极限::递推数列', '递推数列（单调有界）',
      r'\( n!\sim\sqrt{2\pi n}\left(\dfrac{n}{e}\right)^n \)，\( (\sqrt{2\pi n})^{1/n}\to1 \)<br>'
      r'施托尔兹：\( \lim\dfrac{a_n}{b_n}=\lim\dfrac{a_{n+1}-a_n}{b_{n+1}-b_n} \)（\( b_n\nearrow+\infty \)）<br>'
      r'推广：\( \lim\sqrt[n]{x_n}=\lim\dfrac{x_{n+1}}{x_n} \)（\( x_n>0 \)，右端极限存在）<br>'
      r'• 单调有界必存在；单调性可用定义证。<br>'
      r'• 收敛则 \( a=f(a) \)，结合实际意义筛根。<br>'
      r'例：\( x_{n+1}=\sqrt{6+x_n} \) → \( a=3 \)（舍 \( -2 \)）。',
      'rec')

    R('数学回顾::数列极限::暂不深入', '暂不深入',
      '暂不深挖：数列收敛/发散/有界构造（\( (-1)^n,\sin n \)）、最值、比阶、证明题。',
      'skip')

    # ---------- 渐近线 ----------
    R('数学回顾::渐近线::基本方法', '斜渐近线（定义法）',
      r'\( k=\lim\dfrac{f(x)}{x} \)（把函数「拉平」后的一次项系数）<br>'
      r'\( b=\lim[f(x)-kx] \) → 斜渐近线 \( y=kx+b \)。',
      'asy-k')

    R('数学回顾::渐近线::垂直渐近线', '垂直渐近线',
      '找无定义点 → 看极限是否为 \( \pm\infty \)（可能从左右两侧逼近）。',
      'asy-v')

    R('数学回顾::渐近线::水平渐近线', '水平渐近线',
      r'分别算 \( x\to+\infty \) 与 \( x\to-\infty \) 的极限（如 \( e^x \) 两侧不同）。<br>'
      '若已存在水平渐近线（同侧），通常无斜渐近线。',
      'asy-h')

    R('数学回顾::渐近线::斜渐近线特殊方法', '斜渐近线拆分法',
      r'\( f=\alpha x+\beta+\gamma(x) \)，\( \gamma\to0 \) → \( y=\alpha x+\beta \)。<br>'
      r'展开对象是趋于 0 的小量。\( (1+x)^\alpha=x^\alpha\left(1+\dfrac{1}{x}\right)^\alpha \)（\( x\to\infty \) 先代换）。<br>'
      '有理函数：长除法，丢余项即得斜渐近线。',
      'asys')

    R('数学回顾::极限等式', '极限等式',
      '极限存在则 \( A \) 是<b>确定的实数</b>，可反推未知参数。',
      'par')

    R('数学回顾::无穷小', '无穷小',
      r'\( f=o(x^k)\Leftrightarrow\lim\dfrac{f}{x^k}=0 \)（严格证明用定义）<br>'
      r'\( \lim\dfrac{\beta}{\alpha}=0 \Rightarrow \beta \) 是 \( \alpha \) 的高阶无穷小（\( x^3 \) 对 \( x^2 \)）<br>'
      '极限为 0 的数列/函数称为无穷小。',
      'inf')

    R('数学回顾::无穷大', '无穷大',
      r'<table><tr><th>函数</th><th>特征</th></tr>'
      r'<tr><td>\( x\sin x \)</td><td>扩音器；无界或极限不存在</td></tr>'
      r'<tr><td>\( \dfrac{\sin x}{x} \)</td><td>缩音器；有界</td></tr></table>'
      r'<br>取子列经 \( \sin x=0 \) 的点说明无界或极限不存在。',
      'infy')

    R('数学回顾::泰勒多项式', '泰勒多项式概念',
      r'\( f(x)=\sum\dfrac{f^{(n)}(a)}{n!}(x-a)^n \)；多为麦克劳林（\( a=0 \)）。<br>'
      r'佩亚诺余项 \( o((x-a)^n) \)；拉格朗日余项含 \( \xi\in(a,x) \)。',
      'tay')

    R('数学回顾::泰勒多项式::使用条件', '泰勒使用条件',
      r'• 麦克劳林要求变量趋于 <b>0</b>（无穷小量上才能用）。<br>'
      r'• \( \ln(1+f) \) 至少展到 \( \dfrac{f^2}{2} \)。<br>'
      r'• \( (1+x)^{1/x} \) 在 \( x\to\infty \)：先取对数 \( \exp\left(\dfrac{\ln(1+x)}{x}\right) \)，令 \( t=\dfrac{1}{x}\to0 \) 再展。',
      'tayu')

    R('数学回顾::泰勒多项式::求极限常用', '求极限常用泰勒（二阶/三阶）',
      r'\( e^x=1+x+\dfrac{x^2}{2}+o(x^2) \)，\( \ln(1+x)=x-\dfrac{x^2}{2}+o(x^2) \)<br>'
      r'\( \sin x=x-\dfrac{x^3}{6}+o(x^3) \)，\( \cos x=1-\dfrac{x^2}{2}+o(x^2) \)<br>'
      r'\( \tan x=x+\dfrac{x^3}{3}+o(x^3) \)，\( (1+x)^\alpha=1+\alpha x+\dfrac{\alpha(\alpha-1)}{2}x^2+o(x^2) \)<br>'
      r'\( \arcsin x=x+\dfrac{x^3}{6}+o(x^3) \)，\( \arctan x=x-\dfrac{x^3}{3}+o(x^3) \)',
      'tayc')

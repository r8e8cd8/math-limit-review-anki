# 高数极限与连续 · 笔记与 Anki 卡组

将《极限与连续》原始笔记整理为结构化 Markdown，并一键生成 **Anki 填空卡组**（45 张，LaTeX 由 MathJax 渲染）。

## 内容

| 路径 | 说明 |
|------|------|
| `source/极限与连续.md` | 桌面原始笔记（极限、连续、函数性质等） |
| `数学回顾要点.md` | 整理后的完整知识结构（520 行，含修正） |
| `generate_math_review_apkg.py` | 生成 Anki `.apkg` 的主脚本 |
| `math_to_image.py` | LaTeX→PNG 渲染（墨墨图片版历史方案，见 `docs/`） |
| `docs/开发笔记-踩坑记录.md` | 墨墨/Anki、卡片设计、笔记勘误等经验 |

## 快速开始

```bash
pip install -r requirements.txt
python generate_math_review_apkg.py
```

输出：`数学回顾要点-Anki.apkg`（45 张卡，按 `数学回顾::章节::小节` 分层）

### 导入 Anki

1. 安装 [Anki](https://apps.ankiweb.net/)（Windows 常见路径：`%LOCALAPPDATA%\Programs\Anki\Anki.exe`）
2. 文件 → 导入 → 选择 `.apkg`
3. 或直接双击 `.apkg` 文件

Anki 2.1+ 会自动用 MathJax 渲染 `\( … \)` / `\[ … \]` 公式。

## 卡片设计

- **公式卡**：背面只有公式/答案，直接背诵
- **方法/概念卡**：背面含 **例（方法）**，演示解题思路
- 同类公式合并（二倍角、泰勒分组等），避免 155 张过碎
- 方法卡采用 `①②③【标签】` + 问句填空，减少猜词

## 笔记勘误（已写入 `数学回顾要点.md`）

整理过程中修正了若干笔误，详见 `docs/开发笔记-踩坑记录.md`，包括：

- 高阶无穷小定义（β 是 α 的高阶，非写反）
- 有界性反例：`sin(1/x)` 极限不存在但有界
- 周期性需加「f 可积」前提
- 绝对值三角不等式拆成恒成立式与证明专用估计

## 许可

个人学习笔记与工具脚本，仅供复习参考。

## 作者

[r8e8cd8](https://github.com/r8e8cd8)

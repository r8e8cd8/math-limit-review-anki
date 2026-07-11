# 高数极限与连续 · 笔记与 Anki 卡组

将《极限与连续》原始笔记整理为结构化 Markdown，并生成 **阅读卡 + 练习卡**（与 `数学回顾要点.md` 章节框架一致）。

## 内容

| 路径 | 说明 |
|------|------|
| `数学回顾要点.md` | 知识结构主文档（框架不变） |
| `cards_reading.py` | **阅读卡**：完整要点/表格，通读理解 |
| `cards_limit.py` | **函数极限**原理速记 |
| `cards_content.py` | 其余章节原理速记 |
| `generate_math_review_apkg.py` | 生成 `.apkg` + `数学回顾要点-记忆卡.md` |
| `math_to_image.py` | LaTeX→PNG 渲染（墨墨图片版历史方案，见 `docs/`） |
| `docs/开发笔记-踩坑记录.md` | 墨墨/Anki、卡片设计、笔记勘误等经验 |

## 快速开始

```bash
pip install -r requirements.txt
python generate_math_review_apkg.py
```

输出：

- `数学回顾要点-Anki.apkg`
- `数学回顾要点-记忆卡.md`

## 卡片设计

- **阅读卡**（`read-*`）：正面即完整要点，单面通读
- **速记卡**（`memo-*`）：只背**原理/公式/判定/方法选择**，不挂大观具体小题
- 章节层级与 `数学回顾要点.md` 一致

### 导入 Anki

1. 安装 [Anki](https://apps.ankiweb.net/)（Windows 常见路径：`%LOCALAPPDATA%\Programs\Anki\Anki.exe`）
2. 文件 → 导入 → 选择 `.apkg`
3. 或直接双击 `.apkg` 文件

Anki 2.1+ 会自动用 MathJax 渲染 `\( … \)` / `\[ … \]` 公式。

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

# Collage Art Director

A Codex skill for art-directing one to six user photos into expressive collage posters with deliberate relationships between image, type, background, and theme-specific material.

This skill treats collage as an art-direction problem rather than a template. It decides what each image, word, background field, and graphic material is doing before a finished poster is generated.

## What It Does

- Analyzes the source photo or photos before composition.
- Preserves identity, pose, key objects, and context anchors.
- Selects an image role such as full-scene background, framed photo object, subject reconstruction, break-frame hybrid, cropped fragments, or multi-image narrative.
- Treats typography as a compositional layer that can cross, press against, nest with, sit behind, or interrupt a photo.
- Selects materials because they belong to the subject, not because a generic sticker set is available.
- Uses exact deterministic typography for Chinese, names, dates, brands, URLs, and other copy that must be correct.
- Produces three structurally different directions in Direction mode, or one finished route in Production mode.

It does not prescribe one fixed collage style. Visual references contribute relationship grammar, not copied subjects, wording, logos, or exact palettes.

## Modes

### Direction Mode

Use when exploring ideas, evaluating a reference, or choosing a route.

The skill returns three concise directions. Each direction must differ structurally in at least three dimensions, such as image role, z-order, type treatment, spatial structure, crop, background strategy, or material family. Changing only the color or font does not count as a new direction.

### Production Mode

Use when a finished poster is requested.

The skill selects one strongest route by default and follows the production protocol:

```text
source analysis
-> art-direction record
-> recipe selection
-> text-free base
-> source-preservation check
-> deterministic typography
-> final quality gates
-> finished preview + recipe
```

The result includes the finished preview, a compact production recipe, the lettering strategy, the image-type relationship, and any unresolved limitation.

## Typography

Deterministic type is the default:

1. Generate or edit a text-free visual base.
2. Inspect source fidelity and composition.
3. Add exact wording with a real installed or loadable font using HTML, SVG, Canvas, or a design tool.
4. Inspect the final result at the requested output size.

Model-rendered display lettering is allowed only as a controlled exception for one short phrase whose irregular lettering is part of the source medium. It is never the default for Chinese, names, dates, brand copy, support text, or microcopy.

## SVG Text Overlay Helper

`scripts/create_text_overlay.py` builds an editable SVG from a JSON composition specification:

```bash
python3 scripts/create_text_overlay.py spec.json finished-poster.svg
```

The specification requires:

- `canvas.width`
- `canvas.height`
- either `canvas.background_image` or `canvas.background_color`
- at least one `text_blocks` entry

Each text block requires `text`, `x`, `y`, `font_family`, and `font_size`. Optional fields include `font_weight`, `fill`, `anchor`, `letter_spacing`, `opacity`, `rotate`, `stroke`, and `stroke_width`.

For photo-object layouts, `image_blocks` entries require `image`, `x`, `y`, and `width`/`height`. The generated SVG embeds the image material and keeps the final text editable.

The helper is for deterministic typesetting and image placement. It does not replace the art-direction process or generate a collage style by itself.

## Repository Structure

```text
SKILL.md                         Complete skill instructions
README.md                        Public overview and usage
LICENSE                          CC BY-NC-SA 4.0 license
agents/openai.yaml               Invocation metadata
references/
  composition-modes.md            Source-aware composition modes
  layout-grammar.md              Reusable layout grammars
  production-protocol.md         Production workflow and quality gates
  reference-interaction-grammar.md
  theme-language.md              Subject-specific material guidance
  typography-and-qc.md           Type and final-review rules
scripts/
  create_text_overlay.py          Editable SVG text overlay helper
```

## Installation

Clone the repository into your Codex skills directory:

```bash
git clone https://github.com/esthersjw/collage-art-director-skill.git \\
  ~/.codex/skills/collage-art-director
```

Restart Codex if the skill does not appear immediately.

## Usage

```text
Use $collage-art-director to turn these photos into an editorial collage poster.
The exact title is: "WONDER".
```

You can provide one to six photos, a content brief, a visual reference, exact copy, or a request for creative directions.

## License

This repository is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](LICENSE) (CC BY-NC-SA 4.0).

You must provide attribution, may not use the material commercially, and must share adaptations under the same license. The complete legal code is available at:

https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode

---

# 拼贴艺术指导器

这是一个 Codex Skill，用来把 1–6 张照片编排成具有明确图文关系的拼贴海报。它关注照片、文字、背景和主题材料各自承担什么作用，而不是套用固定模板。

## 它能做什么

- 在构图之前分析照片内容、主体、动作、场景、色彩和可裁切区域。
- 保留人物身份、姿态、关键物件和能够解释场景意义的上下文锚点。
- 根据照片状态选择图片角色：完整场景背景、框中照片、主体重构、突破照片边界、局部碎片或多图叙事。
- 把文字当作构图层处理，让文字穿过、压住、嵌入、位于照片之后，或打断照片的结构。
- 根据主题选择有语义关系的材料，而不是随便添加贴纸、胶带和装饰。
- 对中文、姓名、日期、品牌、网址和其他必须准确的文案使用确定性排版。
- 在方向模式下输出三个结构真正不同的方案；在生产模式下默认完成一条最强路线。

它不规定一种固定的视觉风格。参考图提供的是背景、照片、文字和材料之间的关系语法，不是要照抄的主体、文案、Logo 或配色。

## 两种模式

### Direction Mode：方向模式

适合探索想法、评估参考图、比较构图或迭代方案。

Skill 会输出三个简洁方向。每两个方向至少要在三项结构上不同，例如图片角色、层级顺序、文字处理、空间结构、裁切方式、背景策略或材料家族。只换颜色或字体，不算新的方向。

### Production Mode：生产模式

适合用户要求制作一张完成品时使用。

默认只选择一条最强路线，并按照生产协议执行：

```text
读取来源
→ 记录艺术指导决策
→ 选择构图配方
→ 生成无最终文字的底图
→ 检查来源保真
→ 使用真实字体排版
→ 执行最终质量门
→ 返回成品和配方
```

交付内容包括成品预览、简洁生产配方、文字处理策略、图文关系，以及任何尚未解决的限制。

## 文字处理

默认使用确定性文字排版：

1. 先生成或编辑无最终文字的视觉底图。
2. 检查来源保真和构图关系。
3. 使用真实安装或可加载的字体，通过 HTML、SVG、Canvas 或设计工具写入准确文字。
4. 按最终输出尺寸检查文字是否完整、清晰和位于正确层级。

只有当不规则手写或印刷字本身就是来源媒介的重要组成部分时，才允许让模型生成一条很短的展示文字。中文、姓名、日期、品牌文案、辅助文字和微文案默认不能交给图片模型代写。

## SVG 文字叠加脚本

`scripts/create_text_overlay.py` 可以根据 JSON 构图规格生成可编辑 SVG：

```bash
python3 scripts/create_text_overlay.py spec.json finished-poster.svg
```

规格必须包含：

- `canvas.width`
- `canvas.height`
- `canvas.background_image` 或 `canvas.background_color` 之一
- 至少一个 `text_blocks` 条目

每个文字块必须包含 `text`、`x`、`y`、`font_family` 和 `font_size`。还可以设置 `font_weight`、`fill`、`anchor`、`letter_spacing`、`opacity`、`rotate`、`stroke` 和 `stroke_width`。

照片对象布局可以使用 `image_blocks`。每个图像块需要 `image`、`x`、`y`、`width` 和 `height`。生成的 SVG 会嵌入图片材料，并保留可编辑的最终文字。

这个脚本负责确定性文字和图片放置，不负责凭空生成拼贴风格，也不能替代艺术指导和来源分析。

## 仓库结构

```text
SKILL.md                         完整 Skill 规则
README.md                        中英文项目说明
LICENSE                          CC BY-NC-SA 4.0 许可证
agents/openai.yaml               调用元数据
references/
  composition-modes.md            来源状态与构图模式
  layout-grammar.md              可复用版式语法
  production-protocol.md         生产流程与质量门
  reference-interaction-grammar.md
  theme-language.md              主题相关的材料指导
  typography-and-qc.md           文字与最终检查规则
scripts/
  create_text_overlay.py          可编辑 SVG 文字叠加脚本
```

## 安装

将仓库克隆到 Codex 的 Skill 目录：

```bash
git clone https://github.com/esthersjw/collage-art-director-skill.git \\
  ~/.codex/skills/collage-art-director
```

如果 Skill 没有立即出现，请重启 Codex。

## 使用

```text
使用 $collage-art-director 把这些照片做成一张编辑感拼贴海报。
标题必须准确写成：“WONDER”。
```

你可以提供 1–6 张照片、内容简报、视觉参考图、准确文案，或者只要求先给出几个创意方向。

## 许可证

本仓库使用 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](LICENSE)（CC BY-NC-SA 4.0）许可证。

使用时必须署名，不得将本材料用于商业目的；如果对本材料进行改编、重混或再创作，必须使用相同许可证分享。完整法律文本见：

https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode

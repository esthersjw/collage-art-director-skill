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

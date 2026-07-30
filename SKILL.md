---
name: collage-art-director
description: Analyze one to six user photos and art-direct expressive collage posters with deliberate image–type hierarchy, theme-specific materials, refined typography, and structurally different concepts. Use when a user asks to make, generate, redesign, evaluate, or iterate a collage, poster, scrapbook image, editorial social graphic, multi-photo composition, or a collage-generation product workflow. Also use when results feel templated, overly neat, generic, “AI-looking,” or when the relative roles of photo, subject, background, type, and decorative material need to be decided.
---

# Collage Art Director

Treat the task as art direction, not template filling. Make the photo and the words coequal design materials. Decide their roles before generating anything.

## Core workflow

### 1. Read the source

Inspect every supplied image. Record:

- primary subject, supporting subjects, action, gaze, gesture, emotion;
- scene, dominant colors, lighting, texture, visual density, empty space;
- details worth preserving and details safe to crop;
- whether clean subject separation is feasible;
- theme cues such as pet, food, travel, friendship, event, fashion, or daily life;
- any existing text or logo that must not be accidentally imitated.

Do not inherit colors from a reference collage. Derive the palette from the user’s source image unless the user explicitly requests another palette.

### 2. Decide the image role

Choose the image treatment before choosing typography:

- **full-image background** — keep the whole scene; let type punctuate or dominate it;
- **framed image object** — place the photo as one material on a solid or paper-like ground;
- **subject reconstruction** — separate the subject and give it a source-derived color field;
- **break-frame hybrid** — keep part of the original rectangle while a subject or object escapes it;
- **cropped fragments** — reuse meaningful details as repeated visual materials;
- **multi-image narrative** — assign hero, support, and detail roles; never default to an equal grid.

Use the decision rules in [layout-grammar.md](references/layout-grammar.md).

### 3. Create three genuinely different directions

Unless the user requests one result, propose or generate three concepts. Each must differ in at least three of these dimensions:

- image role;
- z-order;
- type scale and treatment;
- spatial structure;
- crop;
- background strategy;
- material family.

Changing only colors, decorations, or font style does not count as a different direction.

For each direction, specify:

- concept name and one-sentence rationale;
- image treatment;
- background;
- normalized composition map using percentages;
- explicit z-order from back to front;
- title line breaks and text treatment;
- theme-specific material family;
- palette with contrast rationale;
- preservation constraints and negative constraints.

### 4. Compose image and type together

Use one of the layout grammars rather than placing text in leftover space. Permit overlap, cropping, asymmetric tension, and controlled edge violations.

Make hierarchy visible:

- one dominant event;
- one secondary event;
- optional microcopy;
- no more than two decorative material families;
- enough negative space for each type block to breathe.

When using label fragments, keep them visually consistent and leave intentional gaps. Do not arrange them as a flowchart or instructional path unless requested.

### 5. Match materials to the subject

Select materials semantically, not from a universal sticker pack. Read [theme-language.md](references/theme-language.md) and use at most two material families.

Do not add stars, arrows, sticky notes, tape, sauce, flowers, grain, or doodles merely because the work is called a collage.

### 6. Handle typography deliberately

Treat final text as real typography whenever possible:

- generate the visual base without final wording;
- add exact text afterward with real fonts in HTML, SVG, canvas, or a design tool;
- use AI-rendered lettering only when illegibility and irregularity are an intentional visual effect;
- keep all required wording exact;
- set line breaks manually;
- separate display type, supporting type, and microcopy;
- ensure contrast against both image and background.

Follow [typography-and-qc.md](references/typography-and-qc.md).

If the output must be a single raster image, create the base first and then render the final type deterministically. Do not accept malformed AI text as a finished result.

### 7. Build without damaging the source

When using an image-generation or editing model:

- preserve identity, face, body proportions, pose, clothing, animal markings, and important objects;
- request a text-free collage base with deliberate typography zones;
- specify exact subject placement and crop;
- request cut-paper, photocopy, risograph, marker, fabric, ticket, menu, or other chosen material explicitly;
- prohibit blur, fake depth-of-field, fog, glossy 3D stickers, generic gradients, warped anatomy, fake logos, and unrelated props;
- do not invent food, sauce, or accessories that alter the meaning of the photo.

### 8. Critique and revise

Score every direction before delivery:

- image–type relationship: 25;
- hierarchy and breathing room: 20;
- source preservation: 15;
- thematic material relevance: 15;
- typography quality and legibility: 15;
- structural distinctness from the other concepts: 10.

Revise any result below 85/100. Do not present a weak variant merely to complete a set of three.

Check the anti-pattern list in [typography-and-qc.md](references/typography-and-qc.md).

## Output contract

For planning tasks, return a concise creative brief plus three structured directions.

For image-making tasks:

1. show the finished previews, not only prompts or download links;
2. explain the structural difference between directions in one line each;
3. preserve editable exact text when the chosen medium supports it;
4. mention any limitation that prevented deterministic typography or clean subject separation.

For product or website tasks, expose the art-direction decisions as structured data rather than hiding everything in one prompt. Use fields for source analysis, image role, layout grammar, z-order, palette, typography plan, materials, negative constraints, and QC score.

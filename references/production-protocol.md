# Production protocol

Use this protocol only for Production mode. It improves repeatability without prescribing a visual style.

## 1. Compile an art-direction record

Build the record before generating. Keep it concise, but make every field explicit.

```yaml
mode: production
canvas: "aspect ratio and pixel target"
source:
  hero: "photo or subject to preserve"
  preserve: ["identity", "pose", "key object"]
  crop_safe: "what may be cropped"
recipe:
  layout_grammar: "one grammar from layout-grammar.md"
  image_role: "hero image treatment"
  composition: "major regions as percentages"
  z_order: ["back", "to", "front"]
  materials: ["one primary", "one optional support"]
  palette: "source-derived colors and contrast plan"
typography:
  exact_text: ["display", "support", "microcopy"]
  hierarchy: "display / support / microcopy"
  type_zone: "clear area or intentional overlap"
  overlay_method: "HTML, SVG, canvas, or design tool"
negative_constraints: ["specific visual failures to prevent"]
```

Do not invent unspecified words. If text is missing, use no display text or one short optional phrase only when the user permits creative copy.

## 2. Select a recipe deliberately

Use one layout grammar and one image role. Select materials from the subject's theme; do not use a universal sticker set.

For multi-photo work, name one hero, one support, and optional detail. For a single image, choose either full-image, framed object, subject reconstruction, break-frame hybrid, or fragments. Do not mix several image roles merely to make the work look busy.

When three directions are requested, record a distinct recipe for each. Reject directions that share the same image role, title location, and z-order.

## 3. Compile the text-free base prompt

Write the prompt in this field order. Keep it decisive and specific; include only visible instructions.

1. **Canvas and source:** output ratio, source-photo fidelity, subject, allowed crop, and preserved details.
2. **Composition:** layout grammar, image role, percentage-based scale, placement, and explicit layer relationship.
3. **Materials and palette:** source-derived palette, selected material family, texture, and type-free zones.
4. **Negative constraints:** no final lettering, malformed text, fake logos, identity drift, unrelated props, generic decorations, blur, glossy 3D stickers, or unrequested style effects.

Request a text-free base with clearly reserved typography zones. Never ask an image model to render exact required wording.

## 4. Render and typeset

1. Generate the base with the available image-generation or editing capability.
2. Inspect the result before typesetting. Regenerate the base once if it fails a source-preservation gate or its selected recipe is not recognizable.
3. Add final wording with real installed or loadable fonts in HTML, SVG, canvas, or a design tool. Set line breaks, positions, contrast patches, and front/behind-subject relationships explicitly.
4. For a reusable SVG route, create a JSON composition specification and run `python3 scripts/create_text_overlay.py spec.json finished-poster.svg`. Use one `text_blocks` entry per intended line. Each entry requires `text`, `x`, `y`, `font_family`, and `font_size`; it may also set `font_weight`, `fill`, `anchor`, `letter_spacing`, `opacity`, and `rotate`. The `canvas` object requires `width`, `height`, and a `background_image` path relative to the JSON file. The generated SVG embeds the base image and preserves exact editable text.
5. Export the SVG through the available browser or design tool when a PNG is required. Inspect the rasterized result at the requested output size before delivery.

If deterministic typesetting is unavailable, say so before delivery. Do not claim malformed model lettering is exact final text.

## 5. Apply the hard quality gates

Pass every gate before delivery:

- **Source fidelity:** preserve identity, pose, clothing, markings, and declared key objects; do not add semantic props.
- **Structure:** show one dominant event and one secondary event; for multi-image work, the hero occupies about 45–70% of image area.
- **Material discipline:** use one primary material family and at most one support family; every material has a subject-specific reason.
- **Typography:** reproduce required text exactly with real type; keep it readable and sufficiently contrasted at its actual overlap area.
- **No template drift:** do not use equal photo grids, centered-everything layouts, generic sticker outlines, decorative filler, fake brands, or an unrequested style treatment.
- **Recipe fidelity:** make the selected layout grammar, image role, and layer order visible in the finished image.

Score the result using the main skill's 100-point rubric after it passes the gates. If a gate fails, fix that failure rather than merely adjusting the score. Make at most two revision cycles: one base-image retry and one typography/composition correction. Report any remaining limitation instead of silently delivering a failed result.

## Production return format

Return:

1. the finished preview;
2. a compact production recipe containing the canvas, grammar, image role, palette, materials, typography plan, and QC result;
3. a one-line note on the image–type relationship;
4. any unresolved limitation.

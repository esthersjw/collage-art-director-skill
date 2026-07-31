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
  context_anchor: "source elements that must remain together to preserve the scene's meaning, or none"
  crop_safe: "what may be cropped"
  state: "complete-scene, cutout-ready subject, or photo-block breakout"
  existing_text_policy: "preserve, remove/crop, or replace"
reference_grammar:
  background_field: "how the background participates"
  photo_object: "how the photo behaves as an object"
  type_interaction: "how type meets the photo"
  graphic_material_role: "why any accent exists"
recipe:
  composition_mode: "one mode from composition-modes.md"
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
  lettering_strategy: "deterministic type (default), model-led display exception, or hybrid"
  overlay_method: "HTML, SVG, canvas, or design tool"
  final_z_order: "topmost, behind-subject, or intentional split"
negative_constraints: ["specific visual failures to prevent"]
```

Do not invent unspecified words. If text is missing, use no display text or one short optional phrase only when the user permits creative copy.

## 2. Select a recipe deliberately

Use one composition mode, one layout grammar, and one image role. Select materials from the subject's theme or crop them from the source; do not use a universal sticker set.

Choose the mode from the source state before writing a prompt. Preserve an already complete scene in **original-scene annotation** mode; full-scene type overlay is a primary route, not a fallback. Use a pure field and cutout subject only when the source benefits from reconstruction. When reconstruction separates a subject from its environment, preserve the declared context anchor as an intact group. Use a retained photo rectangle plus selective breakout when the original photo is a valuable physical object. Read [composition-modes.md](composition-modes.md) before choosing.

For multi-photo work, name one hero, one support, and optional detail. For a single image, choose either full-image, framed object, subject reconstruction, break-frame hybrid, or fragments. Do not mix several image roles merely to make the work look busy.

When three directions are requested, record a distinct recipe for each. Reject directions that share the same image role, title location, and z-order.

## 3. Select the lettering strategy

Use **deterministic type** by default. It is mandatory for Chinese, names, dates, product or brand copy, multi-line required wording, and any copy likely to be revised.

Use the **model-led display exception** only for one short display phrase where the lettering itself must share the source medium's irregularity. Before accepting it, require all of the following:

1. the phrase is verbatim and has no pseudo-letters, spelling errors, or unwanted extra words;
2. it is readable at a phone-preview scale (about 25% of the final image height);
3. its baseline, scale, texture, and z-order visibly improve the chosen image–type interaction versus a real-font overlay;
4. it does not cover eyes, mouth, hands, or the key gesture; and
5. no support text or microcopy depends on the image model.

If any condition fails, use deterministic type. Use **hybrid** only when an accepted model-led display phrase is paired with deterministic support text.

Record the choice in `typography.lettering_strategy` and explain the reason in one sentence in the delivery recipe.

## 4. Compile the base prompt

Write the prompt in this field order. Keep it decisive and specific; include only visible instructions.

1. **Canvas and source:** output ratio, source-photo fidelity, subject, allowed crop, and preserved details.
2. **Composition:** source state, composition mode, layout grammar, image role, percentage-based scale, placement, complete z-order, declared context anchor, and explicit image–type relationship. When a visual reference is supplied, name its chosen interaction family and make that relationship visible; do not translate it into separated text cards. State explicitly whether the route is seamless full-scene overlay or an extracted reconstruction; do not add paper pieces or color blocks by default.
3. **Materials and palette:** source-derived palette, source-harvested or semantically specific materials, texture, and the planned type path. Do not reserve a blank text card or a polite safe panel when the selected relationship requires type to cross the photo.
4. **Negative constraints:** no final lettering, malformed text, fake logos, identity drift, unrelated props, generic decorations, blur, glossy 3D stickers, or unrequested style effects. For the model-led display exception, replace “no final lettering” with the exact one permitted display phrase and prohibit all other text.

Request a text-free base with a planned typography path unless the model-led display exception is selected. In that exception, ask the model for only the one permitted phrase, then apply the acceptance gate before delivery. The path may cross the photo or a subject's non-critical area; protect eyes, mouth, hands, and the key gesture rather than isolating words in generic empty panels.

## 5. Render and typeset

1. Generate the base with the available image-generation or editing capability.
2. Inspect the result before typesetting. Regenerate the base once if it fails a source-preservation gate or its selected recipe is not recognizable.
3. For deterministic type, add final wording with real installed or loadable fonts in HTML, SVG, canvas, or a design tool. Set line breaks, positions, contrast patches, and front/behind-subject relationships explicitly.
4. For the model-led display exception, inspect the single rendered phrase against the acceptance gate. Replace it with deterministic type if it fails. For hybrid, add all remaining wording deterministically.
5. For a reusable SVG route, create a JSON composition specification and run `python3 scripts/create_text_overlay.py spec.json finished-poster.svg`. Use one `text_blocks` entry per intended line. Each entry requires `text`, `x`, `y`, `font_family`, and `font_size`; it may also set `font_weight`, `fill`, `anchor`, `letter_spacing`, `opacity`, `rotate`, `stroke`, and `stroke_width`. Use `stroke` only when a type block crosses backgrounds with incompatible contrast. The `canvas` object requires `width`, `height`, and either `background_image` or `background_color`. For a photo-object layout, add `image_blocks`: each entry requires `image`, `x`, `y`, `width`, and `height`, and can set `rotate`, `opacity`, and `preserve_aspect_ratio`. The generated SVG embeds the image material and preserves exact editable text.
6. Export the SVG through the available browser or design tool when a PNG is required. Inspect the rasterized result at the requested output size before delivery.

If deterministic typesetting is unavailable, say so before delivery. Do not claim malformed model lettering is exact final text.

## 5. Apply the hard quality gates

Pass every gate before delivery:

- **Source fidelity:** preserve identity, pose, clothing, markings, and declared key objects; do not add semantic props.
- **Structure:** show one dominant event and one secondary event; for multi-image work, the hero occupies about 45–70% of image area.
- **Context integrity:** when a cutout subject depends on a source setting for its meaning, retain the declared anchor intact. Do not reduce a building to a floating roof, a person-and-pet scene to an unexplained pet, or an action scene to unrelated fragments.
- **Material discipline:** use one primary material family and at most one support family; every material has a subject-specific reason.
- **Typography:** for deterministic or hybrid copy, reproduce every non-exception word exactly with real type; keep it readable and sufficiently contrasted at its actual overlap area. Accept model-led display type only when every condition in the lettering-strategy gate passes.
- **Layer intent:** honor the selected final z-order. In type-on-top modes, the final title visibly crosses the background and photo or breakout subject; it is never accidentally hidden beneath them.
- **Mode fit:** use original-scene annotation only when the photograph already carries the scene; otherwise use a reconstruction, photo-block breakout, or type-led mode deliberately.
- **No template drift:** do not use equal photo grids, centered-everything layouts, generic sticker outlines, decorative filler, fake brands, or an unrequested style treatment.
- **Recipe fidelity:** make the selected layout grammar, image role, and layer order visible in the finished image.
- **Reference fidelity:** when a visual reference is supplied, preserve its relationship grammar—background field, photo-object role, type interaction, and material purpose—without copying its literal subject matter.

Score the result using the main skill's 100-point rubric after it passes the gates. If a gate fails, fix that failure rather than merely adjusting the score. Make at most two revision cycles: one base-image retry and one typography/composition correction. Report any remaining limitation instead of silently delivering a failed result.

## Production return format

Return:

1. the finished preview;
2. a compact production recipe containing the canvas, grammar, image role, palette, materials, typography plan, and QC result;
3. the lettering strategy and a one-line note on the image–type relationship;
4. any unresolved limitation.

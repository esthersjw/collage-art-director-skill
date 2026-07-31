#!/usr/bin/env python3
"""Create an editable SVG poster from a base image and exact text blocks.

Usage:
    python3 create_text_overlay.py spec.json finished-poster.svg

The JSON spec has a ``canvas`` object and a ``text_blocks`` list. See
references/production-protocol.md for the schema and workflow.
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import mimetypes
from pathlib import Path


def number(value: object, field: str) -> float:
    if not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number")
    return value


def attribute(value: object) -> str:
    return html.escape(str(value), quote=True)


def image_data_uri(path_value: object, spec_path: Path, field: str) -> str:
    if not isinstance(path_value, str) or not path_value:
        raise ValueError(f"{field} must be a non-empty path")
    image_path = (spec_path.parent / path_value).resolve()
    if not image_path.is_file():
        raise ValueError(f"image does not exist: {image_path}")
    mime_type = mimetypes.guess_type(image_path.name)[0] or "image/png"
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def image_element(block: object, index: int, spec_path: Path) -> str:
    if not isinstance(block, dict):
        raise ValueError(f"image_blocks[{index}] must be an object")
    image = image_data_uri(block.get("image"), spec_path, f"image_blocks[{index}].image")
    x = number(block.get("x"), f"image_blocks[{index}].x")
    y = number(block.get("y"), f"image_blocks[{index}].y")
    width = number(block.get("width"), f"image_blocks[{index}].width")
    height = number(block.get("height"), f"image_blocks[{index}].height")
    if width <= 0 or height <= 0:
        raise ValueError(f"image_blocks[{index}] dimensions must be positive")

    attributes = {
        "href": image,
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "opacity": block.get("opacity", 1),
        "preserveAspectRatio": block.get("preserve_aspect_ratio", "xMidYMid slice"),
    }
    transform = ""
    if "rotate" in block:
        angle = number(block["rotate"], f"image_blocks[{index}].rotate")
        center_x = x + width / 2
        center_y = y + height / 2
        transform = (
            f' transform="rotate({attribute(angle)} {attribute(center_x)} '
            f'{attribute(center_y)})"'
        )
    rendered_attributes = " ".join(
        f'{key}="{attribute(value)}"' for key, value in attributes.items()
    )
    return f"  <image {rendered_attributes}{transform} />"


def text_element(block: object, index: int) -> str:
    if not isinstance(block, dict):
        raise ValueError(f"text_blocks[{index}] must be an object")
    value = block.get("text")
    if not isinstance(value, str) or not value:
        raise ValueError(f"text_blocks[{index}].text must be a non-empty string")

    x = number(block.get("x"), f"text_blocks[{index}].x")
    y = number(block.get("y"), f"text_blocks[{index}].y")
    size = number(block.get("font_size"), f"text_blocks[{index}].font_size")
    family = block.get("font_family")
    if not isinstance(family, str) or not family:
        raise ValueError(f"text_blocks[{index}].font_family must be a non-empty string")

    attributes = {
        "x": x,
        "y": y,
        "font-family": family,
        "font-size": size,
        "font-weight": block.get("font_weight", 400),
        "fill": block.get("fill", "#111111"),
        "text-anchor": block.get("anchor", "start"),
        "letter-spacing": block.get("letter_spacing", 0),
        "opacity": block.get("opacity", 1),
    }
    if "stroke" in block:
        attributes["stroke"] = block["stroke"]
        attributes["stroke-width"] = number(
            block.get("stroke_width", 1), f"text_blocks[{index}].stroke_width"
        )
        attributes["paint-order"] = "stroke fill"
    transform = ""
    if "rotate" in block:
        angle = number(block["rotate"], f"text_blocks[{index}].rotate")
        transform = f' transform="rotate({attribute(angle)} {attribute(x)} {attribute(y)})"'

    rendered_attributes = " ".join(
        f'{key}="{attribute(value)}"' for key, value in attributes.items()
    )
    return f"  <text {rendered_attributes}{transform}>{html.escape(value)}</text>"


def build_svg(spec: dict, spec_path: Path) -> str:
    canvas = spec.get("canvas")
    if not isinstance(canvas, dict):
        raise ValueError("canvas must be an object")
    width = number(canvas.get("width"), "canvas.width")
    height = number(canvas.get("height"), "canvas.height")
    if width <= 0 or height <= 0:
        raise ValueError("canvas dimensions must be positive")

    blocks = spec.get("text_blocks")
    if not isinstance(blocks, list) or not blocks:
        raise ValueError("text_blocks must be a non-empty list")

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{attribute(width)}" height="{attribute(height)}" viewBox="0 0 {attribute(width)} {attribute(height)}">',
    ]
    background_color = canvas.get("background_color")
    if background_color is not None:
        if not isinstance(background_color, str) or not background_color:
            raise ValueError("canvas.background_color must be a non-empty string")
        lines.append(
            f'  <rect width="{attribute(width)}" height="{attribute(height)}" '
            f'fill="{attribute(background_color)}" />'
        )
    background_path = canvas.get("background_image")
    if background_path is not None:
        background = image_data_uri(background_path, spec_path, "canvas.background_image")
        lines.append(
            f'  <image href="{attribute(background)}" width="{attribute(width)}" '
            f'height="{attribute(height)}" preserveAspectRatio="xMidYMid slice" />'
        )
    if background_color is None and background_path is None:
        raise ValueError("canvas must include background_color or background_image")

    image_blocks = spec.get("image_blocks", [])
    if not isinstance(image_blocks, list):
        raise ValueError("image_blocks must be a list")
    lines.extend(
        image_element(block, index, spec_path)
        for index, block in enumerate(image_blocks)
    )
    lines.extend(text_element(block, index) for index, block in enumerate(blocks))
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an editable SVG poster with exact text.")
    parser.add_argument("spec", type=Path, help="JSON composition specification")
    parser.add_argument("output", type=Path, help="Output SVG path")
    args = parser.parse_args()

    try:
        spec = json.loads(args.spec.read_text(encoding="utf-8"))
        if not isinstance(spec, dict):
            raise ValueError("the specification root must be an object")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(build_svg(spec, args.spec.resolve()), encoding="utf-8")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"error: {exc}")


if __name__ == "__main__":
    main()

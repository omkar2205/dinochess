from __future__ import annotations

from collections import deque
from io import BytesIO
from pathlib import Path

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OUTPUT = ASSETS / "rendered"

PIECES = {
    "ivory-pawn": "ivory-pawn.svg",
    "ivory-knight": "Ivory-knight.svg",
    "ivory-bishop": "ivory-bishop.svg",
    "ivory-rook": "ivory-rook.svg",
    "ivory-queen": "ivory-queen.svg",
    "ivory-king": "ivory-king.svg",
    "obsidian-pawn": "obsidian-pawn.svg",
    "obsidian-knight": "obsidian-knight.svg",
    "obsidian-bishop": "obsidian-bishop.svg",
    "obsidian-rook": "obsidian-rook.svg",
    "obsidian-queen": "obsidian-queen.svg",
    "obsidian-king": "obsidian-king.svg",
}

CANVAS_SIZE = 512
ART_SIZE = 464
DARK_THRESHOLD = 58


def is_edge_background(pixel: tuple[int, int, int, int]) -> bool:
    r, g, b, a = pixel
    if a <= 8:
        return True
    return max(r, g, b) <= DARK_THRESHOLD


def remove_edge_connected_black(image: Image.Image) -> Image.Image:
    """Make only dark pixels connected to the image edge transparent.

    This removes exported black canvases while preserving dark outlines and
    internal shadows that are enclosed by the actual chess-piece artwork.
    """
    image = image.convert("RGBA")
    pixels = image.load()
    width, height = image.size
    visited = bytearray(width * height)
    queue: deque[tuple[int, int]] = deque()

    def enqueue(x: int, y: int) -> None:
        index = y * width + x
        if visited[index]:
            return
        visited[index] = 1
        if is_edge_background(pixels[x, y]):
            queue.append((x, y))

    for x in range(width):
        enqueue(x, 0)
        enqueue(x, height - 1)
    for y in range(height):
        enqueue(0, y)
        enqueue(width - 1, y)

    while queue:
        x, y = queue.popleft()
        r, g, b, _ = pixels[x, y]
        pixels[x, y] = (r, g, b, 0)
        if x > 0:
            enqueue(x - 1, y)
        if x + 1 < width:
            enqueue(x + 1, y)
        if y > 0:
            enqueue(x, y - 1)
        if y + 1 < height:
            enqueue(x, y + 1)

    return image


def crop_and_normalise(image: Image.Image) -> Image.Image:
    alpha = image.getchannel("A")
    bbox = alpha.getbbox()
    if not bbox:
        raise ValueError("The rendered SVG contains no visible artwork.")

    cropped = image.crop(bbox)
    cropped.thumbnail((ART_SIZE, ART_SIZE), Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    x = (CANVAS_SIZE - cropped.width) // 2
    y = CANVAS_SIZE - cropped.height - 20
    canvas.alpha_composite(cropped, (x, max(0, y)))
    return canvas


def render_piece(source: Path, destination: Path) -> None:
    png_bytes = cairosvg.svg2png(
        url=str(source),
        output_width=900,
        output_height=900,
        background_color="transparent",
    )
    image = Image.open(BytesIO(png_bytes)).convert("RGBA")
    image = remove_edge_connected_black(image)
    image = crop_and_normalise(image)
    image.save(destination, format="PNG", optimize=True)


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)

    missing = [filename for filename in PIECES.values() if not (ASSETS / filename).exists()]
    if missing:
        raise FileNotFoundError(f"Missing piece SVG files: {', '.join(missing)}")

    for output_name, source_name in PIECES.items():
        source = ASSETS / source_name
        destination = OUTPUT / f"{output_name}.png"
        render_piece(source, destination)
        print(f"Rendered {source_name} -> {destination.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

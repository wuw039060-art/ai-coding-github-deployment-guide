"""Correct the author credit on the v2.3 cover without changing its artwork."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "book" / "assets" / "cover.png"
PREVIEW = ROOT / "assets" / "cover-v2.3.0-preview.jpg"
FONT = Path("/System/Library/Fonts/Palatino.ttc")


def main() -> None:
    image = Image.open(SOURCE).convert("RGBA")
    if image.size != (1600, 2400):
        raise ValueError(f"unexpected cover size: {image.size}")
    draw = ImageDraw.Draw(image)
    # The existing author credit sits on a nearly flat blue pill. Restore its
    # background row by row, so only the small text region is changed.
    left, top, right, bottom = 197, 2203, 337, 2251
    for y in range(top, bottom):
        a = image.getpixel((190, y))
        b = image.getpixel((350, y))
        for x in range(left, right):
            t = (x - left) / (right - left - 1)
            color = tuple(round(a[i] * (1 - t) + b[i] * t) for i in range(4))
            draw.point((x, y), fill=color)
    font = ImageFont.truetype(str(FONT), 31)
    draw.text((267, 2228), "Stallen", font=font, anchor="mm", fill=(239, 230, 216, 255))
    image.save(SOURCE)
    image.convert("RGB").save(PREVIEW, quality=92, optimize=True)


if __name__ == "__main__":
    main()

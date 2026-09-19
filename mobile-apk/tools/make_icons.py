import math, os
from PIL import Image, ImageDraw

ROOT = r"C:\Users\ibrah\Documents\Gemini\Ibrahim\NIEE_NJEES\CRIF-NN\mobile-apk\app\src\main\res"

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

TOP = (16, 122, 87)
BOT = (9, 60, 47)

def draw_icon(size, round_corners=True):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if round_corners:
        radius = int(size * 0.18)
        d.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=TOP)
    else:
        d.rectangle([0, 0, size - 1, size - 1], fill=TOP)
    px = img.load()
    for y in range(size):
        for x in range(size):
            r, g, b, a = px[x, y]
            if a > 0:
                px[x, y] = lerp(TOP, BOT, y / (size - 1)) + (255,)
    d = ImageDraw.Draw(img)
    c = lerp(TOP, BOT, 0.5) + (255,)
    # road "C": outer thick arc forming the letter C
    pad = size * 0.22
    cx = size * 0.5
    cy = size * 0.52
    out_r = size * 0.5 - pad
    in_r = out_r - size * 0.11
    bbox_out = (cx - out_r, cy - out_r, cx + out_r, cy + out_r)
    bbox_in = (cx - in_r, cy - in_r, cx + in_r, cy + in_r)
    d.arc(bbox_out, start=115, end=425, fill=(255, 255, 255, 255), width=max(2, int(size * 0.05)))
    # inner cut to make it a ring letter C
    d.arc(bbox_in, start=115, end=425, fill=(255, 255, 255, 255), width=max(2, int(size * 0.05)))
    return img

def save_legacy(density, px):
    d = os.path.join(ROOT, f"mipmap-{density}")
    os.makedirs(d, exist_ok=True)
    draw_icon(px, round_corners=True).save(os.path.join(d, "ic_launcher.png"))
    draw_icon(px, round_corners=True).save(os.path.join(d, "ic_launcher_round.png"))

legacy = [
    ("mdpi", 48), ("hdpi", 72), ("xhdpi", 96),
    ("xxhdpi", 144), ("xxxhdpi", 192),
]
for den, px in legacy:
    save_legacy(den, px)

# Adaptive foreground: 108dp canvas; safe glyph centered on ~66dp core
fg_dir = os.path.join(ROOT, "drawable")
os.makedirs(fg_dir, exist_ok=True)
S = 432  # xxxhdpi => 108dp at 4x, rendered icon 192px
fg = Image.new("RGBA", (S, S), (0, 0, 0, 0))
g = ImageDraw.Draw(fg)
center = S * 0.5
glyph_r = S * 0.30
thick = S * 0.075
b_out = (center - glyph_r, center - glyph_r * 1.04, center + glyph_r, center + glyph_r * 1.04)
b_in = (center - glyph_r + thick, center - glyph_r * 1.04 + thick, center + glyph_r - thick, center + glyph_r * 1.04 - thick)
g.arc(b_out, start=110, end=430, fill=(255, 255, 255, 255), width=int(thick))
g.arc(b_in, start=110, end=430, fill=(255, 255, 255, 255), width=int(thick))
fg.save(os.path.join(fg_dir, "ic_launcher_foreground.png"))
print("icons written")
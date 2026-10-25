# SPDX-License-Identifier: MIT
"""Check basic atlas structure; this does not replace visual motion review."""
from pathlib import Path
import hashlib
import json
from PIL import Image

root = Path(__file__).resolve().parents[1]
config = json.loads((root / "sprite.json").read_text(encoding="utf-8"))
path = root / config["image"]
errors = []
with Image.open(path) as source:
    if source.size != (1536, 2288):
        errors.append(f"Wrong dimensions: {source.size}")
    if "A" not in source.getbands():
        errors.append("Missing alpha channel")
    image = source.convert("RGBA")
    expected = [s["frames"] for s in config["states"]] + [8, 8]
    occupied = 0
    for row, count in enumerate(expected):
        for col in range(8):
            alpha = image.crop((col*192,row*208,(col+1)*192,(row+1)*208)).getchannel("A")
            visible = alpha.getbbox() is not None
            if col < count:
                occupied += int(visible)
                if not visible:
                    errors.append(f"Missing artwork: row {row}, col {col}")
                if alpha.getextrema()[0] > 0:
                    errors.append(f"No transparent margin: row {row}, col {col}")
            elif visible:
                errors.append(f"Unused cell is not transparent: row {row}, col {col}")
result = {"ok": not errors, "occupiedCells": occupied, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "errors": errors}
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["ok"] else 1)

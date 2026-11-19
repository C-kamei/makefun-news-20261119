"""Entry program for make.fun competition news-image-20261119.

It places the front-page image for Thursday 19 November 2026 into the
grader's output directory. The image is a fixed file shipped in this
repository, so the two grader runs produce byte-identical output: no
network access, no clock, no randomness anywhere in this program.
"""

import hashlib
import os
import sys
from pathlib import Path

ENTRY_NAME = "entry.png"


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def place_entry() -> Path:
    here = Path(__file__).resolve().parent
    source = here / ENTRY_NAME
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / ENTRY_NAME
    target.write_bytes(source.read_bytes())
    if sha256_of(target) != sha256_of(source):
        raise SystemExit("entry.png copy failed verification")
    return target


if __name__ == "__main__":
    placed = place_entry()
    print(f"wrote {placed} ({placed.stat().st_size} bytes, "
          f"sha256 {sha256_of(placed)[:16]}...)")
    sys.exit(0)

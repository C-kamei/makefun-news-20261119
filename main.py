"""make.fun entry for competition news-image-20261119.

The entry image is a newspaper front page summing up the world news of
Thursday 19 November 2026. This program copies the bundled ``entry.png``
to the output directory, so both grader runs write identical bytes.
The image itself is a fixed file: no network, no randomness, no clock.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    assert destination.stat().st_size == source.stat().st_size


if __name__ == "__main__":
    main()

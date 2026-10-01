"""Demo-only extractor for the checked-in canonical sample snapshots."""

from __future__ import annotations

import json
import sys
from pathlib import Path


if len(sys.argv) != 2:
    raise SystemExit("usage: demo_extract_canonical.py <artifact>")

print(Path(sys.argv[1]).read_text(encoding="utf-8"))

"""Demo-only extractor for the checked-in canonical sample snapshots."""

from __future__ import annotations

import json
import sys
from hashlib import sha256
from pathlib import Path


if len(sys.argv) != 2:
    raise SystemExit("usage: demo_extract_canonical.py <artifact>")

artifact = Path(sys.argv[1])
manifest = json.loads(artifact.read_text(encoding="utf-8"))
manifest.setdefault("source", {})["artifactSha256"] = sha256(
    artifact.read_bytes()
).hexdigest()
print(json.dumps(manifest))

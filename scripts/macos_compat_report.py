#!/usr/bin/env python3
"""Print OpenMontage runtime guidance for the current macOS host."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from lib.platform_compat import (  # noqa: E402
    catalina_runtime_notes,
    is_macos_catalina_or_older,
    macos_display_name,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hyperframes-supported",
        action="store_true",
        help="Exit 0 only when this OS should attempt HyperFrames setup.",
    )
    args = parser.parse_args()

    if args.hyperframes_supported:
        return 1 if is_macos_catalina_or_older() else 0

    print(f"Platform: {macos_display_name()}")
    notes = catalina_runtime_notes()
    if not notes:
        print("No Catalina-specific runtime restrictions detected.")
        return 0

    print("Catalina compatibility mode:")
    for note in notes:
        print(f"  - {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


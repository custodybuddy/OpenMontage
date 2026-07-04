"""Platform compatibility helpers.

OpenMontage can run useful local workflows on older macOS releases, but not
every optional runtime is viable there. Keep OS checks centralized so setup,
registry reporting, and runtime tools explain the same constraints.
"""

from __future__ import annotations

import platform
from functools import lru_cache
from typing import Optional


def _parse_version(raw: str) -> tuple[int, ...]:
    parts: list[int] = []
    for piece in raw.split("."):
        if not piece.isdigit():
            break
        parts.append(int(piece))
    return tuple(parts)


@lru_cache(maxsize=1)
def macos_version() -> Optional[tuple[int, ...]]:
    """Return the current macOS version tuple, or None on non-macOS hosts."""
    if platform.system() != "Darwin":
        return None
    raw = platform.mac_ver()[0]
    if not raw:
        return None
    return _parse_version(raw)


def is_macos() -> bool:
    return macos_version() is not None


def is_macos_older_than(major: int, minor: int = 0) -> bool:
    version = macos_version()
    if version is None:
        return False
    return version < (major, minor)


def is_macos_catalina_or_older() -> bool:
    """Catalina is macOS 10.15; earlier versions have the same constraints."""
    return is_macos_older_than(11, 0)


def macos_display_name() -> str:
    version = macos_version()
    if version is None:
        return "non-macOS"
    version_text = ".".join(str(part) for part in version)
    if version[:2] == (10, 15):
        return f"macOS Catalina {version_text}"
    return f"macOS {version_text}"


def catalina_runtime_notes() -> list[str]:
    """Human-readable constraints for macOS Catalina and older."""
    if not is_macos_catalina_or_older():
        return []
    return [
        "Use `python3`; Catalina's system `python` is Python 2.7.",
        "Use Remotion/FFmpeg for local composition. HyperFrames is disabled because its Node 22 + modern browser runtime is not supported on Catalina.",
        "Use CPU local ML paths unless you have a separate supported GPU stack. Apple MPS requires macOS 12.3+.",
    ]


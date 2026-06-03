"""Postprocess extracted text before SSMD generation or playback."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any


EPUB_CHAPTER_MARKER_PATTERN = re.compile(
    r"^\s*<<CHAPTER:[^>]*>>\s*\n*", re.MULTILINE
)
ELLIPSIS_PATTERN = re.compile(r"\.\.\.(?=\s|$)")
NON_BOOK_ABBREVIATION_PATTERN = re.compile(
    r"\b(?P<word>No|no)\.(?=(?:[\"'\u201d\u2019])?(?:\s|$))"
)


@dataclass(frozen=True)
class TextPostprocessOptions:
    """Controls for extracted-text postprocessing.

    Direct SSMD input is expected to be hand-tuned and should not use this stage.
    """

    replace_non_book_abbreviations: bool = False


def resolve_text_postprocess_options(
    config: dict[str, Any],
) -> TextPostprocessOptions:
    """Resolve text postprocessing options."""
    return TextPostprocessOptions(
        replace_non_book_abbreviations=bool(
            config.get("replace_non_book_abbreviations", False)
        )
    )


def postprocess_extracted_text(
    text: str,
    options: TextPostprocessOptions | None = None,
) -> str:
    """Apply safe postprocessing to extracted non-SSMD text."""
    result = EPUB_CHAPTER_MARKER_PATTERN.sub("", text, count=1)
    result = ELLIPSIS_PATTERN.sub("\u2026", result)
    if options and options.replace_non_book_abbreviations:
        result = NON_BOOK_ABBREVIATION_PATTERN.sub(
            "\\g<word>\N{EN DASH}.",
            result,
        )
    return result

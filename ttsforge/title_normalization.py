"""Helpers for normalizing detected title/header text before TTS."""

from __future__ import annotations


def capitalize_title_for_tts(title: str) -> str:
    """Uppercase the first letter and lowercase the rest of a title."""
    title = title.strip()
    if not title:
        return title

    lowered = title.lower()
    for index, char in enumerate(lowered):
        if char.isalpha():
            return lowered[:index] + char.upper() + lowered[index + 1 :]
    return lowered


def normalize_chapter_titles(chapters: list[object]) -> None:
    """Normalize chapter-like objects with a mutable ``title`` attribute."""
    for chapter in chapters:
        title = getattr(chapter, "title", None)
        if isinstance(title, str):
            setattr(chapter, "title", capitalize_title_for_tts(title))

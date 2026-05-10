"""Tests for ttsforge.kokoro_runner."""

from ttsforge.kokoro_runner import KokoroRunOptions


def test_kokoro_run_options_accepts_short_sentence_override():
    opts = KokoroRunOptions(
        voice="af_heart",
        speed=1.0,
        use_gpu=False,
        pause_clause=0.3,
        pause_sentence=0.5,
        pause_paragraph=0.9,
        pause_variance=0.05,
        enable_short_sentence=True,
    )

    assert opts.enable_short_sentence is True


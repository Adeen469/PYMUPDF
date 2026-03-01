"""
Function: fitz.jm_lineart_clip_stroke_text
Signature: jm_lineart_clip_stroke_text(dev, ctx, text, stroke, ctm, scissor)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_clip_stroke_text:
def jm_lineart_clip_stroke_text(dev, ctx, text, stroke, ctm, scissor):
    if not dev.clips:
        return
    compute_scissor(dev)
    dev.depth += 1

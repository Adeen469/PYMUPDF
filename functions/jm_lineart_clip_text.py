"""
Function: fitz.jm_lineart_clip_text
Signature: jm_lineart_clip_text(dev, ctx, text, ctm, scissor)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_clip_text:
def jm_lineart_clip_text(dev, ctx, text, ctm, scissor):
    if not dev.clips:
        return
    compute_scissor(dev)
    dev.depth += 1

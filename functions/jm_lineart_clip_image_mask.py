"""
Function: fitz.jm_lineart_clip_image_mask
Signature: jm_lineart_clip_image_mask(dev, ctx, image, ctm, scissor)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_clip_image_mask:
def jm_lineart_clip_image_mask( dev, ctx, image, ctm, scissor):
    if not dev.clips:
        return
    compute_scissor(dev)
    dev.depth += 1

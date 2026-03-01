"""
Function: fitz.jm_lineart_pop_clip
Signature: jm_lineart_pop_clip(dev, ctx)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_pop_clip:
def jm_lineart_pop_clip(dev, ctx):
    if not dev.clips or not dev.scissors:
        return
    len_ = len(dev.scissors)
    if len_ < 1:
        return
    del dev.scissors[-1]
    dev.depth -= 1

"""
Function: fitz.jm_lineart_stroke_text
Signature: jm_lineart_stroke_text(dev, ctx, text, stroke, ctm, colorspace, color, alpha, color_params)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_stroke_text:
def jm_lineart_stroke_text(dev, ctx, text, stroke, ctm, colorspace, color, alpha, color_params):
    jm_trace_text(dev, text, 1, ctm, colorspace, color, alpha, dev.seqno)
    dev.seqno += 1

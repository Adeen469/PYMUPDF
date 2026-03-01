"""
Function: fitz.jm_bbox_stroke_text
Signature: jm_bbox_stroke_text(dev, ctx, text, stroke, ctm, *args)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_bbox_stroke_text:
def jm_bbox_stroke_text( dev, ctx, text, stroke, ctm, *args):
    try:
        jm_bbox_add_rect( dev, ctx, mupdf.ll_fz_bound_text( text, stroke, ctm), "stroke-text")
    except Exception:
        if g_exceptions_verbose:    exception_info()
        raise

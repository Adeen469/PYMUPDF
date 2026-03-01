"""
Function: fitz.jm_bbox_fill_text
Signature: jm_bbox_fill_text(dev, ctx, text, ctm, *args)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_bbox_fill_text:
def jm_bbox_fill_text( dev, ctx, text, ctm, *args):
    try:
        jm_bbox_add_rect( dev, ctx, mupdf.ll_fz_bound_text( text, None, ctm), "fill-text")
    except Exception:
        if g_exceptions_verbose:    exception_info()
        raise

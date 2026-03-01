"""
Function: fitz.jm_bbox_fill_shade
Signature: jm_bbox_fill_shade(dev, ctx, shade, ctm, alpha, color_params)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_bbox_fill_shade:
def jm_bbox_fill_shade( dev, ctx, shade, ctm, alpha, color_params):
    try:
        jm_bbox_add_rect( dev, ctx, mupdf.ll_fz_bound_shade( shade, ctm), "fill-shade")
    except Exception:
        if g_exceptions_verbose:    exception_info()
        raise

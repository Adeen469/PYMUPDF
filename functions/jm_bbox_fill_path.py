"""
Function: fitz.jm_bbox_fill_path
Signature: jm_bbox_fill_path(dev, ctx, path, even_odd, ctm, colorspace, color, alpha, color_params)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_bbox_fill_path:
def jm_bbox_fill_path( dev, ctx, path, even_odd, ctm, colorspace, color, alpha, color_params):
    even_odd = True if even_odd else False
    try:
        jm_bbox_add_rect( dev, ctx, mupdf.ll_fz_bound_path(path, None, ctm), "fill-path")
    except Exception:
        if g_exceptions_verbose:    exception_info()
        raise

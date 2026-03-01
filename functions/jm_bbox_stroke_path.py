"""
Function: fitz.jm_bbox_stroke_path
Signature: jm_bbox_stroke_path(dev, ctx, path, stroke, ctm, colorspace, color, alpha, color_params)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_bbox_stroke_path:
def jm_bbox_stroke_path( dev, ctx, path, stroke, ctm, colorspace, color, alpha, color_params):
    try:
        jm_bbox_add_rect( dev, ctx, mupdf.ll_fz_bound_path( path, stroke, ctm), "stroke-path")
    except Exception:
        if g_exceptions_verbose:    exception_info()
        raise

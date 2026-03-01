"""
Function: fitz.jm_bbox_fill_image_mask
Signature: jm_bbox_fill_image_mask(dev, ctx, image, ctm, colorspace, color, alpha, color_params)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_bbox_fill_image_mask:
def jm_bbox_fill_image_mask( dev, ctx, image, ctm, colorspace, color, alpha, color_params):
    try:
        jm_bbox_add_rect( dev, ctx, mupdf.ll_fz_transform_rect(mupdf.fz_unit_rect, ctm), "fill-imgmask")
    except Exception:
        if g_exceptions_verbose:    exception_info()
        raise

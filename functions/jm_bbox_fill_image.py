"""
Function: fitz.jm_bbox_fill_image
Signature: jm_bbox_fill_image(dev, ctx, image, ctm, alpha, color_params)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_bbox_fill_image:
def jm_bbox_fill_image( dev, ctx, image, ctm, alpha, color_params):
    r = mupdf.FzRect(mupdf.FzRect.Fixed_UNIT)
    r = mupdf.ll_fz_transform_rect( r.internal(), ctm)
    jm_bbox_add_rect( dev, ctx, r, "fill-image")

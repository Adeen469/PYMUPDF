"""
Function: fitz.JM_image_filter
Signature: JM_image_filter(opaque, ctm, name, image)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_image_filter:
def JM_image_filter(opaque, ctm, name, image):
    assert isinstance(ctm, mupdf.FzMatrix)
    r = mupdf.FzRect(mupdf.FzRect.Fixed_UNIT)
    q = mupdf.fz_transform_quad( mupdf.fz_quad_from_rect(r), ctm)
    q = mupdf.fz_transform_quad( q, g_img_info_matrix)
    temp = name, JM_py_from_quad(q)
    g_img_info.append(temp)

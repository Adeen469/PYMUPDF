"""
Function: fitz.JM_make_image_block
Signature: JM_make_image_block(block, block_dict)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_make_image_block:
def JM_make_image_block(block, block_dict):
    img = block.i_image()
    _make_image_dict(img, block_dict)
    # if the image has a mask, store it as a PNG buffer
    mask = img.mask()
    if mask.m_internal:
        buff = mask.fz_new_buffer_from_image_as_png(mupdf.FzColorParams(mupdf.fz_default_color_params))
        block_dict["mask"] = buff.fz_buffer_extract()
    else:
        block_dict["mask"] = None
    block_dict[dictkey_matrix] = JM_py_from_matrix(block.i_transform())

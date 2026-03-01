"""
Function: fitz.jm_bbox_add_rect
Signature: jm_bbox_add_rect(dev, ctx, rect, code)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_bbox_add_rect:
def jm_bbox_add_rect( dev, ctx, rect, code):
    if not dev.layers:
        dev.result.append( (code, JM_py_from_rect(rect)))
    else:
        dev.result.append( (code, JM_py_from_rect(rect), dev.layer_name))

"""
Function: fitz.JM_new_bbox_device
Signature: JM_new_bbox_device(rc, inc_layers)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_new_bbox_device:
def JM_new_bbox_device(rc, inc_layers):
    assert isinstance(rc, list)
    return JM_new_bbox_device_Device( rc, inc_layers)

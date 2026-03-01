"""
Function: fitz.JM_FLOAT_ITEM
Signature: JM_FLOAT_ITEM(obj, idx)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_FLOAT_ITEM:
def JM_FLOAT_ITEM(obj, idx):
    if not PySequence_Check(obj):
        return None
    return float(obj[idx])

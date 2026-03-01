"""
Function: fitz.JM_INT_ITEM
Signature: JM_INT_ITEM(obj, idx)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_INT_ITEM:
def JM_INT_ITEM(obj, idx):
    if idx < len(obj):
        temp = obj[idx]
        if isinstance(temp, (int, float)):
            return 0, temp
    return 1, None

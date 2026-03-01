"""
Function: fitz.ENSURE_OPERATION
Signature: ENSURE_OPERATION(pdf)
Description: No docstring available.
"""

import fitz

# Source code of fitz.ENSURE_OPERATION:
def ENSURE_OPERATION(pdf):
    if not JM_have_operation(pdf):
        raise Exception("No journalling operation started")

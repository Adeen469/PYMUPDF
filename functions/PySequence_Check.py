"""
Function: fitz.PySequence_Check
Signature: PySequence_Check(s)
Description: No docstring available.
"""

import fitz

# Source code of fitz.PySequence_Check:
def PySequence_Check(s):
    return isinstance(s, (tuple, list))

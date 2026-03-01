"""
Function: fitz.canon
Signature: canon(c)
Description: No docstring available.
"""

import fitz

# Source code of fitz.canon:
def canon(c):
    assert isinstance(c, int)
    # TODO: proper unicode case folding
    # TODO: character equivalence (a matches ä, etc)
    if c == 0xA0 or c == 0x2028 or c == 0x2029:
        return ord(' ')
    if c == ord('\r') or c == ord('\n') or c == ord('\t'):
        return ord(' ')
    if c >= ord('A') and c <= ord('Z'):
        return c - ord('A') + ord('a')
    return c

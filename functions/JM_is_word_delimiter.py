"""
Function: fitz.JM_is_word_delimiter
Signature: JM_is_word_delimiter(ch, delimiters)
Description:
Check if ch is an extra word delimiting character.
    
"""

import fitz

# Source code of fitz.JM_is_word_delimiter:
def JM_is_word_delimiter(ch, delimiters):
    """Check if ch is an extra word delimiting character.
    """
    if (0
        or ch <= 32
        or ch == 160
        or 0x202a <= ch <= 0x202e
    ):
        # covers any whitespace plus unicodes that switch between
        # right-to-left and left-to-right languages
        return True
    if not delimiters:  # no extra delimiters provided
        return False
    char = chr(ch)
    for d in delimiters:
        if d == char:
            return True
    return False

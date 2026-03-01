"""
Function: fitz.find_string
Signature: find_string(s, needle)
Description: No docstring available.
"""

import fitz

# Source code of fitz.find_string:
def find_string(s, needle):
    assert isinstance(s, str)
    for i in range(len(s)):
        end = match_string(s[i:], needle)
        if end is not None:
            end += i
            return i, end
    return None, None

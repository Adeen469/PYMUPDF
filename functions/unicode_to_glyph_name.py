"""
Function: fitz.unicode_to_glyph_name
Signature: unicode_to_glyph_name(ch: int) -> str
Description:
Convenience function accessing unicodedata.
"""

import fitz

# Source code of fitz.unicode_to_glyph_name:
def unicode_to_glyph_name(ch: int) -> str:
    """
    Convenience function accessing unicodedata.
    """
    import unicodedata
    try:
        name = unicodedata.name(chr(ch))
    except ValueError:
        name = ".notdef"
    return name

"""
Function: fitz.glyph_name_to_unicode
Signature: glyph_name_to_unicode(name: str) -> int
Description:
Convenience function accessing unicodedata.
"""

import fitz

# Source code of fitz.glyph_name_to_unicode:
def glyph_name_to_unicode(name: str) -> int:
    """Convenience function accessing unicodedata."""
    import unicodedata
    try:
        unc = ord(unicodedata.lookup(name))
    except Exception:
        unc = 65533
    return unc

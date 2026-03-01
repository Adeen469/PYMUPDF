"""
Function: fitz.repair_mono_font
Signature: repair_mono_font(page: 'Page', font: 'Font') -> None
Description:
Repair character spacing for mono fonts.

Notes:
    Some mono-spaced fonts are displayed with a too large character
    distance, e.g. "a b c" instead of "abc". This utility adds an entry
    "/W[0 65535 w]" to the descendent font(s) of font. The float w is
    taken to be the width of 0x20 (space).
    This should enforce viewers to use 'w' as the character width.

Args:
    page: pymupdf.Page object.
    font: pymupdf.Font object.
"""

import fitz

# Source code of fitz.repair_mono_font:
def repair_mono_font(page: "Page", font: "Font") -> None:
    """Repair character spacing for mono fonts.

    Notes:
        Some mono-spaced fonts are displayed with a too large character
        distance, e.g. "a b c" instead of "abc". This utility adds an entry
        "/W[0 65535 w]" to the descendent font(s) of font. The float w is
        taken to be the width of 0x20 (space).
        This should enforce viewers to use 'w' as the character width.

    Args:
        page: pymupdf.Page object.
        font: pymupdf.Font object.
    """
    if not font.flags["mono"]:  # font not flagged as monospaced
        return None
    doc = page.parent  # the document
    fontlist = page.get_fonts()  # list of fonts on page
    xrefs = [  # list of objects referring to font
        f[0]
        for f in fontlist
        if (f[3] == font.name and f[4].startswith("F") and f[5].startswith("Identity"))
    ]
    if xrefs == []:  # our font does not occur
        return
    xrefs = set(xrefs)  # drop any double counts
    width = int(round((font.glyph_advance(32) * 1000)))
    for xref in xrefs:
        if not TOOLS.set_font_width(doc, xref, width):
            log("Cannot set width for '%s' in xref %i" % (font.name, xref))

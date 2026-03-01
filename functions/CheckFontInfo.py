"""
Function: fitz.CheckFontInfo
Signature: CheckFontInfo(doc: pymupdf.Document, xref: int) -> list
Description:
Return a font info if present in the document.
    
"""

import fitz

# Source code of fitz.CheckFontInfo:
def CheckFontInfo(doc: Document, xref: int) -> list:
    """Return a font info if present in the document.
    """
    for f in doc.FontInfos:
        if xref == f[0]:
            return f

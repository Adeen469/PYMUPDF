"""
Function: fitz.CheckFont
Signature: CheckFont(page: pymupdf.Page, fontname: str) -> tuple
Description:
Return an entry in the page's font list if reference name matches.
    
"""

import fitz

# Source code of fitz.CheckFont:
def CheckFont(page: Page, fontname: str) -> tuple:
    """Return an entry in the page's font list if reference name matches.
    """
    for f in page.get_fonts():
        if f[4] == fontname:
            return f

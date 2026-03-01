"""
Function: fitz.paper_rect
Signature: paper_rect(s: str) -> pymupdf.Rect
Description:
Return a Rect for the paper size indicated in string 's'. Must conform to the argument of method 'PaperSize', which will be invoked.
    
"""

import fitz

# Source code of fitz.paper_rect:
def paper_rect(s: str) -> Rect:
    """Return a Rect for the paper size indicated in string 's'. Must conform to the argument of method 'PaperSize', which will be invoked.
    """
    width, height = paper_size(s)
    return Rect(0.0, 0.0, width, height)

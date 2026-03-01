"""
Function: fitz.UpdateFontInfo
Signature: UpdateFontInfo(doc: pymupdf.Document, info: Sequence)
Description: No docstring available.
"""

import fitz

# Source code of fitz.UpdateFontInfo:
def UpdateFontInfo(doc: Document, info: typing.Sequence):
    xref = info[0]
    found = False
    for i, fi in enumerate(doc.FontInfos):
        if fi[0] == xref:
            found = True
            break
    if found:
        doc.FontInfos[i] = info
    else:
        doc.FontInfos.append(info)

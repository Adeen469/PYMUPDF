"""
Function: fitz.JM_annot_colors
Signature: JM_annot_colors(annot_obj)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_annot_colors:
def JM_annot_colors(annot_obj):
    res = dict()
    bc = list() # stroke colors
    fc =list()  # fill colors
    o = mupdf.pdf_dict_get(annot_obj, mupdf.PDF_ENUM_NAME_C)
    if mupdf.pdf_is_array(o):
        n = mupdf.pdf_array_len(o)
        for i in range(n):
            col = mupdf.pdf_to_real( mupdf.pdf_array_get(o, i))
            bc.append(col)
    res[dictkey_stroke] = bc

    o = mupdf.pdf_dict_gets(annot_obj, "IC")
    if mupdf.pdf_is_array(o):
        n = mupdf.pdf_array_len(o)
        for i in range(n):
            col = mupdf.pdf_to_real( mupdf.pdf_array_get(o, i))
            fc.append(col)

    res[dictkey_fill] = fc
    return res

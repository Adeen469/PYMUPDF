"""
Function: fitz.JM_get_annot_xref_list2
Signature: JM_get_annot_xref_list2(page)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_get_annot_xref_list2:
def JM_get_annot_xref_list2(page):
    page = page._pdf_page(required=False)
    if not page.m_internal:
        return list()
    return JM_get_annot_xref_list( page.obj())

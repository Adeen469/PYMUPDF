"""
Function: fitz.JM_set_ocg_arrays_imp
Signature: JM_set_ocg_arrays_imp(arr, list_)
Description:
Set OCG arrays from dict of Python lists
Works with dict like {"basestate":name, "on":list, "off":list, "rbg":list}
"""

import fitz

# Source code of fitz.JM_set_ocg_arrays_imp:
def JM_set_ocg_arrays_imp(arr, list_):
    '''
    Set OCG arrays from dict of Python lists
    Works with dict like {"basestate":name, "on":list, "off":list, "rbg":list}
    '''
    pdf = mupdf.pdf_get_bound_document(arr)
    for xref in list_:
        obj = mupdf.pdf_new_indirect(pdf, xref, 0)
        mupdf.pdf_array_push(arr, obj)

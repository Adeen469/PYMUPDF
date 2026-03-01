"""
Function: fitz.JM_get_ocg_arrays_imp
Signature: JM_get_ocg_arrays_imp(arr)
Description:
Get OCG arrays from OC configuration
Returns dict {"basestate":name, "on":list, "off":list, "rbg":list, "locked":list}
"""

import fitz

# Source code of fitz.JM_get_ocg_arrays_imp:
def JM_get_ocg_arrays_imp(arr):
    '''
    Get OCG arrays from OC configuration
    Returns dict {"basestate":name, "on":list, "off":list, "rbg":list, "locked":list}
    '''
    list_ = list()
    if mupdf.pdf_is_array( arr):
        n = mupdf.pdf_array_len( arr)
        for i in range(n):
            obj = mupdf.pdf_array_get( arr, i)
            item = mupdf.pdf_to_num( obj)
            if item not in list_:
                list_.append(item)
    return list_

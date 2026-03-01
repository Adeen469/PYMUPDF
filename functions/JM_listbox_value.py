"""
Function: fitz.JM_listbox_value
Signature: JM_listbox_value(annot)
Description:
ListBox retrieve value
"""

import fitz

# Source code of fitz.JM_listbox_value:
def JM_listbox_value( annot):
    '''
    ListBox retrieve value
    '''
    # may be single value or array
    annot_obj = mupdf.pdf_annot_obj( annot)
    optarr = mupdf.pdf_dict_get( annot_obj, PDF_NAME('V'))
    if mupdf.pdf_is_string( optarr):   # a single string
        return mupdf.pdf_to_text_string( optarr)

    # value is an array (may have len 0)
    n = mupdf.pdf_array_len( optarr)
    liste = []

    # extract a list of strings
    # each entry may again be an array: take second entry then
    for i in range( n):
        elem = mupdf.pdf_array_get( optarr, i)
        if mupdf.pdf_is_array( elem):
            elem = mupdf.pdf_array_get( elem, 1)
        liste.append( JM_UnicodeFromStr( mupdf.pdf_to_text_string( elem)))
    return liste

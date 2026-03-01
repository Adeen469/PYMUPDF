"""
Function: fitz.JM_set_choice_options
Signature: JM_set_choice_options(annot, liste)
Description:
set ListBox / ComboBox values
"""

import fitz

# Source code of fitz.JM_set_choice_options:
def JM_set_choice_options(annot, liste):
    '''
    set ListBox / ComboBox values
    '''
    if not liste:
        return
    assert isinstance( liste, (tuple, list))
    n = len( liste)
    if n == 0:
        return
    annot_obj = mupdf.pdf_annot_obj( annot)
    pdf = mupdf.pdf_get_bound_document( annot_obj)
    optarr = mupdf.pdf_new_array( pdf, n)
    for i in range(n):
        val = liste[i]
        opt = val
        if isinstance(opt, str):
            mupdf.pdf_array_push_text_string( optarr, opt)
        else:
            assert isinstance( val, (tuple, list)) and len( val) == 2, 'bad choice field list'
            opt1, opt2 = val
            assert opt1 and opt2, 'bad choice field list'
            optarrsub = mupdf.pdf_array_push_array( optarr, 2)
            mupdf.pdf_array_push_text_string( optarrsub, opt1)
            mupdf.pdf_array_push_text_string( optarrsub, opt2)
    mupdf.pdf_dict_put( annot_obj, PDF_NAME('Opt'), optarr)

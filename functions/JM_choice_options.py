"""
Function: fitz.JM_choice_options
Signature: JM_choice_options(annot)
Description:
return list of choices for list or combo boxes
"""

import fitz

# Source code of fitz.JM_choice_options:
def JM_choice_options(annot):
    '''
    return list of choices for list or combo boxes
    '''
    annot_obj = mupdf.pdf_annot_obj( annot.this)
    
    opts = mupdf.pdf_choice_widget_options2( annot, 0)
    n = len( opts)
    if n == 0:
        return  # wrong widget type

    optarr = mupdf.pdf_dict_get( annot_obj, PDF_NAME('Opt'))
    liste = []

    for i in range( n):
        m = mupdf.pdf_array_len( mupdf.pdf_array_get( optarr, i))
        if m == 2:
            val = (
                    mupdf.pdf_to_text_string( mupdf.pdf_array_get( mupdf.pdf_array_get( optarr, i), 0)),
                    mupdf.pdf_to_text_string( mupdf.pdf_array_get( mupdf.pdf_array_get( optarr, i), 1)),
                    )
            liste.append( val)
        else:
            val = mupdf.pdf_to_text_string( mupdf.pdf_array_get( optarr, i))
            liste.append( val)
    return liste

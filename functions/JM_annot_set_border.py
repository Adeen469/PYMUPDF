"""
Function: fitz.JM_annot_set_border
Signature: JM_annot_set_border(border, doc, annot_obj)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_annot_set_border:
def JM_annot_set_border( border, doc, annot_obj):
    assert isinstance(border, dict)
    obj = None
    dashlen = 0
    nwidth = border.get( dictkey_width)     # new width
    ndashes = border.get( dictkey_dashes)   # new dashes
    nstyle = border.get( dictkey_style)     # new style
    nclouds  = border.get( 'clouds', -1)    # new clouds value

    # get old border properties
    oborder = JM_annot_border( annot_obj)

    # delete border-related entries
    mupdf.pdf_dict_del( annot_obj, PDF_NAME('BS'))
    mupdf.pdf_dict_del( annot_obj, PDF_NAME('BE'))
    mupdf.pdf_dict_del( annot_obj, PDF_NAME('Border'))

    # populate border items: keep old values for any omitted new ones
    if nwidth < 0:
        nwidth = oborder.get( dictkey_width)    # no new width: keep current
    if ndashes is None:
        ndashes = oborder.get( dictkey_dashes)  # no new dashes: keep old
    if nstyle is None:
        nstyle  = oborder.get( dictkey_style)   # no new style: keep old
    if nclouds < 0:
        nclouds  = oborder.get( "clouds", -1)   # no new clouds: keep old

    if isinstance( ndashes, tuple) and len( ndashes) > 0:
        dashlen = len( ndashes)
        darr = mupdf.pdf_new_array( doc, dashlen)
        for d in ndashes:
            mupdf.pdf_array_push_int( darr, d)
        mupdf.pdf_dict_putl( annot_obj, darr, PDF_NAME('BS'), PDF_NAME('D'))

    mupdf.pdf_dict_putl(
            annot_obj,
            mupdf.pdf_new_real( nwidth),
            PDF_NAME('BS'),
            PDF_NAME('W'),
            )

    if dashlen == 0:
        obj = JM_get_border_style( nstyle)
    else:
        obj = PDF_NAME('D')
    mupdf.pdf_dict_putl( annot_obj, obj, PDF_NAME('BS'), PDF_NAME('S'))

    if nclouds > 0:
        mupdf.pdf_dict_put_dict( annot_obj, PDF_NAME('BE'), 2)
        obj = mupdf.pdf_dict_get( annot_obj, PDF_NAME('BE'))
        mupdf.pdf_dict_put( obj, PDF_NAME('S'), PDF_NAME('C'))
        mupdf.pdf_dict_put_int( obj, PDF_NAME('I'), nclouds)

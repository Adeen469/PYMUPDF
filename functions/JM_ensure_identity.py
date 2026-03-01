"""
Function: fitz.JM_ensure_identity
Signature: JM_ensure_identity(pdf)
Description:
Store ID in PDF trailer
"""

import fitz

# Source code of fitz.JM_ensure_identity:
def JM_ensure_identity(pdf):
    '''
    Store ID in PDF trailer
    '''
    id_ = mupdf.pdf_dict_get( mupdf.pdf_trailer(pdf), PDF_NAME('ID'))
    if not id_.m_internal:
        rnd0 = mupdf.fz_memrnd2(16)
        # Need to convert raw bytes into a str to send to
        # mupdf.pdf_new_string(). chr() seems to work for this.
        rnd = ''
        for i in rnd0:
            rnd += chr(i)
        id_ = mupdf.pdf_dict_put_array( mupdf.pdf_trailer( pdf), PDF_NAME('ID'), 2)
        mupdf.pdf_array_push( id_, mupdf.pdf_new_string( rnd, len(rnd)))
        mupdf.pdf_array_push( id_, mupdf.pdf_new_string( rnd, len(rnd)))

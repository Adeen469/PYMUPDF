"""
Function: fitz.JM_add_oc_object
Signature: JM_add_oc_object(pdf, ref, xref)
Description:
Add OC object reference to a dictionary
"""

import fitz

# Source code of fitz.JM_add_oc_object:
def JM_add_oc_object(pdf, ref, xref):
    '''
    Add OC object reference to a dictionary
    '''
    indobj = mupdf.pdf_new_indirect(pdf, xref, 0)
    if not mupdf.pdf_is_dict(indobj):
        RAISEPY(MSG_BAD_OC_REF, PyExc_ValueError)
    type_ = mupdf.pdf_dict_get(indobj, PDF_NAME('Type'))
    if (mupdf.pdf_objcmp(type_, PDF_NAME('OCG')) == 0
            or mupdf.pdf_objcmp(type_, PDF_NAME('OCMD')) == 0
            ):
        mupdf.pdf_dict_put(ref, PDF_NAME('OC'), indobj)
    else:
        RAISEPY(MSG_BAD_OC_REF, PyExc_ValueError)

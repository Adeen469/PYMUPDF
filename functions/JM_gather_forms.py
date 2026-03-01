"""
Function: fitz.JM_gather_forms
Signature: JM_gather_forms(doc, dict_: pymupdf.mupdf.PdfObj, imagelist, stream_xref: int)
Description:
Store info of a /Form xobject in Python list
"""

import fitz

# Source code of fitz.JM_gather_forms:
def JM_gather_forms(doc, dict_: mupdf.PdfObj, imagelist, stream_xref: int):
    '''
    Store info of a /Form xobject in Python list
    '''
    assert isinstance(doc, mupdf.PdfDocument)
    rc = 1
    n = mupdf.pdf_dict_len(dict_)
    for i in range(n):
        refname = mupdf.pdf_dict_get_key( dict_, i)
        imagedict = mupdf.pdf_dict_get_val(dict_, i)
        if not mupdf.pdf_is_dict(imagedict):
            mupdf.fz_warn( f"'{mupdf.pdf_to_name(refname)}' is no form dict ({mupdf.pdf_to_num(imagedict)} 0 R)")
            continue

        type_ = mupdf.pdf_dict_get(imagedict, PDF_NAME('Subtype'))
        if not mupdf.pdf_name_eq(type_, PDF_NAME('Form')):
            continue

        o = mupdf.pdf_dict_get(imagedict, PDF_NAME('BBox'))
        m = mupdf.pdf_dict_get(imagedict, PDF_NAME('Matrix'))
        if m.m_internal:
            mat = mupdf.pdf_to_matrix(m)
        else:
            mat = mupdf.FzMatrix()
        if o.m_internal:
            bbox = mupdf.fz_transform_rect( mupdf.pdf_to_rect(o), mat)
        else:
            bbox = mupdf.FzRect(mupdf.FzRect.Fixed_INFINITE)
        xref = mupdf.pdf_to_num(imagedict)

        entry = (
                xref,
                mupdf.pdf_to_name( refname),
                stream_xref,
                JM_py_from_rect(bbox),
                )
        imagelist.append(entry)
    return rc

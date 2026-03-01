"""
Function: fitz.JM_xobject_from_page
Signature: JM_xobject_from_page(pdfout, fsrcpage, xref, gmap)
Description:
Make an XObject from a PDF page
For a positive xref assume that its object can be used instead
"""

import fitz

# Source code of fitz.JM_xobject_from_page:
def JM_xobject_from_page(pdfout, fsrcpage, xref, gmap):
    '''
    Make an XObject from a PDF page
    For a positive xref assume that its object can be used instead
    '''
    assert isinstance(gmap, mupdf.PdfGraftMap), f'{type(gmap)=}'
    if xref > 0:
        xobj1 = mupdf.pdf_new_indirect(pdfout, xref, 0)
    else:
        srcpage = _as_pdf_page(fsrcpage.this)
        spageref = srcpage.obj()
        mediabox = mupdf.pdf_to_rect(mupdf.pdf_dict_get_inheritable(spageref, PDF_NAME('MediaBox')))
        # Deep-copy resources object of source page
        o = mupdf.pdf_dict_get_inheritable(spageref, PDF_NAME('Resources'))
        if gmap.m_internal:
            # use graftmap when possible
            resources = mupdf.pdf_graft_mapped_object(gmap, o)
        else:
            resources = mupdf.pdf_graft_object(pdfout, o)

        # get spgage contents source
        res = JM_read_contents(spageref)

        #-------------------------------------------------------------
        # create XObject representing the source page
        #-------------------------------------------------------------
        xobj1 = mupdf.pdf_new_xobject(pdfout, mediabox, mupdf.FzMatrix(), mupdf.PdfObj(0), res)
        # store spage contents
        JM_update_stream(pdfout, xobj1, res, 1)

        # store spage resources
        mupdf.pdf_dict_put(xobj1, PDF_NAME('Resources'), resources)
    return xobj1

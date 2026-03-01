"""
Function: fitz.JM_scan_resources
Signature: JM_scan_resources(pdf, rsrc, liste, what, stream_xref, tracer)
Description:
Step through /Resources, looking up image, xobject or font information
"""

import fitz

# Source code of fitz.JM_scan_resources:
def JM_scan_resources(pdf, rsrc, liste, what, stream_xref, tracer):
    '''
    Step through /Resources, looking up image, xobject or font information
    '''
    if mupdf.pdf_mark_obj(rsrc):
        mupdf.fz_warn('Circular dependencies! Consider page cleaning.')
        return  # Circular dependencies!
    try:
        xobj = mupdf.pdf_dict_get(rsrc, mupdf.PDF_ENUM_NAME_XObject)

        if what == 1:   # lookup fonts
            font = mupdf.pdf_dict_get(rsrc, mupdf.PDF_ENUM_NAME_Font)
            JM_gather_fonts(pdf, font, liste, stream_xref)
        elif what == 2: # look up images
            JM_gather_images(pdf, xobj, liste, stream_xref)
        elif what == 3: # look up form xobjects
            JM_gather_forms(pdf, xobj, liste, stream_xref)
        else:   # should never happen
            return

        # check if we need to recurse into Form XObjects
        n = mupdf.pdf_dict_len(xobj)
        for i in range(n):
            obj = mupdf.pdf_dict_get_val(xobj, i)
            if mupdf.pdf_is_stream(obj):
                sxref = mupdf.pdf_to_num(obj)
            else:
                sxref = 0
            subrsrc = mupdf.pdf_dict_get(obj, mupdf.PDF_ENUM_NAME_Resources)
            if subrsrc.m_internal:
                sxref_t = sxref
                if sxref_t not in tracer:
                    tracer.append(sxref_t)
                    JM_scan_resources( pdf, subrsrc, liste, what, sxref, tracer)
                else:
                    mupdf.fz_warn('Circular dependencies! Consider page cleaning.')
                    return
    finally:
        mupdf.pdf_unmark_obj(rsrc)

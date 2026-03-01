"""
Function: fitz.JM_get_fontbuffer
Signature: JM_get_fontbuffer(doc, xref)
Description:
Return the contents of a font file, identified by xref
"""

import fitz

# Source code of fitz.JM_get_fontbuffer:
def JM_get_fontbuffer(doc, xref):
    '''
    Return the contents of a font file, identified by xref
    '''
    if xref < 1:
        return
    o = mupdf.pdf_load_object(doc, xref)
    desft = mupdf.pdf_dict_get(o, PDF_NAME('DescendantFonts'))
    if desft.m_internal:
        obj = mupdf.pdf_resolve_indirect(mupdf.pdf_array_get(desft, 0))
        obj = mupdf.pdf_dict_get(obj, PDF_NAME('FontDescriptor'))
    else:
        obj = mupdf.pdf_dict_get(o, PDF_NAME('FontDescriptor'))

    if not obj.m_internal:
        message(f"invalid font - FontDescriptor missing")
        return

    o = obj

    stream = None

    obj = mupdf.pdf_dict_get(o, PDF_NAME('FontFile'))
    if obj.m_internal:
        stream = obj    # ext = "pfa"

    obj = mupdf.pdf_dict_get(o, PDF_NAME('FontFile2'))
    if obj.m_internal:
        stream = obj    # ext = "ttf"

    obj = mupdf.pdf_dict_get(o, PDF_NAME('FontFile3'))
    if obj.m_internal:
        stream = obj

        obj = mupdf.pdf_dict_get(obj, PDF_NAME('Subtype'))
        if obj.m_internal and not mupdf.pdf_is_name(obj):
            message("invalid font descriptor subtype")
            return

        if mupdf.pdf_name_eq(obj, PDF_NAME('Type1C')):
            pass    # Prev code did: ext = "cff", but this has no effect.
        elif mupdf.pdf_name_eq(obj, PDF_NAME('CIDFontType0C')):
            pass    # Prev code did: ext = "cid", but this has no effect.
        elif mupdf.pdf_name_eq(obj, PDF_NAME('OpenType')):
            pass    # Prev code did: ext = "otf", but this has no effect. */
        else:
            message('warning: unhandled font type {pdf_to_name(ctx, obj)!r}')

    if not stream:
        message('warning: unhandled font type')
        return

    return mupdf.pdf_load_stream(stream)

"""
Function: fitz.JM_get_resource_properties
Signature: JM_get_resource_properties(ref)
Description:
Return the items of Resources/Properties (used for Marked Content)
Argument may be e.g. a page object or a Form XObject
"""

import fitz

# Source code of fitz.JM_get_resource_properties:
def JM_get_resource_properties(ref):
    '''
    Return the items of Resources/Properties (used for Marked Content)
    Argument may be e.g. a page object or a Form XObject
    '''
    properties = mupdf.pdf_dict_getl(ref, PDF_NAME('Resources'), PDF_NAME('Properties'))
    if not properties.m_internal:
        return ()
    else:
        n = mupdf.pdf_dict_len(properties)
        if n < 1:
            return ()
        rc = []
        for i in range(n):
            key = mupdf.pdf_dict_get_key(properties, i)
            val = mupdf.pdf_dict_get_val(properties, i)
            c = mupdf.pdf_to_name(key)
            xref = mupdf.pdf_to_num(val)
            rc.append((c, xref))
    return rc

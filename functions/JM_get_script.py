"""
Function: fitz.JM_get_script
Signature: JM_get_script(key)
Description:
JavaScript extractor
Returns either the script source or None. Parameter is a PDF action
dictionary, which must have keys /S and /JS. The value of /S must be
'/JavaScript'. The value of /JS is returned.
"""

import fitz

# Source code of fitz.JM_get_script:
def JM_get_script(key):
    '''
    JavaScript extractor
    Returns either the script source or None. Parameter is a PDF action
    dictionary, which must have keys /S and /JS. The value of /S must be
    '/JavaScript'. The value of /JS is returned.
    '''
    if not key.m_internal:
        return

    j = mupdf.pdf_dict_get(key, PDF_NAME('S'))
    jj = mupdf.pdf_to_name(j)
    if jj == "JavaScript":
        js = mupdf.pdf_dict_get(key, PDF_NAME('JS'))
        if not js.m_internal:
            return
    else:
        return

    if mupdf.pdf_is_string(js):
        script = JM_UnicodeFromStr(mupdf.pdf_to_text_string(js))
    elif mupdf.pdf_is_stream(js):
        res = mupdf.pdf_load_stream(js)
        script = JM_EscapeStrFromBuffer(res)
    else:
        return
    if script:  # do not return an empty script
        return script
    return

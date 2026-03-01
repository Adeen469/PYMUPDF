"""
Function: fitz.JM_insert_contents
Signature: JM_insert_contents(pdf, pageref, newcont, overlay)
Description:
Insert a buffer as a new separate /Contents object of a page.
1. Create a new stream object from buffer 'newcont'
2. If /Contents already is an array, then just prepend or append this object
3. Else, create new array and put old content obj and this object into it.
   If the page had no /Contents before, just create a 1-item array.
"""

import fitz

# Source code of fitz.JM_insert_contents:
def JM_insert_contents(pdf, pageref, newcont, overlay):
    '''
    Insert a buffer as a new separate /Contents object of a page.
    1. Create a new stream object from buffer 'newcont'
    2. If /Contents already is an array, then just prepend or append this object
    3. Else, create new array and put old content obj and this object into it.
       If the page had no /Contents before, just create a 1-item array.
    '''
    contents = mupdf.pdf_dict_get(pageref, PDF_NAME('Contents'))
    newconts = mupdf.pdf_add_stream(pdf, newcont, mupdf.PdfObj(), 0)
    xref = mupdf.pdf_to_num(newconts)
    if mupdf.pdf_is_array(contents):
        if overlay:  # append new object
            mupdf.pdf_array_push(contents, newconts)
        else:   # prepend new object
            mupdf.pdf_array_insert(contents, newconts, 0)
    else:
        carr = mupdf.pdf_new_array(pdf, 5)
        if overlay:
            if contents.m_internal:
                mupdf.pdf_array_push(carr, contents)
            mupdf.pdf_array_push(carr, newconts)
        else:
            mupdf.pdf_array_push(carr, newconts)
            if contents.m_internal:
                mupdf.pdf_array_push(carr, contents)
        mupdf.pdf_dict_put(pageref, PDF_NAME('Contents'), carr)
    return xref

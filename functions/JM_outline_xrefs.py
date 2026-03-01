"""
Function: fitz.JM_outline_xrefs
Signature: JM_outline_xrefs(obj, xrefs)
Description:
Return list of outline xref numbers. Recursive function. Arguments:
'obj' first OL item
'xrefs' empty Python list
"""

import fitz

# Source code of fitz.JM_outline_xrefs:
def JM_outline_xrefs(obj, xrefs):
    '''
    Return list of outline xref numbers. Recursive function. Arguments:
    'obj' first OL item
    'xrefs' empty Python list
    '''
    if not obj.m_internal:
        return xrefs
    thisobj = obj
    while thisobj.m_internal:
        newxref = mupdf.pdf_to_num( thisobj)
        if newxref in xrefs or mupdf.pdf_dict_get( thisobj, PDF_NAME('Type')).m_internal:
            # circular ref or top of chain: terminate
            break
        xrefs.append( newxref)
        first = mupdf.pdf_dict_get( thisobj, PDF_NAME('First'))    # try go down
        if mupdf.pdf_is_dict( first):
            xrefs = JM_outline_xrefs( first, xrefs)
        thisobj = mupdf.pdf_dict_get( thisobj, PDF_NAME('Next'))   # try go next
        parent = mupdf.pdf_dict_get( thisobj, PDF_NAME('Parent'))  # get parent
        if not mupdf.pdf_is_dict( thisobj):
            thisobj = parent
    return xrefs

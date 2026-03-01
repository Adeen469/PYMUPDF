"""
Function: fitz.strip_outline
Signature: strip_outline(doc, outlines, page_count, page_object_nums, names_list)
Description:
Returns (count, first, prev).
"""

import fitz

# Source code of fitz.strip_outline:
def strip_outline(doc, outlines, page_count, page_object_nums, names_list):
    '''
    Returns (count, first, prev).
    '''
    first = None
    count = 0
    current = outlines
    prev = None
    while current.m_internal:
        # Strip any children to start with. This takes care of
        # First / Last / Count for us.
        nc = strip_outlines(doc, current, page_count, page_object_nums, names_list)

        if not dest_is_valid(current, page_count, page_object_nums, names_list):
            if nc == 0:
                # Outline with invalid dest and no children. Drop it by
                # pulling the next one in here.
                next = mupdf.pdf_dict_get(current, PDF_NAME('Next'))
                if not next.m_internal:
                    # There is no next one to pull in
                    if prev.m_internal:
                        mupdf.pdf_dict_del(prev, PDF_NAME('Next'))
                elif prev.m_internal:
                    mupdf.pdf_dict_put(prev, PDF_NAME('Next'), next)
                    mupdf.pdf_dict_put(next, PDF_NAME('Prev'), prev)
                else:
                    mupdf.pdf_dict_del(next, PDF_NAME('Prev'))
                current = next
            else:
                # Outline with invalid dest, but children. Just drop the dest.
                mupdf.pdf_dict_del(current, PDF_NAME('Dest'))
                mupdf.pdf_dict_del(current, PDF_NAME('A'))
                current = mupdf.pdf_dict_get(current, PDF_NAME('Next'))
        else:
            # Keep this one
            if not first or not first.m_internal:
                first = current
            prev = current
            current = mupdf.pdf_dict_get(current, PDF_NAME('Next'))
            count += 1

    return count, first, prev

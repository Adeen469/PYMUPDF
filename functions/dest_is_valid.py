"""
Function: fitz.dest_is_valid
Signature: dest_is_valid(o, page_count, page_object_nums, names_list)
Description: No docstring available.
"""

import fitz

# Source code of fitz.dest_is_valid:
def dest_is_valid(o, page_count, page_object_nums, names_list):
    p = mupdf.pdf_dict_get( o, PDF_NAME('A'))
    if (
            mupdf.pdf_name_eq(
                mupdf.pdf_dict_get( p, PDF_NAME('S')),
                PDF_NAME('GoTo')
                )
            and not string_in_names_list(
                mupdf.pdf_dict_get( p, PDF_NAME('D')),
                names_list
                )
            ):
        return 0

    p = mupdf.pdf_dict_get( o, PDF_NAME('Dest'))
    if not p.m_internal:
        pass
    elif mupdf.pdf_is_string( p):
        return string_in_names_list( p, names_list)
    elif not dest_is_valid_page(
            mupdf.pdf_array_get( p, 0),
            page_object_nums,
            page_count,
            ):
        return 0
    return 1

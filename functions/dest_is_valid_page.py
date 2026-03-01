"""
Function: fitz.dest_is_valid_page
Signature: dest_is_valid_page(obj, page_object_nums, pagecount)
Description: No docstring available.
"""

import fitz

# Source code of fitz.dest_is_valid_page:
def dest_is_valid_page(obj, page_object_nums, pagecount):
    num = mupdf.pdf_to_num(obj)

    if num == 0:
        return 0
    for i in range(pagecount):
        if page_object_nums[i] == num:
            return 1
    return 0

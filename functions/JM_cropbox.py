"""
Function: fitz.JM_cropbox
Signature: JM_cropbox(page_obj)
Description:
return a PDF page's CropBox
"""

import fitz

# Source code of fitz.JM_cropbox:
def JM_cropbox(page_obj):
    '''
    return a PDF page's CropBox
    '''
    if g_use_extra:
        return extra.JM_cropbox(page_obj)
    
    mediabox = JM_mediabox(page_obj)
    cropbox = mupdf.pdf_to_rect(
                mupdf.pdf_dict_get_inheritable(page_obj, PDF_NAME('CropBox'))
                )
    if mupdf.fz_is_infinite_rect(cropbox) or mupdf.fz_is_empty_rect(cropbox):
        cropbox = mediabox
    y0 = mediabox.y1 - cropbox.y1
    y1 = mediabox.y1 - cropbox.y0
    cropbox.y0 = y0
    cropbox.y1 = y1
    return cropbox

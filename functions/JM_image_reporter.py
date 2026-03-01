"""
Function: fitz.JM_image_reporter
Signature: JM_image_reporter(page)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_image_reporter:
def JM_image_reporter(page):
    doc = page.doc()
    global g_img_info_matrix
    g_img_info_matrix = mupdf.FzMatrix()
    mediabox = mupdf.FzRect()
    mupdf.pdf_page_transform(page, mediabox, g_img_info_matrix)

    class SanitizeFilterOptions(mupdf.PdfSanitizeFilterOptions2):
        def __init__(self):
            super().__init__()
            self.use_virtual_image_filter()
        def image_filter(self, ctx, ctm, name, image, scissor):
            JM_image_filter(None, mupdf.FzMatrix(ctm), name, image)

    sanitize_filter_options = SanitizeFilterOptions()

    filter_options = _make_PdfFilterOptions(
            instance_forms=1,
            ascii=1,
            no_update=1,
            sanitize=1,
            sopts=sanitize_filter_options,
            )

    global g_img_info
    g_img_info = []

    mupdf.pdf_filter_page_contents( doc, page, filter_options)

    rc = tuple(g_img_info)
    g_img_info = []
    return rc

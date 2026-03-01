"""
Function: fitz.JM_refresh_links
Signature: JM_refresh_links(page)
Description:
refreshes the link and annotation tables of a page
"""

import fitz

# Source code of fitz.JM_refresh_links:
def JM_refresh_links( page):
    '''
    refreshes the link and annotation tables of a page
    '''
    if page is None or not page.m_internal:
        return
    obj = mupdf.pdf_dict_get( page.obj(), PDF_NAME('Annots'))
    if obj.m_internal:
        pdf = page.doc()
        number = mupdf.pdf_lookup_page_number( pdf, page.obj())
        page_mediabox = mupdf.FzRect()
        page_ctm = mupdf.FzMatrix()
        mupdf.pdf_page_transform( page, page_mediabox, page_ctm)
        link = mupdf.pdf_load_link_annots( pdf, page, obj, number, page_ctm)
        page.m_internal.links = mupdf.ll_fz_keep_link( link.m_internal)

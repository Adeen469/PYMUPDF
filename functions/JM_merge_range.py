"""
Function: fitz.JM_merge_range
Signature: JM_merge_range(doc_des, doc_src, spage, epage, apage, rotate, links, annots, show_progress, graft_map)
Description:
Copy a range of pages (spage, epage) from a source PDF to a specified
location (apage) of the target PDF.
If spage > epage, the sequence of source pages is reversed.
"""

import fitz

# Source code of fitz.JM_merge_range:
def JM_merge_range(
        doc_des,
        doc_src,
        spage,
        epage,
        apage,
        rotate,
        links,
        annots,
        show_progress,
        graft_map,
        ):
    '''
    Copy a range of pages (spage, epage) from a source PDF to a specified
    location (apage) of the target PDF.
    If spage > epage, the sequence of source pages is reversed.
    '''
    if g_use_extra:
        return extra.JM_merge_range(
                doc_des,
                doc_src,
                spage,
                epage,
                apage,
                rotate,
                links,
                annots,
                show_progress,
                graft_map,
                )
    afterpage = apage
    counter = 0  # copied pages counter
    total = mupdf.fz_absi(epage - spage) + 1   # total pages to copy

    if spage < epage:
        page = spage
        while page <= epage:
            page_merge(doc_des, doc_src, page, afterpage, rotate, links, annots, graft_map)
            counter += 1
            if show_progress > 0 and counter % show_progress == 0:
                message(f"Inserted {counter} of {total} pages.")
            page += 1
            afterpage += 1
    else:
        page = spage
        while page >= epage:
            page_merge(doc_des, doc_src, page, afterpage, rotate, links, annots, graft_map)
            counter += 1
            if show_progress > 0 and counter % show_progress == 0:
                message(f"Inserted {counter} of {total} pages.")
            page -= 1
            afterpage += 1

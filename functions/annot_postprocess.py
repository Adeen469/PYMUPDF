"""
Function: fitz.annot_postprocess
Signature: annot_postprocess(page: 'Page', annot: 'Annot') -> None
Description:
Clean up after annotation insertion.

Set ownership flag and store annotation in page annotation dictionary.
"""

import fitz

# Source code of fitz.annot_postprocess:
def annot_postprocess(page: "Page", annot: "Annot") -> None:
    """Clean up after annotation insertion.

    Set ownership flag and store annotation in page annotation dictionary.
    """
    #annot.parent = weakref.proxy(page)
    assert isinstance( page, Page)
    assert isinstance( annot, Annot)
    annot.parent = page
    page._annot_refs[id(annot)] = annot
    annot.thisown = True



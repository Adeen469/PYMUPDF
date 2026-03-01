"""
Function: fitz.annot_preprocess
Signature: annot_preprocess(page: 'Page') -> int
Description:
Prepare for annotation insertion on the page.

Returns:
    Old page rotation value. Temporarily sets rotation to 0 when required.
"""

import fitz

# Source code of fitz.annot_preprocess:
def annot_preprocess(page: "Page") -> int:
    """Prepare for annotation insertion on the page.

    Returns:
        Old page rotation value. Temporarily sets rotation to 0 when required.
    """
    CheckParent(page)
    if not page.parent.is_pdf:
        raise ValueError("is no PDF")
    old_rotation = page.rotation
    if old_rotation != 0:
        page.set_rotation(0)
    return old_rotation

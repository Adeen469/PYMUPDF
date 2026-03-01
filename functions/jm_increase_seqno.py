"""
Function: fitz.jm_increase_seqno
Signature: jm_increase_seqno(dev, ctx, *vargs)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_increase_seqno:
def jm_increase_seqno( dev, ctx, *vargs):
    try:
        dev.seqno += 1
    except Exception:
        if g_exceptions_verbose:    exception_info()
        raise

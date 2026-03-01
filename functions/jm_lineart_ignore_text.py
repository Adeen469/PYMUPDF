"""
Function: fitz.jm_lineart_ignore_text
Signature: jm_lineart_ignore_text(dev, text, ctm)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_lineart_ignore_text:
def jm_lineart_ignore_text(dev, text, ctm):
    #log(f'{getattr(dev, "pathdict", None)=}')
    jm_trace_text(dev, text, 3, ctm, None, None, 1, dev.seqno)
    dev.seqno += 1

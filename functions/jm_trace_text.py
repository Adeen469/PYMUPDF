"""
Function: fitz.jm_trace_text
Signature: jm_trace_text(dev, text, type_, ctm, colorspace, color, alpha, seqno)
Description: No docstring available.
"""

import fitz

# Source code of fitz.jm_trace_text:
def jm_trace_text( dev, text, type_, ctm, colorspace, color, alpha, seqno):
    span = text.head
    while 1:
        if not span:
            break
        jm_trace_text_span( dev, span, type_, ctm, colorspace, color, alpha, seqno)
        span = span.next

"""
Function: fitz.match_string
Signature: match_string(h0, n0)
Description: No docstring available.
"""

import fitz

# Source code of fitz.match_string:
def match_string(h0, n0):
    h = 0
    n = 0
    e = h
    delta_h, hc = chartocanon(h0[h:])
    h += delta_h
    delta_n, nc = chartocanon(n0[n:])
    n += delta_n
    while hc == nc:
        e = h
        if hc == ord(' '):
            while 1:
                delta_h, hc = chartocanon(h0[h:])
                h += delta_h
                if hc != ord(' '):
                    break
        else:
            delta_h, hc = chartocanon(h0[h:])
            h += delta_h
        if nc == ord(' '):
            while 1:
                delta_n, nc = chartocanon(n0[n:])
                n += delta_n
                if nc != ord(' '):
                    break
        else:
            delta_n, nc = chartocanon(n0[n:])
            n += delta_n
    return None if nc != 0 else e

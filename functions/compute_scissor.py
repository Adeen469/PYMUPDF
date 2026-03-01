"""
Function: fitz.compute_scissor
Signature: compute_scissor(dev)
Description:
Every scissor of a clip is a sub rectangle of the preceding clip scissor
if the clip level is larger.
"""

import fitz

# Source code of fitz.compute_scissor:
def compute_scissor(dev):
    '''
    Every scissor of a clip is a sub rectangle of the preceding clip scissor
    if the clip level is larger.
    '''
    if dev.scissors is None:
        dev.scissors = list()
    num_scissors = len(dev.scissors)
    if num_scissors > 0:
        last_scissor = dev.scissors[num_scissors-1]
        scissor = JM_rect_from_py(last_scissor)
        scissor = mupdf.fz_intersect_rect(scissor, dev.pathrect)
    else:
        scissor = dev.pathrect
    dev.scissors.append(JM_py_from_rect(scissor))
    return scissor

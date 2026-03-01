"""
Function: fitz.JM_color_FromSequence
Signature: JM_color_FromSequence(color)
Description: No docstring available.
"""

import fitz

# Source code of fitz.JM_color_FromSequence:
def JM_color_FromSequence(color):
    
    if isinstance(color, (int, float)):    # maybe just a single float
        color = [color]
    
    if not isinstance( color, (list, tuple)):
        return -1, []
    
    if len(color) not in (0, 1, 3, 4):
        return -1, []
    
    ret = color[:]
    for i in range(len(ret)):
        if ret[i] < 0 or ret[i] > 1:
            ret[i] = 1
    return len(ret), ret

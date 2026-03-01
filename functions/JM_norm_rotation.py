"""
Function: fitz.JM_norm_rotation
Signature: JM_norm_rotation(rotate)
Description:
# return normalized /Rotate value:one of 0, 90, 180, 270
"""

import fitz

# Source code of fitz.JM_norm_rotation:
def JM_norm_rotation(rotate):
    '''
    # return normalized /Rotate value:one of 0, 90, 180, 270
    '''
    while rotate < 0:
        rotate += 360
    while rotate >= 360:
        rotate -= 360
    if rotate % 90 != 0:
        return 0
    return rotate

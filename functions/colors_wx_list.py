"""
Function: fitz.colors_wx_list
Signature: colors_wx_list()
Description:
Returns list of (name, red, green, blue) tuples:
    name: upper-case name.
    red, green, blue: integers in range 0..255.
"""

import fitz

# Source code of fitz.colors_wx_list:
def colors_wx_list():
    '''
    Returns list of (name, red, green, blue) tuples:
        name: upper-case name.
        red, green, blue: integers in range 0..255.
    '''
    return _wxcolors

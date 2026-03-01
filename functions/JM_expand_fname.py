"""
Function: fitz.JM_expand_fname
Signature: JM_expand_fname(name)
Description:
Make /DA string of annotation
"""

import fitz

# Source code of fitz.JM_expand_fname:
def JM_expand_fname(name):
    '''
    Make /DA string of annotation
    '''
    if not name:    return "Helv"
    if name.startswith("Co"):   return "Cour"
    if name.startswith("co"):   return "Cour"
    if name.startswith("Ti"):   return "TiRo"
    if name.startswith("ti"):   return "TiRo"
    if name.startswith("Sy"):   return "Symb"
    if name.startswith("sy"):   return "Symb"
    if name.startswith("Za"):   return "ZaDb"
    if name.startswith("za"):   return "ZaDb"
    return "Helv"

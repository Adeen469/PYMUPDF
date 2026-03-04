"""
Class: fitz.Graftmap

Description: No docstring available.

Inheritance (MRO): Graftmap -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Graftmap =====

# __del__(self)  [function]

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, doc)  [function]
#     -> Initialize self.  See help(type(self)) for accurate signature.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self, /)  [wrapper_descriptor]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).


# ===== Source Code =====
class Graftmap:

    def __del__(self):
        if not type(self) is Graftmap:
            return
        self.thisown = False

    def __init__(self, doc):
        dst = _as_pdf_document(doc)
        map_ = mupdf.pdf_new_graft_map(dst)
        self.this = map_
        self.thisown = True

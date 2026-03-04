"""
Class: fitz.Colorspace

Description: No docstring available.

Inheritance (MRO): Colorspace -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Colorspace =====

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, type_)  [function]
#     -> Supported are GRAY, RGB and CMYK.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self)  [function]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# n = <property object at 0x000002052DE31350>  [property]

# name = <property object at 0x000002052DE313A0>  [property]


# ===== Source Code =====
class Colorspace:

    def __init__(self, type_):
        """Supported are GRAY, RGB and CMYK."""
        if isinstance( type_, mupdf.FzColorspace):
            self.this = type_
        elif type_ == CS_GRAY:
            self.this = mupdf.FzColorspace(mupdf.FzColorspace.Fixed_GRAY)
        elif type_ == CS_CMYK:
            self.this = mupdf.FzColorspace(mupdf.FzColorspace.Fixed_CMYK)
        elif type_ == CS_RGB:
            self.this = mupdf.FzColorspace(mupdf.FzColorspace.Fixed_RGB)
        else:
            self.this = mupdf.FzColorspace(mupdf.FzColorspace.Fixed_RGB)

    def __repr__(self):
        x = ("", "GRAY", "", "RGB", "CMYK")[self.n]
        return "Colorspace(CS_%s) - %s" % (x, self.name)

    def _name(self):
        return mupdf.fz_colorspace_name(self.this)

    @property
    def n(self):
        """Size of one pixel."""
        return mupdf.fz_colorspace_n(self.this)

    @property
    def name(self):
        """Name of the Colorspace."""
        return self._name()

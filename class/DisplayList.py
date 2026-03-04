"""
Class: fitz.DisplayList

Description: No docstring available.

Inheritance (MRO): DisplayList -> object

"""

import fitz

# ===== Methods and Attributes of fitz.DisplayList =====

# __del__(self)  [function]

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, *args)  [function]
#     -> Initialize self.  See help(type(self)) for accurate signature.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self, /)  [wrapper_descriptor]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# get_pixmap(self, matrix=None, colorspace=None, alpha=0, clip=None)  [function]

# get_textpage(self, flags=3)  [function]
#     -> Make a TextPage from a DisplayList.

# rect = <property object at 0x000002052DE31490>  [property]

# run(self, dw, m, area)  [function]


# ===== Source Code =====
class DisplayList:
    def __del__(self):
        if not type(self) is DisplayList: return
        self.thisown = False

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], mupdf.FzRect):
            self.this = mupdf.FzDisplayList(args[0])
        elif len(args) == 1 and isinstance(args[0], mupdf.FzDisplayList):
            self.this = args[0]
        else:
            assert 0, f'Unrecognised {args=}'

    def get_pixmap(self, matrix=None, colorspace=None, alpha=0, clip=None):
        if isinstance(colorspace, Colorspace):
            colorspace = colorspace.this
        else:
            colorspace = mupdf.FzColorspace(mupdf.FzColorspace.Fixed_RGB)
        val = JM_pixmap_from_display_list(self.this, matrix, colorspace, alpha, clip, None)
        val.thisown = True
        return val

    def get_textpage(self, flags=3):
        """Make a TextPage from a DisplayList."""
        stext_options = mupdf.FzStextOptions()
        stext_options.flags = flags
        val = mupdf.FzStextPage(self.this, stext_options)
        val.thisown = True
        return val

    @property
    def rect(self):
        val = JM_py_from_rect(mupdf.fz_bound_display_list(self.this))
        val = Rect(val)
        return val

    def run(self, dw, m, area):
        mupdf.fz_run_display_list(
                self.this,
                dw.device,
                JM_matrix_from_py(m),
                JM_rect_from_py(area),
                mupdf.FzCookie(),
                )

"""
Class: fitz.DeviceWrapper

Description: No docstring available.

Inheritance (MRO): DeviceWrapper -> object

"""

import fitz

# ===== Methods and Attributes of fitz.DeviceWrapper =====

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


# ===== Source Code =====
class DeviceWrapper:
    def __init__(self, *args):
        if args_match( args, mupdf.FzDevice):
            device, = args
            self.this = device
        elif args_match( args, Pixmap, None):
            pm, clip = args
            bbox = JM_irect_from_py( clip)
            if mupdf.fz_is_infinite_irect( bbox):
                self.this = mupdf.fz_new_draw_device( mupdf.FzMatrix(), pm)
            else:
                self.this = mupdf.fz_new_draw_device_with_bbox( mupdf.FzMatrix(), pm, bbox)
        elif args_match( args, mupdf.FzDisplayList):
            dl, = args
            self.this = mupdf.fz_new_list_device( dl)
        elif args_match( args, mupdf.FzStextPage, None):
            tp, flags = args
            opts = mupdf.FzStextOptions( flags)
            self.this = mupdf.fz_new_stext_device( tp, opts)
        else:
            raise Exception( f'Unrecognised args for DeviceWrapper: {args!r}')

"""
Class: fitz.JM_image_reporter_Filter

Description:
Wrapper class for struct pdf_filter_options with virtual fns for each fnptr; this is for use as a SWIG Director class.

Inheritance (MRO): JM_image_reporter_Filter -> PdfFilterOptions2 -> PdfFilterOptions -> object

"""

import fitz

# ===== Methods and Attributes of fitz.JM_image_reporter_Filter =====

# __eq__(self, rhs)  [function]
#     -> Comparison method.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__ = None  [NoneType]

# __init__(self)  [function]
#     -> == Constructor.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, rhs)  [function]
#     -> Comparison method.

# __repr__(self)  [function]

# __str__(self)  [function]

# add_factory(self, factory)  [function]
#     -> We use default copy constructor and operator=.  Appends `factory` to internal vector and updates this->filters.

# ascii = <property object at 0x000002052DD1E980>  [property]

# complete(self, arg_0, arg_1)  [function]
#     -> Default virtual method implementations; these all throw an exception.

# filters = <property object at 0x000002052DD1EAC0>  [property]

# image_filter(self, ctx, ctm, name, image)  [function]

# instance_forms = <property object at 0x000002052DD1E930>  [property]

# internal(self, *args)  [function]
#     -> *Overload 1:*

# m_filters = <property object at 0x000002052DD1EBB0>  [property]

# newlines = <property object at 0x000002052DD1EB10>  [property]

# no_update = <property object at 0x000002052DD1E9D0>  [property]

# opaque = <property object at 0x000002052DD1EA20>  [property]

# recurse = <property object at 0x000002052DD1E8E0>  [property]

# s_num_instances = <property object at 0x000002052DD1EB60>  [property]

# thisown = <property object at 0x000002052DD1EC50>  [property]

# to_string(self)  [function]
#     -> Returns string containing our members, labelled and inside (...), using operator<<.

# use_virtual_complete(self, use=True)  [function]
#     -> These methods set the function pointers in *m_internal


# ===== Source Code =====
class JM_image_reporter_Filter(mupdf.PdfFilterOptions2):
    def __init__(self):
        super().__init__()
        self.use_virtual_image_filter()

    def image_filter( self, ctx, ctm, name, image):
        assert isinstance(ctm, mupdf.fz_matrix)
        JM_image_filter(self, mupdf.FzMatrix(ctm), name, image)
        if mupdf_cppyy:
            # cppyy doesn't appear to treat returned None as nullptr,
            # resulting in obscure 'python exception' exception.
            return 0

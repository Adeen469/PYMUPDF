"""
Class: fitz.DocumentWriter

Description: No docstring available.

Inheritance (MRO): DocumentWriter -> object

"""

import fitz

# ===== Methods and Attributes of fitz.DocumentWriter =====

# __enter__(self)  [function]

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __exit__(self, *args)  [function]

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, path, options='')  [function]
#     -> Initialize self.  See help(type(self)) for accurate signature.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self, /)  [wrapper_descriptor]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# begin_page(self, mediabox)  [function]

# close(self)  [function]

# end_page(self)  [function]


# ===== Source Code =====
class DocumentWriter:

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __init__(self, path, options=''):
        if isinstance( path, str):
            pass
        elif hasattr( path, 'absolute'):
            path = str( path)
        elif hasattr( path, 'name'):
            path = path.name
        if isinstance( path, str):
            self.this = mupdf.FzDocumentWriter( path, options, mupdf.FzDocumentWriter.PathType_PDF)
        else:
            # Need to keep the Python JM_new_output_fileptr_Output instance
            # alive for the lifetime of this DocumentWriter, otherwise calls
            # to virtual methods implemented in Python fail. So we make it a
            # member of this DocumentWriter.
            #
            # Unrelated to this, mupdf.FzDocumentWriter will set
            # self._out.m_internal to null because ownership is passed in.
            #
            out = JM_new_output_fileptr( path)
            self.this = mupdf.FzDocumentWriter( out, options, mupdf.FzDocumentWriter.OutputType_PDF)
            assert out.m_internal_value() == 0
            assert hasattr( self.this, '_out')
    
    def begin_page( self, mediabox):
        mediabox2 = JM_rect_from_py(mediabox)
        device = mupdf.fz_begin_page( self.this, mediabox2)
        device_wrapper = DeviceWrapper( device)
        return device_wrapper
    
    def close( self):
        mupdf.fz_close_document_writer( self.this)
        
    def end_page( self):
        mupdf.fz_end_page( self.this)

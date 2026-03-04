"""
Class: fitz.FileNotFoundError

Description:
Raised if file does not exist.

Inheritance (MRO): FileNotFoundError -> RuntimeError -> Exception -> BaseException -> object

"""

import fitz

# ===== Methods and Attributes of fitz.FileNotFoundError =====

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, /, *args, **kwargs)  [wrapper_descriptor]
#     -> Initialize self.  See help(type(self)) for accurate signature.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self, /)  [wrapper_descriptor]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# add_note(self, object, /)  [method_descriptor]
#     -> Exception.add_note(note) --

# args = <attribute 'args' of 'BaseException' objects>  [getset_descriptor]

# with_traceback(self, object, /)  [method_descriptor]
#     -> Exception.with_traceback(tb) --


# ===== Source Code =====
class FileNotFoundError(RuntimeError):
    """Raised if file does not exist."""
    pass

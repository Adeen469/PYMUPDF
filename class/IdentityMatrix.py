"""
Class: fitz.IdentityMatrix

Description:
Identity matrix [1, 0, 0, 1, 0, 0]

Inheritance (MRO): IdentityMatrix -> Matrix -> object

"""

import fitz

# ===== Methods and Attributes of fitz.IdentityMatrix =====

# __abs__(self)  [function]

# __add__(self, m)  [function]

# __bool__(self)  [function]

# __eq__(self, mat)  [function]
#     -> Return self==value.

# __getitem__(self, i)  [function]

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self)  [function]
#     -> The type of the None singleton.

# __init__(self)  [function]
#     -> Matrix() - all zeros

# __len__(self)  [function]

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __mul__(self, m)  [function]

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __neg__(self)  [function]

# __repr__(self)  [function]
#     -> Return repr(self).

# __setitem__(self, i, v)  [function]

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# __sub__(self, m)  [function]

# __truediv__(self, m)  [function]

# checkargs(*args)  [function]

# concat(self, one, two)  [function]
#     -> Multiply two matrices and replace current one.

# invert(self, src=None)  [function]
#     -> Calculate the inverted matrix. Return 0 if successful and replace

# is_rectilinear = <property object at 0x000002052DE32480>  [property]

# norm(self)  [function]

# prerotate(self, theta)  [function]
#     -> Calculate pre rotation and replace current matrix.

# prescale(self, sx, sy)  [function]
#     -> Calculate pre scaling and replace current matrix.

# preshear(self, h, v)  [function]
#     -> Calculate pre shearing and replace current matrix.

# pretranslate(self, tx, ty)  [function]
#     -> Calculate pre translation and replace current matrix.


# ===== Source Code =====
class IdentityMatrix(Matrix):
    """Identity matrix [1, 0, 0, 1, 0, 0]"""

    def __hash__(self):
        return hash((1,0,0,1,0,0))

    def __init__(self):
        Matrix.__init__(self, 1.0, 1.0)

    def __repr__(self):
        return "IdentityMatrix(1.0, 0.0, 0.0, 1.0, 0.0, 0.0)"

    def __setattr__(self, name, value):
        if name in "ad":
            self.__dict__[name] = 1.0
        elif name in "bcef":
            self.__dict__[name] = 0.0
        else:
            self.__dict__[name] = value

    def checkargs(*args):
        raise NotImplementedError("Identity is readonly")

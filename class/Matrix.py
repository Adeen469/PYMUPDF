"""
Class: fitz.Matrix

Description: No docstring available.

Inheritance (MRO): Matrix -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Matrix =====

# __abs__(self)  [function]

# __add__(self, m)  [function]

# __bool__(self)  [function]

# __eq__(self, mat)  [function]
#     -> Return self==value.

# __getitem__(self, i)  [function]

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__ = None  [NoneType]

# __init__(self, *args, a=None, b=None, c=None, d=None, e=None, f=None)  [function]
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
class Matrix:

    def __abs__(self):
        return math.sqrt(sum([c*c for c in self]))

    def __add__(self, m):
        if hasattr(m, "__float__"):
            return Matrix(self.a + m, self.b + m, self.c + m,
                          self.d + m, self.e + m, self.f + m)
        if len(m) != 6:
            raise ValueError("Matrix: bad seq len")
        return Matrix(self.a + m[0], self.b + m[1], self.c + m[2],
                          self.d + m[3], self.e + m[4], self.f + m[5])

    def __bool__(self):
        return not (max(self) == min(self) == 0)

    def __eq__(self, mat):
        if not hasattr(mat, "__len__"):
            return False
        return len(mat) == 6 and not (self - mat)

    def __getitem__(self, i):
        return (self.a, self.b, self.c, self.d, self.e, self.f)[i]

    def __init__(self, *args, a=None, b=None, c=None, d=None, e=None, f=None):
        """
        Matrix() - all zeros
        Matrix(a, b, c, d, e, f)
        Matrix(zoom-x, zoom-y) - zoom
        Matrix(shear-x, shear-y, 1) - shear
        Matrix(degree) - rotate
        Matrix(Matrix) - new copy
        Matrix(sequence) - from 'sequence'
        Matrix(mupdf.FzMatrix) - from MuPDF class wrapper for fz_matrix.
        
        Explicit keyword args a, b, c, d, e, f override any earlier settings if
        not None.
        """
        if not args:
            self.a = self.b = self.c = self.d = self.e = self.f = 0.0
        elif len(args) > 6:
            raise ValueError("Matrix: bad seq len")
        elif len(args) == 6:  # 6 numbers
            self.a, self.b, self.c, self.d, self.e, self.f = map(float, args)
        elif len(args) == 1:  # either an angle or a sequ
            if isinstance(args[0], mupdf.FzMatrix):
                self.a = args[0].a
                self.b = args[0].b
                self.c = args[0].c
                self.d = args[0].d
                self.e = args[0].e
                self.f = args[0].f
            elif hasattr(args[0], "__float__"):
                theta = math.radians(args[0])
                c_ = round(math.cos(theta), 8)
                s_ = round(math.sin(theta), 8)
                self.a = self.d = c_
                self.b = s_
                self.c = -s_
                self.e = self.f = 0.0
            else:
                self.a, self.b, self.c, self.d, self.e, self.f = map(float, args[0])
        elif len(args) == 2 or len(args) == 3 and args[2] == 0:
            self.a, self.b, self.c, self.d, self.e, self.f = float(args[0]), \
                0.0, 0.0, float(args[1]), 0.0, 0.0
        elif len(args) == 3 and args[2] == 1:
            self.a, self.b, self.c, self.d, self.e, self.f = 1.0, \
                float(args[1]), float(args[0]), 1.0, 0.0, 0.0
        else:
            raise ValueError("Matrix: bad args")
        
        # Override with explicit args if specified.
        if a is not None:   self.a = a
        if b is not None:   self.b = b
        if c is not None:   self.c = c
        if d is not None:   self.d = d
        if e is not None:   self.e = e
        if f is not None:   self.f = f

    def __invert__(self):
        """Calculate inverted matrix."""
        m1 = Matrix()
        m1.invert(self)
        return m1

    def __len__(self):
        return 6

    def __mul__(self, m):
        if hasattr(m, "__float__"):
            return Matrix(self.a * m, self.b * m, self.c * m,
                          self.d * m, self.e * m, self.f * m)
        m1 = Matrix(1,1)
        return m1.concat(self, m)

    def __neg__(self):
        return Matrix(-self.a, -self.b, -self.c, -self.d, -self.e, -self.f)

    def __nonzero__(self):
        return not (max(self) == min(self) == 0)

    def __pos__(self):
        return Matrix(self)

    def __repr__(self):
        return "Matrix" + str(tuple(self))

    def __setitem__(self, i, v):
        v = float(v)
        if   i == 0: self.a = v
        elif i == 1: self.b = v
        elif i == 2: self.c = v
        elif i == 3: self.d = v
        elif i == 4: self.e = v
        elif i == 5: self.f = v
        else:
            raise IndexError("index out of range")
        return

    def __sub__(self, m):
        if hasattr(m, "__float__"):
            return Matrix(self.a - m, self.b - m, self.c - m,
                          self.d - m, self.e - m, self.f - m)
        if len(m) != 6:
            raise ValueError("Matrix: bad seq len")
        return Matrix(self.a - m[0], self.b - m[1], self.c - m[2],
                          self.d - m[3], self.e - m[4], self.f - m[5])

    def __truediv__(self, m):
        if hasattr(m, "__float__"):
            return Matrix(self.a * 1./m, self.b * 1./m, self.c * 1./m,
                          self.d * 1./m, self.e * 1./m, self.f * 1./m)
        m1 = util_invert_matrix(m)[1]
        if not m1:
            raise ZeroDivisionError("matrix not invertible")
        m2 = Matrix(1,1)
        return m2.concat(self, m1)

    def concat(self, one, two):
        """Multiply two matrices and replace current one."""
        if not len(one) == len(two) == 6:
            raise ValueError("Matrix: bad seq len")
        self.a, self.b, self.c, self.d, self.e, self.f = util_concat_matrix(one, two)
        return self

    def invert(self, src=None):
        """Calculate the inverted matrix. Return 0 if successful and replace
        current one. Else return 1 and do nothing.
        """
        if src is None:
            dst = util_invert_matrix(self)
        else:
            dst = util_invert_matrix(src)
        if dst[0] == 1:
            return 1
        self.a, self.b, self.c, self.d, self.e, self.f = dst[1]
        return 0

    @property
    def is_rectilinear(self):
        """True if rectangles are mapped to rectangles."""
        return (abs(self.b) < EPSILON and abs(self.c) < EPSILON) or \
            (abs(self.a) < EPSILON and abs(self.d) < EPSILON)

    def prerotate(self, theta):
        """Calculate pre rotation and replace current matrix."""
        theta = float(theta)
        while theta < 0: theta += 360
        while theta >= 360: theta -= 360
        if abs(0 - theta) < EPSILON:
            pass

        elif abs(90.0 - theta) < EPSILON:
            a = self.a
            b = self.b
            self.a = self.c
            self.b = self.d
            self.c = -a
            self.d = -b

        elif abs(180.0 - theta) < EPSILON:
            self.a = -self.a
            self.b = -self.b
            self.c = -self.c
            self.d = -self.d

        elif abs(270.0 - theta) < EPSILON:
            a = self.a
            b = self.b
            self.a = -self.c
            self.b = -self.d
            self.c = a
            self.d = b

        else:
            rad = math.radians(theta)
            s = math.sin(rad)
            c = math.cos(rad)
            a = self.a
            b = self.b
            self.a = c * a + s * self.c
            self.b = c * b + s * self.d
            self.c =-s * a + c * self.c
            self.d =-s * b + c * self.d

        return self

    def prescale(self, sx, sy):
        """Calculate pre scaling and replace current matrix."""
        sx = float(sx)
        sy = float(sy)
        self.a *= sx
        self.b *= sx
        self.c *= sy
        self.d *= sy
        return self

    def preshear(self, h, v):
        """Calculate pre shearing and replace current matrix."""
        h = float(h)
        v = float(v)
        a, b = self.a, self.b
        self.a += v * self.c
        self.b += v * self.d
        self.c += h * a
        self.d += h * b
        return self

    def pretranslate(self, tx, ty):
        """Calculate pre translation and replace current matrix."""
        tx = float(tx)
        ty = float(ty)
        self.e += tx * self.a + ty * self.c
        self.f += tx * self.b + ty * self.d
        return self

    __inv__ = __invert__
    __div__ = __truediv__
    norm = __abs__

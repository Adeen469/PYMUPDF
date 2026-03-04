"""
Class: fitz.Rect

Description: No docstring available.

Inheritance (MRO): Rect -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Rect =====

# __abs__(self)  [function]

# __add__(self, p)  [function]

# __bool__(self)  [function]

# __contains__(self, x)  [function]

# __eq__(self, rect)  [function]
#     -> Return self==value.

# __getitem__(self, i)  [function]

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self)  [function]
#     -> Return hash(self).

# __init__(self, *args, p0=None, p1=None, x0=None, y0=None, x1=None, y1=None)  [function]
#     -> Rect() - all zeros

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

# __sub__(self, p)  [function]

# __truediv__(self, m)  [function]

# bl = <property object at 0x000002052DE33970>  [property]

# bottom_left = <property object at 0x000002052DE33970>  [property]

# bottom_right = <property object at 0x000002052DE339C0>  [property]

# br = <property object at 0x000002052DE339C0>  [property]

# contains(self, x)  [function]
#     -> Check if containing point-like or rect-like x.

# get_area(self, *args) -> float  [function]
#     -> Calculate area of rectangle.

# height = <property object at 0x000002052DE33A10>  [property]

# include_point(self, p)  [function]
#     -> Extend to include point-like p.

# include_rect(self, r)  [function]
#     -> Extend to include rect-like r.

# intersect(self, r)  [function]
#     -> Restrict to common rect with rect-like r.

# intersects(self, x)  [function]
#     -> Check if intersection with rectangle x is not empty.

# irect = <property object at 0x000002052DE33C90>  [property]

# is_empty = <property object at 0x000002052DE33A60>  [property]

# is_infinite = <property object at 0x000002052DE33AB0>  [property]

# is_valid = <property object at 0x000002052DE33B00>  [property]

# morph(self, p, m)  [function]
#     -> Morph with matrix-like m and point-like p.

# norm(self)  [function]

# normalize(self)  [function]
#     -> Replace rectangle with its finite version.

# quad = <property object at 0x000002052DE33B50>  [property]

# round(self)  [function]
#     -> Return the IRect.

# tl = <property object at 0x000002052DE33BA0>  [property]

# top_left = <property object at 0x000002052DE33BA0>  [property]

# top_right = <property object at 0x000002052DE33BF0>  [property]

# torect(self, r)  [function]
#     -> Return matrix that converts to target rect.

# tr = <property object at 0x000002052DE33BF0>  [property]

# transform(self, m)  [function]
#     -> Replace with the transformation by matrix-like m.

# width = <property object at 0x000002052DE33C40>  [property]


# ===== Source Code =====
class Rect:
    
    def __abs__(self):
        if self.is_empty or self.is_infinite:
            return 0.0
        return (self.x1 - self.x0) * (self.y1 - self.y0)

    def __add__(self, p):
        if hasattr(p, "__float__"):
            return Rect(self.x0 + p, self.y0 + p, self.x1 + p, self.y1 + p)
        if len(p) != 4:
            raise ValueError("Rect: bad seq len")
        return Rect(self.x0 + p[0], self.y0 + p[1], self.x1 + p[2], self.y1 + p[3])

    def __and__(self, x):
        if not hasattr(x, "__len__"):
            raise ValueError("bad operand 2")

        r1 = Rect(x)
        r = Rect(self)
        return r.intersect(r1)

    def __bool__(self):
        return not (max(self) == min(self) == 0)

    def __contains__(self, x):
        if hasattr(x, "__float__"):
            return x in tuple(self)
        l = len(x)
        if l == 2:
            return util_is_point_in_rect(x, self)
        if l == 4:
            r = INFINITE_RECT()
            try:
                r = Rect(x)
            except Exception:
                if g_exceptions_verbose > 1:    exception_info()
                r = Quad(x).rect
            return (self.x0 <= r.x0 <= r.x1 <= self.x1 and
                    self.y0 <= r.y0 <= r.y1 <= self.y1)
        return False

    def __eq__(self, rect):
        if not hasattr(rect, "__len__"):
            return False
        return len(rect) == 4 and not (self - rect)

    def __getitem__(self, i):
        return (self.x0, self.y0, self.x1, self.y1)[i]

    def __hash__(self):
        return hash(tuple(self))

    def __init__(self, *args, p0=None, p1=None, x0=None, y0=None, x1=None, y1=None):
        """
        Rect() - all zeros
        Rect(x0, y0, x1, y1)
        Rect(top-left, x1, y1)
        Rect(x0, y0, bottom-right)
        Rect(top-left, bottom-right)
        Rect(Rect or IRect) - new copy
        Rect(sequence) - from 'sequence'
    
        Explicit keyword args p0, p1, x0, y0, x1, y1 override earlier settings
        if not None.
        """
        x0, y0, x1, y1 = util_make_rect( *args, p0=p0, p1=p1, x0=x0, y0=y0, x1=x1, y1=y1)
        self.x0 = float( x0)
        self.y0 = float( y0)
        self.x1 = float( x1)
        self.y1 = float( y1)

    def __len__(self):
        return 4

    def __mul__(self, m):
        if hasattr(m, "__float__"):
            return Rect(self.x0 * m, self.y0 * m, self.x1 * m, self.y1 * m)
        r = Rect(self)
        r = r.transform(m)
        return r

    def __neg__(self):
        return Rect(-self.x0, -self.y0, -self.x1, -self.y1)

    def __nonzero__(self):
        return not (max(self) == min(self) == 0)

    def __or__(self, x):
        if not hasattr(x, "__len__"):
            raise ValueError("bad operand 2")
        r = Rect(self)
        if len(x) == 2:
            return r.include_point(x)
        if len(x) == 4:
            return r.include_rect(x)
        raise ValueError("bad operand 2")

    def __pos__(self):
        return Rect(self)

    def __repr__(self):
        return "Rect" + str(tuple(self))

    def __setitem__(self, i, v):
        v = float(v)
        if   i == 0: self.x0 = v
        elif i == 1: self.y0 = v
        elif i == 2: self.x1 = v
        elif i == 3: self.y1 = v
        else:
            raise IndexError("index out of range")
        return None

    def __sub__(self, p):
        if hasattr(p, "__float__"):
            return Rect(self.x0 - p, self.y0 - p, self.x1 - p, self.y1 - p)
        if len(p) != 4:
            raise ValueError("Rect: bad seq len")
        return Rect(self.x0 - p[0], self.y0 - p[1], self.x1 - p[2], self.y1 - p[3])

    def __truediv__(self, m):
        if hasattr(m, "__float__"):
            return Rect(self.x0 * 1./m, self.y0 * 1./m, self.x1 * 1./m, self.y1 * 1./m)
        im = util_invert_matrix(m)[1]
        if not im:
            raise ZeroDivisionError(f"Matrix not invertible: {m}")
        r = Rect(self)
        r = r.transform(im)
        return r

    @property
    def bottom_left(self):
        """Bottom-left corner."""
        return Point(self.x0, self.y1)

    @property
    def bottom_right(self):
        """Bottom-right corner."""
        return Point(self.x1, self.y1)

    def contains(self, x):
        """Check if containing point-like or rect-like x."""
        return self.__contains__(x)

    @property
    def height(self):
        return max(0, self.y1 - self.y0)

    def get_area(self, *args) -> float:
        """Calculate area of rectangle.\nparameter is one of 'px' (default), 'in', 'cm', or 'mm'."""
        return _rect_area(self.width, self.height, args)

    def include_point(self, p):
        """Extend to include point-like p."""
        if len(p) != 2:
            raise ValueError("Point: bad seq len")
        self.x0, self.y0, self.x1, self.y1 = util_include_point_in_rect(self, p)
        return self

    def include_rect(self, r):
        """Extend to include rect-like r."""
        if len(r) != 4:
            raise ValueError("Rect: bad seq len")
        r = Rect(r)
        if r.is_infinite or self.is_infinite:
            self.x0, self.y0, self.x1, self.y1 = FZ_MIN_INF_RECT, FZ_MIN_INF_RECT, FZ_MAX_INF_RECT, FZ_MAX_INF_RECT
        elif r.is_empty:
            return self
        elif self.is_empty:
            self.x0, self.y0, self.x1, self.y1 = r.x0, r.y0, r.x1, r.y1
        else:
            self.x0, self.y0, self.x1, self.y1 = util_union_rect(self, r)
        return self

    def intersect(self, r):
        """Restrict to common rect with rect-like r."""
        if not len(r) == 4:
            raise ValueError("Rect: bad seq len")
        r = Rect(r)
        if r.is_infinite:
            return self
        elif self.is_infinite:
            self.x0, self.y0, self.x1, self.y1 = r.x0, r.y0, r.x1, r.y1
        elif r.is_empty:
            self.x0, self.y0, self.x1, self.y1 = r.x0, r.y0, r.x1, r.y1
        elif self.is_empty:
            return self
        else:
            self.x0, self.y0, self.x1, self.y1 = util_intersect_rect(self, r)
        return self

    def intersects(self, x):
        """Check if intersection with rectangle x is not empty."""
        rect2 = Rect(x)
        return (1
                and not self.is_empty
                and not self.is_infinite
                and not rect2.is_empty
                and not rect2.is_infinite
                and self.x0 < rect2.x1
                and rect2.x0 < self.x1
                and self.y0 < rect2.y1
                and rect2.y0 < self.y1
               )

    @property
    def is_empty(self):
        """True if rectangle area is empty."""
        return self.x0 >= self.x1 or self.y0 >= self.y1

    @property
    def is_infinite(self):
        """True if this is the infinite rectangle."""
        return self.x0 == self.y0 == FZ_MIN_INF_RECT and self.x1 == self.y1 == FZ_MAX_INF_RECT

    @property
    def is_valid(self):
        """True if rectangle is valid."""
        return self.x0 <= self.x1 and self.y0 <= self.y1

    def morph(self, p, m):
        """Morph with matrix-like m and point-like p.

        Returns a new quad."""
        if self.is_infinite:
            return INFINITE_QUAD()
        return self.quad.morph(p, m)

    def norm(self):
        return math.sqrt(sum([c*c for c in self]))

    def normalize(self):
        """Replace rectangle with its finite version."""
        if self.x1 < self.x0:
            self.x0, self.x1 = self.x1, self.x0
        if self.y1 < self.y0:
            self.y0, self.y1 = self.y1, self.y0
        return self

    @property
    def quad(self):
        """Return Quad version of rectangle."""
        return Quad(self.tl, self.tr, self.bl, self.br)

    def round(self):
        """Return the IRect."""
        return IRect(util_round_rect(self))

    @property
    def top_left(self):
        """Top-left corner."""
        return Point(self.x0, self.y0)

    @property
    def top_right(self):
        """Top-right corner."""
        return Point(self.x1, self.y0)
    
    def torect(self, r):
        """Return matrix that converts to target rect."""

        r = Rect(r)
        if self.is_infinite or self.is_empty or r.is_infinite or r.is_empty:
            raise ValueError("rectangles must be finite and not empty")
        return (
            Matrix(1, 0, 0, 1, -self.x0, -self.y0)
            * Matrix(r.width / self.width, r.height / self.height)
            * Matrix(1, 0, 0, 1, r.x0, r.y0)
        )

    def transform(self, m):
        """Replace with the transformation by matrix-like m."""
        if not len(m) == 6:
            raise ValueError("Matrix: bad seq len")
        self.x0, self.y0, self.x1, self.y1 = util_transform_rect(self, m)
        return self

    @property
    def width(self):
        return max(0, self.x1 - self.x0)

    __div__ = __truediv__

    bl = bottom_left
    br = bottom_right
    irect = property(round)
    tl = top_left
    tr = top_right

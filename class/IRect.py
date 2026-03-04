"""
Class: fitz.IRect

Description:
IRect() - all zeros
IRect(x0, y0, x1, y1) - 4 coordinates
IRect(top-left, x1, y1) - point and 2 coordinates
IRect(x0, y0, bottom-right) - 2 coordinates and point
IRect(top-left, bottom-right) - 2 points
IRect(sequ) - new from sequence or rect-like

Inheritance (MRO): IRect -> object

"""

import fitz

# ===== Methods and Attributes of fitz.IRect =====

# __add__(self, p)  [function]

# __contains__(self, x)  [function]

# __eq__(self, r)  [function]
#     -> Return self==value.

# __getitem__(self, i)  [function]

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self)  [function]
#     -> Return hash(self).

# __init__(self, *args, p0=None, p1=None, x0=None, y0=None, x1=None, y1=None)  [function]
#     -> Initialize self.  See help(type(self)) for accurate signature.

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

# bl = <property object at 0x000002052DE441D0>  [property]

# bottom_left = <property object at 0x000002052DE441D0>  [property]

# bottom_right = <property object at 0x000002052DE44220>  [property]

# br = <property object at 0x000002052DE44220>  [property]

# contains(self, x)  [function]
#     -> Check if x is in the rectangle.

# get_area(self, *args) -> float  [function]
#     -> Calculate area of rectangle.

# height = <property object at 0x000002052DE44270>  [property]

# include_point(self, p)  [function]
#     -> Extend rectangle to include point p.

# include_rect(self, r)  [function]
#     -> Extend rectangle to include rectangle r.

# intersect(self, r)  [function]
#     -> Restrict rectangle to intersection with rectangle r.

# intersects(self, x)  [function]

# is_empty = <property object at 0x000002052DE442C0>  [property]

# is_infinite = <property object at 0x000002052DE44310>  [property]

# is_valid = <property object at 0x000002052DE44360>  [property]

# morph(self, p, m)  [function]
#     -> Morph with matrix-like m and point-like p.

# norm(self)  [function]

# normalize(self)  [function]
#     -> Replace rectangle with its valid version.

# quad = <property object at 0x000002052DE443B0>  [property]

# rect = <property object at 0x000002052DE44400>  [property]

# tl = <property object at 0x000002052DE44450>  [property]

# top_left = <property object at 0x000002052DE44450>  [property]

# top_right = <property object at 0x000002052DE444A0>  [property]

# torect(self, r)  [function]
#     -> Return matrix that converts to target rect.

# tr = <property object at 0x000002052DE444A0>  [property]

# transform(self, m)  [function]

# width = <property object at 0x000002052DE444F0>  [property]


# ===== Source Code =====
class IRect:
    """
    IRect() - all zeros
    IRect(x0, y0, x1, y1) - 4 coordinates
    IRect(top-left, x1, y1) - point and 2 coordinates
    IRect(x0, y0, bottom-right) - 2 coordinates and point
    IRect(top-left, bottom-right) - 2 points
    IRect(sequ) - new from sequence or rect-like
    """

    def __add__(self, p):
        return Rect.__add__(self, p).round()

    def __and__(self, x):
        return Rect.__and__(self, x).round()

    def __contains__(self, x):
        return Rect.__contains__(self, x)

    def __eq__(self, r):
        if not hasattr(r, "__len__"):
            return False
        return len(r) == 4 and self.x0 == r[0] and self.y0 == r[1] and self.x1 == r[2] and self.y1 == r[3]

    def __getitem__(self, i):
        return (self.x0, self.y0, self.x1, self.y1)[i]

    def __hash__(self):
        return hash(tuple(self))

    def __init__(self, *args, p0=None, p1=None, x0=None, y0=None, x1=None, y1=None):
        self.x0, self.y0, self.x1, self.y1 = util_make_irect( *args, p0=p0, p1=p1, x0=x0, y0=y0, x1=x1, y1=y1)

    def __len__(self):
        return 4

    def __mul__(self, m):
        return Rect.__mul__(self, m).round()

    def __neg__(self):
        return IRect(-self.x0, -self.y0, -self.x1, -self.y1)

    def __or__(self, x):
        return Rect.__or__(self, x).round()

    def __pos__(self):
        return IRect(self)

    def __repr__(self):
        return "IRect" + str(tuple(self))

    def __setitem__(self, i, v):
        v = int(v)
        if   i == 0: self.x0 = v
        elif i == 1: self.y0 = v
        elif i == 2: self.x1 = v
        elif i == 3: self.y1 = v
        else:
            raise IndexError("index out of range")
        return None

    def __sub__(self, p):
        return Rect.__sub__(self, p).round()

    def __truediv__(self, m):
        return Rect.__truediv__(self, m).round()

    @property
    def bottom_left(self):
        """Bottom-left corner."""
        return Point(self.x0, self.y1)

    @property
    def bottom_right(self):
        """Bottom-right corner."""
        return Point(self.x1, self.y1)

    @property
    def height(self):
        return max(0, self.y1 - self.y0)

    def contains(self, x):
        """Check if x is in the rectangle."""
        return self.__contains__(x)

    def get_area(self, *args) -> float:
        """Calculate area of rectangle.\nparameter is one of 'px' (default), 'in', 'cm', or 'mm'."""
        return _rect_area(self.width, self.height, args)

    def include_point(self, p):
        """Extend rectangle to include point p."""
        rect = self.rect.include_point(p)
        return rect.irect

    def include_rect(self, r):
        """Extend rectangle to include rectangle r."""
        rect = self.rect.include_rect(r)
        return rect.irect

    def intersect(self, r):
        """Restrict rectangle to intersection with rectangle r."""
        return Rect.intersect(self, r).round()

    def intersects(self, x):
        return Rect.intersects(self, x)

    @property
    def is_empty(self):
        """True if rectangle area is empty."""
        return self.x0 >= self.x1 or self.y0 >= self.y1

    @property
    def is_infinite(self):
        """True if rectangle is infinite."""
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
        """Replace rectangle with its valid version."""
        if self.x1 < self.x0:
            self.x0, self.x1 = self.x1, self.x0
        if self.y1 < self.y0:
            self.y0, self.y1 = self.y1, self.y0
        return self

    @property
    def quad(self):
        """Return Quad version of rectangle."""
        return Quad(self.tl, self.tr, self.bl, self.br)

    @property
    def rect(self):
        return Rect(self)

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
        return Rect.transform(self, m).round()

    @property
    def width(self):
        return max(0, self.x1 - self.x0)

    br = bottom_right
    bl = bottom_left
    tl = top_left
    tr = top_right

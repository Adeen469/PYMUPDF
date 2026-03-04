"""
Class: fitz.Point

Description: No docstring available.

Inheritance (MRO): Point -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Point =====

# __abs__(self)  [function]

# __add__(self, p)  [function]

# __bool__(self)  [function]

# __eq__(self, p)  [function]
#     -> Return self==value.

# __getitem__(self, i)  [function]

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self)  [function]
#     -> Return hash(self).

# __init__(self, *args, x=None, y=None)  [function]
#     -> Point() - all zeros

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

# abs_unit = <property object at 0x000002052DE33600>  [property]

# distance_to(self, *args)  [function]
#     -> Return distance to rectangle or another point.

# norm(self)  [function]

# transform(self, m)  [function]
#     -> Replace point by its transformation with matrix-like m.

# unit = <property object at 0x000002052DE33650>  [property]


# ===== Source Code =====
class Point:

    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __add__(self, p):
        if hasattr(p, "__float__"):
            return Point(self.x + p, self.y + p)
        if len(p) != 2:
            raise ValueError("Point: bad seq len")
        return Point(self.x + p[0], self.y + p[1])

    def __bool__(self):
        return not (max(self) == min(self) == 0)

    def __eq__(self, p):
        if not hasattr(p, "__len__"):
            return False
        return len(p) == 2 and not (self - p)

    def __getitem__(self, i):
        return (self.x, self.y)[i]

    def __hash__(self):
        return hash(tuple(self))

    def __init__(self, *args, x=None, y=None):
        '''
        Point() - all zeros
        Point(x, y)
        Point(Point) - new copy
        Point(sequence) - from 'sequence'

        Explicit keyword args x, y override earlier settings if not None.
        '''
        if not args:
            self.x = 0.0
            self.y = 0.0
        elif len(args) > 2:
            raise ValueError("Point: bad seq len")
        elif len(args) == 2:
            self.x = float(args[0])
            self.y = float(args[1])
        elif len(args) == 1:
            l = args[0]
            if isinstance(l, (mupdf.FzPoint, mupdf.fz_point)):
                self.x = l.x
                self.y = l.y
            else:
                if not hasattr(l, "__getitem__"):
                    raise ValueError("Point: bad args")
                if len(l) != 2:
                    raise ValueError("Point: bad seq len")
                self.x = float(l[0])
                self.y = float(l[1])
        else:
            raise ValueError("Point: bad seq len")
        if x is not None:   self.x = x
        if y is not None:   self.y = y

    def __len__(self):
        return 2

    def __mul__(self, m):
        if hasattr(m, "__float__"):
            return Point(self.x * m, self.y * m)
        if hasattr(m, "__getitem__") and len(m) == 2:
            # dot product
            return self.x * m[0] + self.y * m[1]
        p = Point(self)
        return p.transform(m)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __nonzero__(self):
        return not (max(self) == min(self) == 0)

    def __pos__(self):
        return Point(self)

    def __repr__(self):
        return "Point" + str(tuple(self))

    def __setitem__(self, i, v):
        v = float(v)
        if   i == 0: self.x = v
        elif i == 1: self.y = v
        else:
            raise IndexError("index out of range")
        return None

    def __sub__(self, p):
        if hasattr(p, "__float__"):
            return Point(self.x - p, self.y - p)
        if len(p) != 2:
            raise ValueError("Point: bad seq len")
        return Point(self.x - p[0], self.y - p[1])

    def __truediv__(self, m):
        if hasattr(m, "__float__"):
            return Point(self.x * 1./m, self.y * 1./m)
        m1 = util_invert_matrix(m)[1]
        if not m1:
            raise ZeroDivisionError("matrix not invertible")
        p = Point(self)
        return p.transform(m1)

    @property
    def abs_unit(self):
        """Unit vector with positive coordinates."""
        s = self.x * self.x + self.y * self.y
        if s < EPSILON:
            return Point(0,0)
        s = math.sqrt(s)
        return Point(abs(self.x) / s, abs(self.y) / s)

    def distance_to(self, *args):
        """Return distance to rectangle or another point."""
        if not len(args) > 0:
            raise ValueError("at least one parameter must be given")

        x = args[0]
        if len(x) == 2:
            x = Point(x)
        elif len(x) == 4:
            x = Rect(x)
        else:
            raise ValueError("arg1 must be point-like or rect-like")

        if len(args) > 1:
            unit = args[1]
        else:
            unit = "px"
        u = {"px": (1.,1.), "in": (1.,72.), "cm": (2.54, 72.),
             "mm": (25.4, 72.)}
        f = u[unit][0] / u[unit][1]

        if type(x) is Point:
            return abs(self - x) * f

        # from here on, x is a rectangle
        # as a safeguard, make a finite copy of it
        r = Rect(x.top_left, x.top_left)
        r = r | x.bottom_right
        if self in r:
            return 0.0
        if self.x > r.x1:
            if self.y >= r.y1:
                return self.distance_to(r.bottom_right, unit)
            elif self.y <= r.y0:
                return self.distance_to(r.top_right, unit)
            else:
                return (self.x - r.x1) * f
        elif r.x0 <= self.x <= r.x1:
            if self.y >= r.y1:
                return (self.y - r.y1) * f
            else:
                return (r.y0 - self.y) * f
        else:
            if self.y >= r.y1:
                return self.distance_to(r.bottom_left, unit)
            elif self.y <= r.y0:
                return self.distance_to(r.top_left, unit)
            else:
                return (r.x0 - self.x) * f

    def transform(self, m):
        """Replace point by its transformation with matrix-like m."""
        if len(m) != 6:
            raise ValueError("Matrix: bad seq len")
        self.x, self.y = util_transform_point(self, m)
        return self

    @property
    def unit(self):
        """Unit vector of the point."""
        s = self.x * self.x + self.y * self.y
        if s < EPSILON:
            return Point(0,0)
        s = math.sqrt(s)
        return Point(self.x / s, self.y / s)

    __div__ = __truediv__
    norm = __abs__

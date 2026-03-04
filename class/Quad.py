"""
Class: fitz.Quad

Description: No docstring available.

Inheritance (MRO): Quad -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Quad =====

# __abs__(self)  [function]

# __add__(self, q)  [function]

# __bool__(self)  [function]

# __contains__(self, x)  [function]

# __eq__(self, quad)  [function]
#     -> Return self==value.

# __getitem__(self, i)  [function]

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self)  [function]
#     -> Return hash(self).

# __init__(self, *args, ul=None, ur=None, ll=None, lr=None)  [function]
#     -> Quad() - all zero points

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

# __sub__(self, q)  [function]

# __truediv__(self, m)  [function]

# height = <property object at 0x000002052DE338D0>  [property]

# is_convex = <property object at 0x000002052DE336F0>  [property]

# is_empty = <property object at 0x000002052DE33740>  [property]

# is_infinite = <property object at 0x000002052DE33790>  [property]

# is_rectangular = <property object at 0x000002052DE337E0>  [property]

# morph(self, p, m)  [function]
#     -> Morph the quad with matrix-like 'm' and point-like 'p'.

# rect = <property object at 0x000002052DE33830>  [property]

# transform(self, m)  [function]
#     -> Replace quad by its transformation with matrix m.

# width = <property object at 0x000002052DE33880>  [property]


# ===== Source Code =====
class Quad:

    def __abs__(self):
        if self.is_empty:
            return 0.0
        return abs(self.ul - self.ur) * abs(self.ul - self.ll)

    def __add__(self, q):
        if hasattr(q, "__float__"):
            return Quad(self.ul + q, self.ur + q, self.ll + q, self.lr + q)
        if len(q) != 4:
            raise ValueError("Quad: bad seq len")
        return Quad(self.ul + q[0], self.ur + q[1], self.ll + q[2], self.lr + q[3])

    def __bool__(self):
        return not self.is_empty

    def __contains__(self, x):
        try:
            l = x.__len__()
        except Exception:
            if g_exceptions_verbose > 1:    exception_info()
            return False
        if l == 2:
            return util_point_in_quad(x, self)
        if l != 4:
            return False
        if CheckRect(x):
            if Rect(x).is_empty:
                return True
            return util_point_in_quad(x[:2], self) and util_point_in_quad(x[2:], self)
        if CheckQuad(x):
            for i in range(4):
                if not util_point_in_quad(x[i], self):
                    return False
            return True
        return False

    def __eq__(self, quad):
        if not hasattr(quad, "__len__"):
            return False
        return len(quad) == 4 and (
            self.ul == quad[0] and
            self.ur == quad[1] and
            self.ll == quad[2] and
            self.lr == quad[3]
        )

    def __getitem__(self, i):
        return (self.ul, self.ur, self.ll, self.lr)[i]

    def __hash__(self):
        return hash(tuple(self))

    def __init__(self, *args, ul=None, ur=None, ll=None, lr=None):
        '''
        Quad() - all zero points
        Quad(ul, ur, ll, lr)
        Quad(quad) - new copy
        Quad(sequence) - from 'sequence'

        Explicit keyword args ul, ur, ll, lr override earlier settings if not
        None.
    
        '''
        if not args:
            self.ul = self.ur = self.ll = self.lr = Point()
        elif len(args) > 4:
            raise ValueError("Quad: bad seq len")
        elif len(args) == 4:
            self.ul, self.ur, self.ll, self.lr = map(Point, args)
        elif len(args) == 1:
            l = args[0]
            if isinstance(l, mupdf.FzQuad):
                self.this = l
                self.ul, self.ur, self.ll, self.lr = Point(l.ul), Point(l.ur), Point(l.ll), Point(l.lr)
            elif not hasattr(l, "__getitem__"):
                raise ValueError("Quad: bad args")
            elif len(l) != 4:
                raise ValueError("Quad: bad seq len")
            else:
                self.ul, self.ur, self.ll, self.lr = map(Point, l)
        else:
            raise ValueError("Quad: bad args")
        if ul is not None:  self.ul = Point(ul)
        if ur is not None:  self.ur = Point(ur)
        if ll is not None:  self.ll = Point(ll)
        if lr is not None:  self.lr = Point(lr)

    def __len__(self):
        return 4

    def __mul__(self, m):
        q = Quad(self)
        q = q.transform(m)
        return q

    def __neg__(self):
        return Quad(-self.ul, -self.ur, -self.ll, -self.lr)

    def __nonzero__(self):
        return not self.is_empty

    def __pos__(self):
        return Quad(self)

    def __repr__(self):
        return "Quad" + str(tuple(self))

    def __setitem__(self, i, v):
        if   i == 0: self.ul = Point(v)
        elif i == 1: self.ur = Point(v)
        elif i == 2: self.ll = Point(v)
        elif i == 3: self.lr = Point(v)
        else:
            raise IndexError("index out of range")
        return None

    def __sub__(self, q):
        if hasattr(q, "__float__"):
            return Quad(self.ul - q, self.ur - q, self.ll - q, self.lr - q)
        if len(q) != 4:
            raise ValueError("Quad: bad seq len")
        return Quad(self.ul - q[0], self.ur - q[1], self.ll - q[2], self.lr - q[3])

    def __truediv__(self, m):
        if hasattr(m, "__float__"):
            im = 1. / m
        else:
            im = util_invert_matrix(m)[1]
            if not im:
                raise ZeroDivisionError("Matrix not invertible")
        q = Quad(self)
        q = q.transform(im)
        return q

    @property
    def is_convex(self):
        """Check if quad is convex and not degenerate.

        Notes:
            Check that for the two diagonals, the other two corners are not
            on the same side of the diagonal.
        Returns:
            True or False.
        """
        m = planish_line(self.ul, self.lr)  # puts this diagonal on x-axis
        p1 = self.ll * m  # transform the
        p2 = self.ur * m  # other two points
        if p1.y * p2.y > 0:
            return False
        m = planish_line(self.ll, self.ur)  # puts other diagonal on x-axis
        p1 = self.lr * m  # transform the
        p2 = self.ul * m  # remaining points
        if p1.y * p2.y > 0:
            return False
        return True

    @property
    def is_empty(self):
        """Check whether all quad corners are on the same line.

        This is the case if width or height is zero.
        """
        return self.width < EPSILON or self.height < EPSILON

    @property
    def is_infinite(self):
        """Check whether this is the infinite quad."""
        return self.rect.is_infinite

    @property
    def is_rectangular(self):
        """Check if quad is rectangular.

        Notes:
            Some rotation matrix can thus transform it into a rectangle.
            This is equivalent to three corners enclose 90 degrees.
        Returns:
            True or False.
        """

        sine = util_sine_between(self.ul, self.ur, self.lr)
        if abs(sine - 1) > EPSILON:  # the sine of the angle
            return False

        sine = util_sine_between(self.ur, self.lr, self.ll)
        if abs(sine - 1) > EPSILON:
            return False

        sine = util_sine_between(self.lr, self.ll, self.ul)
        if abs(sine - 1) > EPSILON:
            return False

        return True

    def morph(self, p, m):
        """Morph the quad with matrix-like 'm' and point-like 'p'.

        Return a new quad."""
        if self.is_infinite:
            return INFINITE_QUAD()
        delta = Matrix(1, 1).pretranslate(p.x, p.y)
        q = self * ~delta * m * delta
        return q

    @property
    def rect(self):
        r = Rect()
        r.x0 = min(self.ul.x, self.ur.x, self.lr.x, self.ll.x)
        r.y0 = min(self.ul.y, self.ur.y, self.lr.y, self.ll.y)
        r.x1 = max(self.ul.x, self.ur.x, self.lr.x, self.ll.x)
        r.y1 = max(self.ul.y, self.ur.y, self.lr.y, self.ll.y)
        return r

    def transform(self, m):
        """Replace quad by its transformation with matrix m."""
        if hasattr(m, "__float__"):
            pass
        elif len(m) != 6:
            raise ValueError("Matrix: bad seq len")
        self.ul *= m
        self.ur *= m
        self.ll *= m
        self.lr *= m
        return self

    __div__ = __truediv__
    width  = property(lambda self: max(abs(self.ul - self.ur), abs(self.ll - self.lr)))
    height = property(lambda self: max(abs(self.ul - self.ll), abs(self.ur - self.lr)))

"""
Class: fitz.Shape

Description:
Create a new shape.

Inheritance (MRO): Shape -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Shape =====

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, page: pymupdf.Page)  [function]
#     -> Initialize self.  See help(type(self)) for accurate signature.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self, /)  [wrapper_descriptor]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# commit(self, overlay: bool = True) -> None  [function]
#     -> Update the page's /Contents object with Shape data.

# draw_bezier(self, p1: 'point_like', p2: 'point_like', p3: 'point_like', p4: 'point_like') -> pymupdf.Point  [function]
#     -> Draw a standard cubic Bezier curve.

# draw_circle(self, center: 'point_like', radius: float) -> pymupdf.Point  [function]
#     -> Draw a circle given its center and radius.

# draw_curve(self, p1: 'point_like', p2: 'point_like', p3: 'point_like') -> pymupdf.Point  [function]
#     -> Draw a curve between points using one control point.

# draw_line(self, p1: 'point_like', p2: 'point_like') -> pymupdf.Point  [function]
#     -> Draw a line between two points.

# draw_oval(self, tetra: Union[ForwardRef('quad_like'), ForwardRef('rect_like')]) -> pymupdf.Point  [function]
#     -> Draw an ellipse inside a tetrapod.

# draw_polyline(self, points: list) -> pymupdf.Point  [function]
#     -> Draw several connected line segments.

# draw_quad(self, quad: 'quad_like') -> pymupdf.Point  [function]
#     -> Draw a Quad.

# draw_rect(self, rect: 'rect_like', *, radius=None) -> pymupdf.Point  [function]
#     -> Draw a rectangle.

# draw_sector(self, center: 'point_like', point: 'point_like', beta: float, fullSector: bool = True) -> pymupdf.Point  [function]
#     -> Draw a circle sector.

# draw_squiggle(self, p1: 'point_like', p2: 'point_like', breadth=2) -> pymupdf.Point  [function]
#     -> Draw a squiggly line from p1 to p2.

# draw_zigzag(self, p1: 'point_like', p2: 'point_like', breadth: float = 2) -> pymupdf.Point  [function]
#     -> Draw a zig-zagged line from p1 to p2.

# finish(self, width: float = 1, color: Optional[Sequence] = (0,), fill: Optional[Sequence] = None, lineCap: int = 0, lineJoin: int = 0, dashes: Optional[str] = None, even_odd: bool = False, morph: Optional[Sequence] = None, closePath: bool = True, fill_opacity: float = 1, stroke_opacity: float = 1, oc: int = 0) -> None  [function]
#     -> Finish the current drawing segment.

# horizontal_angle(C, P)  [function]
#     -> Return the angle to the horizontal for the connection from C to P.

# insert_text(self, point: 'point_like', buffer: Union[str, list], *, fontsize: float = 11, lineheight: Optional[float] = None, fontname: str = 'helv', fontfile: Optional[str] = None, set_simple: bool = 0, encoding: int = 0, color: Optional[Sequence] = None, fill: Optional[Sequence] = None, render_mode: int = 0, border_width: float = 0.05, miter_limit: float = 1, rotate: int = 0, morph: Optional[Sequence] = None, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0) -> int  [function]

# insert_textbox(self, rect: 'rect_like', buffer: Union[str, list], *, fontname: Optional[str] = 'helv', fontfile: Optional[str] = None, fontsize: float = 11, lineheight: Optional[float] = None, set_simple: bool = 0, encoding: int = 0, color: Optional[Sequence] = None, fill: Optional[Sequence] = None, expandtabs: int = 1, border_width: float = 0.05, miter_limit: float = 1, align: int = 0, render_mode: int = 0, rotate: int = 0, morph: Optional[Sequence] = None, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0) -> float  [function]
#     -> Insert text into a given rectangle.

# updateRect(self, x)  [function]


# ===== Source Code =====
class Shape:
    """Create a new shape."""

    @staticmethod
    def horizontal_angle(C, P):
        """Return the angle to the horizontal for the connection from C to P.
        This uses the arcus sine function and resolves its inherent ambiguity by
        looking up in which quadrant vector S = P - C is located.
        """
        S = Point(P - C).unit  # unit vector 'C' -> 'P'
        alfa = math.asin(abs(S.y))  # absolute angle from horizontal
        if S.x < 0:  # make arcsin result unique
            if S.y <= 0:  # bottom-left
                alfa = -(math.pi - alfa)
            else:  # top-left
                alfa = math.pi - alfa
        else:
            if S.y >= 0:  # top-right
                pass
            else:  # bottom-right
                alfa = -alfa
        return alfa

    def __init__(self, page: Page):
        CheckParent(page)
        self.page = page
        self.doc = page.parent
        if not self.doc.is_pdf:
            raise ValueError("is no PDF")
        self.height = page.mediabox_size.y
        self.width = page.mediabox_size.x
        self.x = page.cropbox_position.x
        self.y = page.cropbox_position.y

        self.pctm = page.transformation_matrix  # page transf. matrix
        self.ipctm = ~self.pctm  # inverted transf. matrix

        self.draw_cont = ""
        self.text_cont = ""
        self.totalcont = ""
        self.last_point = None
        self.rect = None

    def updateRect(self, x):
        if self.rect is None:
            if len(x) == 2:
                self.rect = Rect(x, x)
            else:
                self.rect = Rect(x)

        else:
            if len(x) == 2:
                x = Point(x)
                self.rect.x0 = min(self.rect.x0, x.x)
                self.rect.y0 = min(self.rect.y0, x.y)
                self.rect.x1 = max(self.rect.x1, x.x)
                self.rect.y1 = max(self.rect.y1, x.y)
            else:
                x = Rect(x)
                self.rect.x0 = min(self.rect.x0, x.x0)
                self.rect.y0 = min(self.rect.y0, x.y0)
                self.rect.x1 = max(self.rect.x1, x.x1)
                self.rect.y1 = max(self.rect.y1, x.y1)

    def draw_line(self, p1: point_like, p2: point_like) -> Point:
        """Draw a line between two points."""
        p1 = Point(p1)
        p2 = Point(p2)
        if not (self.last_point == p1):
            self.draw_cont += _format_g(JM_TUPLE(p1 * self.ipctm)) + " m\n"
            self.last_point = p1
            self.updateRect(p1)

        self.draw_cont += _format_g(JM_TUPLE(p2 * self.ipctm)) + " l\n"
        self.updateRect(p2)
        self.last_point = p2
        return self.last_point

    def draw_polyline(self, points: list) -> Point:
        """Draw several connected line segments."""
        for i, p in enumerate(points):
            if i == 0:
                if not (self.last_point == Point(p)):
                    self.draw_cont += _format_g(JM_TUPLE(Point(p) * self.ipctm)) + " m\n"
                    self.last_point = Point(p)
            else:
                self.draw_cont += _format_g(JM_TUPLE(Point(p) * self.ipctm)) + " l\n"
            self.updateRect(p)

        self.last_point = Point(points[-1])
        return self.last_point

    def draw_bezier(
        self,
        p1: point_like,
        p2: point_like,
        p3: point_like,
        p4: point_like,
    ) -> Point:
        """Draw a standard cubic Bezier curve."""
        p1 = Point(p1)
        p2 = Point(p2)
        p3 = Point(p3)
        p4 = Point(p4)
        if not (self.last_point == p1):
            self.draw_cont += _format_g(JM_TUPLE(p1 * self.ipctm)) + " m\n"
        args = JM_TUPLE(list(p2 * self.ipctm) + list(p3 * self.ipctm) + list(p4 * self.ipctm))
        self.draw_cont += _format_g(args) + " c\n"
        self.updateRect(p1)
        self.updateRect(p2)
        self.updateRect(p3)
        self.updateRect(p4)
        self.last_point = p4
        return self.last_point

    def draw_oval(self, tetra: typing.Union[quad_like, rect_like]) -> Point:
        """Draw an ellipse inside a tetrapod."""
        if len(tetra) != 4:
            raise ValueError("invalid arg length")
        if hasattr(tetra[0], "__float__"):
            q = Rect(tetra).quad
        else:
            q = Quad(tetra)

        mt = q.ul + (q.ur - q.ul) * 0.5
        mr = q.ur + (q.lr - q.ur) * 0.5
        mb = q.ll + (q.lr - q.ll) * 0.5
        ml = q.ul + (q.ll - q.ul) * 0.5
        if not (self.last_point == ml):
            self.draw_cont += _format_g(JM_TUPLE(ml * self.ipctm)) + " m\n"
            self.last_point = ml
        self.draw_curve(ml, q.ll, mb)
        self.draw_curve(mb, q.lr, mr)
        self.draw_curve(mr, q.ur, mt)
        self.draw_curve(mt, q.ul, ml)
        self.updateRect(q.rect)
        self.last_point = ml
        return self.last_point

    def draw_circle(self, center: point_like, radius: float) -> Point:
        """Draw a circle given its center and radius."""
        if not radius > EPSILON:
            raise ValueError("radius must be positive")
        center = Point(center)
        p1 = center - (radius, 0)
        return self.draw_sector(center, p1, 360, fullSector=False)

    def draw_curve(
        self,
        p1: point_like,
        p2: point_like,
        p3: point_like,
    ) -> Point:
        """Draw a curve between points using one control point."""
        kappa = 0.55228474983
        p1 = Point(p1)
        p2 = Point(p2)
        p3 = Point(p3)
        k1 = p1 + (p2 - p1) * kappa
        k2 = p3 + (p2 - p3) * kappa
        return self.draw_bezier(p1, k1, k2, p3)

    def draw_sector(
        self,
        center: point_like,
        point: point_like,
        beta: float,
        fullSector: bool = True,
    ) -> Point:
        """Draw a circle sector."""
        center = Point(center)
        point = Point(point)
        l3 = lambda a, b: _format_g((a, b)) + " m\n"
        l4 = lambda a, b, c, d, e, f: _format_g((a, b, c, d, e, f)) + " c\n"
        l5 = lambda a, b: _format_g((a, b)) + " l\n"
        betar = math.radians(-beta)
        w360 = math.radians(math.copysign(360, betar)) * (-1)
        w90 = math.radians(math.copysign(90, betar))
        w45 = w90 / 2
        while abs(betar) > 2 * math.pi:
            betar += w360  # bring angle below 360 degrees
        if not (self.last_point == point):
            self.draw_cont += l3(*JM_TUPLE(point * self.ipctm))
            self.last_point = point
        Q = Point(0, 0)  # just make sure it exists
        C = center
        P = point
        S = P - C  # vector 'center' -> 'point'
        rad = abs(S)  # circle radius

        if not rad > EPSILON:
            raise ValueError("radius must be positive")

        alfa = self.horizontal_angle(center, point)
        while abs(betar) > abs(w90):  # draw 90 degree arcs
            q1 = C.x + math.cos(alfa + w90) * rad
            q2 = C.y + math.sin(alfa + w90) * rad
            Q = Point(q1, q2)  # the arc's end point
            r1 = C.x + math.cos(alfa + w45) * rad / math.cos(w45)
            r2 = C.y + math.sin(alfa + w45) * rad / math.cos(w45)
            R = Point(r1, r2)  # crossing point of tangents
            kappah = (1 - math.cos(w45)) * 4 / 3 / abs(R - Q)
            kappa = kappah * abs(P - Q)
            cp1 = P + (R - P) * kappa  # control point 1
            cp2 = Q + (R - Q) * kappa  # control point 2
            self.draw_cont += l4(*JM_TUPLE(
                list(cp1 * self.ipctm) + list(cp2 * self.ipctm) + list(Q * self.ipctm)
            ))

            betar -= w90  # reduce param angle by 90 deg
            alfa += w90  # advance start angle by 90 deg
            P = Q  # advance to arc end point
        # draw (remaining) arc
        if abs(betar) > 1e-3:  # significant degrees left?
            beta2 = betar / 2
            q1 = C.x + math.cos(alfa + betar) * rad
            q2 = C.y + math.sin(alfa + betar) * rad
            Q = Point(q1, q2)  # the arc's end point
            r1 = C.x + math.cos(alfa + beta2) * rad / math.cos(beta2)
            r2 = C.y + math.sin(alfa + beta2) * rad / math.cos(beta2)
            R = Point(r1, r2)  # crossing point of tangents
            # kappa height is 4/3 of segment height
            kappah = (1 - math.cos(beta2)) * 4 / 3 / abs(R - Q)  # kappa height
            kappa = kappah * abs(P - Q) / (1 - math.cos(betar))
            cp1 = P + (R - P) * kappa  # control point 1
            cp2 = Q + (R - Q) * kappa  # control point 2
            self.draw_cont += l4(*JM_TUPLE(
                list(cp1 * self.ipctm) + list(cp2 * self.ipctm) + list(Q * self.ipctm)
            ))
        if fullSector:
            self.draw_cont += l3(*JM_TUPLE(point * self.ipctm))
            self.draw_cont += l5(*JM_TUPLE(center * self.ipctm))
            self.draw_cont += l5(*JM_TUPLE(Q * self.ipctm))
        self.last_point = Q
        return self.last_point

    def draw_rect(self, rect: rect_like, *, radius=None) -> Point:
        """Draw a rectangle.

        Args:
            radius: if not None, the rectangle will have rounded corners.
                This is the radius of the curvature, given as percentage of
                the rectangle width or height. Valid are values 0 < v <= 0.5.
                For a sequence of two values, the corners will have different
                radii. Otherwise, the percentage will be computed from the
                shorter side. A value of (0.5, 0.5) will draw an ellipse.
        """
        r = Rect(rect)
        if radius is None:  # standard rectangle
            self.draw_cont += _format_g(JM_TUPLE(
                list(r.bl * self.ipctm) + [r.width, r.height]
            )) + " re\n"
            self.updateRect(r)
            self.last_point = r.tl
            return self.last_point
        # rounded corners requested. This requires 1 or 2 values, each
        # with 0 < value <= 0.5
        if hasattr(radius, "__float__"):
            if radius <= 0 or radius > 0.5:
                raise ValueError(f"bad radius value {radius}.")
            d = min(r.width, r.height) * radius
            px = (d, 0)
            py = (0, d)
        elif hasattr(radius, "__len__") and len(radius) == 2:
            rx, ry = radius
            px = (rx * r.width, 0)
            py = (0, ry * r.height)
            if min(rx, ry) <= 0 or max(rx, ry) > 0.5:
                raise ValueError(f"bad radius value {radius}.")
        else:
            raise ValueError(f"bad radius value {radius}.")

        lp = self.draw_line(r.tl + py, r.bl - py)
        lp = self.draw_curve(lp, r.bl, r.bl + px)

        lp = self.draw_line(lp, r.br - px)
        lp = self.draw_curve(lp, r.br, r.br - py)

        lp = self.draw_line(lp, r.tr + py)
        lp = self.draw_curve(lp, r.tr, r.tr - px)

        lp = self.draw_line(lp, r.tl + px)
        self.last_point = self.draw_curve(lp, r.tl, r.tl + py)

        self.updateRect(r)
        return self.last_point

    def draw_quad(self, quad: quad_like) -> Point:
        """Draw a Quad."""
        q = Quad(quad)
        return self.draw_polyline([q.ul, q.ll, q.lr, q.ur, q.ul])

    def draw_zigzag(
        self,
        p1: point_like,
        p2: point_like,
        breadth: float = 2,
    ) -> Point:
        """Draw a zig-zagged line from p1 to p2."""
        p1 = Point(p1)
        p2 = Point(p2)
        S = p2 - p1  # vector start - end
        rad = abs(S)  # distance of points
        cnt = 4 * int(round(rad / (4 * breadth), 0))  # always take full phases
        if cnt < 4:
            raise ValueError("points too close")
        mb = rad / cnt  # revised breadth
        matrix = Matrix(util_hor_matrix(p1, p2))  # normalize line to x-axis
        i_mat = ~matrix  # get original position
        points = []  # stores edges
        for i in range(1, cnt):
            if i % 4 == 1:  # point "above" connection
                p = Point(i, -1) * mb
            elif i % 4 == 3:  # point "below" connection
                p = Point(i, 1) * mb
            else:  # ignore others
                continue
            points.append(p * i_mat)
        self.draw_polyline([p1] + points + [p2])  # add start and end points
        return p2

    def draw_squiggle(
        self,
        p1: point_like,
        p2: point_like,
        breadth=2,
    ) -> Point:
        """Draw a squiggly line from p1 to p2."""
        p1 = Point(p1)
        p2 = Point(p2)
        S = p2 - p1  # vector start - end
        rad = abs(S)  # distance of points
        cnt = 4 * int(round(rad / (4 * breadth), 0))  # always take full phases
        if cnt < 4:
            raise ValueError("points too close")
        mb = rad / cnt  # revised breadth
        matrix = Matrix(util_hor_matrix(p1, p2))  # normalize line to x-axis
        i_mat = ~matrix  # get original position
        k = 2.4142135623765633  # y of draw_curve helper point

        points = []  # stores edges
        for i in range(1, cnt):
            if i % 4 == 1:  # point "above" connection
                p = Point(i, -k) * mb
            elif i % 4 == 3:  # point "below" connection
                p = Point(i, k) * mb
            else:  # else on connection line
                p = Point(i, 0) * mb
            points.append(p * i_mat)

        points = [p1] + points + [p2]
        cnt = len(points)
        i = 0
        while i + 2 < cnt:
            self.draw_curve(points[i], points[i + 1], points[i + 2])
            i += 2
        return p2

    # ==============================================================================
    # Shape.insert_text
    # ==============================================================================
    def insert_text(
        self,
        point: point_like,
        buffer: typing.Union[str, list],
        *,
        fontsize: float = 11,
        lineheight: OptFloat = None,
        fontname: str = "helv",
        fontfile: OptStr = None,
        set_simple: bool = 0,
        encoding: int = 0,
        color: OptSeq = None,
        fill: OptSeq = None,
        render_mode: int = 0,
        border_width: float = 0.05,
        miter_limit: float = 1,
        rotate: int = 0,
        morph: OptSeq = None,
        stroke_opacity: float = 1,
        fill_opacity: float = 1,
        oc: int = 0,
    ) -> int:

        # ensure 'text' is a list of strings, worth dealing with
        if not bool(buffer):
            return 0

        if type(buffer) not in (list, tuple):
            text = buffer.splitlines()
        else:
            text = buffer

        if not len(text) > 0:
            return 0

        point = Point(point)
        try:
            maxcode = max([ord(c) for c in " ".join(text)])
        except Exception:
            exception_info()
            return 0

        # ensure valid 'fontname'
        fname = fontname
        if fname.startswith("/"):
            fname = fname[1:]

        xref = self.page.insert_font(
            fontname=fname, fontfile=fontfile, encoding=encoding, set_simple=set_simple
        )
        fontinfo = CheckFontInfo(self.doc, xref)

        fontdict = fontinfo[1]
        ordering = fontdict["ordering"]
        simple = fontdict["simple"]
        bfname = fontdict["name"]
        ascender = fontdict["ascender"]
        descender = fontdict["descender"]
        if lineheight:
            lheight = fontsize * lineheight
        elif ascender - descender <= 1:
            lheight = fontsize * 1.2
        else:
            lheight = fontsize * (ascender - descender)

        if maxcode > 255:
            glyphs = self.doc.get_char_widths(xref, maxcode + 1)
        else:
            glyphs = fontdict["glyphs"]

        tab = []
        for t in text:
            if simple and bfname not in ("Symbol", "ZapfDingbats"):
                g = None
            else:
                g = glyphs
            tab.append(getTJstr(t, g, simple, ordering))
        text = tab

        color_str = ColorCode(color, "c")
        fill_str = ColorCode(fill, "f")
        if not fill and render_mode == 0:  # ensure fill color when 0 Tr
            fill = color
            fill_str = ColorCode(color, "f")

        morphing = CheckMorph(morph)
        rot = rotate
        if rot % 90 != 0:
            raise ValueError("bad rotate value")

        while rot < 0:
            rot += 360
        rot = rot % 360  # text rotate = 0, 90, 270, 180

        templ1 = lambda a, b, c, d, e, f, g: f"\nq\n{a}{b}BT\n{c}1 0 0 1 {_format_g((d, e))} Tm\n/{f} {_format_g(g)} Tf "
        templ2 = lambda a: f"TJ\n0 -{_format_g(a)} TD\n"
        cmp90 = "0 1 -1 0 0 0 cm\n"  # rotates 90 deg counter-clockwise
        cmm90 = "0 -1 1 0 0 0 cm\n"  # rotates 90 deg clockwise
        cm180 = "-1 0 0 -1 0 0 cm\n"  # rotates by 180 deg.
        height = self.height
        width = self.width

        # setting up for standard rotation directions
        # case rotate = 0
        if morphing:
            m1 = Matrix(1, 0, 0, 1, morph[0].x + self.x, height - morph[0].y - self.y)
            mat = ~m1 * morph[1] * m1
            cm = _format_g(JM_TUPLE(mat)) + " cm\n"
        else:
            cm = ""
        top = height - point.y - self.y  # start of 1st char
        left = point.x + self.x  # start of 1. char
        space = top  # space available
        #headroom = point.y + self.y  # distance to page border
        if rot == 90:
            left = height - point.y - self.y
            top = -point.x - self.x
            cm += cmp90
            space = width - abs(top)
            #headroom = point.x + self.x

        elif rot == 270:
            left = -height + point.y + self.y
            top = point.x + self.x
            cm += cmm90
            space = abs(top)
            #headroom = width - point.x - self.x

        elif rot == 180:
            left = -point.x - self.x
            top = -height + point.y + self.y
            cm += cm180
            space = abs(point.y + self.y)
            #headroom = height - point.y - self.y

        optcont = self.page._get_optional_content(oc)
        if optcont is not None:
            bdc = "/OC /%s BDC\n" % optcont
            emc = "EMC\n"
        else:
            bdc = emc = ""

        alpha = self.page._set_opacity(CA=stroke_opacity, ca=fill_opacity)
        if alpha is None:
            alpha = ""
        else:
            alpha = "/%s gs\n" % alpha
        nres = templ1(bdc, alpha, cm, left, top, fname, fontsize)

        if render_mode > 0:
            nres += "%i Tr " % render_mode
            nres += _format_g(border_width * fontsize) + " w "
            if miter_limit is not None:
                nres += _format_g(miter_limit) + " M "
        if color is not None:
            nres += color_str
        if fill is not None:
            nres += fill_str

        # =========================================================================
        #   start text insertion
        # =========================================================================
        nres += text[0]
        nlines = 1  # set output line counter
        if len(text) > 1:
            nres += templ2(lheight)  # line 1
        else:
            nres += 'TJ'
        for i in range(1, len(text)):
            if space < lheight:
                break  # no space left on page
            if i > 1:
                nres += "\nT* "
            nres += text[i] + 'TJ'
            space -= lheight
            nlines += 1

        nres += "\nET\n%sQ\n" % emc

        # =========================================================================
        #   end of text insertion
        # =========================================================================
        # update the /Contents object
        self.text_cont += nres
        return nlines

    # ==============================================================================
    # Shape.insert_textbox
    # ==============================================================================
    def insert_textbox(
        self,
        rect: rect_like,
        buffer: typing.Union[str, list],
        *,
        fontname: OptStr = "helv",
        fontfile: OptStr = None,
        fontsize: float = 11,
        lineheight: OptFloat = None,
        set_simple: bool = 0,
        encoding: int = 0,
        color: OptSeq = None,
        fill: OptSeq = None,
        expandtabs: int = 1,
        border_width: float = 0.05,
        miter_limit: float = 1,
        align: int = 0,
        render_mode: int = 0,
        rotate: int = 0,
        morph: OptSeq = None,
        stroke_opacity: float = 1,
        fill_opacity: float = 1,
        oc: int = 0,
    ) -> float:
        """Insert text into a given rectangle.

        Args:
            rect -- the textbox to fill
            buffer -- text to be inserted
            fontname -- a Base-14 font, font name or '/name'
            fontfile -- name of a font file
            fontsize -- font size
            lineheight -- overwrite the font property
            color -- RGB stroke color triple
            fill -- RGB fill color triple
            render_mode -- text rendering control
            border_width -- thickness of glyph borders as percentage of fontsize
            expandtabs -- handles tabulators with string function
            align -- left, center, right, justified
            rotate -- 0, 90, 180, or 270 degrees
            morph -- morph box with a matrix and a fixpoint
        Returns:
            unused or deficit rectangle area (float)
        """
        rect = Rect(rect)
        if rect.is_empty or rect.is_infinite:
            raise ValueError("text box must be finite and not empty")

        color_str = ColorCode(color, "c")
        fill_str = ColorCode(fill, "f")
        if fill is None and render_mode == 0:  # ensure fill color for 0 Tr
            fill = color
            fill_str = ColorCode(color, "f")

        optcont = self.page._get_optional_content(oc)
        if optcont is not None:
            bdc = "/OC /%s BDC\n" % optcont
            emc = "EMC\n"
        else:
            bdc = emc = ""

        # determine opacity / transparency
        alpha = self.page._set_opacity(CA=stroke_opacity, ca=fill_opacity)
        if alpha is None:
            alpha = ""
        else:
            alpha = "/%s gs\n" % alpha

        if rotate % 90 != 0:
            raise ValueError("rotate must be multiple of 90")

        rot = rotate
        while rot < 0:
            rot += 360
        rot = rot % 360

        # is buffer worth of dealing with?
        if not bool(buffer):
            return rect.height if rot in (0, 180) else rect.width

        cmp90 = "0 1 -1 0 0 0 cm\n"  # rotates counter-clockwise
        cmm90 = "0 -1 1 0 0 0 cm\n"  # rotates clockwise
        cm180 = "-1 0 0 -1 0 0 cm\n"  # rotates by 180 deg.
        height = self.height

        fname = fontname
        if fname.startswith("/"):
            fname = fname[1:]

        xref = self.page.insert_font(
            fontname=fname, fontfile=fontfile, encoding=encoding, set_simple=set_simple
        )
        fontinfo = CheckFontInfo(self.doc, xref)

        fontdict = fontinfo[1]
        ordering = fontdict["ordering"]
        simple = fontdict["simple"]
        glyphs = fontdict["glyphs"]
        bfname = fontdict["name"]
        ascender = fontdict["ascender"]
        descender = fontdict["descender"]

        if lineheight:
            lheight_factor = lineheight
        elif ascender - descender <= 1:
            lheight_factor = 1.2
        else:
            lheight_factor = ascender - descender
        lheight = fontsize * lheight_factor

        # create a list from buffer, split into its lines
        if type(buffer) in (list, tuple):
            t0 = "\n".join(buffer)
        else:
            t0 = buffer

        maxcode = max([ord(c) for c in t0])
        # replace invalid char codes for simple fonts
        if simple and maxcode > 255:
            t0 = "".join([c if ord(c) < 256 else "?" for c in t0])

        t0 = t0.splitlines()

        glyphs = self.doc.get_char_widths(xref, maxcode + 1)
        if simple and bfname not in ("Symbol", "ZapfDingbats"):
            tj_glyphs = None
        else:
            tj_glyphs = glyphs

        # ----------------------------------------------------------------------
        # calculate pixel length of a string
        # ----------------------------------------------------------------------
        def pixlen(x):
            """Calculate pixel length of x."""
            if ordering < 0:
                return sum([glyphs[ord(c)][1] for c in x]) * fontsize
            else:
                return len(x) * fontsize

        # ---------------------------------------------------------------------

        if ordering < 0:
            blen = glyphs[32][1] * fontsize  # pixel size of space character
        else:
            blen = fontsize

        text = ""  # output buffer

        if CheckMorph(morph):
            m1 = Matrix(
                1, 0, 0, 1, morph[0].x + self.x, self.height - morph[0].y - self.y
            )
            mat = ~m1 * morph[1] * m1
            cm = _format_g(JM_TUPLE(mat)) + " cm\n"
        else:
            cm = ""

        # ---------------------------------------------------------------------
        # adjust for text orientation / rotation
        # ---------------------------------------------------------------------
        progr = 1  # direction of line progress
        c_pnt = Point(0, fontsize * ascender)  # used for line progress
        if rot == 0:  # normal orientation
            point = rect.tl + c_pnt  # line 1 is 'lheight' below top
            maxwidth = rect.width  # pixels available in one line
            maxheight = rect.height  # available text height

        elif rot == 90:  # rotate counter clockwise
            c_pnt = Point(fontsize * ascender, 0)  # progress in x-direction
            point = rect.bl + c_pnt  # line 1 'lheight' away from left
            maxwidth = rect.height  # pixels available in one line
            maxheight = rect.width  # available text height
            cm += cmp90

        elif rot == 180:  # text upside down
            # progress upwards in y direction
            c_pnt = -Point(0, fontsize * ascender)
            point = rect.br + c_pnt  # line 1 'lheight' above bottom
            maxwidth = rect.width  # pixels available in one line
            progr = -1  # subtract lheight for next line
            maxheight =rect.height  # available text height
            cm += cm180

        else:  # rotate clockwise (270 or -90)
            # progress from right to left
            c_pnt = -Point(fontsize * ascender, 0)
            point = rect.tr + c_pnt  # line 1 'lheight' left of right
            maxwidth = rect.height  # pixels available in one line
            progr = -1  # subtract lheight for next line
            maxheight = rect.width  # available text height
            cm += cmm90

        # =====================================================================
        # line loop
        # =====================================================================
        just_tab = []  # 'justify' indicators per line

        for i, line in enumerate(t0):
            line_t = line.expandtabs(expandtabs).split(" ")  # split into words
            num_words = len(line_t)
            lbuff = ""  # init line buffer
            rest = maxwidth  # available line pixels
            # =================================================================
            # word loop
            # =================================================================
            for j in range(num_words):
                word = line_t[j]
                pl_w = pixlen(word)  # pixel len of word
                if rest >= pl_w:  # does it fit on the line?
                    lbuff += word + " "  # yes, append word
                    rest -= pl_w + blen  # update available line space
                    continue  # next word

                # word doesn't fit - output line (if not empty)
                if lbuff:
                    lbuff = lbuff.rstrip() + "\n"  # line full, append line break
                    text += lbuff  # append to total text
                    just_tab.append(True)  # can align-justify

                lbuff = ""  # re-init line buffer
                rest = maxwidth  # re-init avail. space

                if pl_w <= maxwidth:  # word shorter than 1 line?
                    lbuff = word + " "  # start the line with it
                    rest = maxwidth - pl_w - blen  # update free space
                    continue

                # long word: split across multiple lines - char by char ...
                if len(just_tab) > 0:
                    just_tab[-1] = False  # cannot align-justify
                for c in word:
                    if pixlen(lbuff) <= maxwidth - pixlen(c):
                        lbuff += c
                    else:  # line full
                        lbuff += "\n"  # close line
                        text += lbuff  # append to text
                        just_tab.append(False)  # cannot align-justify
                        lbuff = c  # start new line with this char

                lbuff += " "  # finish long word
                rest = maxwidth - pixlen(lbuff)  # long word stored

            if lbuff:  # unprocessed line content?
                text += lbuff.rstrip()  # append to text
                just_tab.append(False)  # cannot align-justify

            if i < len(t0) - 1:  # not the last line?
                text += "\n"  # insert line break

        # compute used part of the textbox
        if text.endswith("\n"):
            text = text[:-1]
        lb_count = text.count("\n") + 1  # number of lines written

        # text height = line count * line height plus one descender value
        text_height = lheight * lb_count - descender * fontsize

        more = text_height - maxheight  # difference to height limit
        if more > EPSILON:  # landed too much outside rect
            return (-1) * more  # return deficit, don't output

        more = abs(more)
        if more < EPSILON:
            more = 0  # don't bother with epsilons
        nres = "\nq\n%s%sBT\n" % (bdc, alpha) + cm  # initialize output buffer
        templ = lambda a, b, c, d: f"1 0 0 1 {_format_g((a, b))} Tm /{c} {_format_g(d)} Tf "
        # center, right, justify: output each line with its own specifics
        text_t = text.splitlines()  # split text in lines again
        just_tab[-1] = False  # never justify last line
        for i, t in enumerate(text_t):
            spacing = 0
            pl = maxwidth - pixlen(t)  # length of empty line part
            pnt = point + c_pnt * (i * lheight_factor)  # text start of line
            if align == 1:  # center: right shift by half width
                if rot in (0, 180):
                    pnt = pnt + Point(pl / 2, 0) * progr
                else:
                    pnt = pnt - Point(0, pl / 2) * progr
            elif align == 2:  # right: right shift by full width
                if rot in (0, 180):
                    pnt = pnt + Point(pl, 0) * progr
                else:
                    pnt = pnt - Point(0, pl) * progr
            elif align == 3:  # justify
                spaces = t.count(" ")  # number of spaces in line
                if spaces > 0 and just_tab[i]:  # if any, and we may justify
                    spacing = pl / spaces  # make every space this much larger
                else:
                    spacing = 0  # keep normal space length
            top = height - pnt.y - self.y
            left = pnt.x + self.x
            if rot == 90:
                left = height - pnt.y - self.y
                top = -pnt.x - self.x
            elif rot == 270:
                left = -height + pnt.y + self.y
                top = pnt.x + self.x
            elif rot == 180:
                left = -pnt.x - self.x
                top = -height + pnt.y + self.y

            nres += templ(left, top, fname, fontsize)

            if render_mode > 0:
                nres += "%i Tr " % render_mode
                nres += _format_g(border_width * fontsize) + " w "
                if miter_limit is not None:
                    nres += _format_g(miter_limit) + " M "

            if align == 3:
                nres += _format_g(spacing) + " Tw "

            if color is not None:
                nres += color_str
            if fill is not None:
                nres += fill_str
            nres += "%sTJ\n" % getTJstr(t, tj_glyphs, simple, ordering)

        nres += "ET\n%sQ\n" % emc

        self.text_cont += nres
        self.updateRect(rect)
        return more

    def finish(
        self,
        width: float = 1,
        color: OptSeq = (0,),
        fill: OptSeq = None,
        lineCap: int = 0,
        lineJoin: int = 0,
        dashes: OptStr = None,
        even_odd: bool = False,
        morph: OptSeq = None,
        closePath: bool = True,
        fill_opacity: float = 1,
        stroke_opacity: float = 1,
        oc: int = 0,
    ) -> None:
        """Finish the current drawing segment.

        Notes:
            Apply colors, opacity, dashes, line style and width, or
            morphing. Also whether to close the path
            by connecting last to first point.
        """
        if self.draw_cont == "":  # treat empty contents as no-op
            return

        if width == 0:  # border color makes no sense then
            color = None
        elif color is None:  # vice versa
            width = 0
        # if color == None and fill == None:
        #     raise ValueError("at least one of 'color' or 'fill' must be given")
        color_str = ColorCode(color, "c")  # ensure proper color string
        fill_str = ColorCode(fill, "f")  # ensure proper fill string

        optcont = self.page._get_optional_content(oc)
        if optcont is not None:
            self.draw_cont = "/OC /%s BDC\n" % optcont + self.draw_cont
            emc = "EMC\n"
        else:
            emc = ""

        alpha = self.page._set_opacity(CA=stroke_opacity, ca=fill_opacity)
        if alpha is not None:
            self.draw_cont = "/%s gs\n" % alpha + self.draw_cont

        if width != 1 and width != 0:
            self.draw_cont += _format_g(width) + " w\n"

        if lineCap != 0:
            self.draw_cont = "%i J\n" % lineCap + self.draw_cont
        if lineJoin != 0:
            self.draw_cont = "%i j\n" % lineJoin + self.draw_cont

        if dashes not in (None, "", "[] 0"):
            self.draw_cont = "%s d\n" % dashes + self.draw_cont

        if closePath:
            self.draw_cont += "h\n"
            self.last_point = None

        if color is not None:
            self.draw_cont += color_str

        if fill is not None:
            self.draw_cont += fill_str
            if color is not None:
                if not even_odd:
                    self.draw_cont += "B\n"
                else:
                    self.draw_cont += "B*\n"
            else:
                if not even_odd:
                    self.draw_cont += "f\n"
                else:
                    self.draw_cont += "f*\n"
        else:
            self.draw_cont += "S\n"

        self.draw_cont += emc
        if CheckMorph(morph):
            m1 = Matrix(
                1, 0, 0, 1, morph[0].x + self.x, self.height - morph[0].y - self.y
            )
            mat = ~m1 * morph[1] * m1
            self.draw_cont = _format_g(JM_TUPLE(mat)) + " cm\n" + self.draw_cont

        self.totalcont += "\nq\n" + self.draw_cont + "Q\n"
        self.draw_cont = ""
        self.last_point = None
        return

    def commit(self, overlay: bool = True) -> None:
        """Update the page's /Contents object with Shape data.

        The argument controls whether data appear in foreground (default)
        or background.
        """
        CheckParent(self.page)  # doc may have died meanwhile
        self.totalcont += self.text_cont
        self.totalcont = self.totalcont.encode()

        if self.totalcont:
            if overlay:
                self.page.wrap_contents()  # ensure a balanced graphics state
            # make /Contents object with dummy stream
            xref = TOOLS._insert_contents(self.page, b" ", overlay)
            # update it with potential compression
            self.doc.update_stream(xref, self.totalcont)

        self.last_point = None  # clean up ...
        self.rect = None  #
        self.draw_cont = ""  # for potential ...
        self.text_cont = ""  # ...
        self.totalcont = ""  # re-use

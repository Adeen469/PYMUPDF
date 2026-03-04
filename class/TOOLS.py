"""
Class: fitz.TOOLS

Description:
We use @staticmethod to avoid the need to create an instance of this class.

Inheritance (MRO): TOOLS -> object

"""

import fitz

# ===== Methods and Attributes of fitz.TOOLS =====

# JM_annot_id_stem = 'fitz'  [str]

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

# fitz_config = {'base14': True, 'cbz': True, 'epub': True, 'html': True, 'icc': True, 'img': True, 'jpx': True, 'js  [dict]

# gen_id()  [function]

# glyph_cache_empty()  [function]
#     -> Empty the glyph cache.

# image_profile(stream, keep_image=0)  [function]
#     -> Metadata of an image binary stream.

# mupdf_display_errors(on=None)  [function]
#     -> Set MuPDF error display to True or False.

# mupdf_display_warnings(on=None)  [function]
#     -> Set MuPDF warnings display to True or False.

# mupdf_version()  [function]
#     -> Get version of MuPDF binary build.

# mupdf_warnings(reset=1)  [function]
#     -> Get the MuPDF warnings/errors with optional reset (default).

# reset_mupdf_warnings()  [function]

# set_aa_level(level)  [function]
#     -> Set anti-aliasing level.

# set_annot_stem(stem=None)  [function]

# set_font_width(doc, xref, width)  [function]

# set_graphics_min_line_width(min_line_width)  [function]
#     -> Set the graphics minimum line width.

# set_icc(on=0)  [function]
#     -> Set ICC color handling on or off.

# set_low_memory(on=None)  [function]
#     -> Set / unset MuPDF device caching.

# set_small_glyph_heights(on=None)  [function]
#     -> Set / unset small glyph heights.

# set_subset_fontnames(on=None)  [function]
#     -> Set / unset returning fontnames with their subset prefix.

# show_aa_level()  [function]
#     -> Show anti-aliasing values.

# store_maxsize()  [function]
#     -> MuPDF store size limit.

# store_shrink(percent)  [function]
#     -> Free 'percent' of current store size.

# store_size()  [function]
#     -> MuPDF current store size.

# unset_quad_corrections(on=None)  [function]
#     -> Set ascender / descender corrections on or off.


# ===== Source Code =====
class TOOLS:
    '''
    We use @staticmethod to avoid the need to create an instance of this class.
    '''

    def _derotate_matrix(page):
        if isinstance(page, mupdf.PdfPage):
            return JM_py_from_matrix(JM_derotate_page_matrix(page))
        else:
            return JM_py_from_matrix(mupdf.FzMatrix())

    @staticmethod
    def _fill_widget(annot, widget):
        val = JM_get_widget_properties(annot, widget)

        widget.rect = Rect(annot.rect)
        widget.xref = annot.xref
        widget.parent = annot.parent
        widget._annot = annot  # backpointer to annot object
        if not widget.script:
            widget.script = None
        if not widget.script_stroke:
            widget.script_stroke = None
        if not widget.script_format:
            widget.script_format = None
        if not widget.script_change:
            widget.script_change = None
        if not widget.script_calc:
            widget.script_calc = None
        if not widget.script_blur:
            widget.script_blur = None
        if not widget.script_focus:
            widget.script_focus = None
        return val

    @staticmethod
    def _get_all_contents(page):
        page = _as_pdf_page(page.this)
        res = JM_read_contents(page.obj())
        result = JM_BinFromBuffer( res)
        return result

    @staticmethod
    def _insert_contents(page, newcont, overlay=1):
        """Add bytes as a new /Contents object for a page, and return its xref."""
        pdfpage = _as_pdf_page(page, required=1)
        contbuf = JM_BufferFromBytes(newcont)
        xref = JM_insert_contents(pdfpage.doc(), pdfpage.obj(), contbuf, overlay)
        #fixme: pdfpage->doc->dirty = 1;
        return xref

    @staticmethod
    def _le_annot_parms(annot, p1, p2, fill_color):
        """Get common parameters for making annot line end symbols.

        Returns:
            m: matrix that maps p1, p2 to points L, P on the x-axis
            im: its inverse
            L, P: transformed p1, p2
            w: line width
            scol: stroke color string
            fcol: fill color store_shrink
            opacity: opacity string (gs command)
        """
        w = annot.border["width"]  # line width
        sc = annot.colors["stroke"]  # stroke color
        if not sc:  # black if missing
            sc = (0,0,0)
        scol = " ".join(map(str, sc)) + " RG\n"
        if fill_color:
            fc = fill_color
        else:
            fc = annot.colors["fill"]  # fill color
        if not fc:
            fc = (1,1,1)  # white if missing
        fcol = " ".join(map(str, fc)) + " rg\n"
        # nr = annot.rect
        np1 = p1                   # point coord relative to annot rect
        np2 = p2                   # point coord relative to annot rect
        m = Matrix(util_hor_matrix(np1, np2))  # matrix makes the line horizontal
        im = ~m                            # inverted matrix
        L = np1 * m                        # converted start (left) point
        R = np2 * m                        # converted end (right) point
        if 0 <= annot.opacity < 1:
            opacity = "/H gs\n"
        else:
            opacity = ""
        return m, im, L, R, w, scol, fcol, opacity

    @staticmethod
    def _le_butt(annot, p1, p2, lr, fill_color):
        """Make stream commands for butt line end symbol. "lr" denotes left (False) or right point.
        """
        m, im, L, R, w, scol, fcol, opacity = TOOLS._le_annot_parms(annot, p1, p2, fill_color)
        shift = 3
        d = shift * max(1, w)
        M = R if lr else L
        top = (M + (0, -d/2.)) * im
        bot = (M + (0, d/2.)) * im
        ap = "\nq\n%s%f %f m\n" % (opacity, top.x, top.y)
        ap += "%f %f l\n" % (bot.x, bot.y)
        ap += _format_g(w) + " w\n"
        ap += scol + "s\nQ\n"
        return ap

    @staticmethod
    def _le_circle(annot, p1, p2, lr, fill_color):
        """Make stream commands for circle line end symbol. "lr" denotes left (False) or right point.
        """
        m, im, L, R, w, scol, fcol, opacity = TOOLS._le_annot_parms(annot, p1, p2, fill_color)
        shift = 2.5             # 2*shift*width = length of square edge
        d = shift * max(1, w)
        M = R - (d/2., 0) if lr else L + (d/2., 0)
        r = Rect(M, M) + (-d, -d, d, d)         # the square
        ap = "q\n" + opacity + TOOLS._oval_string(r.tl * im, r.tr * im, r.br * im, r.bl * im)
        ap += _format_g(w) + " w\n"
        ap += scol + fcol + "b\nQ\n"
        return ap

    @staticmethod
    def _le_closedarrow(annot, p1, p2, lr, fill_color):
        """Make stream commands for closed arrow line end symbol. "lr" denotes left (False) or right point.
        """
        m, im, L, R, w, scol, fcol, opacity = TOOLS._le_annot_parms(annot, p1, p2, fill_color)
        shift = 2.5
        d = shift * max(1, w)
        p2 = R + (d/2., 0) if lr else L - (d/2., 0)
        p1 = p2 + (-2*d, -d) if lr else p2 + (2*d, -d)
        p3 = p2 + (-2*d, d) if lr else p2 + (2*d, d)
        p1 *= im
        p2 *= im
        p3 *= im
        ap = "\nq\n%s%f %f m\n" % (opacity, p1.x, p1.y)
        ap += "%f %f l\n" % (p2.x, p2.y)
        ap += "%f %f l\n" % (p3.x, p3.y)
        ap += _format_g(w) + " w\n"
        ap += scol + fcol + "b\nQ\n"
        return ap

    @staticmethod
    def _le_diamond(annot, p1, p2, lr, fill_color):
        """Make stream commands for diamond line end symbol. "lr" denotes left (False) or right point.
        """
        m, im, L, R, w, scol, fcol, opacity = TOOLS._le_annot_parms(annot, p1, p2, fill_color)
        shift = 2.5             # 2*shift*width = length of square edge
        d = shift * max(1, w)
        M = R - (d/2., 0) if lr else L + (d/2., 0)
        r = Rect(M, M) + (-d, -d, d, d)         # the square
        # the square makes line longer by (2*shift - 1)*width
        p = (r.tl + (r.bl - r.tl) * 0.5) * im
        ap = "q\n%s%f %f m\n" % (opacity, p.x, p.y)
        p = (r.tl + (r.tr - r.tl) * 0.5) * im
        ap += "%f %f l\n"   % (p.x, p.y)
        p = (r.tr + (r.br - r.tr) * 0.5) * im
        ap += "%f %f l\n"   % (p.x, p.y)
        p = (r.br + (r.bl - r.br) * 0.5) * im
        ap += "%f %f l\n"   % (p.x, p.y)
        ap += _format_g(w) + " w\n"
        ap += scol + fcol + "b\nQ\n"
        return ap

    @staticmethod
    def _le_openarrow(annot, p1, p2, lr, fill_color):
        """Make stream commands for open arrow line end symbol. "lr" denotes left (False) or right point.
        """
        m, im, L, R, w, scol, fcol, opacity = TOOLS._le_annot_parms(annot, p1, p2, fill_color)
        shift = 2.5
        d = shift * max(1, w)
        p2 = R + (d/2., 0) if lr else L - (d/2., 0)
        p1 = p2 + (-2*d, -d) if lr else p2 + (2*d, -d)
        p3 = p2 + (-2*d, d) if lr else p2 + (2*d, d)
        p1 *= im
        p2 *= im
        p3 *= im
        ap = "\nq\n%s%f %f m\n" % (opacity, p1.x, p1.y)
        ap += "%f %f l\n" % (p2.x, p2.y)
        ap += "%f %f l\n" % (p3.x, p3.y)
        ap += _format_g(w) + " w\n"
        ap += scol + "S\nQ\n"
        return ap

    @staticmethod
    def _le_rclosedarrow(annot, p1, p2, lr, fill_color):
        """Make stream commands for right closed arrow line end symbol. "lr" denotes left (False) or right point.
        """
        m, im, L, R, w, scol, fcol, opacity = TOOLS._le_annot_parms(annot, p1, p2, fill_color)
        shift = 2.5
        d = shift * max(1, w)
        p2 = R - (2*d, 0) if lr else L + (2*d, 0)
        p1 = p2 + (2*d, -d) if lr else p2 + (-2*d, -d)
        p3 = p2 + (2*d, d) if lr else p2 + (-2*d, d)
        p1 *= im
        p2 *= im
        p3 *= im
        ap = "\nq\n%s%f %f m\n" % (opacity, p1.x, p1.y)
        ap += "%f %f l\n" % (p2.x, p2.y)
        ap += "%f %f l\n" % (p3.x, p3.y)
        ap += _format_g(w) + " w\n"
        ap += scol + fcol + "b\nQ\n"
        return ap

    @staticmethod
    def _le_ropenarrow(annot, p1, p2, lr, fill_color):
        """Make stream commands for right open arrow line end symbol. "lr" denotes left (False) or right point.
        """
        m, im, L, R, w, scol, fcol, opacity = TOOLS._le_annot_parms(annot, p1, p2, fill_color)
        shift = 2.5
        d = shift * max(1, w)
        p2 = R - (d/3., 0) if lr else L + (d/3., 0)
        p1 = p2 + (2*d, -d) if lr else p2 + (-2*d, -d)
        p3 = p2 + (2*d, d) if lr else p2 + (-2*d, d)
        p1 *= im
        p2 *= im
        p3 *= im
        ap = "\nq\n%s%f %f m\n" % (opacity, p1.x, p1.y)
        ap += "%f %f l\n" % (p2.x, p2.y)
        ap += "%f %f l\n" % (p3.x, p3.y)
        ap += _format_g(w) + " w\n"
        ap += scol + fcol + "S\nQ\n"
        return ap

    @staticmethod
    def _le_slash(annot, p1, p2, lr, fill_color):
        """Make stream commands for slash line end symbol. "lr" denotes left (False) or right point.
        """
        m, im, L, R, w, scol, fcol, opacity = TOOLS._le_annot_parms(annot, p1, p2, fill_color)
        rw = 1.1547 * max(1, w) * 1.0         # makes rect diagonal a 30 deg inclination
        M = R if lr else L
        r = Rect(M.x - rw, M.y - 2 * w, M.x + rw, M.y + 2 * w)
        top = r.tl * im
        bot = r.br * im
        ap = "\nq\n%s%f %f m\n" % (opacity, top.x, top.y)
        ap += "%f %f l\n" % (bot.x, bot.y)
        ap += _format_g(w) + " w\n"
        ap += scol + "s\nQ\n"
        return ap

    @staticmethod
    def _le_square(annot, p1, p2, lr, fill_color):
        """Make stream commands for square line end symbol. "lr" denotes left (False) or right point.
        """
        m, im, L, R, w, scol, fcol, opacity = TOOLS._le_annot_parms(annot, p1, p2, fill_color)
        shift = 2.5             # 2*shift*width = length of square edge
        d = shift * max(1, w)
        M = R - (d/2., 0) if lr else L + (d/2., 0)
        r = Rect(M, M) + (-d, -d, d, d)         # the square
        # the square makes line longer by (2*shift - 1)*width
        p = r.tl * im
        ap = "q\n%s%f %f m\n" % (opacity, p.x, p.y)
        p = r.tr * im
        ap += "%f %f l\n"   % (p.x, p.y)
        p = r.br * im
        ap += "%f %f l\n"   % (p.x, p.y)
        p = r.bl * im
        ap += "%f %f l\n"   % (p.x, p.y)
        ap += _format_g(w) + " w\n"
        ap += scol + fcol + "b\nQ\n"
        return ap

    @staticmethod
    def _oval_string(p1, p2, p3, p4):
        """Return /AP string defining an oval within a 4-polygon provided as points
        """
        def bezier(p, q, r):
            f = "%f %f %f %f %f %f c\n"
            return f % (p.x, p.y, q.x, q.y, r.x, r.y)

        kappa = 0.55228474983              # magic number
        ml = p1 + (p4 - p1) * 0.5          # middle points ...
        mo = p1 + (p2 - p1) * 0.5          # for each ...
        mr = p2 + (p3 - p2) * 0.5          # polygon ...
        mu = p4 + (p3 - p4) * 0.5          # side
        ol1 = ml + (p1 - ml) * kappa       # the 8 bezier
        ol2 = mo + (p1 - mo) * kappa       # helper points
        or1 = mo + (p2 - mo) * kappa
        or2 = mr + (p2 - mr) * kappa
        ur1 = mr + (p3 - mr) * kappa
        ur2 = mu + (p3 - mu) * kappa
        ul1 = mu + (p4 - mu) * kappa
        ul2 = ml + (p4 - ml) * kappa
        # now draw, starting from middle point of left side
        ap = "%f %f m\n" % (ml.x, ml.y)
        ap += bezier(ol1, ol2, mo)
        ap += bezier(or1, or2, mr)
        ap += bezier(ur1, ur2, mu)
        ap += bezier(ul1, ul2, ml)
        return ap

    @staticmethod
    def _parse_da(annot):

        if g_use_extra:
            val = extra.Tools_parse_da( annot.this)
        else:
            def Tools__parse_da(annot):
                this_annot = annot.this
                assert isinstance(this_annot, mupdf.PdfAnnot)
                this_annot_obj = mupdf.pdf_annot_obj( this_annot)
                pdf = mupdf.pdf_get_bound_document( this_annot_obj)
                try:
                    da = mupdf.pdf_dict_get_inheritable( this_annot_obj, PDF_NAME('DA'))
                    if not da.m_internal:
                        trailer = mupdf.pdf_trailer(pdf)
                        da = mupdf.pdf_dict_getl(trailer,
                                PDF_NAME('Root'),
                                PDF_NAME('AcroForm'),
                                PDF_NAME('DA'),
                                )
                    da_str = mupdf.pdf_to_text_string(da)
                except Exception:
                    if g_exceptions_verbose:    exception_info()
                    return
                return da_str
            val = Tools__parse_da(annot)

        if not val:
            return ((0,), "", 0)
        font = "Helv"
        fsize = 12
        col = (0, 0, 0)
        dat = val.split()  # split on any whitespace
        for i, item in enumerate(dat):
            if item == "Tf":
                font = dat[i - 2][1:]
                fsize = float(dat[i - 1])
                dat[i] = dat[i-1] = dat[i-2] = ""
                continue
            if item == "g":            # unicolor text
                col = [(float(dat[i - 1]))]
                dat[i] = dat[i-1] = ""
                continue
            if item == "rg":           # RGB colored text
                col = [float(f) for f in dat[i - 3:i]]
                dat[i] = dat[i-1] = dat[i-2] = dat[i-3] = ""
                continue
            if item == "k":           # CMYK colored text
                col = [float(f) for f in dat[i - 4:i]]
                dat[i] = dat[i-1] = dat[i-2] = dat[i-3] = dat[i-4] = ""
                continue

        val = (col, font, fsize)
        return val

    @staticmethod
    def _reset_widget(annot):
        this_annot = annot
        this_annot_obj = mupdf.pdf_annot_obj(this_annot)
        pdf = mupdf.pdf_get_bound_document(this_annot_obj)
        mupdf.pdf_field_reset(pdf, this_annot_obj)

    @staticmethod
    def _rotate_matrix(page):
        pdfpage = page._pdf_page(required=False)
        if not pdfpage.m_internal:
            return JM_py_from_matrix(mupdf.FzMatrix())
        return JM_py_from_matrix(JM_rotate_page_matrix(pdfpage))

    @staticmethod
    def _save_widget(annot, widget):
        JM_set_widget_properties(annot, widget)

    def _update_da(annot, da_str):
        if g_use_extra:
            extra.Tools_update_da( annot.this, da_str)
        else:
            try:
                this_annot = annot.this
                assert isinstance(this_annot, mupdf.PdfAnnot)
                mupdf.pdf_dict_put_text_string(mupdf.pdf_annot_obj(this_annot), PDF_NAME('DA'), da_str)
                mupdf.pdf_dict_del(mupdf.pdf_annot_obj(this_annot), PDF_NAME('DS'))    # /* not supported */
                mupdf.pdf_dict_del(mupdf.pdf_annot_obj(this_annot), PDF_NAME('RC'))    # /* not supported */
            except Exception:
                if g_exceptions_verbose:    exception_info()
                return
            return
    
    @staticmethod
    def gen_id():
        global TOOLS_JM_UNIQUE_ID
        TOOLS_JM_UNIQUE_ID += 1
        return TOOLS_JM_UNIQUE_ID

    @staticmethod
    def glyph_cache_empty():
        '''
        Empty the glyph cache.
        '''
        mupdf.fz_purge_glyph_cache()

    @staticmethod
    def image_profile(stream, keep_image=0):
        '''
        Metadata of an image binary stream.
        '''
        return JM_image_profile(stream, keep_image)
    
    @staticmethod
    def mupdf_display_errors(on=None):
        '''
        Set MuPDF error display to True or False.
        '''
        global JM_mupdf_show_errors
        if on is not None:
            JM_mupdf_show_errors = bool(on)
        return JM_mupdf_show_errors

    @staticmethod
    def mupdf_display_warnings(on=None):
        '''
        Set MuPDF warnings display to True or False.
        '''
        global JM_mupdf_show_warnings
        if on is not None:
            JM_mupdf_show_warnings = bool(on)
        return JM_mupdf_show_warnings

    @staticmethod
    def mupdf_version():
        '''Get version of MuPDF binary build.'''
        return mupdf.FZ_VERSION

    @staticmethod
    def mupdf_warnings(reset=1):
        '''
        Get the MuPDF warnings/errors with optional reset (default).
        '''
        # Get any trailing `... repeated <N> times...` message.
        mupdf.fz_flush_warnings()
        ret = '\n'.join( JM_mupdf_warnings_store)
        if reset:
            TOOLS.reset_mupdf_warnings()
        return ret

    @staticmethod
    def reset_mupdf_warnings():
        global JM_mupdf_warnings_store
        JM_mupdf_warnings_store = list()
        
    @staticmethod
    def set_aa_level(level):
        '''
        Set anti-aliasing level.
        '''
        mupdf.fz_set_aa_level(level)
    
    @staticmethod
    def set_annot_stem( stem=None):
        global JM_annot_id_stem
        if stem is None:
            return JM_annot_id_stem
        len_ = len(stem) + 1
        if len_ > 50:
            len_ = 50
        JM_annot_id_stem = stem[:50]
        return JM_annot_id_stem

    @staticmethod
    def set_font_width(doc, xref, width):
        pdf = _as_pdf_document(doc, required=0)
        if not pdf.m_internal:
            return False
        font = mupdf.pdf_load_object(pdf, xref)
        dfonts = mupdf.pdf_dict_get(font, PDF_NAME('DescendantFonts'))
        if mupdf.pdf_is_array(dfonts):
            n = mupdf.pdf_array_len(dfonts)
            for i in range(n):
                dfont = mupdf.pdf_array_get(dfonts, i)
                warray = mupdf.pdf_new_array(pdf, 3)
                mupdf.pdf_array_push(warray, mupdf.pdf_new_int(0))
                mupdf.pdf_array_push(warray, mupdf.pdf_new_int(65535))
                mupdf.pdf_array_push(warray, mupdf.pdf_new_int(width))
                mupdf.pdf_dict_put(dfont, PDF_NAME('W'), warray)
        return True

    @staticmethod
    def set_graphics_min_line_width(min_line_width):
        '''
        Set the graphics minimum line width.
        '''
        mupdf.fz_set_graphics_min_line_width(min_line_width)

    @staticmethod
    def set_icc( on=0):
        """Set ICC color handling on or off."""
        if on:
            if mupdf.FZ_ENABLE_ICC:
                mupdf.fz_enable_icc()
            else:
                RAISEPY( "MuPDF built w/o ICC support",PyExc_ValueError)
        elif mupdf.FZ_ENABLE_ICC:
            mupdf.fz_disable_icc()
 
    @staticmethod
    def set_low_memory( on=None):
        """Set / unset MuPDF device caching."""
        if on is not None:
            _globals.no_device_caching = bool(on)
        return _globals.no_device_caching

    @staticmethod
    def set_small_glyph_heights(on=None):
        """Set / unset small glyph heights."""
        if on is not None:
            _globals.small_glyph_heights = bool(on)
            if g_use_extra:
                extra.set_small_glyph_heights(_globals.small_glyph_heights)
        return _globals.small_glyph_heights
    
    @staticmethod
    def set_subset_fontnames(on=None):
        '''
        Set / unset returning fontnames with their subset prefix.
        '''
        if on is not None:
            _globals.subset_fontnames = bool(on)
            if g_use_extra:
                extra.set_subset_fontnames(_globals.subset_fontnames)
        return _globals.subset_fontnames
    
    @staticmethod
    def show_aa_level():
        '''
        Show anti-aliasing values.
        '''
        return dict(
                graphics = mupdf.fz_graphics_aa_level(),
                text = mupdf.fz_text_aa_level(),
                graphics_min_line_width = mupdf.fz_graphics_min_line_width(),
                )

    @staticmethod
    def store_maxsize():
        '''
        MuPDF store size limit.
        '''
        # fixme: return gctx->store->max.
        return None

    @staticmethod
    def store_shrink(percent):
        '''
        Free 'percent' of current store size.
        '''
        if percent >= 100:
            mupdf.fz_empty_store()
            return 0
        if percent > 0:
            mupdf.fz_shrink_store( 100 - percent)
        # fixme: return gctx->store->size.
    
    @staticmethod
    def store_size():
        '''
        MuPDF current store size.
        '''
        # fixme: return gctx->store->size.
        return None
    
    @staticmethod
    def unset_quad_corrections(on=None):
        '''
        Set ascender / descender corrections on or off.
        '''
        if on is not None:
            _globals.skip_quad_corrections = bool(on)
            if g_use_extra:
                extra.set_skip_quad_corrections(_globals.skip_quad_corrections)
        return _globals.skip_quad_corrections

    # fixme: also defined at top-level.
    JM_annot_id_stem = 'fitz'

    fitz_config = JM_fitz_config()

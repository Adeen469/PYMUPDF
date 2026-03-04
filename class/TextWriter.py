"""
Class: fitz.TextWriter

Description: No docstring available.

Inheritance (MRO): TextWriter -> object

"""

import fitz

# ===== Methods and Attributes of fitz.TextWriter =====

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, page_rect, opacity=1, color=None)  [function]
#     -> Stores text spans for later output on compatible PDF pages.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self, /)  [wrapper_descriptor]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# append(self, pos, text, font=None, fontsize=11, language=None, right_to_left=0, small_caps=0)  [function]
#     -> Store 'text' at point 'pos' using 'font' and 'fontsize'.

# appendv(self, pos, text, font=None, fontsize=11, language=None, small_caps=False)  [function]

# clean_rtl(self, text)  [function]
#     -> Revert the sequence of Latin text parts.

# fill_textbox(writer: 'TextWriter', rect: 'rect_like', text: Union[str, list], pos: 'point_like' = None, font: Optional[pymupdf.Font] = None, fontsize: float = 11, lineheight: Optional[float] = None, align: int = 0, warn: bool = None, right_to_left: bool = False, small_caps: bool = False) -> tuple  [function]
#     -> Fill a rectangle with text.

# write_text(self, page, color=None, opacity=-1, overlay=1, morph=None, matrix=None, render_mode=0, oc=0)  [function]
#     -> Write the text to a PDF page having the TextWriter's page size.


# ===== Source Code =====
class TextWriter:

    def __init__(self, page_rect, opacity=1, color=None):
        """Stores text spans for later output on compatible PDF pages."""
        self.this = mupdf.fz_new_text()

        self.opacity = opacity
        self.color = color
        self.rect = Rect(page_rect)
        self.ctm = Matrix(1, 0, 0, -1, 0, self.rect.height)
        self.ictm = ~self.ctm
        self.last_point = Point()
        self.last_point.__doc__ = "Position following last text insertion."
        self.text_rect = Rect()
        
        self.text_rect.__doc__ = "Accumulated area of text spans."
        self.used_fonts = set()
        self.thisown = True

    @property
    def _bbox(self):
        val = JM_py_from_rect( mupdf.fz_bound_text( self.this, mupdf.FzStrokeState(None), mupdf.FzMatrix()))
        val = Rect(val)
        return val

    def append(self, pos, text, font=None, fontsize=11, language=None, right_to_left=0, small_caps=0):
        """Store 'text' at point 'pos' using 'font' and 'fontsize'."""
        pos = Point(pos) * self.ictm
        #log( '{font=}')
        if font is None:
            font = Font("helv")
        if not font.is_writable:
            if 0:
                log( '{font.this.m_internal.name=}')
                log( '{font.this.m_internal.t3matrix=}')
                log( '{font.this.m_internal.bbox=}')
                log( '{font.this.m_internal.glyph_count=}')
                log( '{font.this.m_internal.use_glyph_bbox=}')
                log( '{font.this.m_internal.width_count=}')
                log( '{font.this.m_internal.width_default=}')
                log( '{font.this.m_internal.has_digest=}')
                log( 'Unsupported font {font.name=}')
                if mupdf_cppyy:
                    import cppyy
                    log( f'Unsupported font {cppyy.gbl.mupdf_font_name(font.this.m_internal)=}')
            raise ValueError("Unsupported font '%s'." % font.name)
        if right_to_left:
            text = self.clean_rtl(text)
            text = "".join(reversed(text))
            right_to_left = 0

        lang = mupdf.fz_text_language_from_string(language)
        p = JM_point_from_py(pos)
        trm = mupdf.fz_make_matrix(fontsize, 0, 0, fontsize, p.x, p.y)
        markup_dir = 0
        wmode = 0
        if small_caps == 0:
            trm = mupdf.fz_show_string( self.this, font.this, trm, text, wmode, right_to_left, markup_dir, lang)
        else:
            trm = JM_show_string_cs( self.this, font.this, trm, text, wmode, right_to_left, markup_dir, lang)
        val = JM_py_from_matrix(trm)

        self.last_point = Point(val[-2:]) * self.ctm
        self.text_rect = self._bbox * self.ctm
        val = self.text_rect, self.last_point
        if font.flags["mono"] == 1:
            self.used_fonts.add(font)
        return val

    def appendv(self, pos, text, font=None, fontsize=11, language=None, small_caps=False):
        lheight = fontsize * 1.2
        for c in text:
            self.append(pos, c, font=font, fontsize=fontsize,
                language=language, small_caps=small_caps)
            pos.y += lheight
        return self.text_rect, self.last_point

    def clean_rtl(self, text):
        """Revert the sequence of Latin text parts.

        Text with right-to-left writing direction (Arabic, Hebrew) often
        contains Latin parts, which are written in left-to-right: numbers, names,
        etc. For output as PDF text we need *everything* in right-to-left.
        E.g. an input like "<arabic> ABCDE FG HIJ <arabic> KL <arabic>" will be
        converted to "<arabic> JIH GF EDCBA <arabic> LK <arabic>". The Arabic
        parts remain untouched.

        Args:
            text: str
        Returns:
            Massaged string.
        """
        if not text:
            return text
        # split into words at space boundaries
        words = text.split(" ")
        idx = []
        for i in range(len(words)):
            w = words[i]
        # revert character sequence for Latin only words
            if not (len(w) < 2 or max([ord(c) for c in w]) > 255):
                words[i] = "".join(reversed(w))
                idx.append(i)  # stored index of Latin word

        # adjacent Latin words must revert their sequence, too
        idx2 = []  # store indices of adjacent Latin words
        for i in range(len(idx)):
            if idx2 == []:  # empty yet?
                idx2.append(idx[i]) # store Latin word number

            elif idx[i] > idx2[-1] + 1:  # large gap to last?
                if len(idx2) > 1:  # at least two consecutives?
                    words[idx2[0] : idx2[-1] + 1] = reversed(
                        words[idx2[0] : idx2[-1] + 1]
                    )  # revert their sequence
                idx2 = [idx[i]]  # re-initialize

            elif idx[i] == idx2[-1] + 1:  # new adjacent Latin word
                idx2.append(idx[i])

        text = " ".join(words)
        return text

    def fill_textbox(
            writer: 'TextWriter',
            rect: rect_like,
            text: typing.Union[str, list],
            pos: point_like = None,
            font: typing.Optional[Font] = None,
            fontsize: float = 11,
            lineheight: OptFloat = None,
            align: int = 0,
            warn: bool = None,
            right_to_left: bool = False,
            small_caps: bool = False,
            ) -> tuple:
        """Fill a rectangle with text.

        Args:
            writer: pymupdf.TextWriter object (= "self")
            rect: rect-like to receive the text.
            text: string or list/tuple of strings.
            pos: point-like start position of first word.
            font: pymupdf.Font object (default pymupdf.Font('helv')).
            fontsize: the fontsize.
            lineheight: overwrite the font property
            align: (int) 0 = left, 1 = center, 2 = right, 3 = justify
            warn: (bool) text overflow action: none, warn, or exception
            right_to_left: (bool) indicate right-to-left language.
        """
        rect = Rect(rect)
        if rect.is_empty:
            raise ValueError("fill rect must not empty.")
        if type(font) is not Font:
            font = Font("helv")

        def textlen(x):
            """Return length of a string."""
            return font.text_length(
                x, fontsize=fontsize, small_caps=small_caps
            )  # abbreviation

        def char_lengths(x):
            """Return list of single character lengths for a string."""
            return font.char_lengths(x, fontsize=fontsize, small_caps=small_caps)

        def append_this(pos, text):
            ret = writer.append(
                    pos, text, font=font, fontsize=fontsize, small_caps=small_caps
                    )
            return ret

        tolerance = fontsize * 0.2  # extra distance to left border
        space_len = textlen(" ")
        std_width = rect.width - tolerance
        std_start = rect.x0 + tolerance

        def norm_words(width, words):
            """Cut any word in pieces no longer than 'width'."""
            nwords = []
            word_lengths = []
            for w in words:
                wl_lst = char_lengths(w)
                wl = sum(wl_lst)
                if wl <= width:  # nothing to do - copy over
                    nwords.append(w)
                    word_lengths.append(wl)
                    continue

                # word longer than rect width - split it in parts
                n = len(wl_lst)
                while n > 0:
                    wl = sum(wl_lst[:n])
                    if wl <= width:
                        nwords.append(w[:n])
                        word_lengths.append(wl)
                        w = w[n:]
                        wl_lst = wl_lst[n:]
                        n = len(wl_lst)
                    else:
                        n -= 1
            return nwords, word_lengths

        def output_justify(start, line):
            """Justified output of a line."""
            # ignore leading / trailing / multiple spaces
            words = [w for w in line.split(" ") if w != ""]
            nwords = len(words)
            if nwords == 0:
                return
            if nwords == 1:  # single word cannot be justified
                append_this(start, words[0])
                return
            tl = sum([textlen(w) for w in words])  # total word lengths
            gaps = nwords - 1  # number of word gaps
            gapl = (std_width - tl) / gaps  # width of each gap
            for w in words:
                _, lp = append_this(start, w)  # output one word
                start.x = lp.x + gapl  # next start at word end plus gap
            return

        asc = font.ascender
        dsc = font.descender
        if not lineheight:
            if asc - dsc <= 1:
                lheight = 1.2
            else:
                lheight = asc - dsc
        else:
            lheight = lineheight

        LINEHEIGHT = fontsize * lheight  # effective line height
        width = std_width  # available horizontal space

        # starting point of text
        if pos is not None:
            pos = Point(pos)
        else:  # default is just below rect top-left
            pos = rect.tl + (tolerance, fontsize * asc)
        if pos not in rect:
            raise ValueError("Text must start in rectangle.")

        # calculate displacement factor for alignment
        if align == TEXT_ALIGN_CENTER:
            factor = 0.5
        elif align == TEXT_ALIGN_RIGHT:
            factor = 1.0
        else:
            factor = 0

        # split in lines if just a string was given
        if type(text) is str:
            textlines = text.splitlines()
        else:
            textlines = []
            for line in text:
                textlines.extend(line.splitlines())

        max_lines = int((rect.y1 - pos.y) / LINEHEIGHT) + 1

        new_lines = []  # the final list of textbox lines
        no_justify = []  # no justify for these line numbers
        for i, line in enumerate(textlines):
            if line in ("", " "):
                new_lines.append((line, space_len))
                width = rect.width - tolerance
                no_justify.append((len(new_lines) - 1))
                continue
            if i == 0:
                width = rect.x1 - pos.x
            else:
                width = rect.width - tolerance

            if right_to_left:  # reverses Arabic / Hebrew text front to back
                line = writer.clean_rtl(line)
            tl = textlen(line)
            if tl <= width:  # line short enough
                new_lines.append((line, tl))
                no_justify.append((len(new_lines) - 1))
                continue

            # we need to split the line in fitting parts
            words = line.split(" ")  # the words in the line

            # cut in parts any words that are longer than rect width
            words, word_lengths = norm_words(width, words)

            n = len(words)
            while True:
                line0 = " ".join(words[:n])
                wl = sum(word_lengths[:n]) + space_len * (n - 1)
                if wl <= width:
                    new_lines.append((line0, wl))
                    words = words[n:]
                    word_lengths = word_lengths[n:]
                    n = len(words)
                    line0 = None
                else:
                    n -= 1

                if len(words) == 0:
                    break
                assert n

        # -------------------------------------------------------------------------
        # List of lines created. Each item is (text, tl), where 'tl' is the PDF
        # output length (float) and 'text' is the text. Except for justified text,
        # this is output-ready.
        # -------------------------------------------------------------------------
        nlines = len(new_lines)
        if nlines > max_lines:
            msg = "Only fitting %i of %i lines." % (max_lines, nlines)
            if warn is None:
                pass
            elif warn:
                message("Warning: " + msg)
            else:
                raise ValueError(msg)

        start = Point()
        no_justify += [len(new_lines) - 1]  # no justifying of last line
        for i in range(max_lines):
            try:
                line, tl = new_lines.pop(0)
            except IndexError:
                if g_exceptions_verbose >= 2:   exception_info()
                break

            if right_to_left:  # Arabic, Hebrew
                line = "".join(reversed(line))

            if i == 0:  # may have different start for first line
                start = pos

            if align == TEXT_ALIGN_JUSTIFY and i not in no_justify and tl < std_width:
                output_justify(start, line)
                start.x = std_start
                start.y += LINEHEIGHT
                continue

            if i > 0 or pos.x == std_start:  # left, center, right alignments
                start.x += (width - tl) * factor

            append_this(start, line)
            start.x = std_start
            start.y += LINEHEIGHT

        return new_lines  # return non-written lines

    def write_text(self, page, color=None, opacity=-1, overlay=1, morph=None, matrix=None, render_mode=0, oc=0):
        """Write the text to a PDF page having the TextWriter's page size.

        Args:
            page: a PDF page having same size.
            color: override text color.
            opacity: override transparency.
            overlay: put in foreground or background.
            morph: tuple(Point, Matrix), apply a matrix with a fixpoint.
            matrix: Matrix to be used instead of 'morph' argument.
            render_mode: (int) PDF render mode operator 'Tr'.
        """
        CheckParent(page)
        if abs(self.rect - page.rect) > 1e-3:
            raise ValueError("incompatible page rect")
        if morph is not None:
            if (type(morph) not in (tuple, list)
                    or type(morph[0]) is not Point
                    or type(morph[1]) is not Matrix
                    ):
                raise ValueError("morph must be (Point, Matrix) or None")
        if matrix is not None and morph is not None:
            raise ValueError("only one of matrix, morph is allowed")
        if getattr(opacity, "__float__", None) is None or opacity == -1:
            opacity = self.opacity
        if color is None:
            color = self.color

        if 1:
            pdfpage = page._pdf_page()
            alpha = 1
            if opacity >= 0 and opacity < 1:
                alpha = opacity
            ncol = 1
            dev_color = [0, 0, 0, 0]
            if color:
                ncol, dev_color = JM_color_FromSequence(color)
            if ncol == 3:
                colorspace = mupdf.fz_device_rgb()
            elif ncol == 4:
                colorspace = mupdf.fz_device_cmyk()
            else:
                colorspace = mupdf.fz_device_gray()

            resources = mupdf.pdf_new_dict(pdfpage.doc(), 5)
            contents = mupdf.fz_new_buffer(1024)
            dev = mupdf.pdf_new_pdf_device( pdfpage.doc(), mupdf.FzMatrix(), resources, contents)
            #log( '=== {dev_color!r=}')
            mupdf.fz_fill_text(
                    dev,
                    self.this,
                    mupdf.FzMatrix(),
                    colorspace,
                    dev_color,
                    alpha,
                    mupdf.FzColorParams(mupdf.fz_default_color_params),
                    )
            mupdf.fz_close_device( dev)

            # copy generated resources into the one of the page
            max_nums = JM_merge_resources( pdfpage, resources)
            cont_string = JM_EscapeStrFromBuffer( contents)
            result = (max_nums, cont_string)
            val = result

        max_nums = val[0]
        content = val[1]
        max_alp, max_font = max_nums
        old_cont_lines = content.splitlines()

        optcont = page._get_optional_content(oc)
        if optcont is not None:
            bdc = "/OC /%s BDC" % optcont
            emc = "EMC"
        else:
            bdc = emc = ""

        new_cont_lines = ["q"]
        if bdc:
            new_cont_lines.append(bdc)

        cb = page.cropbox_position
        if page.rotation in (90, 270):
            delta = page.rect.height - page.rect.width
        else:
            delta = 0
        mb = page.mediabox
        if bool(cb) or mb.y0 != 0 or delta != 0:
            new_cont_lines.append(f"1 0 0 1 {_format_g((cb.x, cb.y + mb.y0 - delta))} cm")

        if morph:
            p = morph[0] * self.ictm
            delta = Matrix(1, 1).pretranslate(p.x, p.y)
            matrix = ~delta * morph[1] * delta
        if morph or matrix:
            new_cont_lines.append(_format_g(JM_TUPLE(matrix)) + " cm")

        for line in old_cont_lines:
            if line.endswith(" cm"):
                continue
            if line == "BT":
                new_cont_lines.append(line)
                new_cont_lines.append("%i Tr" % render_mode)
                continue
            if line.endswith(" gs"):
                alp = int(line.split()[0][4:]) + max_alp
                line = "/Alp%i gs" % alp
            elif line.endswith(" Tf"):
                temp = line.split()
                fsize = float(temp[1])
                if render_mode != 0:
                    w = fsize * 0.05
                else:
                    w = 1
                new_cont_lines.append(_format_g(w) + " w")
                font = int(temp[0][2:]) + max_font
                line = " ".join(["/F%i" % font] + temp[1:])
            elif line.endswith(" rg"):
                new_cont_lines.append(line.replace("rg", "RG"))
            elif line.endswith(" g"):
                new_cont_lines.append(line.replace(" g", " G"))
            elif line.endswith(" k"):
                new_cont_lines.append(line.replace(" k", " K"))
            new_cont_lines.append(line)
        if emc:
            new_cont_lines.append(emc)
        new_cont_lines.append("Q\n")
        content = "\n".join(new_cont_lines).encode("utf-8")
        TOOLS._insert_contents(page, content, overlay=overlay)
        val = None
        for font in self.used_fonts:
            repair_mono_font(page, font)
        return val

"""
Class: fitz.Pixmap

Description: No docstring available.

Inheritance (MRO): Pixmap -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Pixmap =====

# __del__(self)  [function]

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, *args)  [function]
#     -> Pixmap(colorspace, irect, alpha) - empty pixmap.

# __len__(self)  [function]

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self)  [function]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# alpha = <property object at 0x000002052DE33010>  [property]

# clear_with(self, value=None, bbox=None)  [function]
#     -> Fill all color components with same value.

# color_count(self, colors=0, clip=None)  [function]
#     -> Return count of each color.

# color_topusage(self, clip=None)  [function]
#     -> Return most frequent color and its usage ratio.

# colorspace = <property object at 0x000002052DE33060>  [property]

# copy(self, src, bbox)  [function]
#     -> Copy bbox from another Pixmap.

# digest = <property object at 0x000002052DE330B0>  [property]

# gamma_with(self, gamma)  [function]
#     -> Apply correction with some float.

# h = <property object at 0x000002052DE33100>  [property]

# height = <property object at 0x000002052DE33100>  [property]

# invert_irect(self, bbox=None)  [function]
#     -> Invert the colors inside a bbox.

# irect = <property object at 0x000002052DE33150>  [property]

# is_monochrome = <property object at 0x000002052DE331A0>  [property]

# is_unicolor = <property object at 0x000002052DE331F0>  [property]

# n = <property object at 0x000002052DE33240>  [property]

# pdfocr_save(self, filename, compress=1, language=None, tessdata=None)  [function]
#     -> Save pixmap as an OCR-ed PDF page.

# pdfocr_tobytes(self, compress=True, language='eng', tessdata=None)  [function]
#     -> Save pixmap as an OCR-ed PDF page.

# pil_image(self)  [function]
#     -> Create a Pillow Image from the Pixmap.

# pil_save(self, *args, **kwargs)  [function]
#     -> Write to image file using Pillow.

# pil_tobytes(self, *args, **kwargs)  [function]
#     -> Convert to an image in memory using Pillow.

# pixel(self, x, y)  [function]
#     -> Get color tuple of pixel (x, y).

# samples = <property object at 0x000002052DE33290>  [property]

# samples_mv = <property object at 0x000002052DE332E0>  [property]

# samples_ptr = <property object at 0x000002052DE33330>  [property]

# save(self, filename, output=None, jpg_quality=95)  [function]
#     -> Output as image in format determined by filename extension.

# set_alpha(self, alphavalues=None, premultiply=1, opaque=None, matte=None)  [function]
#     -> Set alpha channel to values contained in a byte array.

# set_dpi(self, xres, yres)  [function]
#     -> Set resolution in both dimensions.

# set_origin(self, x, y)  [function]
#     -> Set top-left coordinates.

# set_pixel(self, x, y, color)  [function]
#     -> Set color of pixel (x, y).

# set_rect(self, bbox, color)  [function]
#     -> Set color of all pixels in bbox.

# shrink(self, factor)  [function]
#     -> Divide width and height by 2**factor.

# size = <property object at 0x000002052DE33380>  [property]

# stride = <property object at 0x000002052DE333D0>  [property]

# tint_with(self, black, white)  [function]
#     -> Tint colors with modifiers for black and white.

# tobytes(self, output='png', jpg_quality=95)  [function]
#     -> Convert to binary image stream of desired type.

# w = <property object at 0x000002052DE33420>  [property]

# warp(self, quad, width, height)  [function]
#     -> Return pixmap from a warped quad.

# width = <property object at 0x000002052DE33420>  [property]

# x = <property object at 0x000002052DE33470>  [property]

# xres = <property object at 0x000002052DE334C0>  [property]

# y = <property object at 0x000002052DE33510>  [property]

# yres = <property object at 0x000002052DE33560>  [property]


# ===== Source Code =====
class Pixmap:

    def __init__(self, *args):
        """
        Pixmap(colorspace, irect, alpha) - empty pixmap.
        Pixmap(colorspace, src) - copy changing colorspace.
        Pixmap(src, width, height,[clip]) - scaled copy, float dimensions.
        Pixmap(src, alpha=1) - copy and add or drop alpha channel.
        Pixmap(filename) - from an image in a file.
        Pixmap(image) - from an image in memory (bytes).
        Pixmap(colorspace, width, height, samples, alpha) - from samples data.
        Pixmap(PDFdoc, xref) - from an image at xref in a PDF document.
        """
        # Cache for property `self.samples_mv`. Set here so __del_() sees it if
        # we raise.
        #
        self._samples_mv = None

        # 2024-01-16: Experimental support for a memory-view of the underlying
        # data.  Doesn't seem to make much difference to Pixmap.set_pixel() so
        # not currently used.
        self._memory_view = None
        
        if 0:
            pass

        elif args_match(args,
                (Colorspace, mupdf.FzColorspace),
                (mupdf.FzRect, mupdf.FzIrect, IRect, Rect, tuple)
                ):
            # create empty pixmap with colorspace and IRect
            cs, rect = args
            alpha = 0
            pm = mupdf.fz_new_pixmap_with_bbox(cs, JM_irect_from_py(rect), mupdf.FzSeparations(0), alpha)
            self.this = pm

        elif args_match(args,
                (Colorspace, mupdf.FzColorspace),
                (mupdf.FzRect, mupdf.FzIrect, IRect, Rect, tuple),
                (int, bool)
                ):
            # create empty pixmap with colorspace and IRect
            cs, rect, alpha = args
            pm = mupdf.fz_new_pixmap_with_bbox(cs, JM_irect_from_py(rect), mupdf.FzSeparations(0), alpha)
            self.this = pm

        elif args_match(args, (Colorspace, mupdf.FzColorspace, type(None)), (Pixmap, mupdf.FzPixmap)):
            # copy pixmap, converting colorspace
            cs, spix = args
            if isinstance(cs, Colorspace):
                cs = cs.this
            elif cs is None:
                cs = mupdf.FzColorspace(None)
            if isinstance(spix, Pixmap):
                spix = spix.this
            if not mupdf.fz_pixmap_colorspace(spix).m_internal:
                raise ValueError( "source colorspace must not be None")
            
            if cs.m_internal:
                self.this = mupdf.fz_convert_pixmap(
                        spix,
                        cs,
                        mupdf.FzColorspace(),
                        mupdf.FzDefaultColorspaces(None),
                        mupdf.FzColorParams(),
                        1
                        )
            else:
                self.this = mupdf.fz_new_pixmap_from_alpha_channel( spix)
                if not self.this.m_internal:
                    raise RuntimeError( MSG_PIX_NOALPHA)

        elif args_match(args, (Pixmap, mupdf.FzPixmap), (Pixmap, mupdf.FzPixmap)):
            # add mask to a pixmap w/o alpha channel
            spix, mpix = args
            if isinstance(spix, Pixmap):
                spix = spix.this
            if isinstance(mpix, Pixmap):
                mpix = mpix.this
            spm = spix
            mpm = mpix
            if not spix.m_internal: # intercept NULL for spix: make alpha only pix
                dst = mupdf.fz_new_pixmap_from_alpha_channel(mpm)
                if not dst.m_internal:
                    raise RuntimeError( MSG_PIX_NOALPHA)
            else:
                dst = mupdf.fz_new_pixmap_from_color_and_mask(spm, mpm)
            self.this = dst

        elif (args_match(args, (Pixmap, mupdf.FzPixmap), (float, int), (float, int), None) or
             args_match(args, (Pixmap, mupdf.FzPixmap), (float, int), (float, int))):
            # create pixmap as scaled copy of another one
            if len(args) == 3:
                spix, w, h = args
                bbox = mupdf.FzIrect(mupdf.fz_infinite_irect)
            else:
                spix, w, h, clip = args
                bbox = JM_irect_from_py(clip)
        
            src_pix = spix.this if isinstance(spix, Pixmap) else spix
            if not mupdf.fz_is_infinite_irect(bbox):
                pm = mupdf.fz_scale_pixmap(src_pix, src_pix.x(), src_pix.y(), w, h, bbox)
            else:
                pm = mupdf.fz_scale_pixmap(src_pix, src_pix.x(), src_pix.y(), w, h, mupdf.FzIrect(mupdf.fz_infinite_irect))
            self.this = pm

        elif args_match(args, str, (Pixmap, mupdf.FzPixmap)) and args[0] == 'raw':
            # Special raw construction where we set .this directly.
            _, pm = args
            if isinstance(pm, Pixmap):
                pm = pm.this
            self.this = pm

        elif args_match(args, (Pixmap, mupdf.FzPixmap), (int, None)):
            # Pixmap(struct Pixmap *spix, int alpha=1)
            # copy pixmap & add / drop the alpha channel
            spix = args[0]
            alpha = args[1] if len(args) == 2 else 1
            src_pix = spix.this if isinstance(spix, Pixmap) else spix
            if not _INRANGE(alpha, 0, 1):
                raise ValueError( "bad alpha value")
            cs = mupdf.fz_pixmap_colorspace(src_pix)
            if not cs.m_internal and not alpha:
                raise ValueError( "cannot drop alpha for 'NULL' colorspace")
            seps = mupdf.FzSeparations()
            n = mupdf.fz_pixmap_colorants(src_pix)
            w = mupdf.fz_pixmap_width(src_pix)
            h = mupdf.fz_pixmap_height(src_pix)
            pm = mupdf.fz_new_pixmap(cs, w, h, seps, alpha)
            pm.m_internal.x = src_pix.m_internal.x
            pm.m_internal.y = src_pix.m_internal.y
            pm.m_internal.xres = src_pix.m_internal.xres
            pm.m_internal.yres = src_pix.m_internal.yres

            # copy samples data ------------------------------------------
            if 1:
                # We use our pixmap_copy() to get best performance.
                # test_pixmap.py:test_setalpha(): 3.9s t=0.0062
                extra.pixmap_copy( pm.m_internal, src_pix.m_internal, n)
            elif 1:
                # Use memoryview.
                # test_pixmap.py:test_setalpha(): 4.6 t=0.51
                src_view = mupdf.fz_pixmap_samples_memoryview( src_pix)
                pm_view = mupdf.fz_pixmap_samples_memoryview( pm)
                if src_pix.alpha() == pm.alpha():   # identical samples
                    #memcpy(tptr, sptr, w * h * (n + alpha));
                    size = w * h * (n + alpha)
                    pm_view[ 0 : size] = src_view[ 0 : size]
                else:
                    tptr = 0
                    sptr = 0
                    # This is a little faster than calling
                    # pm.fz_samples_set(), but still quite slow. E.g. reduces
                    # test_pixmap.py:test_setalpha() from 6.7s to 4.5s.
                    #
                    # t=0.53
                    pm_stride = pm.stride()
                    pm_n = pm.n()
                    pm_alpha = pm.alpha()
                    src_stride = src_pix.stride()
                    src_n = src_pix.n()
                    #log( '{=pm_stride pm_n src_stride src_n}')
                    for y in range( h):
                        for x in range( w):
                            pm_i = pm_stride * y + pm_n * x
                            src_i = src_stride * y + src_n * x
                            pm_view[ pm_i : pm_i + n] = src_view[ src_i : src_i + n]
                            if pm_alpha:
                                pm_view[ pm_i + n] = 255
            else:
                # Copy individual bytes from Python. Very slow.
                # test_pixmap.py:test_setalpha(): 6.89 t=2.601
                if src_pix.alpha() == pm.alpha():   # identical samples
                    #memcpy(tptr, sptr, w * h * (n + alpha));
                    for i in range(w * h * (n + alpha)):
                        mupdf.fz_samples_set(pm, i, mupdf.fz_samples_get(src_pix, i))
                else:
                    # t=2.56
                    tptr = 0
                    sptr = 0
                    src_pix_alpha = src_pix.alpha()
                    for i in range(w * h):
                        #memcpy(tptr, sptr, n);
                        for j in range(n):
                            mupdf.fz_samples_set(pm, tptr + j, mupdf.fz_samples_get(src_pix, sptr + j))
                        tptr += n
                        if pm.alpha():
                            mupdf.fz_samples_set(pm, tptr, 255)
                            tptr += 1
                        sptr += n + src_pix_alpha
            self.this = pm

        elif args_match(args, (mupdf.FzColorspace, Colorspace), int, int, None, (int, bool)):
            # create pixmap from samples data
            cs, w, h, samples, alpha = args
            if isinstance(cs, Colorspace):
                cs = cs.this
                assert isinstance(cs, mupdf.FzColorspace)
            n = mupdf.fz_colorspace_n(cs)
            stride = (n + alpha) * w
            seps = mupdf.FzSeparations()
            pm = mupdf.fz_new_pixmap(cs, w, h, seps, alpha)

            if isinstance( samples, (bytes, bytearray)):
                #log('using mupdf.python_buffer_data()')
                samples2 = mupdf.python_buffer_data(samples)
                size = len(samples)
            else:
                res = JM_BufferFromBytes(samples)
                if not res.m_internal:
                    raise ValueError( "bad samples data")
                size, c = mupdf.fz_buffer_storage(res)
                samples2 = mupdf.python_buffer_data(samples) # raw swig proxy for `const unsigned char*`.
            if stride * h != size:
                raise ValueError( f"bad samples length {w=} {h=} {alpha=} {n=} {stride=} {size=}")
            mupdf.ll_fz_pixmap_copy_raw( pm.m_internal, samples2)
            self.this = pm

        elif args_match(args, None):
            # create pixmap from filename, file object, pathlib.Path or memory
            imagedata, = args
            name = 'name'
            if hasattr(imagedata, "resolve"):
                fname = imagedata.__str__()
                if fname:
                    img = mupdf.fz_new_image_from_file(fname)
            elif hasattr(imagedata, name):
                fname = imagedata.name
                if fname:
                    img = mupdf.fz_new_image_from_file(fname)
            elif isinstance(imagedata, str):
                img = mupdf.fz_new_image_from_file(imagedata)
            else:
                res = JM_BufferFromBytes(imagedata)
                if not res.m_internal or not res.m_internal.len:
                    raise ValueError( "bad image data")
                img = mupdf.fz_new_image_from_buffer(res)

            # Original code passed null for subarea and ctm, but that's not
            # possible with MuPDF's python bindings. The equivalent is an
            # infinite rect and identify matrix scaled by img.w() and img.h().
            pm, w, h = mupdf.fz_get_pixmap_from_image(
                    img,
                    mupdf.FzIrect(FZ_MIN_INF_RECT, FZ_MIN_INF_RECT, FZ_MAX_INF_RECT, FZ_MAX_INF_RECT),
                    mupdf.FzMatrix( img.w(), 0, 0, img.h(), 0, 0),
                    )
            xres, yres = mupdf.fz_image_resolution(img)
            pm.m_internal.xres = xres
            pm.m_internal.yres = yres
            self.this = pm

        elif args_match(args, (Document, mupdf.FzDocument), int):
            # Create pixmap from PDF image identified by XREF number
            doc, xref = args
            pdf = _as_pdf_document(doc)
            xreflen = mupdf.pdf_xref_len(pdf)
            if not _INRANGE(xref, 1, xreflen-1):
                raise ValueError( MSG_BAD_XREF)
            ref = mupdf.pdf_new_indirect(pdf, xref, 0)
            type_ = mupdf.pdf_dict_get(ref, PDF_NAME('Subtype'))
            if (not mupdf.pdf_name_eq(type_, PDF_NAME('Image'))
                    and not mupdf.pdf_name_eq(type_, PDF_NAME('Alpha'))
                    and not mupdf.pdf_name_eq(type_, PDF_NAME('Luminosity'))
                    ):
                raise ValueError( MSG_IS_NO_IMAGE)
            img = mupdf.pdf_load_image(pdf, ref)
            # Original code passed null for subarea and ctm, but that's not
            # possible with MuPDF's python bindings. The equivalent is an
            # infinite rect and identify matrix scaled by img.w() and img.h().
            pix, w, h = mupdf.fz_get_pixmap_from_image(
                    img,
                    mupdf.FzIrect(FZ_MIN_INF_RECT, FZ_MIN_INF_RECT, FZ_MAX_INF_RECT, FZ_MAX_INF_RECT),
                    mupdf.FzMatrix(img.w(), 0, 0, img.h(), 0, 0),
                    )
            self.this = pix

        else:
            text = 'Unrecognised args for constructing Pixmap:\n'
            for arg in args:
                text += f'    {type(arg)}: {arg}\n'
            raise Exception( text)

    def __len__(self):
        return self.size

    def __repr__(self):
        if not type(self) is Pixmap: return
        if self.colorspace:
            return "Pixmap(%s, %s, %s)" % (self.colorspace.this.m_internal.name, self.irect, self.alpha)
        else:
            return "Pixmap(%s, %s, %s)" % ('None', self.irect, self.alpha)

    def _tobytes(self, format_, jpg_quality):
        '''
        Pixmap._tobytes
        '''
        pm = self.this
        size = mupdf.fz_pixmap_stride(pm) * pm.h()
        res = mupdf.fz_new_buffer(size)
        out = mupdf.FzOutput(res)
        if   format_ == 1:  mupdf.fz_write_pixmap_as_png(out, pm)
        elif format_ == 2:  mupdf.fz_write_pixmap_as_pnm(out, pm)
        elif format_ == 3:  mupdf.fz_write_pixmap_as_pam(out, pm)
        elif format_ == 5:  mupdf.fz_write_pixmap_as_psd(out, pm)
        elif format_ == 6:  mupdf.fz_write_pixmap_as_ps(out, pm)
        elif format_ == 7:
            mupdf.fz_write_pixmap_as_jpeg(out, pm, jpg_quality, 0)
        else:
            mupdf.fz_write_pixmap_as_png(out, pm)
        out.fz_close_output()
        barray = JM_BinFromBuffer(res)
        return barray

    def _writeIMG(self, filename, format_, jpg_quality):
        pm = self.this
        if   format_ == 1:  mupdf.fz_save_pixmap_as_png(pm, filename)
        elif format_ == 2:  mupdf.fz_save_pixmap_as_pnm(pm, filename)
        elif format_ == 3:  mupdf.fz_save_pixmap_as_pam(pm, filename)
        elif format_ == 5:  mupdf.fz_save_pixmap_as_psd(pm, filename)
        elif format_ == 6:  mupdf.fz_save_pixmap_as_ps(pm, filename)
        elif format_ == 7:  mupdf.fz_save_pixmap_as_jpeg(pm, filename, jpg_quality)
        else:               mupdf.fz_save_pixmap_as_png(pm, filename)

    @property
    def alpha(self):
        """Indicates presence of alpha channel."""
        return mupdf.fz_pixmap_alpha(self.this)

    def clear_with(self, value=None, bbox=None):
        """Fill all color components with same value."""
        if value is None:
            mupdf.fz_clear_pixmap(self.this)
        elif bbox is None:
            mupdf.fz_clear_pixmap_with_value(self.this, value)
        else:
            JM_clear_pixmap_rect_with_value(self.this, value, JM_irect_from_py(bbox))

    def color_count(self, colors=0, clip=None):
        '''
        Return count of each color.
        '''
        pm = self.this
        rc = JM_color_count( pm, clip)
        if not colors:
            return len( rc)
        return rc

    def color_topusage(self, clip=None):
        """Return most frequent color and its usage ratio."""
        allpixels = 0
        cnt = 0
        if clip is not None and self.irect in Rect(clip):
            clip = self.irect
        for pixel, count in self.color_count(colors=True,clip=clip).items():
            allpixels += count
            if count > cnt:
                cnt = count
                maxpixel = pixel
        if not allpixels:
            return (1, bytes([255] * self.n))
        return (cnt / allpixels, maxpixel)

    @property
    def colorspace(self):
        """Pixmap Colorspace."""
        cs = Colorspace(mupdf.fz_pixmap_colorspace(self.this))
        if cs.name == "None":
            return None
        return cs

    def copy(self, src, bbox):
        """Copy bbox from another Pixmap."""
        pm = self.this
        src_pix = src.this
        if not mupdf.fz_pixmap_colorspace(src_pix):
            raise ValueError( "cannot copy pixmap with NULL colorspace")
        if pm.alpha() != src_pix.alpha():
            raise ValueError( "source and target alpha must be equal")
        mupdf.fz_copy_pixmap_rect(pm, src_pix, JM_irect_from_py(bbox), mupdf.FzDefaultColorspaces(None))

    @property
    def digest(self):
        """MD5 digest of pixmap (bytes)."""
        ret = mupdf.fz_md5_pixmap2(self.this)
        return bytes(ret)

    def gamma_with(self, gamma):
        """Apply correction with some float.
        gamma=1 is a no-op."""
        if not mupdf.fz_pixmap_colorspace( self.this):
            message_warning("colorspace invalid for function")
            return
        mupdf.fz_gamma_pixmap( self.this, gamma)

    @property
    def h(self):
        """The height."""
        return mupdf.fz_pixmap_height(self.this)

    def invert_irect(self, bbox=None):
        """Invert the colors inside a bbox."""
        pm = self.this
        if not mupdf.fz_pixmap_colorspace(pm).m_internal:
            message_warning("ignored for stencil pixmap")
            return False
        r = JM_irect_from_py(bbox)
        if mupdf.fz_is_infinite_irect(r):
            mupdf.fz_invert_pixmap(pm)
            return True
        mupdf.fz_invert_pixmap_rect(pm, r)
        return True

    @property
    def irect(self):
        """Pixmap bbox - an IRect object."""
        val = mupdf.fz_pixmap_bbox(self.this)
        return JM_py_from_irect( val)

    @property
    def is_monochrome(self):
        """Check if pixmap is monochrome."""
        return mupdf.fz_is_pixmap_monochrome( self.this)

    @property
    def is_unicolor(self):
        '''
        Check if pixmap has only one color.
        '''
        pm = self.this
        n = pm.n()
        count = pm.w() * pm.h() * n
        def _pixmap_read_samples(pm, offset, n):
            ret = list()
            for i in range(n):
                ret.append(mupdf.fz_samples_get(pm, offset+i))
            return ret
        for offset in range( 0, count, n):
            if offset == 0:
                sample0 = _pixmap_read_samples( pm, 0, n)
            else:
                sample = _pixmap_read_samples( pm, offset, n)
                if sample != sample0:
                    return False
        return True

    @property
    def n(self):
        """The size of one pixel."""
        if g_use_extra:
            # Setting self.__class__.n gives a small reduction in overhead of
            # test_general.py:test_2093, e.g. 1.4x -> 1.3x.
            #return extra.pixmap_n(self.this)
            def n2(self):
                return extra.pixmap_n(self.this)
            self.__class__.n = property(n2)
            return self.n
        return mupdf.fz_pixmap_components(self.this)

    def pdfocr_save(self, filename, compress=1, language=None, tessdata=None):
        '''
        Save pixmap as an OCR-ed PDF page.
        '''
        tessdata = get_tessdata(tessdata)
        opts = mupdf.FzPdfocrOptions()
        opts.compress = compress
        if language:
            opts.language_set2( language)
        if tessdata:
            opts.datadir_set2( tessdata)
        pix = self.this
        if isinstance(filename, str):
            mupdf.fz_save_pixmap_as_pdfocr( pix, filename, 0, opts)
        else:
            out = JM_new_output_fileptr( filename)
            try:
                mupdf.fz_write_pixmap_as_pdfocr( out, pix, opts)
            finally:
                out.fz_close_output()   # Avoid MuPDF warning.

    def pdfocr_tobytes(self, compress=True, language="eng", tessdata=None):
        """Save pixmap as an OCR-ed PDF page.

        Args:
            compress: (bool) compress, default 1 (True).
            language: (str) language(s) occurring on page, default "eng" (English),
                    multiples like "eng+ger" for English and German.
            tessdata: (str) folder name of Tesseract's language support. If None
                    we use environment variable TESSDATA_PREFIX or search for
                    Tesseract installation.
        Notes:
            On failure, make sure Tesseract is installed and you have set
            <tessdata> or environment variable "TESSDATA_PREFIX" to the folder
            containing your Tesseract's language support data.
        """
        tessdata = get_tessdata(tessdata)
        from io import BytesIO
        bio = BytesIO()
        self.pdfocr_save(bio, compress=compress, language=language, tessdata=tessdata)
        return bio.getvalue()

    def pil_image(self):
        """Create a Pillow Image from the Pixmap."""
        try:
            from PIL import Image
        except ImportError:
            message("PIL/Pillow not installed")
            raise

        cspace = self.colorspace
        if not cspace:
            mode = "L"
        elif cspace.n == 1:
            mode = "L" if not self.alpha else "LA"
        elif cspace.n == 3:
            mode = "RGB" if not self.alpha else "RGBA"
        else:
            mode = "CMYK"

        img = Image.frombytes(mode, (self.width, self.height), self.samples)
        return img

    def pil_save(self, *args, **kwargs):
        """Write to image file using Pillow.

        An intermediate PIL Image is created, and its "save" method is used
        to store the image. See Pillow documentation to learn about the
        meaning of possible positional and keyword parameters.
        Use this when other output formats are desired.
        """
        img = self.pil_image()

        if "dpi" not in kwargs.keys():
            kwargs["dpi"] = (self.xres, self.yres)

        img.save(*args, **kwargs)

    def pil_tobytes(self, *args, **kwargs):
        """Convert to an image in memory using Pillow.

        An intermediate PIL Image is created, and its "save" method is used
        to store the image. See Pillow documentation to learn about the
        meaning of possible positional or keyword parameters.
        Use this when other output formats are desired.
        """
        bytes_out = io.BytesIO()
        img = self.pil_image()

        if "dpi" not in kwargs.keys():
            kwargs["dpi"] = (self.xres, self.yres)

        img.save(bytes_out, *args, **kwargs)
        return bytes_out.getvalue()

    def pixel(self, x, y):
        """Get color tuple of pixel (x, y).
        Last item is the alpha if Pixmap.alpha is true."""
        if g_use_extra:
            return extra.pixmap_pixel(self.this.m_internal, x, y)
        if (0
                or x < 0
                or x >= self.this.m_internal.w
                or y < 0
                or y >= self.this.m_internal.h
                ):
            RAISEPY(MSG_PIXEL_OUTSIDE, PyExc_ValueError)
        n = self.this.m_internal.n
        stride = self.this.m_internal.stride
        i = stride * y + n * x
        ret = tuple( self.samples_mv[ i: i+n])
        return ret

    @property
    def samples(self)->bytes:
        mv = self.samples_mv
        return bytes( mv)

    @property
    def samples_mv(self):
        '''
        Pixmap samples memoryview.
        '''
        # We remember the returned memoryview so that our `__del__()` can
        # release it; otherwise accessing it after we have been destructed will
        # fail, possibly crashing Python; this is #4155.
        #
        if self._samples_mv is None:
            self._samples_mv = mupdf.fz_pixmap_samples_memoryview(self.this)
        return self._samples_mv
    
    def _samples_mv_release(self):
        if self._samples_mv:
            self._samples_mv.release()

    @property
    def samples_ptr(self):
        return mupdf.fz_pixmap_samples_int(self.this)

    def save(self, filename, output=None, jpg_quality=95):
        """Output as image in format determined by filename extension.

        Args:
            output: (str) only use to overrule filename extension. Default is PNG.
                    Others are JPEG, JPG, PNM, PGM, PPM, PBM, PAM, PSD, PS.
        """
        valid_formats = {
                "png": 1,
                "pnm": 2,
                "pgm": 2,
                "ppm": 2,
                "pbm": 2,
                "pam": 3,
                "psd": 5,
                "ps": 6,
                "jpg": 7,
                "jpeg": 7,
                }
        
        if type(filename) is str:
            pass
        elif hasattr(filename, "absolute"):
            filename = str(filename)
        elif hasattr(filename, "name"):
            filename = filename.name
        if output is None:
            _, ext = os.path.splitext(filename)
            output = ext[1:]

        idx = valid_formats.get(output.lower(), None)
        if idx is None:
            raise ValueError(f"Image format {output} not in {tuple(valid_formats.keys())}")
        if self.alpha and idx in (2, 6, 7):
            raise ValueError("'%s' cannot have alpha" % output)
        if self.colorspace and self.colorspace.n > 3 and idx in (1, 2, 4):
            raise ValueError(f"unsupported colorspace for '{output}'")
        if idx == 7:
            self.set_dpi(self.xres, self.yres)
        return self._writeIMG(filename, idx, jpg_quality)

    def set_alpha(self, alphavalues=None, premultiply=1, opaque=None, matte=None):
        """Set alpha channel to values contained in a byte array.
        If omitted, set alphas to 255.

        Args:
            alphavalues: (bytes) with length (width * height) or 'None'.
            premultiply: (bool, True) premultiply colors with alpha values.
            opaque: (tuple, length colorspace.n) this color receives opacity 0.
            matte: (tuple, length colorspace.n)) preblending background color.
        """
        pix = self.this
        alpha = 0
        m = 0
        if pix.alpha() == 0:
            raise ValueError( MSG_PIX_NOALPHA)
        n = mupdf.fz_pixmap_colorants(pix)
        w = mupdf.fz_pixmap_width(pix)
        h = mupdf.fz_pixmap_height(pix)
        balen = w * h * (n+1)
        colors = [0, 0, 0, 0]   # make this color opaque
        bgcolor = [0, 0, 0, 0]  # preblending background color
        zero_out = 0
        bground = 0
        if opaque and isinstance(opaque, (list, tuple)) and len(opaque) == n:
            for i in range(n):
                colors[i] = opaque[i]
            zero_out = 1
        if matte and isinstance( matte, (tuple, list)) and len(matte) == n:
            for i in range(n):
                bgcolor[i] = matte[i]
            bground = 1
        data = bytes()
        data_len = 0
        if alphavalues:
            #res = JM_BufferFromBytes(alphavalues)
            #data_len, data = mupdf.fz_buffer_storage(res)
            #if data_len < w * h:
            #    THROWMSG("bad alpha values")
            # fixme: don't seem to need to create an fz_buffer - can
            # use <alphavalues> directly?
            if isinstance(alphavalues, (bytes, bytearray)):
                data = alphavalues
                data_len = len(alphavalues)
            else:
                assert 0, f'unexpected type for alphavalues: {type(alphavalues)}'
            if data_len < w * h:
                raise ValueError( "bad alpha values")
        if 1:
            # Use C implementation for speed.
            mupdf.Pixmap_set_alpha_helper(
                    balen,
                    n,
                    data_len,
                    zero_out,
                    mupdf.python_buffer_data( data),
                    pix.m_internal,
                    premultiply,
                    bground,
                    colors,
                    bgcolor,
                    )
        else:
            i = k = j = 0
            data_fix = 255
            while i < balen:
                alpha = data[k]
                if zero_out:
                    for j in range(i, i+n):
                        if mupdf.fz_samples_get(pix, j) != colors[j - i]:
                            data_fix = 255
                            break
                        else:
                            data_fix = 0
                if data_len:
                    def fz_mul255( a, b):
                        x = a * b + 128
                        x += x // 256
                        return x // 256

                    if data_fix == 0:
                        mupdf.fz_samples_set(pix, i+n, 0)
                    else:
                        mupdf.fz_samples_set(pix, i+n, alpha)
                    if premultiply and not bground:
                        for j in range(i, i+n):
                            mupdf.fz_samples_set(pix, j, fz_mul255( mupdf.fz_samples_get(pix, j), alpha))
                    elif bground:
                        for j in range( i, i+n):
                            m = bgcolor[j - i]
                            mupdf.fz_samples_set(pix, j, fz_mul255( mupdf.fz_samples_get(pix, j) - m, alpha))
                else:
                    mupdf.fz_samples_set(pix, i+n, data_fix)
                i += n+1
                k += 1

    def tobytes(self, output="png", jpg_quality=95):
        '''
        Convert to binary image stream of desired type.
        '''
        valid_formats = {
                "png": 1,
                "pnm": 2,
                "pgm": 2,
                "ppm": 2,
                "pbm": 2,
                "pam": 3,
                "tga": 4,
                "tpic": 4,
                "psd": 5,
                "ps": 6,
                'jpg': 7,
                'jpeg': 7,
                }
        idx = valid_formats.get(output.lower(), None)
        if idx is None:
            raise ValueError(f"Image format {output} not in {tuple(valid_formats.keys())}")
        if self.alpha and idx in (2, 6, 7):
            raise ValueError("'{output}' cannot have alpha")
        if self.colorspace and self.colorspace.n > 3 and idx in (1, 2, 4):
            raise ValueError(f"unsupported colorspace for '{output}'")
        if idx == 7:
            self.set_dpi(self.xres, self.yres)
        barray = self._tobytes(idx, jpg_quality)
        return barray

    def set_dpi(self, xres, yres):
        """Set resolution in both dimensions."""
        pm = self.this
        pm.m_internal.xres = xres
        pm.m_internal.yres = yres

    def set_origin(self, x, y):
        """Set top-left coordinates."""
        pm = self.this
        pm.m_internal.x = x
        pm.m_internal.y = y

    def set_pixel(self, x, y, color):
        """Set color of pixel (x, y)."""
        if g_use_extra:
            return extra.set_pixel(self.this.m_internal, x, y, color)
        pm = self.this
        if not _INRANGE(x, 0, pm.w() - 1) or not _INRANGE(y, 0, pm.h() - 1):
            raise ValueError( MSG_PIXEL_OUTSIDE)
        n = pm.n()
        for j in range(n):
            i = color[j]
            if not _INRANGE(i, 0, 255):
                raise ValueError( MSG_BAD_COLOR_SEQ)
        stride = mupdf.fz_pixmap_stride( pm)
        i = stride * y + n * x
        if 0:
            # Using a cached self._memory_view doesn't actually make much
            # difference to speed.
            if not self._memory_view:
                self._memory_view = self.samples_mv
            for j in range(n):
                self._memory_view[i + j] = color[j]
        else:
            for j in range(n):
                pm.fz_samples_set(i + j, color[j])

    def set_rect(self, bbox, color):
        """Set color of all pixels in bbox."""
        pm = self.this
        n = pm.n()
        c = []
        for j in range(n):
            i = color[j]
            if not _INRANGE(i, 0, 255):
                raise ValueError( MSG_BAD_COLOR_SEQ)
            c.append(i)
        bbox = JM_irect_from_py(bbox)
        i = JM_fill_pixmap_rect_with_color(pm, c, bbox)
        rc = bool(i)
        return rc

    def shrink(self, factor):
        """Divide width and height by 2**factor.
        E.g. factor=1 shrinks to 25% of original size (in place)."""
        if factor < 1:
            message_warning("ignoring shrink factor < 1")
            return
        mupdf.fz_subsample_pixmap( self.this, factor)
        # Pixmap has changed so clear our memory view.
        self._memory_view = None
        self._samples_mv_release()

    @property
    def size(self):
        """Pixmap size."""
        return  mupdf.fz_pixmap_size( self.this)

    @property
    def stride(self):
        """Length of one image line (width * n)."""
        return self.this.stride()

    def tint_with(self, black, white):
        """Tint colors with modifiers for black and white."""
        if not self.colorspace or self.colorspace.n > 3:
            message("warning: colorspace invalid for function")
            return
        return mupdf.fz_tint_pixmap( self.this, black, white)

    @property
    def w(self):
        """The width."""
        return mupdf.fz_pixmap_width(self.this)
    
    def warp(self, quad, width, height):
        """Return pixmap from a warped quad."""
        if not quad.is_convex: raise ValueError("quad must be convex")
        q = JM_quad_from_py(quad)
        points = [ q.ul, q.ur, q.lr, q.ll]
        dst = mupdf.fz_warp_pixmap( self.this, points, width, height)
        return Pixmap( dst)

    @property
    def x(self):
        """x component of Pixmap origin."""
        return mupdf.fz_pixmap_x(self.this)

    @property
    def xres(self):
        """Resolution in x direction."""
        return self.this.xres()

    @property
    def y(self):
        """y component of Pixmap origin."""
        return mupdf.fz_pixmap_y(self.this)

    @property
    def yres(self):
        """Resolution in y direction."""
        return self.this.yres()

    width  = w
    height = h
    
    def __del__(self):
        if self._samples_mv:
            self._samples_mv.release()

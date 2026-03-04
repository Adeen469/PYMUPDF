"""
Class: fitz.Annot

Description: No docstring available.

Inheritance (MRO): Annot -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Annot =====

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, annot)  [function]
#     -> Initialize self.  See help(type(self)) for accurate signature.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self)  [function]
#     -> Return repr(self).

# __str__(self)  [function]
#     -> Return str(self).

# apn_bbox = <property object at 0x000002052E128A90>  [property]

# apn_matrix = <property object at 0x000002052E429990>  [property]

# blendmode = <property object at 0x000002052E48F100>  [property]

# border = <property object at 0x000002052E48F150>  [property]

# clean_contents(self, sanitize=1)  [function]
#     -> Clean appearance contents stream.

# colors = <property object at 0x000002052E48F1A0>  [property]

# delete_responses(self)  [function]
#     -> Delete 'Popup' and responding annotations.

# file_info = <property object at 0x000002052E48F330>  [property]

# flags = <property object at 0x000002052E48F380>  [property]

# get_file(self)  [function]
#     -> Retrieve attached file content.

# get_oc(self)  [function]
#     -> Get annotation optional content reference.

# get_parent(self)  [function]

# get_pixmap(self, matrix=None, dpi=None, colorspace=None, alpha=0)  [function]
#     -> annotation Pixmap

# get_sound(self)  [function]
#     -> Retrieve sound stream.

# get_text(self, *args, **kwargs)  [function]

# get_textbox(self, *args, **kwargs)  [function]

# get_textpage(self, clip=None, flags=0)  [function]
#     -> Make annotation TextPage.

# has_popup = <property object at 0x000002052E48F560>  [property]

# info = <property object at 0x000002052E5258F0>  [property]

# irt_xref = <property object at 0x000002052E525E90>  [property]

# is_open = <property object at 0x000002052E5844A0>  [property]

# language = <property object at 0x000002052DE30B80>  [property]

# line_ends = <property object at 0x000002052DE30BD0>  [property]

# next = <property object at 0x000002052DE30C20>  [property]

# opacity = <property object at 0x000002052DE30C70>  [property]

# popup_rect = <property object at 0x000002052DE30CC0>  [property]

# popup_xref = <property object at 0x000002052DE30D10>  [property]

# rect = <property object at 0x000002052DE30D60>  [property]

# rect_delta = <property object at 0x000002052DE30DB0>  [property]

# rotation = <property object at 0x000002052DE30E00>  [property]

# set_apn_bbox(self, bbox)  [function]
#     -> Set annotation appearance bbox.

# set_apn_matrix(self, matrix)  [function]
#     -> Set annotation appearance matrix.

# set_blendmode(self, blend_mode)  [function]
#     -> Set annotation BlendMode.

# set_border(self, border=None, width=-1, style=None, dashes=None, clouds=-1)  [function]
#     -> Set border properties.

# set_colors(self, colors=None, stroke=None, fill=None)  [function]
#     -> Set 'stroke' and 'fill' colors.

# set_flags(self, flags)  [function]
#     -> Set annotation flags.

# set_info(self, info=None, content=None, title=None, creationDate=None, modDate=None, subject=None)  [function]
#     -> Set various properties.

# set_irt_xref(self, xref)  [function]
#     -> Set annotation IRT xref

# set_language(self, language=None)  [function]
#     -> Set annotation language.

# set_line_ends(self, start, end)  [function]
#     -> Set line end codes.

# set_name(self, name)  [function]
#     -> Set /Name (icon) of annotation.

# set_oc(self, oc=0)  [function]
#     -> Set / remove annotation OC xref.

# set_opacity(self, opacity)  [function]
#     -> Set opacity.

# set_open(self, is_open)  [function]
#     -> Set 'open' status of annotation or its Popup.

# set_popup(self, rect)  [function]
#     -> Create annotation 'Popup' or update rectangle.

# set_rect(self, rect)  [function]
#     -> Set annotation rectangle.

# set_rotation(self, rotate=0)  [function]
#     -> Set annotation rotation.

# type = <property object at 0x000002052DE30E50>  [property]

# update(self, blend_mode: Optional[str] = None, opacity: Optional[float] = None, fontsize: float = 0, fontname: Optional[str] = None, text_color: Optional[Sequence] = None, border_color: Optional[Sequence] = None, fill_color: Optional[Sequence] = None, cross_out: bool = True, rotate: int = -1)  [function]
#     -> Update annot appearance.

# update_file(self, buffer_=None, filename=None, ufilename=None, desc=None)  [function]
#     -> Update attached file.

# update_timing_test()  [function]

# vertices = <property object at 0x000002052DE30EA0>  [property]

# xref = <property object at 0x000002052DE30EF0>  [property]


# ===== Source Code =====
class Annot:

    def __init__(self, annot):
        assert isinstance( annot, mupdf.PdfAnnot)
        self.this = annot

    def __repr__(self):
        parent = getattr(self, 'parent', '<>')
        return "'%s' annotation on %s" % (self.type[1], str(parent))

    def __str__(self):
        return self.__repr__()

    def _erase(self):
        if getattr(self, "thisown", False):
            self.thisown = False

    def _get_redact_values(self):
        annot = self.this
        if mupdf.pdf_annot_type(annot) != mupdf.PDF_ANNOT_REDACT:
            return

        values = dict()
        try:
            obj = mupdf.pdf_dict_gets(mupdf.pdf_annot_obj(annot), "RO")
            if obj.m_internal:
                message_warning("Ignoring redaction key '/RO'.")
                xref = mupdf.pdf_to_num(obj)
                values[dictkey_xref] = xref
            obj = mupdf.pdf_dict_gets(mupdf.pdf_annot_obj(annot), "OverlayText")
            if obj.m_internal:
                text = mupdf.pdf_to_text_string(obj)
                values[dictkey_text] = JM_UnicodeFromStr(text)
            else:
                values[dictkey_text] = ''
            obj = mupdf.pdf_dict_get(mupdf.pdf_annot_obj(annot), PDF_NAME('Q'))
            align = 0
            if obj.m_internal:
                align = mupdf.pdf_to_int(obj)
            values[dictkey_align] = align
        except Exception:
            if g_exceptions_verbose:    exception_info()
            return
        val = values

        if not val:
            return val
        val["rect"] = self.rect
        text_color, fontname, fontsize = TOOLS._parse_da(self)
        val["text_color"] = text_color
        val["fontname"] = fontname
        val["fontsize"] = fontsize
        fill = self.colors["fill"]
        val["fill"] = fill
        return val

    def _getAP(self):
        if g_use_extra:
            assert isinstance( self.this, mupdf.PdfAnnot)
            ret = extra.Annot_getAP(self.this)
            assert isinstance( ret, bytes)
            return ret
        else:
            r = None
            res = None
            annot = self.this
            assert isinstance( annot, mupdf.PdfAnnot)
            annot_obj = mupdf.pdf_annot_obj( annot)
            ap = mupdf.pdf_dict_getl( annot_obj, PDF_NAME('AP'), PDF_NAME('N'))
            if mupdf.pdf_is_stream( ap):
                res = mupdf.pdf_load_stream( ap)
            if res and res.m_internal:
                r = JM_BinFromBuffer(res)
            return r

    def _setAP(self, buffer_, rect=0):
        try:
            annot = self.this
            annot_obj = mupdf.pdf_annot_obj( annot)
            page = _pdf_annot_page(annot)
            apobj = mupdf.pdf_dict_getl( annot_obj, PDF_NAME('AP'), PDF_NAME('N'))
            if not apobj.m_internal:
                raise RuntimeError( MSG_BAD_APN)
            if not mupdf.pdf_is_stream( apobj):
                raise RuntimeError( MSG_BAD_APN)
            res = JM_BufferFromBytes( buffer_)
            if not res.m_internal:
                raise ValueError( MSG_BAD_BUFFER)
            JM_update_stream( page.doc(), apobj, res, 1)
            if rect:
                bbox = mupdf.pdf_dict_get_rect( annot_obj, PDF_NAME('Rect'))
                mupdf.pdf_dict_put_rect( apobj, PDF_NAME('BBox'), bbox)
        except Exception:
            if g_exceptions_verbose:    exception_info()

    def _update_appearance(self, opacity=-1, blend_mode=None, fill_color=None, rotate=-1):
        annot = self.this
        assert annot.m_internal
        annot_obj = mupdf.pdf_annot_obj( annot)
        page = _pdf_annot_page(annot)
        pdf = page.doc()
        type_ = mupdf.pdf_annot_type( annot)
        nfcol, fcol = JM_color_FromSequence(fill_color)

        try:
            # remove fill color from unsupported annots
            # or if so requested
            if nfcol == 0 or type_ not in (
                    mupdf.PDF_ANNOT_SQUARE,
                    mupdf.PDF_ANNOT_CIRCLE,
                    mupdf.PDF_ANNOT_LINE,
                    mupdf.PDF_ANNOT_POLY_LINE,
                    mupdf.PDF_ANNOT_POLYGON
                    ):
                mupdf.pdf_dict_del( annot_obj, PDF_NAME('IC'))
            elif nfcol > 0:
                mupdf.pdf_set_annot_interior_color( annot, fcol[:nfcol])

            insert_rot = 1 if rotate >= 0 else 0
            if type_ not in (
                    mupdf.PDF_ANNOT_CARET,
                    mupdf.PDF_ANNOT_CIRCLE,
                    mupdf.PDF_ANNOT_FREE_TEXT,
                    mupdf.PDF_ANNOT_FILE_ATTACHMENT,
                    mupdf.PDF_ANNOT_INK,
                    mupdf.PDF_ANNOT_LINE,
                    mupdf.PDF_ANNOT_POLY_LINE,
                    mupdf.PDF_ANNOT_POLYGON,
                    mupdf.PDF_ANNOT_SQUARE,
                    mupdf.PDF_ANNOT_STAMP,
                    mupdf.PDF_ANNOT_TEXT,
                    ):
                insert_rot = 0

            if insert_rot:
                mupdf.pdf_dict_put_int(annot_obj, PDF_NAME('Rotate'), rotate)

            # insert fill color
            if type_ == mupdf.PDF_ANNOT_FREE_TEXT:
                if nfcol > 0:
                    mupdf.pdf_set_annot_color(annot, fcol[:nfcol])
            elif nfcol > 0:
                col = mupdf.pdf_new_array(page.doc(), nfcol)
                for i in range( nfcol):
                    mupdf.pdf_array_push_real(col, fcol[i])
                mupdf.pdf_dict_put(annot_obj, PDF_NAME('IC'), col)
            mupdf.pdf_dirty_annot(annot)
            mupdf.pdf_update_annot(annot) # let MuPDF update
            pdf.resynth_required = 0
        except Exception as e:
            if g_exceptions_verbose:
                exception_info()
            message( f'cannot update annot: {e}')
            raise
        
        if (opacity < 0 or opacity >= 1) and not blend_mode:    # no opacity, no blend_mode
            return True

        try:    # create or update /ExtGState
            ap = mupdf.pdf_dict_getl(
                    mupdf.pdf_annot_obj(annot),
                    PDF_NAME('AP'),
                    PDF_NAME('N')
                    )
            if not ap.m_internal:   # should never happen
                raise RuntimeError( MSG_BAD_APN)

            resources = mupdf.pdf_dict_get( ap, PDF_NAME('Resources'))
            if not resources.m_internal:    # no Resources yet: make one
                resources = mupdf.pdf_dict_put_dict( ap, PDF_NAME('Resources'), 2)
            
            alp0 = mupdf.pdf_new_dict( page.doc(), 3)
            if opacity >= 0 and opacity < 1:
                mupdf.pdf_dict_put_real( alp0, PDF_NAME('CA'), opacity)
                mupdf.pdf_dict_put_real( alp0, PDF_NAME('ca'), opacity)
                mupdf.pdf_dict_put_real( annot_obj, PDF_NAME('CA'), opacity)

            if blend_mode:
                mupdf.pdf_dict_put_name( alp0, PDF_NAME('BM'), blend_mode)
                mupdf.pdf_dict_put_name( annot_obj, PDF_NAME('BM'), blend_mode)

            extg = mupdf.pdf_dict_get( resources, PDF_NAME('ExtGState'))
            if not extg.m_internal: # no ExtGState yet: make one
                extg = mupdf.pdf_dict_put_dict( resources, PDF_NAME('ExtGState'), 2)

            mupdf.pdf_dict_put( extg, PDF_NAME('H'), alp0)

        except Exception as e:
            if g_exceptions_verbose:    exception_info()
            message( f'cannot set opacity or blend mode\n: {e}')
            raise

        return True

    @property
    def apn_bbox(self):
        """annotation appearance bbox"""
        CheckParent(self)
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        ap = mupdf.pdf_dict_getl(annot_obj, PDF_NAME('AP'), PDF_NAME('N'))
        if not ap.m_internal:
            val = JM_py_from_rect(mupdf.FzRect(mupdf.FzRect.Fixed_INFINITE))
        else:
            rect = mupdf.pdf_dict_get_rect(ap, PDF_NAME('BBox'))
            val = JM_py_from_rect(rect)

        val = Rect(val) * self.get_parent().transformation_matrix
        val *= self.get_parent().derotation_matrix
        return val

    @property
    def apn_matrix(self):
        """annotation appearance matrix"""
        try:
            CheckParent(self)
            annot = self.this
            assert isinstance(annot, mupdf.PdfAnnot)
            ap = mupdf.pdf_dict_getl(
                    mupdf.pdf_annot_obj(annot),
                    mupdf.PDF_ENUM_NAME_AP,
                    mupdf.PDF_ENUM_NAME_N
                    )
            if not ap.m_internal:
                return JM_py_from_matrix(mupdf.FzMatrix())
            mat = mupdf.pdf_dict_get_matrix(ap, mupdf.PDF_ENUM_NAME_Matrix)
            val = JM_py_from_matrix(mat)

            val = Matrix(val)

            return val
        except Exception:
            if g_exceptions_verbose:    exception_info()
            raise

    @property
    def blendmode(self):
        """annotation BlendMode"""
        CheckParent(self)
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        obj = mupdf.pdf_dict_get(annot_obj, PDF_NAME('BM'))
        blend_mode = None
        if obj.m_internal:
            blend_mode = JM_UnicodeFromStr(mupdf.pdf_to_name(obj))
            return blend_mode
        # loop through the /AP/N/Resources/ExtGState objects
        obj = mupdf.pdf_dict_getl(
                annot_obj,
                PDF_NAME('AP'),
                PDF_NAME('N'),
                PDF_NAME('Resources'),
                PDF_NAME('ExtGState'),
                )
        if mupdf.pdf_is_dict(obj):
            n = mupdf.pdf_dict_len(obj)
            for i in range(n):
                obj1 = mupdf.pdf_dict_get_val(obj, i)
                if mupdf.pdf_is_dict(obj1):
                    m = mupdf.pdf_dict_len(obj1)
                    for j in range(m):
                        obj2 = mupdf.pdf_dict_get_key(obj1, j)
                        if mupdf.pdf_objcmp(obj2, PDF_NAME('BM')) == 0:
                            blend_mode = JM_UnicodeFromStr(mupdf.pdf_to_name(mupdf.pdf_dict_get_val(obj1, j)))
                            return blend_mode
        return blend_mode

    @property
    def border(self):
        """Border information."""
        CheckParent(self)
        atype = self.type[0]
        if atype not in (
                mupdf.PDF_ANNOT_CIRCLE,
                mupdf.PDF_ANNOT_FREE_TEXT,
                mupdf.PDF_ANNOT_INK,
                mupdf.PDF_ANNOT_LINE,
                mupdf.PDF_ANNOT_POLY_LINE,
                mupdf.PDF_ANNOT_POLYGON,
                mupdf.PDF_ANNOT_SQUARE,
                ):
            return dict()
        ao = mupdf.pdf_annot_obj(self.this)
        ret = JM_annot_border(ao)
        return ret

    def clean_contents(self, sanitize=1):
        """Clean appearance contents stream."""
        CheckParent(self)
        annot = self.this
        pdf = mupdf.pdf_get_bound_document(mupdf.pdf_annot_obj(annot))
        filter_ = _make_PdfFilterOptions(recurse=1, instance_forms=0, ascii=0, sanitize=sanitize)
        mupdf.pdf_filter_annot_contents(pdf, annot, filter_)

    @property
    def colors(self):
        """Color definitions."""
        try:
            CheckParent(self)
            annot = self.this
            assert isinstance(annot, mupdf.PdfAnnot)
            return JM_annot_colors(mupdf.pdf_annot_obj(annot))
        except Exception:
            if g_exceptions_verbose:    exception_info()
            raise

    def delete_responses(self):
        """Delete 'Popup' and responding annotations."""
        CheckParent(self)
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        page = _pdf_annot_page(annot)
        while 1:
            irt_annot = JM_find_annot_irt(annot)
            if not irt_annot:
                break
            mupdf.pdf_delete_annot(page, irt_annot)
        mupdf.pdf_dict_del(annot_obj, PDF_NAME('Popup'))

        annots = mupdf.pdf_dict_get(page.obj(), PDF_NAME('Annots'))
        n = mupdf.pdf_array_len(annots)
        found = 0
        for i in range(n-1, -1, -1):
            o = mupdf.pdf_array_get(annots, i)
            p = mupdf.pdf_dict_get(o, PDF_NAME('Parent'))
            if not o.m_internal:
                continue
            if not mupdf.pdf_objcmp(p, annot_obj):
                mupdf.pdf_array_delete(annots, i)
                found = 1
        if found:
            mupdf.pdf_dict_put(page.obj(), PDF_NAME('Annots'), annots)

    @property
    def file_info(self):
        """Attached file information."""
        CheckParent(self)
        res = dict()
        length = -1
        size = -1
        desc = None
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        type_ = mupdf.pdf_annot_type(annot)
        if type_ != mupdf.PDF_ANNOT_FILE_ATTACHMENT:
            raise TypeError( MSG_BAD_ANNOT_TYPE)
        stream = mupdf.pdf_dict_getl(
                annot_obj,
                PDF_NAME('FS'),
                PDF_NAME('EF'),
                PDF_NAME('F'),
                )
        if not stream.m_internal:
            RAISEPY( "bad PDF: file entry not found", JM_Exc_FileDataError)

        fs = mupdf.pdf_dict_get(annot_obj, PDF_NAME('FS'))

        o = mupdf.pdf_dict_get(fs, PDF_NAME('UF'))
        if o.m_internal:
            filename = mupdf.pdf_to_text_string(o)
        else:
            o = mupdf.pdf_dict_get(fs, PDF_NAME('F'))
            if o.m_internal:
                filename = mupdf.pdf_to_text_string(o)

        o = mupdf.pdf_dict_get(fs, PDF_NAME('Desc'))
        if o.m_internal:
            desc = mupdf.pdf_to_text_string(o)

        o = mupdf.pdf_dict_get(stream, PDF_NAME('Length'))
        if o.m_internal:
            length = mupdf.pdf_to_int(o)

        o = mupdf.pdf_dict_getl(stream, PDF_NAME('Params'), PDF_NAME('Size'))
        if o.m_internal:
            size = mupdf.pdf_to_int(o)

        res[ dictkey_filename] = JM_EscapeStrFromStr(filename)
        res[ dictkey_descr] = JM_UnicodeFromStr(desc)
        res[ dictkey_length] = length
        res[ dictkey_size] = size
        return res

    @property
    def flags(self):
        """Flags field."""
        CheckParent(self)
        annot = self.this
        return mupdf.pdf_annot_flags(annot)

    def get_file(self):
        """Retrieve attached file content."""
        CheckParent(self)
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        type = mupdf.pdf_annot_type(annot)
        if type != mupdf.PDF_ANNOT_FILE_ATTACHMENT:
            raise TypeError( MSG_BAD_ANNOT_TYPE)
        stream = mupdf.pdf_dict_getl(annot_obj, PDF_NAME('FS'), PDF_NAME('EF'), PDF_NAME('F'))
        if not stream.m_internal:
            RAISEPY( "bad PDF: file entry not found", JM_Exc_FileDataError)
        buf = mupdf.pdf_load_stream(stream)
        res = JM_BinFromBuffer(buf)
        return res

    def get_oc(self):
        """Get annotation optional content reference."""
        CheckParent(self)
        oc = 0
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        obj = mupdf.pdf_dict_get(annot_obj, PDF_NAME('OC'))
        if obj.m_internal:
            oc = mupdf.pdf_to_num(obj)
        return oc

    # PyMuPDF doesn't seem to have this .parent member, but removing it breaks
    # 11 tests...?
    #@property
    def get_parent(self):
        try:
            ret = getattr( self, 'parent')
        except AttributeError:
            page = _pdf_annot_page(self.this)
            assert isinstance( page, mupdf.PdfPage)
            document = Document( page.doc()) if page.m_internal else None
            ret = Page(page, document)
            #self.parent = weakref.proxy( ret)
            self.parent = ret
            #log(f'No attribute .parent: {type(self)=} {id(self)=}: have set {id(self.parent)=}.')
            #log( f'Have set self.parent')
        return ret

    def get_pixmap(self, matrix=None, dpi=None, colorspace=None, alpha=0):
        """annotation Pixmap"""

        CheckParent(self)
        cspaces = {"gray": csGRAY, "rgb": csRGB, "cmyk": csCMYK}
        if type(colorspace) is str:
            colorspace = cspaces.get(colorspace.lower(), None)
        if dpi:
            matrix = Matrix(dpi / 72, dpi / 72)
        ctm = JM_matrix_from_py(matrix)
        cs = colorspace
        if not cs:
            cs = mupdf.fz_device_rgb()

        pix = mupdf.pdf_new_pixmap_from_annot(self.this, ctm, cs, mupdf.FzSeparations(0), alpha)
        ret = Pixmap(pix)
        if dpi:
            ret.set_dpi(dpi, dpi)
        return ret

    def get_sound(self):
        """Retrieve sound stream."""
        CheckParent(self)
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        type = mupdf.pdf_annot_type(annot)
        sound = mupdf.pdf_dict_get(annot_obj, PDF_NAME('Sound'))
        if type != mupdf.PDF_ANNOT_SOUND or not sound.m_internal:
            raise TypeError( MSG_BAD_ANNOT_TYPE)
        if mupdf.pdf_dict_get(sound, PDF_NAME('F')).m_internal:
            RAISEPY( "unsupported sound stream", JM_Exc_FileDataError)
        res = dict()
        obj = mupdf.pdf_dict_get(sound, PDF_NAME('R'))
        if obj.m_internal:
            res['rate'] = mupdf.pdf_to_real(obj)
        obj = mupdf.pdf_dict_get(sound, PDF_NAME('C'))
        if obj.m_internal:
            res['channels'] = mupdf.pdf_to_int(obj)
        obj = mupdf.pdf_dict_get(sound, PDF_NAME('B'))
        if obj.m_internal:
            res['bps'] = mupdf.pdf_to_int(obj)
        obj = mupdf.pdf_dict_get(sound, PDF_NAME('E'))
        if obj.m_internal:
            res['encoding'] = mupdf.pdf_to_name(obj)
        obj = mupdf.pdf_dict_gets(sound, "CO")
        if obj.m_internal:
            res['compression'] = mupdf.pdf_to_name(obj)
        buf = mupdf.pdf_load_stream(sound)
        stream = JM_BinFromBuffer(buf)
        res['stream'] = stream
        return res
    
    def get_text(self, *args, **kwargs):
        return utils.get_text(self, *args, **kwargs)

    def get_textbox(self, *args, **kwargs):
        return utils.get_textbox(self, *args, **kwargs)

    def get_textpage(self, clip=None, flags=0):
        """Make annotation TextPage."""
        CheckParent(self)
        options = mupdf.FzStextOptions(flags)
        if clip:
            assert hasattr(mupdf, 'FZ_STEXT_CLIP_RECT'), f'MuPDF-{mupdf_version} does not support FZ_STEXT_CLIP_RECT.'
            clip2 = JM_rect_from_py(clip)
            options.clip = clip2.internal()
            options.flags |= mupdf.FZ_STEXT_CLIP_RECT
        annot = self.this
        stextpage = mupdf.FzStextPage(annot, options)
        ret = TextPage(stextpage)
        p = self.get_parent()
        if isinstance(p, weakref.ProxyType):
            ret.parent = p
        else:
            ret.parent = weakref.proxy(p)
        return ret

    @property
    def has_popup(self):
        """Check if annotation has a Popup."""
        CheckParent(self)
        annot = self.this
        obj = mupdf.pdf_dict_get(mupdf.pdf_annot_obj(annot), PDF_NAME('Popup'))
        return True if obj.m_internal else False

    @property
    def info(self):
        """Various information details."""
        CheckParent(self)
        annot = self.this
        res = dict()

        res[dictkey_content] = JM_UnicodeFromStr(mupdf.pdf_annot_contents(annot))

        o = mupdf.pdf_dict_get(mupdf.pdf_annot_obj(annot), PDF_NAME('Name'))
        res[dictkey_name] = JM_UnicodeFromStr(mupdf.pdf_to_name(o))

        # Title (= author)
        o = mupdf.pdf_dict_get(mupdf.pdf_annot_obj(annot), PDF_NAME('T'))
        res[dictkey_title] = JM_UnicodeFromStr(mupdf.pdf_to_text_string(o))

        # CreationDate
        o = mupdf.pdf_dict_gets(mupdf.pdf_annot_obj(annot), "CreationDate")
        res[dictkey_creationDate] = JM_UnicodeFromStr(mupdf.pdf_to_text_string(o))

        # ModDate
        o = mupdf.pdf_dict_get(mupdf.pdf_annot_obj(annot), PDF_NAME('M'))
        res[dictkey_modDate] = JM_UnicodeFromStr(mupdf.pdf_to_text_string(o))

        # Subj
        o = mupdf.pdf_dict_gets(mupdf.pdf_annot_obj(annot), "Subj")
        res[dictkey_subject] = mupdf.pdf_to_text_string(o)

        # Identification (PDF key /NM)
        o = mupdf.pdf_dict_gets(mupdf.pdf_annot_obj(annot), "NM")
        res[dictkey_id] = JM_UnicodeFromStr(mupdf.pdf_to_text_string(o))

        return res

    @property
    def irt_xref(self):
        '''
        annotation IRT xref
        '''
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj( annot)
        irt = mupdf.pdf_dict_get( annot_obj, PDF_NAME('IRT'))
        if not irt.m_internal:
            return 0
        return mupdf.pdf_to_num( irt)

    @property
    def is_open(self):
        """Get 'open' status of annotation or its Popup."""
        CheckParent(self)
        return mupdf.pdf_annot_is_open(self.this)

    @property
    def language(self):
        """annotation language"""
        this_annot = self.this
        lang = mupdf.pdf_annot_language(this_annot)
        if lang == mupdf.FZ_LANG_UNSET:
            return
        assert hasattr(mupdf, 'fz_string_from_text_language2')
        return mupdf.fz_string_from_text_language2(lang)

    @property
    def line_ends(self):
        """Line end codes."""
        CheckParent(self)
        annot = self.this
        # return nothing for invalid annot types
        if not mupdf.pdf_annot_has_line_ending_styles(annot):
            return
        lstart = mupdf.pdf_annot_line_start_style(annot)
        lend = mupdf.pdf_annot_line_end_style(annot)
        return lstart, lend

    @property
    def next(self):
        """Next annotation."""
        CheckParent(self)
        this_annot = self.this
        assert isinstance(this_annot, mupdf.PdfAnnot)
        assert this_annot.m_internal
        type_ = mupdf.pdf_annot_type(this_annot)
        if type_ != mupdf.PDF_ANNOT_WIDGET:
            annot = mupdf.pdf_next_annot(this_annot)
        else:
            annot = mupdf.pdf_next_widget(this_annot)

        val = Annot(annot) if annot.m_internal else None
        if not val:
            return None
        val.thisown = True
        assert val.get_parent().this.m_internal_value() == self.get_parent().this.m_internal_value()
        val.parent._annot_refs[id(val)] = val

        if val.type[0] == mupdf.PDF_ANNOT_WIDGET:
            widget = Widget()
            TOOLS._fill_widget(val, widget)
            val = widget
        return val

    @property
    def opacity(self):
        """Opacity."""
        CheckParent(self)
        annot = self.this
        opy = -1
        ca = mupdf.pdf_dict_get( mupdf.pdf_annot_obj(annot), mupdf.PDF_ENUM_NAME_CA)
        if mupdf.pdf_is_number(ca):
            opy = mupdf.pdf_to_real(ca)
        return opy

    @property
    def popup_rect(self):
        """annotation 'Popup' rectangle"""
        CheckParent(self)
        rect = mupdf.FzRect(mupdf.FzRect.Fixed_INFINITE)
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj( annot)
        obj = mupdf.pdf_dict_get( annot_obj, PDF_NAME('Popup'))
        if obj.m_internal:
            rect = mupdf.pdf_dict_get_rect(obj, PDF_NAME('Rect'))
            #log( '{rect=}')
        val = JM_py_from_rect(rect)
        #log( '{val=}')
        
        val = Rect(val) * self.get_parent().transformation_matrix
        val *= self.get_parent().derotation_matrix
        
        return val

    @property
    def popup_xref(self):
        """annotation 'Popup' xref"""
        CheckParent(self)
        xref = 0
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        obj = mupdf.pdf_dict_get(annot_obj, PDF_NAME('Popup'))
        if obj.m_internal:
            xref = mupdf.pdf_to_num(obj)
        return xref

    @property
    def rect(self):
        """annotation rectangle"""
        if g_use_extra:
            val = extra.Annot_rect3( self.this)
        else:
            val = mupdf.pdf_bound_annot(self.this)
        val = Rect(val)
        
        # Caching self.parent_() reduces 1000x from 0.07 to 0.04.
        #
        p = self.get_parent()
        #p = getattr( self, 'parent', None)
        #if p is None:
        #    p = self.parent
        #    self.parent = p
        #p = self.parent_()
        val *= p.derotation_matrix
        return val

    @property
    def rect_delta(self):
        '''
        annotation delta values to rectangle
        '''
        annot_obj = mupdf.pdf_annot_obj(self.this)
        arr = mupdf.pdf_dict_get( annot_obj, PDF_NAME('RD'))
        if mupdf.pdf_array_len( arr) == 4:
            return (
                    mupdf.pdf_to_real( mupdf.pdf_array_get( arr, 0)),
                    mupdf.pdf_to_real( mupdf.pdf_array_get( arr, 1)),
                    -mupdf.pdf_to_real( mupdf.pdf_array_get( arr, 2)),
                    -mupdf.pdf_to_real( mupdf.pdf_array_get( arr, 3)),
                    )

    @property
    def rotation(self):
        """annotation rotation"""
        CheckParent(self)
        annot = self.this
        rotation = mupdf.pdf_dict_get( mupdf.pdf_annot_obj(annot), mupdf.PDF_ENUM_NAME_Rotate)
        if not rotation.m_internal:
            return -1
        return mupdf.pdf_to_int( rotation)

    def set_apn_bbox(self, bbox):
        """
        Set annotation appearance bbox.
        """
        CheckParent(self)
        page = self.get_parent()
        rot = page.rotation_matrix
        mat = page.transformation_matrix
        bbox *= rot * ~mat
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        ap = mupdf.pdf_dict_getl(annot_obj, PDF_NAME('AP'), PDF_NAME('N'))
        if not ap.m_internal:
            raise RuntimeError( MSG_BAD_APN)
        rect = JM_rect_from_py(bbox)
        mupdf.pdf_dict_put_rect(ap, PDF_NAME('BBox'), rect)

    def set_apn_matrix(self, matrix):
        """Set annotation appearance matrix."""
        CheckParent(self)
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        ap = mupdf.pdf_dict_getl(annot_obj, PDF_NAME('AP'), PDF_NAME('N'))
        if not ap.m_internal:
            raise RuntimeError( MSG_BAD_APN)
        mat = JM_matrix_from_py(matrix)
        mupdf.pdf_dict_put_matrix(ap, PDF_NAME('Matrix'), mat)

    def set_blendmode(self, blend_mode):
        """Set annotation BlendMode."""
        CheckParent(self)
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        mupdf.pdf_dict_put_name(annot_obj, PDF_NAME('BM'), blend_mode)

    def set_border(self, border=None, width=-1, style=None, dashes=None, clouds=-1):
        """Set border properties.

        Either a dict, or direct arguments width, style, dashes or clouds."""
        CheckParent(self)
        atype, atname = self.type[:2]  # annotation type
        if atype not in (
                mupdf.PDF_ANNOT_CIRCLE,
                mupdf.PDF_ANNOT_FREE_TEXT,
                mupdf.PDF_ANNOT_INK,
                mupdf.PDF_ANNOT_LINE,
                mupdf.PDF_ANNOT_POLY_LINE,
                mupdf.PDF_ANNOT_POLYGON,
                mupdf.PDF_ANNOT_SQUARE,
                ):
            message(f"Cannot set border for '{atname}'.")
            return None
        if atype not in (
                mupdf.PDF_ANNOT_CIRCLE,
                mupdf.PDF_ANNOT_FREE_TEXT,
                mupdf.PDF_ANNOT_POLYGON,
                mupdf.PDF_ANNOT_SQUARE,
                ):
            if clouds > 0:
                message(f"Cannot set cloudy border for '{atname}'.")
                clouds = -1  # do not set border effect
        if type(border) is not dict:
            border = {"width": width, "style": style, "dashes": dashes, "clouds": clouds}
        border.setdefault("width", -1)
        border.setdefault("style", None)
        border.setdefault("dashes", None)
        border.setdefault("clouds", -1)
        if border["width"] is None:
            border["width"] = -1
        if border["clouds"] is None:
            border["clouds"] = -1
        if hasattr(border["dashes"], "__getitem__"):  # ensure sequence items are integers
            border["dashes"] = tuple(border["dashes"])
            for item in border["dashes"]:
                if not isinstance(item, int):
                    border["dashes"] = None
                    break
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj( annot)
        pdf = mupdf.pdf_get_bound_document( annot_obj)
        return JM_annot_set_border( border, pdf, annot_obj)

    def set_colors(self, colors=None, stroke=None, fill=None):
        """Set 'stroke' and 'fill' colors.

        Use either a dict or the direct arguments.
        """
        if self.type[0] == mupdf.PDF_ANNOT_FREE_TEXT:
            raise ValueError("cannot be used for FreeText annotations")

        CheckParent(self)
        doc = self.get_parent().parent
        if type(colors) is not dict:
            colors = {"fill": fill, "stroke": stroke}
        fill = colors.get("fill")
        stroke = colors.get("stroke")

        fill_annots = (mupdf.PDF_ANNOT_CIRCLE, mupdf.PDF_ANNOT_SQUARE, mupdf.PDF_ANNOT_LINE, mupdf.PDF_ANNOT_POLY_LINE, mupdf.PDF_ANNOT_POLYGON,
                       mupdf.PDF_ANNOT_REDACT,)

        if stroke in ([], ()):
            doc.xref_set_key(self.xref, "C", "[]")
        elif stroke is not None:
            if hasattr(stroke, "__float__"):
                stroke = [float(stroke)]
            CheckColor(stroke)
            assert len(stroke) in (1, 3, 4)
            s = f"[{_format_g(stroke)}]"
            doc.xref_set_key(self.xref, "C", s)

        if fill and self.type[0] not in fill_annots:
            message("Warning: fill color ignored for annot type '%s'." % self.type[1])
            return
        if fill in ([], ()):
            doc.xref_set_key(self.xref, "IC", "[]")
        elif fill is not None:
            if hasattr(fill, "__float__"):
                fill = [float(fill)]
            CheckColor(fill)
            assert len(fill) in (1, 3, 4)
            s = f"[{_format_g(fill)}]"
            doc.xref_set_key(self.xref, "IC", s)

    def set_flags(self, flags):
        """Set annotation flags."""
        CheckParent(self)
        annot = self.this
        mupdf.pdf_set_annot_flags(annot, flags)

    def set_info(self, info=None, content=None, title=None, creationDate=None, modDate=None, subject=None):
        """Set various properties."""
        CheckParent(self)
        if type(info) is dict:  # build the args from the dictionary
            content = info.get("content", None)
            title = info.get("title", None)
            creationDate = info.get("creationDate", None)
            modDate = info.get("modDate", None)
            subject = info.get("subject", None)
            info = None
        annot = self.this
        # use this to indicate a 'markup' annot type
        is_markup = mupdf.pdf_annot_has_author(annot)
        # contents
        if content:
            mupdf.pdf_set_annot_contents(annot, content)
        if is_markup:
            # title (= author)
            if title:
                mupdf.pdf_set_annot_author(annot, title)
            # creation date
            if creationDate:
                mupdf.pdf_dict_put_text_string(mupdf.pdf_annot_obj(annot), PDF_NAME('CreationDate'), creationDate)
            # mod date
            if modDate:
                mupdf.pdf_dict_put_text_string(mupdf.pdf_annot_obj(annot), PDF_NAME('M'), modDate)
            # subject
            if subject:
                mupdf.pdf_dict_puts(mupdf.pdf_annot_obj(annot), "Subj", mupdf.pdf_new_text_string(subject))

    def set_irt_xref(self, xref):
        '''
        Set annotation IRT xref
        '''
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj( annot)
        page = _pdf_annot_page(annot)
        if xref < 1 or xref >= mupdf.pdf_xref_len( page.doc()):
            raise ValueError( MSG_BAD_XREF)
        irt = mupdf.pdf_new_indirect( page.doc(), xref, 0)
        subt = mupdf.pdf_dict_get( irt, PDF_NAME('Subtype'))
        irt_subt = mupdf.pdf_annot_type_from_string( mupdf.pdf_to_name( subt))
        if irt_subt < 0:
            raise ValueError( MSG_IS_NO_ANNOT)
        mupdf.pdf_dict_put( annot_obj, PDF_NAME('IRT'), irt)

    def set_language(self, language=None):
        """Set annotation language."""
        CheckParent(self)
        this_annot = self.this
        if not language:
            lang = mupdf.FZ_LANG_UNSET
        else:
            lang = mupdf.fz_text_language_from_string(language)
        mupdf.pdf_set_annot_language(this_annot, lang)

    def set_line_ends(self, start, end):
        """Set line end codes."""
        CheckParent(self)
        annot = self.this
        if mupdf.pdf_annot_has_line_ending_styles(annot):
            mupdf.pdf_set_annot_line_ending_styles(annot, start, end)
        else:
            message_warning("bad annot type for line ends")

    def set_name(self, name):
        """Set /Name (icon) of annotation."""
        CheckParent(self)
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        mupdf.pdf_dict_put_name(annot_obj, PDF_NAME('Name'), name)

    def set_oc(self, oc=0):
        """Set / remove annotation OC xref."""
        CheckParent(self)
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        if not oc:
            mupdf.pdf_dict_del(annot_obj, PDF_NAME('OC'))
        else:
            JM_add_oc_object(mupdf.pdf_get_bound_document(annot_obj), annot_obj, oc)

    def set_opacity(self, opacity):
        """Set opacity."""
        CheckParent(self)
        annot = self.this
        if not _INRANGE(opacity, 0.0, 1.0):
            mupdf.pdf_set_annot_opacity(annot, 1)
            return
        mupdf.pdf_set_annot_opacity(annot, opacity)
        if opacity < 1.0:
            page = _pdf_annot_page(annot)
            page.transparency = 1

    def set_open(self, is_open):
        """Set 'open' status of annotation or its Popup."""
        CheckParent(self)
        annot = self.this
        mupdf.pdf_set_annot_is_open(annot, is_open)

    def set_popup(self, rect):
        '''
        Create annotation 'Popup' or update rectangle.
        '''
        CheckParent(self)
        annot = self.this
        pdfpage = _pdf_annot_page(annot)
        rot = JM_rotate_page_matrix(pdfpage)
        r = mupdf.fz_transform_rect(JM_rect_from_py(rect), rot)
        mupdf.pdf_set_annot_popup(annot, r)

    def set_rect(self, rect):
        """Set annotation rectangle."""
        CheckParent(self)
        annot = self.this
        
        pdfpage = _pdf_annot_page(annot)
        rot = JM_rotate_page_matrix(pdfpage)
        r = mupdf.fz_transform_rect(JM_rect_from_py(rect), rot)
        if mupdf.fz_is_empty_rect(r) or mupdf.fz_is_infinite_rect(r):
            raise ValueError( MSG_BAD_RECT)
        try:
            mupdf.pdf_set_annot_rect(annot, r)
        except Exception as e:
            message(f'cannot set rect: {e}')
            return False

    def set_rotation(self, rotate=0):
        """Set annotation rotation."""
        CheckParent(self)
        
        annot = self.this
        type = mupdf.pdf_annot_type(annot)
        if type not in (
                mupdf.PDF_ANNOT_CARET,
                mupdf.PDF_ANNOT_CIRCLE,
                mupdf.PDF_ANNOT_FREE_TEXT,
                mupdf.PDF_ANNOT_FILE_ATTACHMENT,
                mupdf.PDF_ANNOT_INK,
                mupdf.PDF_ANNOT_LINE,
                mupdf.PDF_ANNOT_POLY_LINE,
                mupdf.PDF_ANNOT_POLYGON,
                mupdf.PDF_ANNOT_SQUARE,
                mupdf.PDF_ANNOT_STAMP,
                mupdf.PDF_ANNOT_TEXT,
                ):
            return
        rot = rotate
        while rot < 0:
            rot += 360
        while rot >= 360:
            rot -= 360
        if type == mupdf.PDF_ANNOT_FREE_TEXT and rot % 90 != 0:
            rot = 0
        annot_obj = mupdf.pdf_annot_obj(annot)
        mupdf.pdf_dict_put_int(annot_obj, PDF_NAME('Rotate'), rot)

    @property
    def type(self):
        """annotation type"""
        CheckParent(self)
        if not self.this.m_internal:
            return 'null'
        type_ = mupdf.pdf_annot_type(self.this)
        c = mupdf.pdf_string_from_annot_type(type_)
        o = mupdf.pdf_dict_gets( mupdf.pdf_annot_obj(self.this), 'IT')
        if not o.m_internal or mupdf.pdf_is_name(o):
            return (type_, c)
        it = mupdf.pdf_to_name(o)
        return (type_, c, it)

    def update(self,
            blend_mode: OptStr =None,
            opacity: OptFloat =None,
            fontsize: float =0,
            fontname: OptStr =None,
            text_color: OptSeq =None,
            border_color: OptSeq =None,
            fill_color: OptSeq =None,
            cross_out: bool =True,
            rotate: int =-1,
            ):
        """Update annot appearance.

        Notes:
            Depending on the annot type, some parameters make no sense,
            while others are only available in this method to achieve the
            desired result. This is especially true for 'FreeText' annots.
        Args:
            blend_mode: set the blend mode, all annotations.
            opacity: set the opacity, all annotations.
            fontsize: set fontsize, 'FreeText' only.
            fontname: set the font, 'FreeText' only.
            border_color: set border color, 'FreeText' only.
            text_color: set text color, 'FreeText' only.
            fill_color: set fill color, all annotations.
            cross_out: draw diagonal lines, 'Redact' only.
            rotate: set rotation, 'FreeText' and some others.
        """
        annot_obj = mupdf.pdf_annot_obj(self.this)
        
        if border_color:
            is_rich_text = mupdf.pdf_dict_get(annot_obj, PDF_NAME("RC"))
            if not is_rich_text:
                raise ValueError("cannot set border_color if rich_text is False")
        Annot.update_timing_test()
        CheckParent(self)
        def color_string(cs, code):
            """Return valid PDF color operator for a given color sequence.
            """
            cc = ColorCode(cs, code)
            if not cc:
                return b""
            return (cc + "\n").encode()

        annot_type = self.type[0]  # get the annot type

        dt = self.border.get("dashes", None)  # get the dashes spec
        bwidth = self.border.get("width", -1)  # get border line width
        stroke = self.colors["stroke"]  # get the stroke color
        if fill_color is not None:
            fill = fill_color
        else:
            fill = self.colors["fill"]
        rect = None  # self.rect  # prevent MuPDF fiddling with it
        apnmat = self.apn_matrix  # prevent MuPDF fiddling with it
        if rotate != -1:  # sanitize rotation value
            while rotate < 0:
                rotate += 360
            while rotate >= 360:
                rotate -= 360
            if annot_type == mupdf.PDF_ANNOT_FREE_TEXT and rotate % 90 != 0:
                rotate = 0

        #------------------------------------------------------------------
        # handle opacity and blend mode
        #------------------------------------------------------------------
        if blend_mode is None:
            blend_mode = self.blendmode
        if not hasattr(opacity, "__float__"):
            opacity = self.opacity

        if 0 <= opacity < 1 or blend_mode:
            opa_code = "/H gs\n"  # then we must reference this 'gs'
        else:
            opa_code = ""

        if annot_type == mupdf.PDF_ANNOT_FREE_TEXT:
            CheckColor(text_color)
            CheckColor(fill_color)
            tcol, fname, fsize = TOOLS._parse_da(self)

            # read and update default appearance as necessary
            if fsize <= 0:
                fsize = 12
            if text_color:
                tcol = text_color
            if fontname:
                fname = fontname
            if fontsize > 0:
                fsize = fontsize
            JM_make_annot_DA(self, len(tcol), tcol, fname, fsize)
            blend_mode = None  # not supported for free text annotations!

        #------------------------------------------------------------------
        # now invoke MuPDF to update the annot appearance
        #------------------------------------------------------------------
        val = self._update_appearance(
            opacity=opacity,
            blend_mode=blend_mode,
            fill_color=fill,
            rotate=rotate,
        )
        if val is False:
            raise RuntimeError("Error updating annotation.")

        if annot_type == mupdf.PDF_ANNOT_FREE_TEXT:
            # in absence of previous opacity, we may need to modify the AP
            ap = self._getAP()
            if 0 <= opacity < 1 and not ap.startswith(b"/H gs"):
                self._setAP(b"/H gs\n" + ap)
            return

        bfill = color_string(fill, "f")
        bstroke = color_string(stroke, "c")

        p_ctm = self.get_parent().transformation_matrix
        imat = ~p_ctm  # inverse page transf. matrix

        if dt:
            dashes = "[" + " ".join(map(str, dt)) + "] 0 d\n"
            dashes = dashes.encode("utf-8")
        else:
            dashes = None

        if self.line_ends:
            line_end_le, line_end_ri = self.line_ends
        else:
            line_end_le, line_end_ri = 0, 0  # init line end codes

        # read contents as created by MuPDF
        ap = self._getAP()
        ap_tab = ap.splitlines()  # split in single lines
        ap_updated = False  # assume we did nothing

        if annot_type == mupdf.PDF_ANNOT_REDACT:
            if cross_out:  # create crossed-out rect
                ap_updated = True
                ap_tab = ap_tab[:-1]
                _, LL, LR, UR, UL = ap_tab
                ap_tab.append(LR)
                ap_tab.append(LL)
                ap_tab.append(UR)
                ap_tab.append(LL)
                ap_tab.append(UL)
                ap_tab.append(b"S")

            if bwidth > 0 or bstroke != b"":
                ap_updated = True
                ntab = [_format_g(bwidth).encode() + b" w"] if bwidth > 0 else []
                for line in ap_tab:
                    if line.endswith(b"w"):
                        continue
                    if line.endswith(b"RG") and bstroke != b"":
                        line = bstroke[:-1]
                    ntab.append(line)
                ap_tab = ntab

            ap = b"\n".join(ap_tab)

        if annot_type in (mupdf.PDF_ANNOT_POLYGON, mupdf.PDF_ANNOT_POLY_LINE):
            ap = b"\n".join(ap_tab[:-1]) + b"\n"
            ap_updated = True
            if bfill != b"":
                if annot_type == mupdf.PDF_ANNOT_POLYGON:
                    ap = ap + bfill + b"b"  # close, fill, and stroke
                elif annot_type == mupdf.PDF_ANNOT_POLY_LINE:
                    ap = ap + b"S"  # stroke
            else:
                if annot_type == mupdf.PDF_ANNOT_POLYGON:
                    ap = ap + b"s"  # close and stroke
                elif annot_type == mupdf.PDF_ANNOT_POLY_LINE:
                    ap = ap + b"S"  # stroke

        if dashes is not None:  # handle dashes
            ap = dashes + ap
            # reset dashing - only applies for LINE annots with line ends given
            ap = ap.replace(b"\nS\n", b"\nS\n[] 0 d\n", 1)
            ap_updated = True

        if opa_code:
            ap = opa_code.encode("utf-8") + ap
            ap_updated = True

        ap = b"q\n" + ap + b"\nQ\n"
        #----------------------------------------------------------------------
        # the following handles line end symbols for 'Polygon' and 'Polyline'
        #----------------------------------------------------------------------
        if line_end_le + line_end_ri > 0 and annot_type in (mupdf.PDF_ANNOT_POLYGON, mupdf.PDF_ANNOT_POLY_LINE):

            le_funcs = (None, TOOLS._le_square, TOOLS._le_circle,
                        TOOLS._le_diamond, TOOLS._le_openarrow,
                        TOOLS._le_closedarrow, TOOLS._le_butt,
                        TOOLS._le_ropenarrow, TOOLS._le_rclosedarrow,
                        TOOLS._le_slash)
            le_funcs_range = range(1, len(le_funcs))
            d = 2 * max(1, self.border["width"])
            rect = self.rect + (-d, -d, d, d)
            ap_updated = True
            points = self.vertices
            if line_end_le in le_funcs_range:
                p1 = Point(points[0]) * imat
                p2 = Point(points[1]) * imat
                left = le_funcs[line_end_le](self, p1, p2, False, fill_color)
                ap += left.encode()
            if line_end_ri in le_funcs_range:
                p1 = Point(points[-2]) * imat
                p2 = Point(points[-1]) * imat
                left = le_funcs[line_end_ri](self, p1, p2, True, fill_color)
                ap += left.encode()

        if ap_updated:
            if rect:                        # rect modified here?
                self.set_rect(rect)
                self._setAP(ap, rect=1)
            else:
                self._setAP(ap, rect=0)

        #-------------------------------
        # handle annotation rotations
        #-------------------------------
        if annot_type not in (  # only these types are supported
                mupdf.PDF_ANNOT_CARET,
                mupdf.PDF_ANNOT_CIRCLE,
                mupdf.PDF_ANNOT_FILE_ATTACHMENT,
                mupdf.PDF_ANNOT_INK,
                mupdf.PDF_ANNOT_LINE,
                mupdf.PDF_ANNOT_POLY_LINE,
                mupdf.PDF_ANNOT_POLYGON,
                mupdf.PDF_ANNOT_SQUARE,
                mupdf.PDF_ANNOT_STAMP,
                mupdf.PDF_ANNOT_TEXT,
                ):
            return

        rot = self.rotation  # get value from annot object
        if rot == -1:  # nothing to change
            return

        M = (self.rect.tl + self.rect.br) / 2  # center of annot rect

        if rot == 0:  # undo rotations
            if abs(apnmat - Matrix(1, 1)) < 1e-5:
                return  # matrix already is a no-op
            quad = self.rect.morph(M, ~apnmat)  # derotate rect
            self.setRect(quad.rect)
            self.set_apn_matrix(Matrix(1, 1))  # appearance matrix = no-op
            return

        mat = Matrix(rot)
        quad = self.rect.morph(M, mat)
        self.set_rect(quad.rect)
        self.set_apn_matrix(apnmat * mat)

    def update_file(self, buffer_=None, filename=None, ufilename=None, desc=None):
        """Update attached file."""
        CheckParent(self)
        annot = self.this
        annot_obj = mupdf.pdf_annot_obj(annot)
        pdf = mupdf.pdf_get_bound_document(annot_obj)  # the owning PDF
        type = mupdf.pdf_annot_type(annot)
        if type != mupdf.PDF_ANNOT_FILE_ATTACHMENT:
            raise TypeError( MSG_BAD_ANNOT_TYPE)
        stream = mupdf.pdf_dict_getl(annot_obj, PDF_NAME('FS'), PDF_NAME('EF'), PDF_NAME('F'))
        # the object for file content
        if not stream.m_internal:
            RAISEPY( "bad PDF: no /EF object", JM_Exc_FileDataError)

        fs = mupdf.pdf_dict_get(annot_obj, PDF_NAME('FS'))

        # file content given
        res = JM_BufferFromBytes(buffer_)
        if buffer_ and not res.m_internal:
            raise ValueError( MSG_BAD_BUFFER)
        if res:
            JM_update_stream(pdf, stream, res, 1)
            # adjust /DL and /Size parameters
            len, _ = mupdf.fz_buffer_storage(res)
            l = mupdf.pdf_new_int(len)
            mupdf.pdf_dict_put(stream, PDF_NAME('DL'), l)
            mupdf.pdf_dict_putl(stream, l, PDF_NAME('Params'), PDF_NAME('Size'))

        if filename:
            mupdf.pdf_dict_put_text_string(stream, PDF_NAME('F'), filename)
            mupdf.pdf_dict_put_text_string(fs, PDF_NAME('F'), filename)
            mupdf.pdf_dict_put_text_string(stream, PDF_NAME('UF'), filename)
            mupdf.pdf_dict_put_text_string(fs, PDF_NAME('UF'), filename)
            mupdf.pdf_dict_put_text_string(annot_obj, PDF_NAME('Contents'), filename)

        if ufilename:
            mupdf.pdf_dict_put_text_string(stream, PDF_NAME('UF'), ufilename)
            mupdf.pdf_dict_put_text_string(fs, PDF_NAME('UF'), ufilename)

        if desc:
            mupdf.pdf_dict_put_text_string(stream, PDF_NAME('Desc'), desc)
            mupdf.pdf_dict_put_text_string(fs, PDF_NAME('Desc'), desc)

    @staticmethod
    def update_timing_test():
        total = 0
        for i in range( 30*1000):
            total += i
        return total
    
    @property
    def vertices(self):
        """annotation vertex points"""
        CheckParent(self)
        annot = self.this
        assert isinstance(annot, mupdf.PdfAnnot)
        annot_obj = mupdf.pdf_annot_obj(annot)
        page = _pdf_annot_page(annot)
        page_ctm = mupdf.FzMatrix()   # page transformation matrix
        dummy = mupdf.FzRect()  # Out-param for mupdf.pdf_page_transform().
        mupdf.pdf_page_transform(page, dummy, page_ctm)
        derot = JM_derotate_page_matrix(page)
        page_ctm = mupdf.fz_concat(page_ctm, derot)

        #----------------------------------------------------------------
        # The following objects occur in different annotation types.
        # So we are sure that (!o) occurs at most once.
        # Every pair of floats is one point, that needs to be separately
        # transformed with the page transformation matrix.
        #----------------------------------------------------------------
        o = mupdf.pdf_dict_get(annot_obj, PDF_NAME('Vertices'))
        if not o.m_internal:    o = mupdf.pdf_dict_get(annot_obj, PDF_NAME('L'))
        if not o.m_internal:    o = mupdf.pdf_dict_get(annot_obj, PDF_NAME('QuadPoints'))
        if not o.m_internal:    o = mupdf.pdf_dict_gets(annot_obj, 'CL')
        
        if o.m_internal:
            # handle lists with 1-level depth
            # weiter
            res = []
            for i in range(0, mupdf.pdf_array_len(o), 2):
                x = mupdf.pdf_to_real(mupdf.pdf_array_get(o, i))
                y = mupdf.pdf_to_real(mupdf.pdf_array_get(o, i+1))
                point = mupdf.FzPoint(x, y)
                point = mupdf.fz_transform_point(point, page_ctm)
                res.append( (point.x, point.y))
            return res
            
        o = mupdf.pdf_dict_gets(annot_obj, 'InkList')
        if o.m_internal:
            # InkList has 2-level lists
            #inklist:
            res = []
            for i in range(mupdf.pdf_array_len(o)):
                res1 = []
                o1 = mupdf.pdf_array_get(o, i)
                for j in range(0, mupdf.pdf_array_len(o1), 2):
                    x = mupdf.pdf_to_real(mupdf.pdf_array_get(o1, j))
                    y = mupdf.pdf_to_real(mupdf.pdf_array_get(o1, j+1))
                    point = mupdf.FzPoint(x, y)
                    point = mupdf.fz_transform_point(point, page_ctm)
                    res1.append( (point.x, point.y))
                res.append(res1)
            return res

    @property
    def xref(self):
        """annotation xref number"""
        CheckParent(self)
        annot = self.this
        return mupdf.pdf_to_num(mupdf.pdf_annot_obj(annot))

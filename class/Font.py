"""
Class: fitz.Font

Description: No docstring available.

Inheritance (MRO): Font -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Font =====

# __del__(self)  [function]

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, fontname=None, fontfile=None, fontbuffer=None, script=0, language=None, ordering=-1, is_bold=0, is_italic=0, is_serif=0, embed=1)  [function]
#     -> Initialize self.  See help(type(self)) for accurate signature.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self)  [function]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# ascender = <property object at 0x000002052DE31D50>  [property]

# bbox = <property object at 0x000002052DE31DA0>  [property]

# buffer = <property object at 0x000002052DE31DF0>  [property]

# char_lengths(self, text, fontsize=11, language=None, script=0, wmode=0, small_caps=0)  [function]
#     -> Return tuple of char lengths of unicode 'text' under a fontsize.

# descender = <property object at 0x000002052DE31E40>  [property]

# flags = <property object at 0x000002052DE31E90>  [property]

# glyph_advance(self, chr_, language=None, script=0, wmode=0, small_caps=0)  [function]
#     -> Return the glyph width of a unicode (font size 1).

# glyph_bbox(self, char, language=None, script=0, small_caps=0)  [function]
#     -> Return the glyph bbox of a unicode (font size 1).

# glyph_count = <property object at 0x000002052DE31EE0>  [property]

# glyph_name_to_unicode(self, name)  [function]
#     -> Return the unicode for a glyph name.

# has_glyph(self, chr, language=None, script=0, fallback=0, small_caps=0)  [function]
#     -> Check whether font has a glyph for this unicode.

# is_bold = <property object at 0x000002052DE31F30>  [property]

# is_italic = <property object at 0x000002052DE31F80>  [property]

# is_monospaced = <property object at 0x000002052DE31FD0>  [property]

# is_serif = <property object at 0x000002052DE32020>  [property]

# is_writable = <property object at 0x000002052DE32070>  [property]

# name = <property object at 0x000002052DE320C0>  [property]

# text_length(self, text, fontsize=11, language=None, script=0, wmode=0, small_caps=0)  [function]
#     -> Return length of unicode 'text' under a fontsize.

# unicode_to_glyph_name(self, ch)  [function]
#     -> Return the glyph name for a unicode.

# valid_codepoints(self)  [function]
#     -> Returns sorted list of valid unicodes of a fz_font.


# ===== Source Code =====
class Font:

    def __del__(self):
        if type(self) is not Font:
            return None

    def __init__(
            self,
            fontname=None,
            fontfile=None,
            fontbuffer=None,
            script=0,
            language=None,
            ordering=-1,
            is_bold=0,
            is_italic=0,
            is_serif=0,
            embed=1,
            ):
        
        if fontbuffer:
            if hasattr(fontbuffer, "getvalue"):
                fontbuffer = fontbuffer.getvalue()
            elif isinstance(fontbuffer, bytearray):
                fontbuffer = bytes(fontbuffer)
            if not isinstance(fontbuffer, bytes):
                raise ValueError("bad type: 'fontbuffer'")
        
        if isinstance(fontname, str):
            fname_lower = fontname.lower()
            if "/" in fname_lower or "\\" in fname_lower or "." in fname_lower:
                message("Warning: did you mean a fontfile?")

            if fname_lower in ("cjk", "china-t", "china-ts"):
                ordering = 0

            elif fname_lower.startswith("china-s"):
                ordering = 1
            elif fname_lower.startswith("korea"):
                ordering = 3
            elif fname_lower.startswith("japan"):
                ordering = 2
            elif fname_lower in fitz_fontdescriptors.keys():
                import pymupdf_fonts  # optional fonts
                fontbuffer = pymupdf_fonts.myfont(fname_lower)  # make a copy
                fontname = None  # ensure using fontbuffer only
                del pymupdf_fonts  # remove package again

            elif ordering < 0:
                fontname = Base14_fontdict.get(fontname, fontname)

        lang = mupdf.fz_text_language_from_string(language)
        font = JM_get_font(fontname, fontfile,
                   fontbuffer, script, lang, ordering,
                   is_bold, is_italic, is_serif, embed)
        self.this = font

    def __repr__(self):
        return "Font('%s')" % self.name

    @property
    def ascender(self):
        """Return the glyph ascender value."""
        return mupdf.fz_font_ascender(self.this)

    @property
    def bbox(self):
        return self.this.fz_font_bbox()
    
    @property
    def buffer(self):
        buffer_ = mupdf.FzBuffer( mupdf.ll_fz_keep_buffer( self.this.m_internal.buffer))
        return mupdf.fz_buffer_extract_copy( buffer_)

    def char_lengths(self, text, fontsize=11, language=None, script=0, wmode=0, small_caps=0):
        """Return tuple of char lengths of unicode 'text' under a fontsize."""
        lang = mupdf.fz_text_language_from_string(language)
        rc = []
        for ch in text:
            c = ord(ch)
            if small_caps:
                gid = mupdf.fz_encode_character_sc(self.this, c)
                if gid >= 0:
                    font = self.this
            else:
                gid, font = mupdf.fz_encode_character_with_fallback(self.this, c, script, lang)
            rc.append(fontsize * mupdf.fz_advance_glyph(font, gid, wmode))
        return rc

    @property
    def descender(self):
        """Return the glyph descender value."""
        return mupdf.fz_font_descender(self.this)

    @property
    def flags(self):
        f = mupdf.ll_fz_font_flags(self.this.m_internal)
        if not f:
            return
        assert isinstance( f, mupdf.fz_font_flags_t)
        #log( '{=f}')
        if mupdf_cppyy:
            # cppyy includes remaining higher bits.
            v = [f.is_mono]
            def b(bits):
                ret = v[0] & ((1 << bits)-1)
                v[0] = v[0] >> bits
                return ret
            is_mono = b(1)
            is_serif = b(1)
            is_bold = b(1)
            is_italic = b(1)
            ft_substitute = b(1)
            ft_stretch = b(1)
            fake_bold = b(1)
            fake_italic = b(1)
            has_opentype = b(1)
            invalid_bbox = b(1)
            cjk_lang = b(1)
            embed = b(1)
            never_embed = b(1)
        return {
                "mono":         is_mono if mupdf_cppyy else f.is_mono,
                "serif":        is_serif if mupdf_cppyy else f.is_serif,
                "bold":         is_bold if mupdf_cppyy else f.is_bold,
                "italic":       is_italic if mupdf_cppyy else f.is_italic,
                "substitute":   ft_substitute if mupdf_cppyy else f.ft_substitute,
                "stretch":      ft_stretch if mupdf_cppyy else f.ft_stretch,
                "fake-bold":    fake_bold if mupdf_cppyy else f.fake_bold,
                "fake-italic":  fake_italic if mupdf_cppyy else f.fake_italic,
                "opentype":     has_opentype if mupdf_cppyy else f.has_opentype,
                "invalid-bbox": invalid_bbox if mupdf_cppyy else f.invalid_bbox,
                'cjk':          cjk_lang if mupdf_cppyy else f.cjk,
                'cjk-lang':     cjk_lang if mupdf_cppyy else f.cjk_lang,
                'embed':        embed if mupdf_cppyy else f.embed,
                'never-embed':  never_embed if mupdf_cppyy else f.never_embed,
                }

    def glyph_advance(self, chr_, language=None, script=0, wmode=0, small_caps=0):
        """Return the glyph width of a unicode (font size 1)."""
        lang = mupdf.fz_text_language_from_string(language)
        if small_caps:
            gid = mupdf.fz_encode_character_sc(self.this, chr_)
            if gid >= 0:
                font = self.this
        else:
            gid, font = mupdf.fz_encode_character_with_fallback(self.this, chr_, script, lang)
        return mupdf.fz_advance_glyph(font, gid, wmode)

    def glyph_bbox(self, char, language=None, script=0, small_caps=0):
        """Return the glyph bbox of a unicode (font size 1)."""
        lang = mupdf.fz_text_language_from_string(language)
        if small_caps:
            gid = mupdf.fz_encode_character_sc( self.this, char)
            if gid >= 0:
                font = self.this
        else:
            gid, font = mupdf.fz_encode_character_with_fallback( self.this, char, script, lang)
        return Rect(mupdf.fz_bound_glyph( font, gid, mupdf.FzMatrix()))

    @property
    def glyph_count(self):
        return self.this.m_internal.glyph_count

    def glyph_name_to_unicode(self, name):
        """Return the unicode for a glyph name."""
        return glyph_name_to_unicode(name)

    def has_glyph(self, chr, language=None, script=0, fallback=0, small_caps=0):
        """Check whether font has a glyph for this unicode."""
        if fallback:
            lang = mupdf.fz_text_language_from_string(language)
            gid, font = mupdf.fz_encode_character_with_fallback(self.this, chr, script, lang)
        else:
            if small_caps:
                gid = mupdf.fz_encode_character_sc(self.this, chr)
            else:
                gid = mupdf.fz_encode_character(self.this, chr)
        return gid

    @property
    def is_bold(self):
        return mupdf.fz_font_is_bold( self.this)

    @property
    def is_italic(self):
        return mupdf.fz_font_is_italic( self.this)

    @property
    def is_monospaced(self):
        return mupdf.fz_font_is_monospaced( self.this)

    @property
    def is_serif(self):
        return mupdf.fz_font_is_serif( self.this)

    @property
    def is_writable(self):
        return True # see pymupdf commit ef4056ee4da2
        font = self.this
        flags = mupdf.ll_fz_font_flags(font.m_internal)
        if mupdf_cppyy:
            # cppyy doesn't handle bitfields correctly.
            import cppyy
            ft_substitute = cppyy.gbl.mupdf_mfz_font_flags_ft_substitute( flags)
        else:
            ft_substitute = flags.ft_substitute
        
        if ( mupdf.ll_fz_font_t3_procs(font.m_internal)
                or ft_substitute
                or not mupdf.pdf_font_writing_supported(font)
                ):
            return False
        return True

    @property
    def name(self):
        ret = mupdf.fz_font_name(self.this)
        #log( '{ret=}')
        return ret

    def text_length(self, text, fontsize=11, language=None, script=0, wmode=0, small_caps=0):
        """Return length of unicode 'text' under a fontsize."""
        thisfont = self.this
        lang = mupdf.fz_text_language_from_string(language)
        rc = 0
        if not isinstance(text, str):
            raise TypeError( MSG_BAD_TEXT)
        for ch in text:
            c = ord(ch)
            if small_caps:
                gid = mupdf.fz_encode_character_sc(thisfont, c)
                if gid >= 0:
                    font = thisfont
            else:
                gid, font = mupdf.fz_encode_character_with_fallback(thisfont, c, script, lang)
            rc += mupdf.fz_advance_glyph(font, gid, wmode)
        rc *= fontsize
        return rc

    def unicode_to_glyph_name(self, ch):
        """Return the glyph name for a unicode."""
        return unicode_to_glyph_name(ch)

    def valid_codepoints(self):
        '''
        Returns sorted list of valid unicodes of a fz_font.
        '''
        ucs_gids = mupdf.fz_enumerate_font_cmap2(self.this)
        ucss = [i.ucs for i in ucs_gids]
        ucss_unique = set(ucss)
        ucss_unique_sorted = sorted(ucss_unique)
        return ucss_unique_sorted

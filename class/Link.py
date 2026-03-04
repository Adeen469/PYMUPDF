"""
Class: fitz.Link

Description: No docstring available.

Inheritance (MRO): Link -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Link =====

# __del__(self)  [function]

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, this)  [function]
#     -> Initialize self.  See help(type(self)) for accurate signature.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self)  [function]
#     -> Return repr(self).

# __str__(self)  [function]
#     -> Return str(self).

# border = <property object at 0x000002052DE321B0>  [property]

# colors = <property object at 0x000002052DE32200>  [property]

# dest = <property object at 0x000002052DE32250>  [property]

# flags = <property object at 0x000002052DE322A0>  [property]

# is_external = <property object at 0x000002052DE322F0>  [property]

# next = <property object at 0x000002052DE32340>  [property]

# page = -1  [int]

# rect = <property object at 0x000002052DE32390>  [property]

# set_border(self, border=None, width=0, dashes=None, style=None)  [function]

# set_colors(self, colors=None, stroke=None, fill=None)  [function]
#     -> Set border colors.

# set_flags(self, flags)  [function]

# uri = <property object at 0x000002052DE323E0>  [property]


# ===== Source Code =====
class Link:
    def __del__(self):
        self._erase()

    def __init__( self, this):
        assert isinstance( this, mupdf.FzLink)
        self.this = this

    def __repr__(self):
        CheckParent(self)
        return "link on " + str(self.parent)

    def __str__(self):
        CheckParent(self)
        return "link on " + str(self.parent)

    def _border(self, doc, xref):
        pdf = _as_pdf_document(doc, required=0)
        if not pdf.m_internal:
            return
        link_obj = mupdf.pdf_new_indirect(pdf, xref, 0)
        if not link_obj.m_internal:
            return
        b = JM_annot_border(link_obj)
        return b

    def _colors(self, doc, xref):
        pdf = _as_pdf_document(doc, required=0)
        if not pdf.m_internal:
            return
        link_obj = mupdf.pdf_new_indirect( pdf, xref, 0)
        if not link_obj.m_internal:
            raise ValueError( MSG_BAD_XREF)
        b = JM_annot_colors( link_obj)
        return b

    def _erase(self):
        self.parent = None
        self.thisown = False

    def _setBorder(self, border, doc, xref):
        pdf = _as_pdf_document(doc, required=0)
        if not pdf.m_internal:
            return
        link_obj = mupdf.pdf_new_indirect(pdf, xref, 0)
        if not link_obj.m_internal:
            return
        b = JM_annot_set_border(border, pdf, link_obj)
        return b
        
    @property
    def border(self):
        return self._border(self.parent.parent.this, self.xref)

    @property
    def colors(self):
        return self._colors(self.parent.parent.this, self.xref)

    @property
    def dest(self):
        """Create link destination details."""
        if hasattr(self, "parent") and self.parent is None:
            raise ValueError("orphaned object: parent is None")
        if self.parent.parent.is_closed or self.parent.parent.is_encrypted:
            raise ValueError("document closed or encrypted")
        doc = self.parent.parent

        if self.is_external or self.uri.startswith("#"):
            uri = None
        else:
            uri = doc.resolve_link(self.uri)

        return linkDest(self, uri, doc)

    @property
    def flags(self)->int:
        CheckParent(self)
        doc = self.parent.parent
        if not doc.is_pdf:
            return 0
        f = doc.xref_get_key(self.xref, "F")
        if f[1] != "null":
            return int(f[1])
        return 0

    @property
    def is_external(self):
        """Flag the link as external."""
        CheckParent(self)
        if g_use_extra:
            return extra.Link_is_external( self.this)
        this_link = self.this
        if not this_link.m_internal or not this_link.m_internal.uri:
            return False
        return bool( mupdf.fz_is_external_link( this_link.m_internal.uri))

    @property
    def next(self):
        """Next link."""
        if not self.this.m_internal:
            return None
        CheckParent(self)
        if 0 and g_use_extra:
            val = extra.Link_next( self.this)
        else:
            val = self.this.next()
        if not val.m_internal:
            return None
        val = Link( val)
        if val:
            val.thisown = True
            val.parent = self.parent  # copy owning page from prev link
            val.parent._annot_refs[id(val)] = val
            if self.xref > 0:  # prev link has an xref
                link_xrefs = [x[0] for x in self.parent.annot_xrefs() if x[1] == mupdf.PDF_ANNOT_LINK]
                link_ids = [x[2] for x in self.parent.annot_xrefs() if x[1] == mupdf.PDF_ANNOT_LINK]
                idx = link_xrefs.index(self.xref)
                val.xref = link_xrefs[idx + 1]
                val.id = link_ids[idx + 1]
            else:
                val.xref = 0
                val.id = ""
        return val

    @property
    def rect(self):
        """Rectangle ('hot area')."""
        CheckParent(self)
        # utils.py:getLinkDict() appears to expect exceptions from us, so we
        # ensure that we raise on error.
        if self.this is None or not self.this.m_internal:
            raise Exception( 'self.this.m_internal not available')
        val = JM_py_from_rect( self.this.rect())
        val = Rect(val)
        return val

    def set_border(self, border=None, width=0, dashes=None, style=None):
        if type(border) is not dict:
            border = {"width": width, "style": style, "dashes": dashes}
        return self._setBorder(border, self.parent.parent.this, self.xref)

    def set_colors(self, colors=None, stroke=None, fill=None):
        """Set border colors."""
        CheckParent(self)
        doc = self.parent.parent
        if type(colors) is not dict:
            colors = {"fill": fill, "stroke": stroke}
        fill = colors.get("fill")
        stroke = colors.get("stroke")
        if fill is not None:
            message("warning: links have no fill color")
        if stroke in ([], ()):
            doc.xref_set_key(self.xref, "C", "[]")
            return
        if hasattr(stroke, "__float__"):
            stroke = [float(stroke)]
        CheckColor(stroke)
        assert len(stroke) in (1, 3, 4)
        s = f"[{_format_g(stroke)}]"
        doc.xref_set_key(self.xref, "C", s)

    def set_flags(self, flags):
        CheckParent(self)
        doc = self.parent.parent
        if not doc.is_pdf:
            raise ValueError("is no PDF")
        if not type(flags) is int:
            raise ValueError("bad 'flags' value")
        doc.xref_set_key(self.xref, "F", str(flags))
        return None

    @property
    def uri(self):
        """Uri string."""
        #CheckParent(self)
        if g_use_extra:
            return extra.link_uri(self.this)
        this_link = self.this
        return this_link.m_internal.uri if this_link.m_internal else ''

    page = -1

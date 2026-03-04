"""
Class: fitz.Page

Description: No docstring available.

Inheritance (MRO): Page -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Page =====

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, page, document)  [function]
#     -> Initialize self.  See help(type(self)) for accurate signature.

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self)  [function]
#     -> Return repr(self).

# __str__(self)  [function]
#     -> Return str(self).

# add_caret_annot(self, point: 'point_like') -> pymupdf.Annot  [function]
#     -> Add a 'Caret' annotation.

# add_circle_annot(self, rect: 'rect_like') -> pymupdf.Annot  [function]
#     -> Add a 'Circle' (ellipse, oval) annotation.

# add_file_annot(self, point: 'point_like', buffer_: ByteString, filename: str, ufilename: Optional[str] = None, desc: Optional[str] = None, icon: Optional[str] = None) -> pymupdf.Annot  [function]
#     -> Add a 'FileAttachment' annotation.

# add_freetext_annot(self, rect: 'rect_like', text: str, *, fontsize: float = 11, fontname: Optional[str] = None, text_color: Optional[Sequence] = None, fill_color: Optional[Sequence] = None, border_color: Optional[Sequence] = None, border_width: float = 0, dashes: Optional[Sequence] = None, callout: Optional[Sequence] = None, line_end: int = 4, opacity: float = 1, align: int = 0, rotate: int = 0, richtext=False, style=None) -> pymupdf.Annot  [function]
#     -> Add a 'FreeText' annotation.

# add_highlight_annot(self, quads=None, start=None, stop=None, clip=None) -> pymupdf.Annot  [function]
#     -> Add a 'Highlight' annotation.

# add_ink_annot(self, handwriting: list) -> pymupdf.Annot  [function]
#     -> Add a 'Ink' ('handwriting') annotation.

# add_line_annot(self, p1: 'point_like', p2: 'point_like') -> pymupdf.Annot  [function]
#     -> Add a 'Line' annotation.

# add_polygon_annot(self, points: list) -> pymupdf.Annot  [function]
#     -> Add a 'Polygon' annotation.

# add_polyline_annot(self, points: list) -> pymupdf.Annot  [function]
#     -> Add a 'PolyLine' annotation.

# add_rect_annot(self, rect: 'rect_like') -> pymupdf.Annot  [function]
#     -> Add a 'Square' (rectangle) annotation.

# add_redact_annot(self, quad, text: Optional[str] = None, fontname: Optional[str] = None, fontsize: float = 11, align: int = 0, fill: Optional[Sequence] = None, text_color: Optional[Sequence] = None, cross_out: bool = True) -> pymupdf.Annot  [function]
#     -> Add a 'Redact' annotation.

# add_squiggly_annot(self, quads=None, start=None, stop=None, clip=None) -> pymupdf.Annot  [function]
#     -> Add a 'Squiggly' annotation.

# add_stamp_annot(self, rect: 'rect_like', stamp=0) -> pymupdf.Annot  [function]
#     -> Add a ('rubber') 'Stamp' annotation.

# add_strikeout_annot(self, quads=None, start=None, stop=None, clip=None) -> pymupdf.Annot  [function]
#     -> Add a 'StrikeOut' annotation.

# add_text_annot(self, point: 'point_like', text: str, icon: str = 'Note') -> pymupdf.Annot  [function]
#     -> Add a 'Text' (sticky note) annotation.

# add_underline_annot(self, quads=None, start=None, stop=None, clip=None) -> pymupdf.Annot  [function]
#     -> Add a 'Underline' annotation.

# add_widget(self, widget: pymupdf.Widget) -> pymupdf.Annot  [function]
#     -> Add a 'Widget' (form field).

# annot_names(self)  [function]
#     -> page get list of annot names

# annot_xrefs(self)  [function]
#     -> List of xref numbers of annotations, fields and links.

# annots(self, types=None)  [function]
#     -> Generator over the annotations of a page.

# apply_redactions(page: 'Page', images: int = 2, graphics: int = 1, text: int = 0) -> bool  [function]
#     -> Apply the redaction annotations of the page.

# artbox = <property object at 0x000002052DE329D0>  [property]

# bleedbox = <property object at 0x000002052DE32A20>  [property]

# bound(self)  [function]
#     -> Get page rectangle.

# clean_contents(self, sanitize=1)  [function]

# clip_to_rect(self, rect)  [function]
#     -> Clip away page content outside the rectangle.

# cluster_drawings(self, clip=None, drawings=None, x_tolerance: float = 3, y_tolerance: float = 3, final_filter: bool = True) -> list  [function]
#     -> Join rectangles of neighboring vector graphic items.

# cropbox = <property object at 0x000002052DE32A70>  [property]

# cropbox_position = <property object at 0x000002052DE32AC0>  [property]

# delete_annot(self, annot)  [function]
#     -> Delete annot and return next one.

# delete_image(page: 'Page', xref: int)  [function]
#     -> Delete the image referred to by xef.

# delete_link(self, linkdict)  [function]
#     -> Delete a Link.

# delete_widget(page: 'Page', widget: pymupdf.Widget) -> pymupdf.Widget  [function]
#     -> Delete widget from page and return the next one.

# derotation_matrix = <property object at 0x000002052DE32B10>  [property]

# draw_bezier(page: 'Page', p1: 'point_like', p2: 'point_like', p3: 'point_like', p4: 'point_like', color: Optional[Sequence] = (0,), fill: Optional[Sequence] = None, dashes: Optional[str] = None, width: float = 1, morph: Optional[str] = None, closePath: bool = False, lineCap: int = 0, lineJoin: int = 0, overlay: bool = True, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0) -> 'Point_forward_decl'  [function]
#     -> Draw a general cubic Bezier curve from p1 to p4 using control points p2 and p3.

# draw_circle(page: 'Page', center: 'point_like', radius: float, color: Optional[Sequence] = (0,), fill: Optional[Sequence] = None, morph: Optional[Sequence] = None, dashes: Optional[str] = None, width: float = 1, lineCap: int = 0, lineJoin: int = 0, overlay: bool = True, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0) -> 'Point_forward_decl'  [function]
#     -> Draw a circle given its center and radius.

# draw_curve(page: 'Page', p1: 'point_like', p2: 'point_like', p3: 'point_like', color: Optional[Sequence] = (0,), fill: Optional[Sequence] = None, dashes: Optional[str] = None, width: float = 1, morph: Optional[Sequence] = None, closePath: bool = False, lineCap: int = 0, lineJoin: int = 0, overlay: bool = True, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0) -> 'Point_forward_decl'  [function]
#     -> Draw a special Bezier curve from p1 to p3, generating control points on lines p1 to p2 and p2 to p3.

# draw_line(page: 'Page', p1: 'point_like', p2: 'point_like', color: Optional[Sequence] = (0,), dashes: Optional[str] = None, width: float = 1, lineCap: int = 0, lineJoin: int = 0, overlay: bool = True, morph: Optional[Sequence] = None, stroke_opacity: float = 1, fill_opacity: float = 1, oc=0) -> 'Point_forward_decl'  [function]
#     -> Draw a line from point p1 to point p2.

# draw_oval(page: 'Page', rect: Union[ForwardRef('rect_like'), ForwardRef('quad_like')], color: Optional[Sequence] = (0,), fill: Optional[Sequence] = None, dashes: Optional[str] = None, morph: Optional[Sequence] = None, width: float = 1, lineCap: int = 0, lineJoin: int = 0, overlay: bool = True, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0) -> 'Point_forward_decl'  [function]
#     -> Draw an oval given its containing rectangle or quad.

# draw_polyline(page: 'Page', points: list, color: Optional[Sequence] = (0,), fill: Optional[Sequence] = None, dashes: Optional[str] = None, width: float = 1, morph: Optional[Sequence] = None, lineCap: int = 0, lineJoin: int = 0, overlay: bool = True, closePath: bool = False, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0) -> 'Point_forward_decl'  [function]
#     -> Draw multiple connected line segments.

# draw_quad(page: 'Page', quad: 'quad_like', color: Optional[Sequence] = (0,), fill: Optional[Sequence] = None, dashes: Optional[str] = None, width: float = 1, lineCap: int = 0, lineJoin: int = 0, morph: Optional[Sequence] = None, overlay: bool = True, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0) -> 'Point_forward_decl'  [function]
#     -> Draw a quadrilateral.

# draw_rect(page: 'Page', rect: 'rect_like', color: Optional[Sequence] = (0,), fill: Optional[Sequence] = None, dashes: Optional[str] = None, width: float = 1, lineCap: int = 0, lineJoin: int = 0, morph: Optional[Sequence] = None, overlay: bool = True, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0, radius=None) -> 'Point_forward_decl'  [function]
#     -> Draw a rectangle. See Shape class method for details.

# draw_sector(page: 'Page', center: 'point_like', point: 'point_like', beta: float, color: Optional[Sequence] = (0,), fill: Optional[Sequence] = None, dashes: Optional[str] = None, fullSector: bool = True, morph: Optional[Sequence] = None, width: float = 1, closePath: bool = False, lineCap: int = 0, lineJoin: int = 0, overlay: bool = True, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0) -> 'Point_forward_decl'  [function]
#     -> Draw a circle sector given circle center, one arc end point and the angle of the arc.

# draw_squiggle(page: 'Page', p1: 'point_like', p2: 'point_like', breadth: float = 2, color: Optional[Sequence] = (0,), dashes: Optional[str] = None, width: float = 1, lineCap: int = 0, lineJoin: int = 0, overlay: bool = True, morph: Optional[Sequence] = None, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0) -> 'Point_forward_decl'  [function]
#     -> Draw a squiggly line from point p1 to point p2.

# draw_zigzag(page: 'Page', p1: 'point_like', p2: 'point_like', breadth: float = 2, color: Optional[Sequence] = (0,), dashes: Optional[str] = None, width: float = 1, lineCap: int = 0, lineJoin: int = 0, overlay: bool = True, morph: Optional[Sequence] = None, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0) -> 'Point_forward_decl'  [function]
#     -> Draw a zigzag line from point p1 to point p2.

# extend_textpage(self, tpage, flags=0, matrix=None)  [function]

# find_tables(page, clip=None, vertical_strategy: str = 'lines', horizontal_strategy: str = 'lines', vertical_lines: list = None, horizontal_lines: list = None, snap_tolerance: float = 3, snap_x_tolerance: float = None, snap_y_tolerance: float = None, join_tolerance: float = 3, join_x_tolerance: float = None, join_y_tolerance: float = None, edge_min_length: float = 3, min_words_vertical: float = 3, min_words_horizontal: float = 1, intersection_tolerance: float = 3, intersection_x_tolerance: float = None, intersection_y_tolerance: float = None, text_tolerance=3, text_x_tolerance=3, text_y_tolerance=3, strategy=None, add_lines=None, add_boxes=None, paths=None)  [function]

# first_annot = <property object at 0x000002052DE32B60>  [property]

# first_link = <property object at 0x000002052DE32BB0>  [property]

# first_widget = <property object at 0x000002052DE32C00>  [property]

# get_bboxlog(self, layers=None)  [function]

# get_cdrawings(self, extended=None, callback=None, method=None)  [function]
#     -> Extract vector graphics ("line art") from the page.

# get_contents(self)  [function]
#     -> Get xrefs of /Contents objects.

# get_displaylist(self, annots=1)  [function]
#     -> Make a DisplayList from the page for Pixmap generation.

# get_drawings(self, extended: bool = False) -> list  [function]
#     -> Retrieve vector graphics. The extended version includes clips.

# get_fonts(self, full=False)  [function]
#     -> List of fonts defined in the page object.

# get_image_bbox(self, name, transform=0)  [function]
#     -> Get rectangle occupied by image 'name'.

# get_image_info(page: 'Page', hashes: bool = False, xrefs: bool = False) -> list  [function]
#     -> Extract image information only from a pymupdf.TextPage.

# get_image_rects(page: 'Page', name, transform=False) -> list  [function]
#     -> Return list of image positions on a page.

# get_images(self, full=False)  [function]
#     -> List of images defined in the page object.

# get_label(page)  [function]
#     -> Return the label for this PDF page.

# get_layout(self)  [function]
#     -> Try to access layout information.

# get_links(page: 'Page') -> list  [function]
#     -> Create a list of all links contained in a PDF page.

# get_oc_items(self) -> list  [function]
#     -> Get OCGs and OCMDs used in the page's contents.

# get_pixmap(page: 'Page', *, matrix: 'matrix_like' = IdentityMatrix(1.0, 0.0, 0.0, 1.0, 0.0, 0.0), dpi=None, colorspace: pymupdf.Colorspace = None, clip: 'rect_like' = None, alpha: bool = False, annots: bool = True) -> 'Pixmap'  [function]
#     -> Create pixmap of page.

# get_svg_image(self, matrix=None, text_as_path=1)  [function]
#     -> Make SVG image from page.

# get_text(self, *args, **kwargs)  [function]

# get_text_blocks(self, *args, **kwargs)  [function]

# get_text_selection(self, *args, **kwargs)  [function]

# get_text_words(self, *args, **kwargs)  [function]

# get_textbox(page: 'Page_forward_decl', rect: 'rect_like', textpage=None) -> str  [function]

# get_textpage(self, clip: 'rect_like' = None, flags: int = 0, matrix=None) -> 'TextPage'  [function]

# get_textpage_ocr(self, *args, **kwargs)  [function]

# get_texttrace(self)  [function]

# get_xobjects(self)  [function]
#     -> List of xobjects defined in the page object.

# insert_font(self, fontname='helv', fontfile=None, fontbuffer=None, set_simple=False, wmode=0, encoding=0)  [function]

# insert_htmlbox(page, rect, text, *, css=None, scale_low=0, archive=None, rotate=0, oc=0, opacity=1, overlay=True, _scale_word_width=True, _verbose=False) -> tuple  [function]
#     -> Insert text with optional HTML tags and stylings into a rectangle.

# insert_image(page, rect, *, alpha=-1, filename=None, height=0, keep_proportion=True, mask=None, oc=0, overlay=True, pixmap=None, rotate=0, stream=None, width=0, xref=0)  [function]
#     -> Insert an image for display in a rectangle.

# insert_link(page: 'Page', lnk: dict, mark: bool = True) -> None  [function]
#     -> Insert a new link for the current page.

# insert_text(page: 'Page', point: 'point_like', text: Union[str, list], *, fontsize: float = 11, lineheight: Optional[float] = None, fontname: str = 'helv', fontfile: Optional[str] = None, set_simple: int = 0, encoding: int = 0, color: Optional[Sequence] = None, fill: Optional[Sequence] = None, border_width: float = 0.05, miter_limit: float = 1, render_mode: int = 0, rotate: int = 0, morph: Optional[Sequence] = None, overlay: bool = True, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0)  [function]

# insert_textbox(page: 'Page', rect: 'rect_like', buffer: Union[str, list], *, fontname: str = 'helv', fontfile: Optional[str] = None, set_simple: int = 0, encoding: int = 0, fontsize: float = 11, lineheight: Optional[float] = None, color: Optional[Sequence] = None, fill: Optional[Sequence] = None, expandtabs: int = 1, align: int = 0, rotate: int = 0, render_mode: int = 0, miter_limit: float = 1, border_width: float = 0.05, morph: Optional[Sequence] = None, overlay: bool = True, stroke_opacity: float = 1, fill_opacity: float = 1, oc: int = 0) -> float  [function]
#     -> Insert text into a given rectangle.

# is_wrapped = <property object at 0x000002052DE32C50>  [property]

# language = <property object at 0x000002052DE32CA0>  [property]

# layout_information = None  [NoneType]

# links(self, kinds=None)  [function]
#     -> Generator over the links of a page.

# load_annot(self, ident: Union[str, int]) -> pymupdf.Annot  [function]
#     -> Load an annot by name (/NM key) or xref.

# load_links(self)  [function]
#     -> Get first Link.

# load_widget(self, xref)  [function]
#     -> Load a widget by its xref.

# mediabox = <property object at 0x000002052DE32CF0>  [property]

# mediabox_size = <property object at 0x000002052DE32D40>  [property]

# new_shape(self)  [function]

# read_contents(self)  [function]
#     -> All /Contents streams concatenated to one bytes object.

# recolor(self, components=1)  [function]
#     -> Convert colorspaces of objects on the page.

# rect = <property object at 0x000002052DE32F70>  [property]

# refresh(self)  [function]
#     -> Refresh page after link/annot/widget updates.

# remove_rotation(self)  [function]
#     -> Set page rotation to 0 while maintaining visual appearance.

# replace_image(page: 'Page', xref: int, *, filename=None, pixmap=None, stream=None)  [function]
#     -> Replace the image referred to by xref.

# rotation = <property object at 0x000002052DE32DE0>  [property]

# rotation_matrix = <property object at 0x000002052DE32E30>  [property]

# run(self, dw, m)  [function]
#     -> Run page through a device.

# search_for(page, text, *, clip=None, quads=False, flags=None, textpage=None) -> list  [function]
#     -> Search for a string on a page.

# set_artbox(self, rect)  [function]
#     -> Set the ArtBox.

# set_bleedbox(self, rect)  [function]
#     -> Set the BleedBox.

# set_contents(self, xref)  [function]
#     -> Set object at 'xref' as the page's /Contents.

# set_cropbox(self, rect)  [function]
#     -> Set the CropBox. Will also change Page.rect.

# set_language(self, language=None)  [function]
#     -> Set PDF page default language.

# set_mediabox(self, rect)  [function]
#     -> Set the MediaBox.

# set_rotation(self, rotation)  [function]
#     -> Set page rotation.

# set_trimbox(self, rect)  [function]
#     -> Set the TrimBox.

# show_pdf_page(page, rect, docsrc, pno=0, keep_proportion=True, overlay=True, oc=0, rotate=0, clip=None) -> int  [function]
#     -> Show page number 'pno' of PDF 'docsrc' in rectangle 'rect'.

# transformation_matrix = <property object at 0x000002052DE32E80>  [property]

# trimbox = <property object at 0x000002052DE32ED0>  [property]

# update_link(page: 'Page', lnk: dict) -> None  [function]
#     -> Update a link on the current page.

# widgets(self, types=None)  [function]
#     -> Generator over the widgets of a page.

# wrap_contents(self)  [function]
#     -> Ensure page is in a balanced graphics state.

# write_text(page: 'Page', rect=None, writers=None, overlay=True, color=None, opacity=None, keep_proportion=True, rotate=0, oc=0) -> None  [function]
#     -> Write the text of one or more pymupdf.TextWriter objects.

# xref = <property object at 0x000002052DE32F20>  [property]


# ===== Source Code =====
class Page:

    def __init__(self, page, document):
        assert isinstance(page, (mupdf.FzPage, mupdf.PdfPage)), f'page is: {page}'
        self.this = page
        self.thisown = True
        self.last_point = None
        self.draw_cont = ''
        self._annot_refs = dict()
        self.parent = document
        if page.m_internal:
            if isinstance( page, mupdf.PdfPage):
                self.number = page.m_internal.super.number
            else:
                self.number = page.m_internal.number
        else:
            self.number = None

    def __repr__(self):
        return self.__str__()
        CheckParent(self)
        x = self.parent.name
        if self.parent.stream is not None:
            x = "<memory, doc# %i>" % (self.parent._graft_id,)
        if x == "":
            x = "<new PDF, doc# %i>" % self.parent._graft_id
        return "page %s of %s" % (self.number, x)

    def __str__(self):
        #CheckParent(self)
        parent = getattr(self, 'parent', None)
        if isinstance(self.this.m_internal, mupdf.pdf_page):
            number = self.this.m_internal.super.number
        else:
            number = self.this.m_internal.number
        ret = f'page {number}'
        if parent:
            x = self.parent.name
            if self.parent.stream is not None:
                x = "<memory, doc# %i>" % (self.parent._graft_id,)
            if x == "":
                x = "<new PDF, doc# %i>" % self.parent._graft_id
            ret += f' of {x}'
        return ret

    def _add_caret_annot(self, point):
        if g_use_extra:
            annot = extra._add_caret_annot( self.this, JM_point_from_py(point))
        else:
            page = self._pdf_page()
            annot = mupdf.pdf_create_annot(page, mupdf.PDF_ANNOT_CARET)
            if point:
                p = JM_point_from_py(point)
                r = mupdf.pdf_annot_rect(annot)
                r = mupdf.FzRect(p.x, p.y, p.x + r.x1 - r.x0, p.y + r.y1 - r.y0)
                mupdf.pdf_set_annot_rect(annot, r)
            mupdf.pdf_update_annot(annot)
            JM_add_annot_id(annot, "A")
        return annot

    def _add_file_annot(self, point, buffer_, filename, ufilename=None, desc=None, icon=None):
        page = self._pdf_page()
        uf = ufilename if ufilename else filename
        d = desc if desc else filename
        p = JM_point_from_py(point)
        filebuf = JM_BufferFromBytes(buffer_)
        if not filebuf.m_internal:
            raise TypeError( MSG_BAD_BUFFER)
        annot = mupdf.pdf_create_annot(page, mupdf.PDF_ANNOT_FILE_ATTACHMENT)
        r = mupdf.pdf_annot_rect(annot)
        r = mupdf.fz_make_rect(p.x, p.y, p.x + r.x1 - r.x0, p.y + r.y1 - r.y0)
        mupdf.pdf_set_annot_rect(annot, r)
        flags = mupdf.PDF_ANNOT_IS_PRINT
        mupdf.pdf_set_annot_flags(annot, flags)

        if icon:
            mupdf.pdf_set_annot_icon_name(annot, icon)

        val = JM_embed_file(page.doc(), filebuf, filename, uf, d, 1)
        mupdf.pdf_dict_put(mupdf.pdf_annot_obj(annot), PDF_NAME('FS'), val)
        mupdf.pdf_dict_put_text_string(mupdf.pdf_annot_obj(annot), PDF_NAME('Contents'), filename)
        mupdf.pdf_update_annot(annot)
        mupdf.pdf_set_annot_rect(annot, r)
        mupdf.pdf_set_annot_flags(annot, flags)
        JM_add_annot_id(annot, "A")
        return Annot(annot)

    def _add_freetext_annot(
            self, rect,
            text,
            fontsize=11,
            fontname=None,
            text_color=None,
            fill_color=None,
            border_color=None,
            border_width=0,
            dashes=None,
            callout=None,
            line_end=mupdf.PDF_ANNOT_LE_OPEN_ARROW,
            opacity=1,
            align=0,
            rotate=0,
            richtext=False,
            style=None,
            ):
        rc = f"""<?xml version="1.0"?>
            <body xmlns="http://www.w3.org/1999/xtml"
            xmlns:xfa="http://www.xfa.org/schema/xfa-data/1.0/"
            xfa:contentType="text/html" xfa:APIVersion="Acrobat:8.0.0" xfa:spec="2.4">
            {text}"""
        page = self._pdf_page()
        if border_color and not richtext:
            raise ValueError("cannot set border_color if rich_text is False")
        if border_color and not text_color:
            text_color = border_color
        nfcol, fcol = JM_color_FromSequence(fill_color)
        ntcol, tcol = JM_color_FromSequence(text_color)
        r = JM_rect_from_py(rect)
        if mupdf.fz_is_infinite_rect(r) or mupdf.fz_is_empty_rect(r):
            raise ValueError( MSG_BAD_RECT)
        annot = mupdf.pdf_create_annot(page, mupdf.PDF_ANNOT_FREE_TEXT)
        annot_obj = mupdf.pdf_annot_obj(annot)

        #insert text as 'contents' or 'RC' depending on 'richtext'
        if not richtext:
            mupdf.pdf_set_annot_contents(annot, text)
        else:
            mupdf.pdf_dict_put_text_string(annot_obj,PDF_NAME("RC"), rc)
            if style:
                mupdf.pdf_dict_put_text_string(annot_obj,PDF_NAME("DS"), style)

        mupdf.pdf_set_annot_rect(annot, r)

        while rotate < 0:
            rotate += 360
        while rotate >= 360:
            rotate -= 360
        if rotate != 0:
            mupdf.pdf_dict_put_int(annot_obj, PDF_NAME('Rotate'), rotate)

        mupdf.pdf_set_annot_quadding(annot, align)

        if nfcol > 0:
            mupdf.pdf_set_annot_color(annot, fcol[:nfcol])

        mupdf.pdf_set_annot_border_width(annot, border_width)
        mupdf.pdf_set_annot_opacity(annot, opacity)
        if dashes:
            for d in dashes:
                mupdf.pdf_add_annot_border_dash_item(annot, float(d))

        # Insert callout information
        if callout:
            mupdf.pdf_dict_put(annot_obj, PDF_NAME("IT"), PDF_NAME("FreeTextCallout"))
            mupdf.pdf_set_annot_callout_style(annot, line_end)
            point_count = len(callout)
            extra.JM_set_annot_callout_line(annot, tuple(callout), point_count)

        # insert the default appearance string
        if not richtext:
            JM_make_annot_DA(annot, ntcol, tcol, fontname, fontsize)

        mupdf.pdf_update_annot(annot)
        JM_add_annot_id(annot, "A")
        val = Annot(annot)
        return val

    def _add_ink_annot(self, list):
        page = _as_pdf_page(self.this)
        if not PySequence_Check(list):
            raise ValueError( MSG_BAD_ARG_INK_ANNOT)
        ctm = mupdf.FzMatrix()
        mupdf.pdf_page_transform(page, mupdf.FzRect(0), ctm)
        inv_ctm = mupdf.fz_invert_matrix(ctm)
        annot = mupdf.pdf_create_annot(page, mupdf.PDF_ANNOT_INK)
        annot_obj = mupdf.pdf_annot_obj(annot)
        n0 = len(list)
        inklist = mupdf.pdf_new_array(page.doc(), n0)

        for j in range(n0):
            sublist = list[j]
            n1 = len(sublist)
            stroke = mupdf.pdf_new_array(page.doc(), 2 * n1)

            for i in range(n1):
                p = sublist[i]
                if not PySequence_Check(p) or PySequence_Size(p) != 2:
                    raise ValueError( MSG_BAD_ARG_INK_ANNOT)
                point = mupdf.fz_transform_point(JM_point_from_py(p), inv_ctm)
                mupdf.pdf_array_push_real(stroke, point.x)
                mupdf.pdf_array_push_real(stroke, point.y)

            mupdf.pdf_array_push(inklist, stroke)

        mupdf.pdf_dict_put(annot_obj, PDF_NAME('InkList'), inklist)
        mupdf.pdf_update_annot(annot)
        JM_add_annot_id(annot, "A")
        return Annot(annot)

    def _add_line_annot(self, p1, p2):
        page = self._pdf_page()
        annot = mupdf.pdf_create_annot(page, mupdf.PDF_ANNOT_LINE)
        a = JM_point_from_py(p1)
        b = JM_point_from_py(p2)
        mupdf.pdf_set_annot_line(annot, a, b)
        mupdf.pdf_update_annot(annot)
        JM_add_annot_id(annot, "A")
        assert annot.m_internal
        return Annot(annot)

    def _add_multiline(self, points, annot_type):
        page = self._pdf_page()
        if len(points) < 2:
            raise ValueError( MSG_BAD_ARG_POINTS)
        annot = mupdf.pdf_create_annot(page, annot_type)
        for p in points:
            if (PySequence_Size(p) != 2):
                raise ValueError( MSG_BAD_ARG_POINTS)
            point = JM_point_from_py(p)
            mupdf.pdf_add_annot_vertex(annot, point)

        mupdf.pdf_update_annot(annot)
        JM_add_annot_id(annot, "A")
        return Annot(annot)

    def _add_redact_annot(self, quad, text=None, da_str=None, align=0, fill=None, text_color=None):
        page = self._pdf_page()
        fcol = [ 1, 1, 1, 0]
        nfcol = 0
        annot = mupdf.pdf_create_annot(page, mupdf.PDF_ANNOT_REDACT)
        q = JM_quad_from_py(quad)
        r = mupdf.fz_rect_from_quad(q)
        # TODO calculate de-rotated rect
        mupdf.pdf_set_annot_rect(annot, r)
        if fill:
            nfcol, fcol = JM_color_FromSequence(fill)
            arr = mupdf.pdf_new_array(page.doc(), nfcol)
            for i in range(nfcol):
                mupdf.pdf_array_push_real(arr, fcol[i])
            mupdf.pdf_dict_put(mupdf.pdf_annot_obj(annot), PDF_NAME('IC'), arr)
        if text:
            assert da_str
            mupdf.pdf_dict_puts(
                    mupdf.pdf_annot_obj(annot),
                    "OverlayText",
                    mupdf.pdf_new_text_string(text),
                    )
            mupdf.pdf_dict_put_text_string(mupdf.pdf_annot_obj(annot), PDF_NAME('DA'), da_str)
            mupdf.pdf_dict_put_int(mupdf.pdf_annot_obj(annot), PDF_NAME('Q'), align)
        mupdf.pdf_update_annot(annot)
        JM_add_annot_id(annot, "A")
        annot = mupdf.ll_pdf_keep_annot(annot.m_internal)
        annot = mupdf.PdfAnnot( annot)
        return Annot(annot)

    def _add_square_or_circle(self, rect, annot_type):
        page = self._pdf_page()
        r = JM_rect_from_py(rect)
        if mupdf.fz_is_infinite_rect(r) or mupdf.fz_is_empty_rect(r):
            raise ValueError( MSG_BAD_RECT)
        annot = mupdf.pdf_create_annot(page, annot_type)
        mupdf.pdf_set_annot_rect(annot, r)
        mupdf.pdf_update_annot(annot)
        JM_add_annot_id(annot, "A")
        assert annot.m_internal
        return Annot(annot)

    def _add_stamp_annot(self, rect, stamp=0):
        rect = Rect(rect)
        r = JM_rect_from_py(rect)
        if mupdf.fz_is_infinite_rect(r) or mupdf.fz_is_empty_rect(r):
            raise ValueError(MSG_BAD_RECT)
        page = self._pdf_page()
        stamp_id = [
                "Approved",
                "AsIs",
                "Confidential",
                "Departmental",
                "Experimental",
                "Expired",
                "Final",
                "ForComment",
                "ForPublicRelease",
                "NotApproved",
                "NotForPublicRelease",
                "Sold",
                "TopSecret",
                "Draft",
                ]
        n = len(stamp_id)
        buf = None
        name = None
        if stamp in range(n):
            name = stamp_id[stamp]
        elif isinstance(stamp, Pixmap):
            buf = stamp.tobytes()
        elif isinstance(stamp, str):
            buf = pathlib.Path(stamp).read_bytes()
        elif isinstance(stamp, (bytes, bytearray)):
            buf = stamp
        elif isinstance(stamp, io.BytesIO):
            buf = stamp.getvalue()
        else:
            name = stamp_id[0]

        annot = mupdf.pdf_create_annot(page, mupdf.PDF_ANNOT_STAMP)
        if buf:  # image stamp
            fzbuff = mupdf.fz_new_buffer_from_copied_data(buf)
            img = mupdf.fz_new_image_from_buffer(fzbuff)

            # compute image boundary box on page
            w, h = img.w(), img.h()
            scale = min(rect.width / w, rect.height / h)
            width = w * scale  # bbox width
            height = h * scale  # bbox height

            # center of "rect"
            center = (rect.tl + rect.br) / 2
            x0 = center.x - width / 2
            y0 = center.y - height / 2
            x1 = x0 + width
            y1 = y0 + height
            r = mupdf.fz_make_rect(x0, y0, x1, y1)
            mupdf.pdf_set_annot_rect(annot, r)
            mupdf.pdf_set_annot_stamp_image(annot, img)
            mupdf.pdf_dict_put(mupdf.pdf_annot_obj(annot), PDF_NAME("Name"), mupdf.pdf_new_name("ImageStamp"))
            mupdf.pdf_set_annot_contents(annot, "Image Stamp")
        else:  # text stamp
            mupdf.pdf_set_annot_rect(annot, r)
            mupdf.pdf_dict_put(mupdf.pdf_annot_obj(annot), PDF_NAME("Name"), PDF_NAME(name))
            mupdf.pdf_set_annot_contents(annot, name)
        mupdf.pdf_update_annot(annot)
        JM_add_annot_id(annot, "A")
        return Annot(annot)

    def _add_text_annot(self, point, text, icon=None):
        page = self._pdf_page()
        p = JM_point_from_py( point)
        annot = mupdf.pdf_create_annot(page, mupdf.PDF_ANNOT_TEXT)
        r = mupdf.pdf_annot_rect(annot)
        r = mupdf.fz_make_rect(p.x, p.y, p.x + r.x1 - r.x0, p.y + r.y1 - r.y0)
        mupdf.pdf_set_annot_rect(annot, r)
        mupdf.pdf_set_annot_contents(annot, text)
        if icon:
            mupdf.pdf_set_annot_icon_name(annot, icon)
        mupdf.pdf_update_annot(annot)
        JM_add_annot_id(annot, "A")
        return Annot(annot)

    def _add_text_marker(self, quads, annot_type):

        CheckParent(self)
        if not self.parent.is_pdf:
            raise ValueError("is no PDF")

        val = Page__add_text_marker(self, quads, annot_type)
        if not val:
            return None
        val.parent = weakref.proxy(self)
        self._annot_refs[id(val)] = val

        return val

    def _addAnnot_FromString(self, linklist):
        """Add links from list of object sources."""
        CheckParent(self)
        if g_use_extra:
            self.__class__._addAnnot_FromString = extra.Page_addAnnot_FromString
            #log('Page._addAnnot_FromString() deferring to extra.Page_addAnnot_FromString().')
            return extra.Page_addAnnot_FromString( self.this, linklist)
        page = _as_pdf_page(self.this)
        lcount = len(linklist)  # link count
        if lcount < 1:
            return
        i = -1

        # insert links from the provided sources
        if not isinstance(linklist, tuple):
            raise ValueError( "bad 'linklist' argument")
        if not mupdf.pdf_dict_get( page.obj(), PDF_NAME('Annots')).m_internal:
            mupdf.pdf_dict_put_array( page.obj(), PDF_NAME('Annots'), lcount)
        annots = mupdf.pdf_dict_get( page.obj(), PDF_NAME('Annots'))
        assert annots.m_internal, f'{lcount=} {annots.m_internal=}'
        for i in range(lcount):
            txtpy = linklist[i]
            text = JM_StrAsChar(txtpy)
            if not text:
                message("skipping bad link / annot item %i.", i)
                continue
            try:
                annot = mupdf.pdf_add_object( page.doc(), JM_pdf_obj_from_str( page.doc(), text))
                ind_obj = mupdf.pdf_new_indirect( page.doc(), mupdf.pdf_to_num( annot), 0)
                mupdf.pdf_array_push( annots, ind_obj)
            except Exception:
                if g_exceptions_verbose:    exception_info()
                message("skipping bad link / annot item %i.\n" % i)

    def _addWidget(self, field_type, field_name):
        page = self._pdf_page()
        pdf = page.doc()
        annot = JM_create_widget(pdf, page, field_type, field_name)
        if not annot.m_internal:
            raise RuntimeError( "cannot create widget")
        JM_add_annot_id(annot, "W")
        return Annot(annot)

    def _apply_redactions(self, text, images, graphics):
        page = self._pdf_page()
        opts = mupdf.PdfRedactOptions()
        opts.black_boxes = 0  # no black boxes
        opts.text = text  # how to treat text
        opts.image_method = images  # how to treat images
        opts.line_art = graphics  # how to treat vector graphics
        success = mupdf.pdf_redact_page(page.doc(), page, opts)
        return success

    def _erase(self):
        self._reset_annot_refs()
        try:
            self.parent._forget_page(self)
        except Exception:
            exception_info()
            pass
        self.parent = None
        self.thisown = False
        self.number = None
        self.this = None

    def _count_q_balance(self):
        """Count missing graphic state pushs and pops.

        Returns:
            A pair of integers (push, pop). Push is the number of missing
            PDF "q" commands, pop is the number of "Q" commands.
            A balanced graphics state for the page will be reached if its
            /Contents is prepended with 'push' copies of string "q\n"
            and appended with 'pop' copies of "\nQ".
        """
        page = _as_pdf_page(self)  # need the underlying PDF page
        res = mupdf.pdf_dict_get(  # access /Resources
            page.obj(),
            mupdf.PDF_ENUM_NAME_Resources,
        )
        cont = mupdf.pdf_dict_get(  # access /Contents
            page.obj(),
            mupdf.PDF_ENUM_NAME_Contents,
        )
        pdf = _as_pdf_document(self.parent)  # need underlying PDF document

        # return value of MuPDF function
        return mupdf.pdf_count_q_balance_outparams_fn(pdf, res, cont)

    def _get_optional_content(self, oc: OptInt) -> OptStr:
        if oc is None or oc == 0:
            return None
        doc = self.parent
        check = doc.xref_object(oc, compressed=True)
        if not ("/Type/OCG" in check or "/Type/OCMD" in check):
            #log( 'raising "bad optional content"')
            raise ValueError("bad optional content: 'oc'")
        #log( 'Looking at self._get_resource_properties()')
        props = {}
        for p, x in self._get_resource_properties():
            props[x] = p
        if oc in props.keys():
            return props[oc]
        i = 0
        mc = "MC%i" % i
        while mc in props.values():
            i += 1
            mc = "MC%i" % i
        self._set_resource_property(mc, oc)
        #log( 'returning {mc=}')
        return mc

    def _get_resource_properties(self):
        '''
        page list Resource/Properties
        '''
        page = self._pdf_page()
        rc = JM_get_resource_properties(page.obj())
        return rc

    def _get_textpage(self, clip=None, flags=0, matrix=None):
        if 1 or g_use_extra:
            ll_tpage = extra.page_get_textpage(self.this, clip, flags, matrix)
            tpage = mupdf.FzStextPage(ll_tpage)
            return tpage
        page = self.this
        options = mupdf.FzStextOptions(flags)
        rect = JM_rect_from_py(clip)
        # Default to page's rect if `clip` not specified, for #2048.
        rect = mupdf.fz_bound_page(page) if clip is None else JM_rect_from_py(clip)
        ctm = JM_matrix_from_py(matrix)
        tpage = mupdf.FzStextPage(rect)
        dev = mupdf.fz_new_stext_device(tpage, options)
        if _globals.no_device_caching:
            mupdf.fz_enable_device_hints( dev, mupdf.FZ_NO_CACHE)
        if isinstance(page, mupdf.FzPage):
            pass
        elif isinstance(page, mupdf.PdfPage):
            page = page.super()
        else:
            assert 0, f'Unrecognised {type(page)=}'
        mupdf.fz_run_page(page, dev, ctm, mupdf.FzCookie())
        mupdf.fz_close_device(dev)
        return tpage

    def _insert_image(self,
            filename=None, pixmap=None, stream=None, imask=None, clip=None,
            overlay=1, rotate=0, keep_proportion=1, oc=0, width=0, height=0,
            xref=0, alpha=-1, _imgname=None, digests=None
            ):
        maskbuf = mupdf.FzBuffer()
        page = self._pdf_page()
        # This will create an empty PdfDocument with a call to
        # pdf_new_document() then assign page.doc()'s return value to it (which
        # drop the original empty pdf_document).
        pdf = page.doc()
        w = width
        h = height
        img_xref = xref
        rc_digest = 0

        do_process_pixmap = 1
        do_process_stream = 1
        do_have_imask = 1
        do_have_image = 1
        do_have_xref = 1

        if xref > 0:
            ref = mupdf.pdf_new_indirect(pdf, xref, 0)
            w = mupdf.pdf_to_int( mupdf.pdf_dict_geta( ref, PDF_NAME('Width'), PDF_NAME('W')))
            h = mupdf.pdf_to_int( mupdf.pdf_dict_geta( ref, PDF_NAME('Height'), PDF_NAME('H')))
            if w + h == 0:
                raise ValueError( MSG_IS_NO_IMAGE)
            #goto have_xref()
            do_process_pixmap = 0
            do_process_stream = 0
            do_have_imask = 0
            do_have_image = 0

        else:
            if stream:
                imgbuf = JM_BufferFromBytes(stream)
                do_process_pixmap = 0
            else:
                if filename:
                    imgbuf = mupdf.fz_read_file(filename)
                    #goto have_stream()
                    do_process_pixmap = 0

        if do_process_pixmap:
            #log( 'do_process_pixmap')
            # process pixmap ---------------------------------
            arg_pix = pixmap.this
            w = arg_pix.w()
            h = arg_pix.h()
            digest = mupdf.fz_md5_pixmap2(arg_pix)
            md5_py = digest
            temp = digests.get(md5_py, None)
            if temp is not None:
                img_xref = temp
                ref = mupdf.pdf_new_indirect(page.doc(), img_xref, 0)
                #goto have_xref()
                do_process_stream = 0
                do_have_imask = 0
                do_have_image = 0
            else:
                if arg_pix.alpha() == 0:
                    image = mupdf.fz_new_image_from_pixmap(arg_pix, mupdf.FzImage())
                else:
                    pm = mupdf.fz_convert_pixmap(
                            arg_pix,
                            mupdf.FzColorspace(),
                            mupdf.FzColorspace(),
                            mupdf.FzDefaultColorspaces(None),
                            mupdf.FzColorParams(),
                            1,
                            )
                    pm.alpha = 0
                    pm.colorspace = None
                    mask = mupdf.fz_new_image_from_pixmap(pm, mupdf.FzImage())
                    image = mupdf.fz_new_image_from_pixmap(arg_pix, mask)
                #goto have_image()
                do_process_stream = 0
                do_have_imask = 0

        if do_process_stream:
            #log( 'do_process_stream')
            # process stream ---------------------------------
            state = mupdf.FzMd5()
            if mupdf_cppyy:
                mupdf.fz_md5_update_buffer( state, imgbuf)
            else:
                mupdf.fz_md5_update(state, imgbuf.m_internal.data, imgbuf.m_internal.len)
            if imask:
                maskbuf = JM_BufferFromBytes(imask)
                if mupdf_cppyy:
                    mupdf.fz_md5_update_buffer( state, maskbuf)
                else:
                    mupdf.fz_md5_update(state, maskbuf.m_internal.data, maskbuf.m_internal.len)
            digest = mupdf.fz_md5_final2(state)
            md5_py = bytes(digest)
            temp = digests.get(md5_py, None)
            if temp is not None:
                img_xref = temp
                ref = mupdf.pdf_new_indirect(page.doc(), img_xref, 0)
                w = mupdf.pdf_to_int( mupdf.pdf_dict_geta( ref, PDF_NAME('Width'), PDF_NAME('W')))
                h = mupdf.pdf_to_int( mupdf.pdf_dict_geta( ref, PDF_NAME('Height'), PDF_NAME('H')))
                #goto have_xref()
                do_have_imask = 0
                do_have_image = 0
            else:
                image = mupdf.fz_new_image_from_buffer(imgbuf)
                w = image.w()
                h = image.h()
                if not imask:
                    #goto have_image()
                    do_have_imask = 0

        if do_have_imask:
            # `fz_compressed_buffer` is reference counted and
            # `mupdf.fz_new_image_from_compressed_buffer2()`
            # is povided as a Swig-friendly wrapper for
            # `fz_new_image_from_compressed_buffer()`, so we can do things
            # straightfowardly.
            #
            cbuf1 = mupdf.fz_compressed_image_buffer( image)
            if not cbuf1.m_internal:
                raise ValueError( "uncompressed image cannot have mask")
            bpc = image.bpc()
            colorspace = image.colorspace()
            xres, yres = mupdf.fz_image_resolution(image)
            mask = mupdf.fz_new_image_from_buffer(maskbuf)
            image = mupdf.fz_new_image_from_compressed_buffer2(
                    w,
                    h,
                    bpc,
                    colorspace,
                    xres,
                    yres,
                    1,  # interpolate
                    0,  # imagemask,
                    list(), # decode
                    list(), # colorkey
                    cbuf1,
                    mask,
                    )
            
        if do_have_image:
            #log( 'do_have_image')
            ref = mupdf.pdf_add_image(pdf, image)
            if oc:
                JM_add_oc_object(pdf, ref, oc)
            img_xref = mupdf.pdf_to_num(ref)
            digests[md5_py] = img_xref
            rc_digest = 1

        if do_have_xref:
            #log( 'do_have_xref')
            resources = mupdf.pdf_dict_get_inheritable(page.obj(), PDF_NAME('Resources'))
            if not resources.m_internal:
                resources = mupdf.pdf_dict_put_dict(page.obj(), PDF_NAME('Resources'), 2)
            xobject = mupdf.pdf_dict_get(resources, PDF_NAME('XObject'))
            if not xobject.m_internal:
                xobject = mupdf.pdf_dict_put_dict(resources, PDF_NAME('XObject'), 2)
            mat = calc_image_matrix(w, h, clip, rotate, keep_proportion)
            mupdf.pdf_dict_puts(xobject, _imgname, ref)
            nres = mupdf.fz_new_buffer(50)
            s = f"\nq\n{_format_g((mat.a, mat.b, mat.c, mat.d, mat.e, mat.f))} cm\n/{_imgname} Do\nQ\n"
            #s = s.replace('\n', '\r\n')
            mupdf.fz_append_string(nres, s)
            JM_insert_contents(pdf, page.obj(), nres, overlay)

        if rc_digest:
            return img_xref, digests
        else:
            return img_xref, None

    def _insertFont(self, fontname, bfname, fontfile, fontbuffer, set_simple, idx, wmode, serif, encoding, ordering):
        page = self._pdf_page()
        pdf = page.doc()

        value = JM_insert_font(pdf, bfname, fontfile,fontbuffer, set_simple, idx, wmode, serif, encoding, ordering)
        # get the objects /Resources, /Resources/Font
        resources = mupdf.pdf_dict_get_inheritable(page.obj(), PDF_NAME('Resources'))
        if not resources.pdf_is_dict():
            resources = mupdf.pdf_dict_put_dict(page.obj(), PDF_NAME("Resources"), 5)
        fonts = mupdf.pdf_dict_get(resources, PDF_NAME('Font'))
        if not fonts.m_internal:    # page has no fonts yet
            fonts = mupdf.pdf_new_dict(pdf, 5)
            mupdf.pdf_dict_putl(page.obj(), fonts, PDF_NAME('Resources'), PDF_NAME('Font'))
        # store font in resources and fonts objects will contain named reference to font
        _, xref = JM_INT_ITEM(value, 0)
        if not xref:
            raise RuntimeError( "cannot insert font")
        font_obj = mupdf.pdf_new_indirect(pdf, xref, 0)
        mupdf.pdf_dict_puts(fonts, fontname, font_obj)
        return value

    def _load_annot(self, name, xref):
        page = self._pdf_page()
        if xref == 0:
            annot = JM_get_annot_by_name(page, name)
        else:
            annot = JM_get_annot_by_xref(page, xref)
        if annot.m_internal:
            return Annot(annot)

    def _makePixmap(self, doc, ctm, cs, alpha=0, annots=1, clip=None):
        pix = JM_pixmap_from_page(doc, self.this, ctm, cs, alpha, annots, clip)
        return Pixmap(pix)

    def _other_box(self, boxtype):
        rect = mupdf.FzRect( mupdf.FzRect.Fixed_INFINITE)
        page = _as_pdf_page(self.this, required=False)
        if page.m_internal:
            obj = mupdf.pdf_dict_gets( page.obj(), boxtype)
            if mupdf.pdf_is_array(obj):
                rect = mupdf.pdf_to_rect(obj)
        if mupdf.fz_is_infinite_rect( rect):
            return
        return JM_py_from_rect(rect)

    def _pdf_page(self, required=True):
        return _as_pdf_page(self.this, required=required)

    def _reset_annot_refs(self):
        """Invalidate / delete all annots of this page."""
        self._annot_refs.clear()

    def _set_opacity(self, gstate=None, CA=1, ca=1, blendmode=None):

        if CA >= 1 and ca >= 1 and blendmode is None:
            return
        tCA = int(round(max(CA , 0) * 100))
        if tCA >= 100:
            tCA = 99
        tca = int(round(max(ca, 0) * 100))
        if tca >= 100:
            tca = 99
        gstate = "fitzca%02i%02i" % (tCA, tca)

        if not gstate:
            return
        page = _as_pdf_page(self.this)
        resources = mupdf.pdf_dict_get(page.obj(), PDF_NAME('Resources'))
        if not resources.m_internal:
            resources = mupdf.pdf_dict_put_dict(page.obj(), PDF_NAME('Resources'), 2)
        extg = mupdf.pdf_dict_get(resources, PDF_NAME('ExtGState'))
        if not extg.m_internal:
            extg = mupdf.pdf_dict_put_dict(resources, PDF_NAME('ExtGState'), 2)
        n = mupdf.pdf_dict_len(extg)
        for i in range(n):
            o1 = mupdf.pdf_dict_get_key(extg, i)
            name = mupdf.pdf_to_name(o1)
            if name == gstate:
                return gstate
        opa = mupdf.pdf_new_dict(page.doc(), 3)
        mupdf.pdf_dict_put_real(opa, PDF_NAME('CA'), CA)
        mupdf.pdf_dict_put_real(opa, PDF_NAME('ca'), ca)
        mupdf.pdf_dict_puts(extg, gstate, opa)
        return gstate

    def _set_pagebox(self, boxtype, rect):
        doc = self.parent
        if doc is None:
            raise ValueError("orphaned object: parent is None")

        if not doc.is_pdf:
            raise ValueError("is no PDF")

        valid_boxes = ("CropBox", "BleedBox", "TrimBox", "ArtBox")

        if boxtype not in valid_boxes:
            raise ValueError("bad boxtype")

        rect = Rect(rect)
        mb = self.mediabox
        rect = Rect(rect[0], mb.y1 - rect[3], rect[2], mb.y1 - rect[1])
        if not (mb.x0 <= rect.x0 < rect.x1 <= mb.x1 and mb.y0 <= rect.y0 < rect.y1 <= mb.y1):
            raise ValueError(f"{boxtype} not in MediaBox")

        doc.xref_set_key(self.xref, boxtype, f"[{_format_g(tuple(rect))}]")

    def _set_resource_property(self, name, xref):
        page = self._pdf_page()
        JM_set_resource_property(page.obj(), name, xref)

    def _show_pdf_page(self, fz_srcpage, overlay=1, matrix=None, xref=0, oc=0, clip=None, graftmap=None, _imgname=None):
        cropbox = JM_rect_from_py(clip)
        mat = JM_matrix_from_py(matrix)
        rc_xref = xref
        tpage = _as_pdf_page(self.this)
        tpageref = tpage.obj()
        pdfout = tpage.doc()    # target PDF
        ENSURE_OPERATION(pdfout)
        #-------------------------------------------------------------
        # convert the source page to a Form XObject
        #-------------------------------------------------------------
        xobj1 = JM_xobject_from_page(pdfout, fz_srcpage, xref, graftmap.this)
        if not rc_xref:
            rc_xref = mupdf.pdf_to_num(xobj1)

        #-------------------------------------------------------------
        # create referencing XObject (controls display on target page)
        #-------------------------------------------------------------
        # fill reference to xobj1 into the /Resources
        #-------------------------------------------------------------
        subres1 = mupdf.pdf_new_dict(pdfout, 5)
        mupdf.pdf_dict_puts(subres1, "fullpage", xobj1)
        subres = mupdf.pdf_new_dict(pdfout, 5)
        mupdf.pdf_dict_put(subres, PDF_NAME('XObject'), subres1)

        res = mupdf.fz_new_buffer(20)
        mupdf.fz_append_string(res, "/fullpage Do")

        xobj2 = mupdf.pdf_new_xobject(pdfout, cropbox, mat, subres, res)
        if oc > 0:
            JM_add_oc_object(pdfout, mupdf.pdf_resolve_indirect(xobj2), oc)

        #-------------------------------------------------------------
        # update target page with xobj2:
        #-------------------------------------------------------------
        # 1. insert Xobject in Resources
        #-------------------------------------------------------------
        resources = mupdf.pdf_dict_get_inheritable(tpageref, PDF_NAME('Resources'))
        if not resources.m_internal:
            resources = mupdf.pdf_dict_put_dict(tpageref,PDF_NAME('Resources'), 5)
        subres = mupdf.pdf_dict_get(resources, PDF_NAME('XObject'))
        if not subres.m_internal:
            subres = mupdf.pdf_dict_put_dict(resources, PDF_NAME('XObject'), 5)

        mupdf.pdf_dict_puts(subres, _imgname, xobj2)

        #-------------------------------------------------------------
        # 2. make and insert new Contents object
        #-------------------------------------------------------------
        nres = mupdf.fz_new_buffer(50) # buffer for Do-command
        mupdf.fz_append_string(nres, " q /")   # Do-command
        mupdf.fz_append_string(nres, _imgname)
        mupdf.fz_append_string(nres, " Do Q ")

        JM_insert_contents(pdfout, tpageref, nres, overlay)
        return rc_xref

    def add_caret_annot(self, point: point_like) -> Annot:
        """Add a 'Caret' annotation."""
        old_rotation = annot_preprocess(self)
        try:
            annot = self._add_caret_annot(point)
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        annot = Annot( annot)
        annot_postprocess(self, annot)
        assert hasattr( annot, 'parent')
        return annot

    def add_circle_annot(self, rect: rect_like) -> Annot:
        """Add a 'Circle' (ellipse, oval) annotation."""
        old_rotation = annot_preprocess(self)
        try:
            annot = self._add_square_or_circle(rect, mupdf.PDF_ANNOT_CIRCLE)
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        annot_postprocess(self, annot)
        return annot

    def add_file_annot(
            self,
            point: point_like,
            buffer_: ByteString,
            filename: str,
            ufilename: OptStr =None,
            desc: OptStr =None,
            icon: OptStr =None
            ) -> Annot:
        """Add a 'FileAttachment' annotation."""
        old_rotation = annot_preprocess(self)
        try:
            annot = self._add_file_annot(point,
                    buffer_,
                    filename,
                    ufilename=ufilename,
                    desc=desc,
                    icon=icon,
                    )
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        annot_postprocess(self, annot)
        return annot

    def add_freetext_annot(
            self,
            rect: rect_like,
            text: str,
            *,
            fontsize: float =11,
            fontname: OptStr =None,
            text_color: OptSeq =None,
            fill_color: OptSeq =None,
            border_color: OptSeq =None,
            border_width: float =0,
            dashes: OptSeq =None,
            callout: OptSeq =None,
            line_end: int=mupdf.PDF_ANNOT_LE_OPEN_ARROW,
            opacity: float =1,
            align: int =0,
            rotate: int =0,
            richtext=False,
            style=None,
            ) -> Annot:
        """Add a 'FreeText' annotation."""

        old_rotation = annot_preprocess(self)
        try:
            annot = self._add_freetext_annot(
                    rect,
                    text,
                    fontsize=fontsize,
                    fontname=fontname,
                    text_color=text_color,
                    fill_color=fill_color,
                    border_color=border_color,
                    border_width=border_width,
                    dashes=dashes,
                    callout=callout,
                    line_end=line_end,
                    opacity=opacity,
                    align=align,
                    rotate=rotate,
                    richtext=richtext,
                    style=style,
                    )
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        annot_postprocess(self, annot)
        return annot

    def add_highlight_annot(self, quads=None, start=None,
                          stop=None, clip=None) -> Annot:
        """Add a 'Highlight' annotation."""
        if quads is None:
            q = get_highlight_selection(self, start=start, stop=stop, clip=clip)
        else:
            q = CheckMarkerArg(quads)
        ret = self._add_text_marker(q, mupdf.PDF_ANNOT_HIGHLIGHT)
        return ret

    def add_ink_annot(self, handwriting: list) -> Annot:
        """Add a 'Ink' ('handwriting') annotation.

        The argument must be a list of lists of point_likes.
        """
        old_rotation = annot_preprocess(self)
        try:
            annot = self._add_ink_annot(handwriting)
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        annot_postprocess(self, annot)
        return annot

    def add_line_annot(self, p1: point_like, p2: point_like) -> Annot:
        """Add a 'Line' annotation."""
        old_rotation = annot_preprocess(self)
        try:
            annot = self._add_line_annot(p1, p2)
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        annot_postprocess(self, annot)
        return annot

    def add_polygon_annot(self, points: list) -> Annot:
        """Add a 'Polygon' annotation."""
        old_rotation = annot_preprocess(self)
        try:
            annot = self._add_multiline(points, mupdf.PDF_ANNOT_POLYGON)
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        annot_postprocess(self, annot)
        return annot

    def add_polyline_annot(self, points: list) -> Annot:
        """Add a 'PolyLine' annotation."""
        old_rotation = annot_preprocess(self)
        try:
            annot = self._add_multiline(points, mupdf.PDF_ANNOT_POLY_LINE)
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        annot_postprocess(self, annot)
        return annot

    def add_rect_annot(self, rect: rect_like) -> Annot:
        """Add a 'Square' (rectangle) annotation."""
        old_rotation = annot_preprocess(self)
        try:
            annot = self._add_square_or_circle(rect, mupdf.PDF_ANNOT_SQUARE)
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        annot_postprocess(self, annot)
        return annot

    def add_redact_annot(
            self,
            quad,
            text: OptStr =None,
            fontname: OptStr =None,
            fontsize: float =11,
            align: int =0,
            fill: OptSeq =None,
            text_color: OptSeq =None,
            cross_out: bool =True,
            ) -> Annot:
        """Add a 'Redact' annotation."""
        da_str = None
        if text and not set(string.whitespace).issuperset(text):
            CheckColor(fill)
            CheckColor(text_color)
            if not fontname:
                fontname = "Helv"
            if not fontsize:
                fontsize = 11
            if not text_color:
                text_color = (0, 0, 0)
            if hasattr(text_color, "__float__"):
                text_color = (text_color, text_color, text_color)
            if len(text_color) > 3:
                text_color = text_color[:3]
            fmt = "{:g} {:g} {:g} rg /{f:s} {s:g} Tf"
            da_str = fmt.format(*text_color, f=fontname, s=fontsize)
            if fill is None:
                fill = (1, 1, 1)
            if fill:
                if hasattr(fill, "__float__"):
                    fill = (fill, fill, fill)
                if len(fill) > 3:
                    fill = fill[:3]
        else:
            text = None

        old_rotation = annot_preprocess(self)
        try:
            annot = self._add_redact_annot(quad, text=text, da_str=da_str,
                       align=align, fill=fill)
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        annot_postprocess(self, annot)
        #-------------------------------------------------------------
        # change appearance to show a crossed-out rectangle
        #-------------------------------------------------------------
        if cross_out:
            ap_tab = annot._getAP().splitlines()[:-1]  # get the 4 commands only
            _, LL, LR, UR, UL = ap_tab
            ap_tab.append(LR)
            ap_tab.append(LL)
            ap_tab.append(UR)
            ap_tab.append(LL)
            ap_tab.append(UL)
            ap_tab.append(b"S")
            ap = b"\n".join(ap_tab)
            annot._setAP(ap, 0)
        return annot

    def add_squiggly_annot(
            self,
            quads=None,
            start=None,
            stop=None,
            clip=None,
            ) -> Annot:
        """Add a 'Squiggly' annotation."""
        if quads is None:
            q = get_highlight_selection(self, start=start, stop=stop, clip=clip)
        else:
            q = CheckMarkerArg(quads)
        return self._add_text_marker(q, mupdf.PDF_ANNOT_SQUIGGLY)

    def add_stamp_annot(self, rect: rect_like, stamp=0) -> Annot:
        """Add a ('rubber') 'Stamp' annotation."""
        old_rotation = annot_preprocess(self)
        try:
            annot = self._add_stamp_annot(rect, stamp)
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        annot_postprocess(self, annot)
        return annot

    def add_strikeout_annot(self, quads=None, start=None, stop=None, clip=None) -> Annot:
        """Add a 'StrikeOut' annotation."""
        if quads is None:
            q = get_highlight_selection(self, start=start, stop=stop, clip=clip)
        else:
            q = CheckMarkerArg(quads)
        return self._add_text_marker(q, mupdf.PDF_ANNOT_STRIKE_OUT)

    def add_text_annot(self, point: point_like, text: str, icon: str ="Note") -> Annot:
        """Add a 'Text' (sticky note) annotation."""
        old_rotation = annot_preprocess(self)
        try:
            annot = self._add_text_annot(point, text, icon=icon)
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        annot_postprocess(self, annot)
        return annot

    def add_underline_annot(self, quads=None, start=None, stop=None, clip=None) -> Annot:
        """Add a 'Underline' annotation."""
        if quads is None:
            q = get_highlight_selection(self, start=start, stop=stop, clip=clip)
        else:
            q = CheckMarkerArg(quads)
        return self._add_text_marker(q, mupdf.PDF_ANNOT_UNDERLINE)

    def add_widget(self, widget: Widget) -> Annot:
        """Add a 'Widget' (form field)."""
        CheckParent(self)
        doc = self.parent
        if not doc.is_pdf:
            raise ValueError("is no PDF")
        widget._validate()
        annot = self._addWidget(widget.field_type, widget.field_name)
        if not annot:
            return None
        annot.thisown = True
        annot.parent = weakref.proxy(self) # owning page object
        self._annot_refs[id(annot)] = annot
        widget.parent = annot.parent
        widget._annot = annot
        widget.update()
        return annot

    def annot_names(self):
        '''
        page get list of annot names
        '''
        """List of names of annotations, fields and links."""
        CheckParent(self)
        page = self._pdf_page(required=False)
        if not page.m_internal:
            return []
        return JM_get_annot_id_list(page)

    def annot_xrefs(self):
        '''
        List of xref numbers of annotations, fields and links.
        '''
        return JM_get_annot_xref_list2(self)
    
    def annots(self, types=None):
        """ Generator over the annotations of a page.

        Args:
            types: (list) annotation types to subselect from. If none,
                   all annotations are returned. E.g. types=[PDF_ANNOT_LINE]
                   will only yield line annotations.
        """
        skip_types = (mupdf.PDF_ANNOT_LINK, mupdf.PDF_ANNOT_POPUP, mupdf.PDF_ANNOT_WIDGET)
        if not hasattr(types, "__getitem__"):
            annot_xrefs = [a[0] for a in self.annot_xrefs() if a[1] not in skip_types]
        else:
            annot_xrefs = [a[0] for a in self.annot_xrefs() if a[1] in types and a[1] not in skip_types]
        for xref in annot_xrefs:
            annot = self.load_annot(xref)
            annot._yielded=True
            yield annot

    def apply_redactions(
            page: 'Page',
            images: int = 2,
            graphics: int = 1,
            text: int = 0,
            ) -> bool:
        """Apply the redaction annotations of the page.

        Args:
            page: the PDF page.
            images:
                  0 - ignore images
                  1 - remove all overlapping images
                  2 - blank out overlapping image parts
                  3 - remove image unless invisible
            graphics:
                  0 - ignore graphics
                  1 - remove graphics if contained in rectangle
                  2 - remove all overlapping graphics
            text:
                  0 - remove text
                  1 - ignore text
        """

        def center_rect(annot_rect, new_text, font, fsize):
            """Calculate minimal sub-rectangle for the overlay text.

            Notes:
                Because 'insert_textbox' supports no vertical text centering,
                we calculate an approximate number of lines here and return a
                sub-rect with smaller height, which should still be sufficient.
            Args:
                annot_rect: the annotation rectangle
                new_text: the text to insert.
                font: the fontname. Must be one of the CJK or Base-14 set, else
                    the rectangle is returned unchanged.
                fsize: the fontsize
            Returns:
                A rectangle to use instead of the annot rectangle.
            """
            if not new_text or annot_rect.width <= EPSILON:
                return annot_rect
            try:
                text_width = get_text_length(new_text, font, fsize)
            except (ValueError, mupdf.FzErrorBase):  # unsupported font
                if g_exceptions_verbose:
                    exception_info()
                return annot_rect
            line_height = fsize * 1.2
            limit = annot_rect.width
            h = math.ceil(text_width / limit) * line_height  # estimate rect height
            if h >= annot_rect.height:
                return annot_rect
            r = annot_rect
            y = (annot_rect.tl.y + annot_rect.bl.y - h) * 0.5
            r.y0 = y
            return r

        CheckParent(page)
        doc = page.parent
        if doc.is_encrypted or doc.is_closed:
            raise ValueError("document closed or encrypted")
        if not doc.is_pdf:
            raise ValueError("is no PDF")

        redact_annots = []  # storage of annot values
        for annot in page.annots(
            types=(mupdf.PDF_ANNOT_REDACT,)  # pylint: disable=no-member
        ):
            # loop redactions
            redact_annots.append(annot._get_redact_values())  # save annot values

        if redact_annots == []:  # any redactions on this page?
            return False  # no redactions

        rc = page._apply_redactions(text, images, graphics)  # call MuPDF
        if not rc:  # should not happen really
            raise ValueError("Error applying redactions.")

        # now write replacement text in old redact rectangles
        shape = page.new_shape()
        for redact in redact_annots:
            annot_rect = redact["rect"]
            fill = redact["fill"]
            if fill:
                shape.draw_rect(annot_rect)  # colorize the rect background
                shape.finish(fill=fill, color=fill)
            if "text" in redact.keys():  # if we also have text
                new_text = redact["text"]
                align = redact.get("align", 0)
                fname = redact["fontname"]
                fsize = redact["fontsize"]
                color = redact["text_color"]
                # try finding vertical centered sub-rect
                trect = center_rect(annot_rect, new_text, fname, fsize)

                rc = -1
                while rc < 0 and fsize >= 4:  # while not enough room
                    # (re-) try insertion
                    rc = shape.insert_textbox(
                        trect,
                        new_text,
                        fontname=fname,
                        fontsize=fsize,
                        color=color,
                        align=align,
                    )
                    fsize -= 0.5  # reduce font if unsuccessful
        shape.commit()  # append new contents object
        return True

    def recolor(self, components=1):
        """Convert colorspaces of objects on the page.
        
        Valid values are 1, 3 and 4.
        """
        if components not in (1, 3, 4):
            raise ValueError("components must be one of 1, 3, 4")
        pdfdoc = _as_pdf_document(self.parent)
        ropt = mupdf.pdf_recolor_options()
        ropt.num_comp = components
        ropts = mupdf.PdfRecolorOptions(ropt)
        mupdf.pdf_recolor_page(pdfdoc, self.number, ropts)

    def clip_to_rect(self, rect):
        """Clip away page content outside the rectangle."""
        clip = Rect(rect)
        if clip.is_infinite or (clip & self.rect).is_empty:
            raise ValueError("rect must not be infinite or empty")
        clip *= self.transformation_matrix
        pdfpage = _as_pdf_page(self)
        pclip = JM_rect_from_py(clip)
        mupdf.pdf_clip_page(pdfpage, pclip)

    def get_layout(self):
        """Try to access layout information."""

        if self.layout_information is not None:
            # layout information already present
            return

        if not _get_layout:
            # no layout information available
            return

        layout_info = _get_layout(self)
        self.layout_information = layout_info

    @property
    def artbox(self):
        """The ArtBox"""
        rect = self._other_box("ArtBox")
        if rect is None:
            return self.cropbox
        mb = self.mediabox
        return Rect(rect[0], mb.y1 - rect[3], rect[2], mb.y1 - rect[1])

    @property
    def bleedbox(self):
        """The BleedBox"""
        rect = self._other_box("BleedBox")
        if rect is None:
            return self.cropbox
        mb = self.mediabox
        return Rect(rect[0], mb.y1 - rect[3], rect[2], mb.y1 - rect[1])

    def bound(self):
        """Get page rectangle."""
        CheckParent(self)
        page = _as_fz_page(self.this)
        val = mupdf.fz_bound_page(page)
        val = Rect(val)
        
        if val.is_infinite and self.parent.is_pdf:
            cb = self.cropbox
            w, h = cb.width, cb.height
            if self.rotation not in (0, 180):
                w, h = h, w
            val = Rect(0, 0, w, h)
            msg = TOOLS.mupdf_warnings(reset=False).splitlines()[-1]
            message(msg)
        
        return val

    def clean_contents(self, sanitize=1):
        if not sanitize and not self.is_wrapped:
            self.wrap_contents()
        page = _as_pdf_page( self.this, required=False)
        if not page.m_internal:
            return
        filter_ = _make_PdfFilterOptions(recurse=1, sanitize=sanitize)
        mupdf.pdf_filter_page_contents( page.doc(), page, filter_)
    
    @property
    def cropbox(self):
        """The CropBox."""
        CheckParent(self)
        page = self._pdf_page(required=False)
        if not page.m_internal:
            val = mupdf.fz_bound_page(self.this)
        else:
            val = JM_cropbox(page.obj())
        val = Rect(val)

        return val

    @property
    def cropbox_position(self):
        return self.cropbox.tl

    def delete_annot(self, annot):
        """Delete annot and return next one."""
        CheckParent(self)
        CheckParent(annot)

        page = self._pdf_page()
        while 1:
            # first loop through all /IRT annots and remove them
            irt_annot = JM_find_annot_irt(annot.this)
            if not irt_annot:    # no more there
                break
            mupdf.pdf_delete_annot(page, irt_annot.this)
        nextannot = mupdf.pdf_next_annot(annot.this)   # store next
        mupdf.pdf_delete_annot(page, annot.this)
        val = Annot(nextannot)

        if val:
            val.thisown = True
            val.parent = weakref.proxy(self) # owning page object
            val.parent._annot_refs[id(val)] = val
        annot._erase()
        return val

    def delete_image(page: 'Page', xref: int):
        """Delete the image referred to by xef.

        Actually replaces by a small transparent Pixmap using method Page.replace_image.

        Args:
            xref: xref of the image to delete.
        """
        # make a small 100% transparent pixmap (of just any dimension)
        pix = Pixmap(csGRAY, (0, 0, 1, 1), 1)
        pix.clear_with()  # clear all samples bytes to 0x00
        page.replace_image(xref, pixmap=pix)

    def delete_link(self, linkdict):
        """Delete a Link."""
        CheckParent(self)
        if not isinstance( linkdict, dict):
            return  # have no dictionary

        def finished():
            if linkdict["xref"] == 0: return
            try:
                linkid = linkdict["id"]
                linkobj = self._annot_refs[linkid]
                linkobj._erase()
            except Exception:
                # Don't print this exception, to match classic. Issue #2841.
                if g_exceptions_verbose > 1:    exception_info()
                pass

        page = _as_pdf_page(self.this, required=False)
        if not page.m_internal:
            return finished()   # have no PDF
        xref = linkdict[dictkey_xref]
        if xref < 1:
            return finished()   # invalid xref
        annots = mupdf.pdf_dict_get( page.obj(), PDF_NAME('Annots'))
        if not annots.m_internal:
            return finished()   # have no annotations
        len_ = mupdf.pdf_array_len( annots)
        if len_ == 0:
            return finished()
        oxref = 0
        for i in range( len_):
            oxref = mupdf.pdf_to_num( mupdf.pdf_array_get( annots, i))
            if xref == oxref:
                break   # found xref in annotations

        if xref != oxref:
            return finished()   # xref not in annotations
        mupdf.pdf_array_delete( annots, i) # delete entry in annotations
        mupdf.pdf_delete_object( page.doc(), xref) # delete link object
        mupdf.pdf_dict_put( page.obj(), PDF_NAME('Annots'), annots)
        JM_refresh_links( page)

        return finished()

    def delete_widget(page: 'Page', widget: Widget) -> Widget:
        """Delete widget from page and return the next one."""
        CheckParent(page)
        annot = getattr(widget, "_annot", None)
        if annot is None:
            raise ValueError("bad type: widget")
        nextwidget = widget.next
        page.delete_annot(annot)
        widget._annot.parent = None
        keylist = list(widget.__dict__.keys())
        for key in keylist:
            del widget.__dict__[key]
        return nextwidget

    @property
    def derotation_matrix(self) -> Matrix:
        """Reflects page de-rotation."""
        if g_use_extra:
            return Matrix(extra.Page_derotate_matrix( self.this))
        pdfpage = self._pdf_page(required=False)
        if not pdfpage.m_internal:
            return Matrix(mupdf.FzRect(mupdf.FzRect.UNIT))
        return Matrix(JM_derotate_page_matrix(pdfpage))

    def draw_bezier(
            page: 'Page',
            p1: point_like,
            p2: point_like,
            p3: point_like,
            p4: point_like,
            color: OptSeq = (0,),
            fill: OptSeq = None,
            dashes: OptStr = None,
            width: float = 1,
            morph: OptStr = None,
            closePath: bool = False,
            lineCap: int = 0,
            lineJoin: int = 0,
            overlay: bool = True,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc: int = 0,
            ) -> Point:
        """Draw a general cubic Bezier curve from p1 to p4 using control points p2 and p3."""
        img = page.new_shape()
        Q = img.draw_bezier(Point(p1), Point(p2), Point(p3), Point(p4))
        img.finish(
                color=color,
                fill=fill,
                dashes=dashes,
                width=width,
                lineCap=lineCap,
                lineJoin=lineJoin,
                morph=morph,
                closePath=closePath,
                stroke_opacity=stroke_opacity,
                fill_opacity=fill_opacity,
                oc=oc,
                )
        img.commit(overlay)

        return Q

    def draw_circle(
            page: 'Page',
            center: point_like,
            radius: float,
            color: OptSeq = (0,),
            fill: OptSeq = None,
            morph: OptSeq = None,
            dashes: OptStr = None,
            width: float = 1,
            lineCap: int = 0,
            lineJoin: int = 0,
            overlay: bool = True,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc: int = 0,
            ) -> Point:
        """Draw a circle given its center and radius."""
        img = page.new_shape()
        Q = img.draw_circle(Point(center), radius)
        img.finish(
                color=color,
                fill=fill,
                dashes=dashes,
                width=width,
                lineCap=lineCap,
                lineJoin=lineJoin,
                morph=morph,
                stroke_opacity=stroke_opacity,
                fill_opacity=fill_opacity,
                oc=oc,
                )
        img.commit(overlay)
        return Q

    def draw_curve(
            page: 'Page',
            p1: point_like,
            p2: point_like,
            p3: point_like,
            color: OptSeq = (0,),
            fill: OptSeq = None,
            dashes: OptStr = None,
            width: float = 1,
            morph: OptSeq = None,
            closePath: bool = False,
            lineCap: int = 0,
            lineJoin: int = 0,
            overlay: bool = True,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc: int = 0,
            ) -> Point:
        """Draw a special Bezier curve from p1 to p3, generating control points on lines p1 to p2 and p2 to p3."""
        img = page.new_shape()
        Q = img.draw_curve(Point(p1), Point(p2), Point(p3))
        img.finish(
                color=color,
                fill=fill,
                dashes=dashes,
                width=width,
                lineCap=lineCap,
                lineJoin=lineJoin,
                morph=morph,
                closePath=closePath,
                stroke_opacity=stroke_opacity,
                fill_opacity=fill_opacity,
                oc=oc,
                )
        img.commit(overlay)

        return Q

    def draw_line(
            page: 'Page',
            p1: point_like,
            p2: point_like,
            color: OptSeq = (0,),
            dashes: OptStr = None,
            width: float = 1,
            lineCap: int = 0,
            lineJoin: int = 0,
            overlay: bool = True,
            morph: OptSeq = None,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc=0,
            ) -> Point:
        """Draw a line from point p1 to point p2."""
        img = page.new_shape()
        p = img.draw_line(Point(p1), Point(p2))
        img.finish(
                color=color,
                dashes=dashes,
                width=width,
                closePath=False,
                lineCap=lineCap,
                lineJoin=lineJoin,
                morph=morph,
                stroke_opacity=stroke_opacity,
                fill_opacity=fill_opacity,
                oc=oc,
                )
        img.commit(overlay)

        return p

    def draw_oval(
            page: 'Page',
            rect: typing.Union[rect_like, quad_like],
            color: OptSeq = (0,),
            fill: OptSeq = None,
            dashes: OptStr = None,
            morph: OptSeq = None,
            width: float = 1,
            lineCap: int = 0,
            lineJoin: int = 0,
            overlay: bool = True,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc: int = 0,
            ) -> Point:
        """Draw an oval given its containing rectangle or quad."""
        img = page.new_shape()
        Q = img.draw_oval(rect)
        img.finish(
                color=color,
                fill=fill,
                dashes=dashes,
                width=width,
                lineCap=lineCap,
                lineJoin=lineJoin,
                morph=morph,
                stroke_opacity=stroke_opacity,
                fill_opacity=fill_opacity,
                oc=oc,
                )
        img.commit(overlay)

        return Q

    def draw_polyline(
            page: 'Page',
            points: list,
            color: OptSeq = (0,),
            fill: OptSeq = None,
            dashes: OptStr = None,
            width: float = 1,
            morph: OptSeq = None,
            lineCap: int = 0,
            lineJoin: int = 0,
            overlay: bool = True,
            closePath: bool = False,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc: int = 0,
            ) -> Point:
        """Draw multiple connected line segments."""
        img = page.new_shape()
        Q = img.draw_polyline(points)
        img.finish(
                color=color,
                fill=fill,
                dashes=dashes,
                width=width,
                lineCap=lineCap,
                lineJoin=lineJoin,
                morph=morph,
                closePath=closePath,
                stroke_opacity=stroke_opacity,
                fill_opacity=fill_opacity,
                oc=oc,
                )
        img.commit(overlay)

        return Q

    def draw_quad(
            page: 'Page',
            quad: quad_like,
            color: OptSeq = (0,),
            fill: OptSeq = None,
            dashes: OptStr = None,
            width: float = 1,
            lineCap: int = 0,
            lineJoin: int = 0,
            morph: OptSeq = None,
            overlay: bool = True,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc: int = 0,
            ) -> Point:
        """Draw a quadrilateral."""
        img = page.new_shape()
        Q = img.draw_quad(Quad(quad))
        img.finish(
                color=color,
                fill=fill,
                dashes=dashes,
                width=width,
                lineCap=lineCap,
                lineJoin=lineJoin,
                morph=morph,
                stroke_opacity=stroke_opacity,
                fill_opacity=fill_opacity,
                oc=oc,
                )
        img.commit(overlay)

        return Q

    def draw_rect(
            page: 'Page',
            rect: rect_like,
            color: OptSeq = (0,),
            fill: OptSeq = None,
            dashes: OptStr = None,
            width: float = 1,
            lineCap: int = 0,
            lineJoin: int = 0,
            morph: OptSeq = None,
            overlay: bool = True,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc: int = 0,
            radius=None,
            ) -> Point:
        '''
        Draw a rectangle. See Shape class method for details.
        '''
        img = page.new_shape()
        Q = img.draw_rect(Rect(rect), radius=radius)
        img.finish(
                color=color,
                fill=fill,
                dashes=dashes,
                width=width,
                lineCap=lineCap,
                lineJoin=lineJoin,
                morph=morph,
                stroke_opacity=stroke_opacity,
                fill_opacity=fill_opacity,
                oc=oc,
                )
        img.commit(overlay)

        return Q

    def draw_sector(
            page: 'Page',
            center: point_like,
            point: point_like,
            beta: float,
            color: OptSeq = (0,),
            fill: OptSeq = None,
            dashes: OptStr = None,
            fullSector: bool = True,
            morph: OptSeq = None,
            width: float = 1,
            closePath: bool = False,
            lineCap: int = 0,
            lineJoin: int = 0,
            overlay: bool = True,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc: int = 0,
            ) -> Point:
        """Draw a circle sector given circle center, one arc end point and the angle of the arc.

        Parameters:
            center -- center of circle
            point -- arc end point
            beta -- angle of arc (degrees)
            fullSector -- connect arc ends with center
        """
        img = page.new_shape()
        Q = img.draw_sector(Point(center), Point(point), beta, fullSector=fullSector)
        img.finish(
                color=color,
                fill=fill,
                dashes=dashes,
                width=width,
                lineCap=lineCap,
                lineJoin=lineJoin,
                morph=morph,
                closePath=closePath,
                stroke_opacity=stroke_opacity,
                fill_opacity=fill_opacity,
                oc=oc,
                )
        img.commit(overlay)

        return Q

    def draw_squiggle(
            page: 'Page',
            p1: point_like,
            p2: point_like,
            breadth: float = 2,
            color: OptSeq = (0,),
            dashes: OptStr = None,
            width: float = 1,
            lineCap: int = 0,
            lineJoin: int = 0,
            overlay: bool = True,
            morph: OptSeq = None,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc: int = 0,
            ) -> Point:
        """Draw a squiggly line from point p1 to point p2."""
        img = page.new_shape()
        p = img.draw_squiggle(Point(p1), Point(p2), breadth=breadth)
        img.finish(
                color=color,
                dashes=dashes,
                width=width,
                closePath=False,
                lineCap=lineCap,
                lineJoin=lineJoin,
                morph=morph,
                stroke_opacity=stroke_opacity,
                fill_opacity=fill_opacity,
                oc=oc,
                )
        img.commit(overlay)

        return p

    def draw_zigzag(
            page: 'Page',
            p1: point_like,
            p2: point_like,
            breadth: float = 2,
            color: OptSeq = (0,),
            dashes: OptStr = None,
            width: float = 1,
            lineCap: int = 0,
            lineJoin: int = 0,
            overlay: bool = True,
            morph: OptSeq = None,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc: int = 0,
            ) -> Point:
        """Draw a zigzag line from point p1 to point p2."""
        img = page.new_shape()
        p = img.draw_zigzag(Point(p1), Point(p2), breadth=breadth)
        img.finish(
                color=color,
                dashes=dashes,
                width=width,
                closePath=False,
                lineCap=lineCap,
                lineJoin=lineJoin,
                morph=morph,
                stroke_opacity=stroke_opacity,
                fill_opacity=fill_opacity,
                oc=oc,
                )
        img.commit(overlay)

        return p

    def extend_textpage(self, tpage, flags=0, matrix=None):
        page = self.this
        tp = tpage.this
        assert isinstance( tp, mupdf.FzStextPage)
        options = mupdf.FzStextOptions()
        options.flags = flags
        ctm = JM_matrix_from_py(matrix)
        dev = mupdf.FzDevice(tp, options)
        mupdf.fz_run_page( page, dev, ctm, mupdf.FzCookie())
        mupdf.fz_close_device( dev)

    @property
    def first_annot(self):
        """First annotation."""
        CheckParent(self)
        page = self._pdf_page(required=False)
        if not page.m_internal:
            return
        annot = mupdf.pdf_first_annot(page)
        if not annot.m_internal:
            return
        val = Annot(annot)
        val.thisown = True
        val.parent = weakref.proxy(self) # owning page object
        self._annot_refs[id(val)] = val
        return val

    @property
    def first_link(self):
        '''
        First link on page
        '''
        return self.load_links()

    @property
    def first_widget(self):
        """First widget/field."""
        CheckParent(self)
        annot = 0
        page = self._pdf_page(required=False)
        if not page.m_internal:
            return
        annot = mupdf.pdf_first_widget(page)
        if not annot.m_internal:
            return
        val = Annot(annot)
        val.thisown = True
        val.parent = weakref.proxy(self) # owning page object
        self._annot_refs[id(val)] = val
        widget = Widget()
        TOOLS._fill_widget(val, widget)
        val = widget
        return val

    def get_bboxlog(self, layers=None):
        CheckParent(self)
        old_rotation = self.rotation
        if old_rotation != 0:
            self.set_rotation(0)
        page = self.this
        rc = []
        inc_layers = True if layers else False
        dev = JM_new_bbox_device( rc, inc_layers)
        mupdf.fz_run_page( page, dev, mupdf.FzMatrix(), mupdf.FzCookie())
        mupdf.fz_close_device( dev)

        if old_rotation != 0:
            self.set_rotation(old_rotation)
        return rc

    def get_cdrawings(self, extended=None, callback=None, method=None):
        """Extract vector graphics ("line art") from the page."""
        CheckParent(self)
        old_rotation = self.rotation
        if old_rotation != 0:
            self.set_rotation(0)
        page = self.this
        if isinstance(page, mupdf.PdfPage):
            # Downcast pdf_page to fz_page.
            page = mupdf.FzPage(page)
        assert isinstance(page, mupdf.FzPage), f'{self.this=}'
        clips = True if extended else False
        prect = mupdf.fz_bound_page(page)
        if 1 or g_use_extra:
            rc = extra.get_cdrawings(page, extended, callback, method)
        else:
            rc = list()
            if callable(callback) or method is not None:
                dev = JM_new_lineart_device_Device(callback, clips, method)
            else:
                dev = JM_new_lineart_device_Device(rc, clips, method)
            dev.ptm = mupdf.FzMatrix(1, 0, 0, -1, 0, prect.y1)
            mupdf.fz_run_page(page, dev, mupdf.FzMatrix(), mupdf.FzCookie())
            mupdf.fz_close_device(dev)

        if old_rotation != 0:
            self.set_rotation(old_rotation)
        if callable(callback) or method is not None:
            return
        return rc

    def get_contents(self):
        """Get xrefs of /Contents objects."""
        CheckParent(self)
        ret = []
        page = _as_pdf_page(self.this)
        obj = page.obj()
        contents = mupdf.pdf_dict_get(obj, mupdf.PDF_ENUM_NAME_Contents)
        if mupdf.pdf_is_array(contents):
            n = mupdf.pdf_array_len(contents)
            for i in range(n):
                icont = mupdf.pdf_array_get(contents, i)
                xref = mupdf.pdf_to_num(icont)
                ret.append(xref)
        elif contents.m_internal:
            xref = mupdf.pdf_to_num(contents)
            ret.append( xref)
        return ret

    def get_displaylist(self, annots=1):
        '''
        Make a DisplayList from the page for Pixmap generation.

        Include (default) or exclude annotations.
        '''
        CheckParent(self)
        if annots:
            dl = mupdf.fz_new_display_list_from_page(self.this)
        else:
            dl = mupdf.fz_new_display_list_from_page_contents(self.this)
        return DisplayList(dl)

    def get_drawings(self, extended: bool=False) -> list:
        """Retrieve vector graphics. The extended version includes clips.

        Note:
        For greater comfort, this method converts point-likes, rect-likes, quad-likes
        of the C version to respective Point / Rect / Quad objects.
        It also adds default items that are missing in original path types.
        """
        allkeys = (
                'closePath',
                'fill',
                'color',
                'width',
                'lineCap',
                'lineJoin',
                'dashes',
                'stroke_opacity',
                'fill_opacity',
                'even_odd',
                )
        val = self.get_cdrawings(extended=extended)
        for i in range(len(val)):
            npath = val[i]
            if not npath["type"].startswith("clip"):
                npath["rect"] = Rect(npath["rect"])
            else:
                npath["scissor"] = Rect(npath["scissor"])
            if npath["type"]!="group":
                items = npath["items"]
                newitems = []
                for item in items:
                    cmd = item[0]
                    rest = item[1:]
                    if  cmd == "re":
                        item = ("re", Rect(rest[0]).normalize(), rest[1])
                    elif cmd == "qu":
                        item = ("qu", Quad(rest[0]))
                    else:
                        item = tuple([cmd] + [Point(i) for i in rest])
                    newitems.append(item)
                npath["items"] = newitems
            if npath['type'] in ('f', 's'):
                for k in allkeys:
                    npath[k] = npath.get(k)

            val[i] = npath
        return val

        class Drawpath(object):
            """Reflects a path dictionary from get_cdrawings()."""
            def __init__(self, **args):
                self.__dict__.update(args)
        
        class Drawpathlist(object):
            """List of Path objects representing get_cdrawings() output."""
            def __getitem__(self, item):
                return self.paths.__getitem__(item)

            def __init__(self):
                self.paths = []
                self.path_count = 0
                self.group_count = 0
                self.clip_count = 0
                self.fill_count = 0
                self.stroke_count = 0
                self.fillstroke_count = 0

            def __len__(self):
                return self.paths.__len__()

            def append(self, path):
                self.paths.append(path)
                self.path_count += 1
                if path.type == "clip":
                    self.clip_count += 1
                elif path.type == "group":
                    self.group_count += 1
                elif path.type == "f":
                    self.fill_count += 1
                elif path.type == "s":
                    self.stroke_count += 1
                elif path.type == "fs":
                    self.fillstroke_count += 1

            def clip_parents(self, i):
                """Return list of parent clip paths.

                Args:
                    i: (int) return parents of this path.
                Returns:
                    List of the clip parents."""
                if i >= self.path_count:
                    raise IndexError("bad path index")
                while i < 0:
                    i += self.path_count
                lvl = self.paths[i].level
                clips = list(  # clip paths before identified one
                    reversed(
                        [
                            p
                            for p in self.paths[:i]
                            if p.type == "clip" and p.level < lvl
                        ]
                    )
                )
                if clips == []:  # none found: empty list
                    return []
                nclips = [clips[0]]  # init return list
                for p in clips[1:]:
                    if p.level >= nclips[-1].level:
                        continue  # only accept smaller clip levels
                    nclips.append(p)
                return nclips

            def group_parents(self, i):
                """Return list of parent group paths.

                Args:
                    i: (int) return parents of this path.
                Returns:
                    List of the group parents."""
                if i >= self.path_count:
                    raise IndexError("bad path index")
                while i < 0:
                    i += self.path_count
                lvl = self.paths[i].level
                groups = list(  # group paths before identified one
                    reversed(
                        [
                            p
                            for p in self.paths[:i]
                            if p.type == "group" and p.level < lvl
                        ]
                    )
                )
                if groups == []:  # none found: empty list
                    return []
                ngroups = [groups[0]]  # init return list
                for p in groups[1:]:
                    if p.level >= ngroups[-1].level:
                        continue  # only accept smaller group levels
                    ngroups.append(p)
                return ngroups

        def get_lineart(self) -> object:
            """Get page drawings paths.

            Note:
            For greater comfort, this method converts point-like, rect-like, quad-like
            tuples of the C version to respective Point / Rect / Quad objects.
            Also adds default items that are missing in original path types.
            In contrast to get_drawings(), this output is an object.
            """

            val = self.get_cdrawings(extended=True)
            paths = self.Drawpathlist()
            for path in val:
                npath = self.Drawpath(**path)
                if npath.type != "clip":
                    npath.rect = Rect(path["rect"])
                else:
                    npath.scissor = Rect(path["scissor"])
                if npath.type != "group":
                    items = path["items"]
                    newitems = []
                    for item in items:
                        cmd = item[0]
                        rest = item[1:]
                        if  cmd == "re":
                            item = ("re", Rect(rest[0]).normalize(), rest[1])
                        elif cmd == "qu":
                            item = ("qu", Quad(rest[0]))
                        else:
                            item = tuple([cmd] + [Point(i) for i in rest])
                        newitems.append(item)
                    npath.items = newitems
                
                if npath.type == "f":
                    npath.stroke_opacity = None
                    npath.dashes = None
                    npath.line_join = None
                    npath.line_cap = None
                    npath.color = None
                    npath.width = None

                paths.append(npath)

            val = None
            return paths

    def get_image_info(
            page: 'Page',
            hashes: bool = False,
            xrefs: bool = False
            ) -> list:
        """Extract image information only from a pymupdf.TextPage.

        Args:
            hashes: (bool) include MD5 hash for each image.
            xrefs: (bool) try to find the xref for each image. Sets hashes to true.
        """
        doc = page.parent
        if xrefs and doc.is_pdf:
            hashes = True
        if not doc.is_pdf:
            xrefs = False
        imginfo = getattr(page, "_image_info", None)
        if imginfo and not xrefs:
            return imginfo
        if not imginfo:
            tp = page.get_textpage(flags=TEXT_PRESERVE_IMAGES)
            imginfo = tp.extractIMGINFO(hashes=hashes)
            del tp
            if hashes:
                page._image_info = imginfo
        if not xrefs or not doc.is_pdf:
            return imginfo
        imglist = page.get_images()
        digests = {}
        for item in imglist:
            xref = item[0]
            pix = Pixmap(doc, xref)
            digests[pix.digest] = xref
            del pix
        for i in range(len(imginfo)):
            item = imginfo[i]
            xref = digests.get(item["digest"], 0)
            item["xref"] = xref
            imginfo[i] = item
        return imginfo

    def get_image_rects(page: 'Page', name, transform=False) -> list:
        """Return list of image positions on a page.

        Args:
            name: (str, list, int) image identification. May be reference name, an
                  item of the page's image list or an xref.
            transform: (bool) whether to also return the transformation matrix.
        Returns:
            A list of pymupdf.Rect objects or tuples of (pymupdf.Rect, pymupdf.Matrix)
            for all image locations on the page.
        """
        if type(name) in (list, tuple):
            xref = name[0]
        elif type(name) is int:
            xref = name
        else:
            imglist = [i for i in page.get_images() if i[7] == name]
            if imglist == []:
                raise ValueError("bad image name")
            elif len(imglist) != 1:
                raise ValueError("multiple image names found")
            xref = imglist[0][0]
        pix = Pixmap(page.parent, xref)  # make pixmap of the image to compute MD5
        digest = pix.digest
        del pix
        infos = page.get_image_info(hashes=True)
        if not transform:
            bboxes = [Rect(im["bbox"]) for im in infos if im["digest"] == digest]
        else:
            bboxes = [
                (Rect(im["bbox"]), Matrix(im["transform"]))
                for im in infos
                if im["digest"] == digest
            ]
        return bboxes

    def get_label(page):
        """Return the label for this PDF page.

        Args:
            page: page object.
        Returns:
            The label (str) of the page. Errors return an empty string.
        """
        # Jorj McKie, 2021-01-06

        labels = page.parent._get_page_labels()
        if not labels:
            return ""
        labels.sort()
        return utils.get_label_pno(page.number, labels)

    def get_links(page: 'Page') -> list:
        """Create a list of all links contained in a PDF page.

        Notes:
            see PyMuPDF ducmentation for details.
        """

        CheckParent(page)
        ln = page.first_link
        links = []
        while ln:
            nl = utils.getLinkDict(ln, page.parent)
            links.append(nl)
            ln = ln.next
        if links != [] and page.parent.is_pdf:
            linkxrefs = [x for x in
                    #page.annot_xrefs()
                    JM_get_annot_xref_list2(page)
                    if x[1] == mupdf.PDF_ANNOT_LINK  # pylint: disable=no-member
                    ]
            if len(linkxrefs) == len(links):
                for i in range(len(linkxrefs)):
                    links[i]["xref"] = linkxrefs[i][0]
                    links[i]["id"] = linkxrefs[i][2]
        return links

    def get_pixmap(
                page: 'Page',
                *,
                matrix: matrix_like=Identity,
                dpi=None,
                colorspace: Colorspace=None,
                clip: rect_like=None,
                alpha: bool=False,
                annots: bool=True,
                ) -> 'Pixmap':
        """Create pixmap of page.

        Keyword args:
            matrix: Matrix for transformation (default: Identity).
            dpi: desired dots per inch. If given, matrix is ignored.
            colorspace: (str/Colorspace) cmyk, rgb, gray - case ignored, default csRGB.
            clip: (irect-like) restrict rendering to this area.
            alpha: (bool) whether to include alpha channel
            annots: (bool) whether to also render annotations
        """
        if colorspace is None:
            colorspace = csRGB
        if dpi:
            zoom = dpi / 72
            matrix = Matrix(zoom, zoom)

        if type(colorspace) is str:
            if colorspace.upper() == "GRAY":
                colorspace = csGRAY
            elif colorspace.upper() == "CMYK":
                colorspace = csCMYK
            else:
                colorspace = csRGB
        if colorspace.n not in (1, 3, 4):
            raise ValueError("unsupported colorspace")

        dl = page.get_displaylist(annots=annots)
        pix = dl.get_pixmap(matrix=matrix, colorspace=colorspace, alpha=alpha, clip=clip)
        dl = None
        if dpi:
            pix.set_dpi(dpi, dpi)
        return pix

    def remove_rotation(self):
        """Set page rotation to 0 while maintaining visual appearance."""
        rot = self.rotation  # normalized rotation value
        if rot == 0:
            return  Identity # nothing to do

        # need to derotate the page's content
        mb = self.mediabox  # current mediabox

        if rot == 90:
            # before derotation, shift content horizontally
            mat0 = Matrix(1, 0, 0, 1, mb.y1 - mb.x1 - mb.x0 - mb.y0, 0)
        elif rot == 270:
            # before derotation, shift content vertically
            mat0 = Matrix(1, 0, 0, 1, 0, mb.x1 - mb.y1 - mb.y0 - mb.x0)
        else:  # rot = 180
            mat0 = Matrix(1, 0, 0, 1, -2 * mb.x0, -2 * mb.y0)

        # prefix with derotation matrix
        mat = mat0 * self.derotation_matrix
        cmd = _format_g(tuple(mat)) + ' cm '
        cmd = cmd.encode('utf8')
        _ = TOOLS._insert_contents(self, cmd, False)  # prepend to page contents

        # swap x- and y-coordinates
        if rot in (90, 270):
            x0, y0, x1, y1 = mb
            mb.x0 = y0
            mb.y0 = x0
            mb.x1 = y1
            mb.y1 = x1
            self.set_mediabox(mb)

        self.set_rotation(0)
        rot = ~mat  # inverse of the derotation matrix

        for annot in self.annots():  # modify rectangles of annotations
            r = annot.rect * rot
            # TODO: only try to set rectangle for applicable annot types
            annot.set_rect(r)
        for link in self.get_links():  # modify 'from' rectangles of links
            r = link["from"] * rot
            self.delete_link(link)
            link["from"] = r
            try:  # invalid links remain deleted
                self.insert_link(link)
            except Exception:
                pass
        for widget in self.widgets():  # modify field rectangles
            r = widget.rect * rot
            widget.rect = r
            widget.update()
        return rot  # the inverse of the generated derotation matrix

    def cluster_drawings(
        self, clip=None, drawings=None, x_tolerance: float = 3, y_tolerance: float = 3,
        final_filter: bool = True,
    ) -> list:
        """Join rectangles of neighboring vector graphic items.

        Args:
            clip: optional rect-like to restrict the page area to consider.
            drawings: (optional) output of a previous "get_drawings()".
            x_tolerance: horizontal neighborhood threshold.
            y_tolerance: vertical neighborhood threshold.

        Notes:
            Vector graphics (also called line-art or drawings) usually consist
            of independent items like rectangles, lines or curves to jointly
            form table grid lines or bar, line, pie charts and similar.
            This method identifies rectangles wrapping these disparate items.

        Returns:
            A list of Rect items, each wrapping line-art items that are close
            enough to be considered forming a common vector graphic.
            Only "significant" rectangles will be returned, i.e. having both,
            width and height larger than the tolerance values.
        """
        CheckParent(self)
        parea = self.rect  # the default clipping area
        if clip is not None:
            parea = Rect(clip)
        delta_x = x_tolerance  # shorter local name
        delta_y = y_tolerance  # shorter local name
        if drawings is None:  # if we cannot re-use a previous output
            drawings = self.get_drawings()

        def are_neighbors(r1, r2):
            """Detect whether r1, r2 are "neighbors".

            Items r1, r2 are called neighbors if the minimum distance between
            their points is less-equal delta.

            Both parameters must be (potentially invalid) rectangles.
            """
            # normalize rectangles as needed
            rr1_x0, rr1_x1 = (r1.x0, r1.x1) if r1.x1 > r1.x0 else (r1.x1, r1.x0)
            rr1_y0, rr1_y1 = (r1.y0, r1.y1) if r1.y1 > r1.y0 else (r1.y1, r1.y0)
            rr2_x0, rr2_x1 = (r2.x0, r2.x1) if r2.x1 > r2.x0 else (r2.x1, r2.x0)
            rr2_y0, rr2_y1 = (r2.y0, r2.y1) if r2.y1 > r2.y0 else (r2.y1, r2.y0)
            if (
                0
                or rr1_x1 < rr2_x0 - delta_x
                or rr1_x0 > rr2_x1 + delta_x
                or rr1_y1 < rr2_y0 - delta_y
                or rr1_y0 > rr2_y1 + delta_y
            ):
                # Rects do not overlap.
                return False
            else:
                # Rects overlap.
                return True

        # exclude graphics not contained in the clip
        paths = [
            p
            for p in drawings
            if 1
            and p["rect"].x0 >= parea.x0
            and p["rect"].x1 <= parea.x1
            and p["rect"].y0 >= parea.y0
            and p["rect"].y1 <= parea.y1
        ]

        # list of all vector graphic rectangles
        prects = sorted([p["rect"] for p in paths], key=lambda r: (r.y1, r.x0))

        new_rects = []  # the final list of the joined rectangles

        # -------------------------------------------------------------------------
        # The strategy is to identify and join all rects that are neighbors
        # -------------------------------------------------------------------------
        while prects:  # the algorithm will empty this list
            r = +prects[0]  # copy of first rectangle
            repeat = True
            while repeat:
                repeat = False
                for i in range(len(prects) - 1, 0, -1):  # from back to front
                    if are_neighbors(prects[i], r):
                        r |= prects[i].tl  # include in first rect
                        r |= prects[i].br  # include in first rect
                        del prects[i]  # delete this rect
                        repeat = True

            new_rects.append(r)
            del prects[0]
            prects = sorted(set(prects), key=lambda r: (r.y1, r.x0))

        new_rects = sorted(set(new_rects), key=lambda r: (r.y1, r.x0))
        if not final_filter:
            return new_rects
        return [r for r in new_rects if r.width > delta_x and r.height > delta_y]

    def get_fonts(self, full=False):
        """List of fonts defined in the page object."""
        CheckParent(self)
        return self.parent.get_page_fonts(self.number, full=full)

    def get_image_bbox(self, name, transform=0):
        """Get rectangle occupied by image 'name'.

        'name' is either an item of the image list, or the referencing
        name string - elem[7] of the resp. item.
        Option 'transform' also returns the image transformation matrix.
        """
        CheckParent(self)
        doc = self.parent
        if doc.is_closed or doc.is_encrypted:
            raise ValueError('document closed or encrypted')

        inf_rect = Rect(1, 1, -1, -1)
        null_mat = Matrix()
        if transform:
            rc = (inf_rect, null_mat)
        else:
            rc = inf_rect

        if type(name) in (list, tuple):
            if not type(name[-1]) is int:
                raise ValueError('need item of full page image list')
            item = name
        else:
            imglist = [i for i in doc.get_page_images(self.number, True) if name == i[7]]
            if len(imglist) == 1:
                item = imglist[0]
            elif imglist == []:
                raise ValueError('bad image name')
            else:
                raise ValueError("found multiple images named '%s'." % name)
        xref = item[-1]
        if xref != 0 or transform:
            try:
                return self.get_image_rects(item, transform=transform)[0]
            except Exception:
                exception_info()
                return inf_rect
        pdf_page = self._pdf_page()
        val = JM_image_reporter(pdf_page)

        if not bool(val):
            return rc

        for v in val:
            if v[0] != item[-3]:
                continue
            q = Quad(v[1])
            bbox = q.rect
            if transform == 0:
                rc = bbox
                break

            hm = Matrix(util_hor_matrix(q.ll, q.lr))
            h = abs(q.ll - q.ul)
            w = abs(q.ur - q.ul)
            m0 = Matrix(1 / w, 0, 0, 1 / h, 0, 0)
            m = ~(hm * m0)
            rc = (bbox, m)
            break
        val = rc

        return val

    def get_images(self, full=False):
        """List of images defined in the page object."""
        CheckParent(self)
        return self.parent.get_page_images(self.number, full=full)

    def get_oc_items(self) -> list:
        """Get OCGs and OCMDs used in the page's contents.

        Returns:
            List of items (name, xref, type), where type is one of "ocg" / "ocmd",
            and name is the property name.
        """
        rc = []
        for pname, xref in self._get_resource_properties():
            text = self.parent.xref_object(xref, compressed=True)
            if "/Type/OCG" in text:
                octype = "ocg"
            elif "/Type/OCMD" in text:
                octype = "ocmd"
            else:
                continue
            rc.append((pname, xref, octype))
        return rc

    def get_svg_image(self, matrix=None, text_as_path=1):
        """Make SVG image from page."""
        CheckParent(self)
        mediabox = mupdf.fz_bound_page(self.this)
        ctm = JM_matrix_from_py(matrix)
        tbounds = mediabox
        text_option = mupdf.FZ_SVG_TEXT_AS_PATH if text_as_path == 1 else mupdf.FZ_SVG_TEXT_AS_TEXT
        tbounds = mupdf.fz_transform_rect(tbounds, ctm)

        res = mupdf.fz_new_buffer(1024)
        out = mupdf.FzOutput(res)
        dev = mupdf.fz_new_svg_device(
                out,
                tbounds.x1-tbounds.x0,  # width
                tbounds.y1-tbounds.y0,  # height
                text_option,
                1,
                )
        mupdf.fz_run_page(self.this, dev, ctm, mupdf.FzCookie())
        mupdf.fz_close_device(dev)
        out.fz_close_output()
        text = JM_EscapeStrFromBuffer(res)
        return text

    def get_textbox(
            page: Page,
            rect: rect_like,
            textpage=None,  #: TextPage = None,
            ) -> str:
        tp = textpage
        if tp is None:
            tp = page.get_textpage()
        elif getattr(tp, "parent") != page:
            raise ValueError("not a textpage of this page")
        rc = tp.extractTextbox(rect)
        if textpage is None:
            del tp
        return rc

    def get_text(self, *args, **kwargs):
        return utils.get_text(self, *args, **kwargs)

    def get_text_blocks(self, *args, **kwargs):
        return utils.get_text_blocks(self, *args, **kwargs)
    
    def get_text_selection(self, *args, **kwargs):
        return utils.get_text_selection(self, *args, **kwargs)
    
    def get_text_words(self, *args, **kwargs):
        return utils.get_text_words(self, *args, **kwargs)
    
    def get_textpage_ocr(self, *args, **kwargs):
        return utils.get_textpage_ocr(self, *args, **kwargs)
    
    def get_textpage(self, clip: rect_like = None, flags: int = 0, matrix=None) -> "TextPage":
        CheckParent(self)
        if matrix is None:
            matrix = Matrix(1, 1)
        old_rotation = self.rotation
        if old_rotation != 0:
            self.set_rotation(0)
        try:
            textpage = self._get_textpage(clip, flags=flags, matrix=matrix)
        finally:
            if old_rotation != 0:
                self.set_rotation(old_rotation)
        textpage = TextPage(textpage)
        textpage.parent = weakref.proxy(self)
        return textpage

    def get_texttrace(self):

        CheckParent(self)
        old_rotation = self.rotation
        if old_rotation != 0:
            self.set_rotation(0)
        page = self.this
        rc = []
        if 1 or g_use_extra:
            dev = extra.JM_new_texttrace_device(rc)
        else:
            dev = JM_new_texttrace_device(rc)
        prect = mupdf.fz_bound_page(page)
        dev.ptm = mupdf.FzMatrix(1, 0, 0, -1, 0, prect.y1)
        mupdf.fz_run_page(page, dev, mupdf.FzMatrix(), mupdf.FzCookie())
        mupdf.fz_close_device(dev)

        if old_rotation != 0:
            self.set_rotation(old_rotation)
        return rc

    def get_xobjects(self):
        """List of xobjects defined in the page object."""
        CheckParent(self)
        return self.parent.get_page_xobjects(self.number)

    def insert_font(self, fontname="helv", fontfile=None, fontbuffer=None,
                   set_simple=False, wmode=0, encoding=0):
        doc = self.parent
        if doc is None:
            raise ValueError("orphaned object: parent is None")
        idx = 0

        if fontname.startswith("/"):
            fontname = fontname[1:]
        inv_chars = INVALID_NAME_CHARS.intersection(fontname)
        if inv_chars != set():
            raise ValueError(f"bad fontname chars {inv_chars}")

        font = CheckFont(self, fontname)
        if font is not None:                    # font already in font list of page
            xref = font[0]                      # this is the xref
            if CheckFontInfo(doc, xref):        # also in our document font list?
                return xref                     # yes: we are done
            # need to build the doc FontInfo entry - done via get_char_widths
            doc.get_char_widths(xref)
            return xref

        #--------------------------------------------------------------------------
        # the font is not present for this page
        #--------------------------------------------------------------------------

        bfname = Base14_fontdict.get(fontname.lower(), None) # BaseFont if Base-14 font

        serif = 0
        CJK_number = -1
        CJK_list_n = ["china-t", "china-s", "japan", "korea"]
        CJK_list_s = ["china-ts", "china-ss", "japan-s", "korea-s"]

        try:
            CJK_number = CJK_list_n.index(fontname)
            serif = 0
        except Exception:
            # Verbose in PyMuPDF/tests.
            if g_exceptions_verbose > 1:    exception_info()
            pass

        if CJK_number < 0:
            try:
                CJK_number = CJK_list_s.index(fontname)
                serif = 1
            except Exception:
                # Verbose in PyMuPDF/tests.
                if g_exceptions_verbose > 1:    exception_info()
                pass

        if fontname.lower() in fitz_fontdescriptors.keys():
            import pymupdf_fonts
            fontbuffer = pymupdf_fonts.myfont(fontname)  # make a copy
            del pymupdf_fonts

        # install the font for the page
        if fontfile is not None:
            if type(fontfile) is str:
                fontfile_str = fontfile
            elif hasattr(fontfile, "absolute"):
                fontfile_str = str(fontfile)
            elif hasattr(fontfile, "name"):
                fontfile_str = fontfile.name
            else:
                raise ValueError("bad fontfile")
        else:
            fontfile_str = None
        val = self._insertFont(fontname, bfname, fontfile_str, fontbuffer, set_simple, idx,
                               wmode, serif, encoding, CJK_number)

        if not val:                   # did not work, error return
            return val

        xref = val[0]                 # xref of installed font
        fontdict = val[1]

        if CheckFontInfo(doc, xref):  # check again: document already has this font
            return xref               # we are done

        # need to create document font info
        doc.get_char_widths(xref, fontdict=fontdict)
        return xref

    def insert_htmlbox(
        page,
        rect,
        text,
        *,
        css=None,
        scale_low=0,
        archive=None,
        rotate=0,
        oc=0,
        opacity=1,
        overlay=True,
        _scale_word_width=True,
        _verbose=False,
    ) -> tuple:
        """Insert text with optional HTML tags and stylings into a rectangle.

        Args:
            rect: (rect-like) rectangle into which the text should be placed.
            text: (str) text with optional HTML tags and stylings.
            css: (str) CSS styling commands.
            scale_low: (float) force-fit content by scaling it down. Must be in
                range [0, 1]. If 1, no scaling will take place. If 0, arbitrary
                down-scaling is acceptable. A value of 0.1 would mean that content
                may be scaled down by at most 90%.
            archive: Archive object pointing to locations of used fonts or images
            rotate: (int) rotate the text in the box by a multiple of 90 degrees.
            oc: (int) the xref of an OCG / OCMD (Optional Content).
            opacity: (float) set opacity of inserted content.
            overlay: (bool) put text on top of page content.
            _scale_word_width: internal, for testing only.
            _verbose: internal, for testing only.
        Returns:
            A tuple of floats (spare_height, scale).
            spare_height:
                The height of the remaining space in <rect> below the
                text, or -1 if we failed to fit.
            scale:
                The scaling required; `0 < scale <= 1`.
                Will be less than `scale_low` if we failed to fit.
        """
        # normalize rotation angle
        if not rotate % 90 == 0:
            raise ValueError("bad rotation angle")
        while rotate < 0:
            rotate += 360
        while rotate >= 360:
            rotate -= 360

        if not 0 <= scale_low <= 1:
            raise ValueError("'scale_low' must be in [0, 1]")

        if css is None:
            css = ""

        rect = Rect(rect)
        if rotate in (90, 270):
            temp_rect = Rect(0, 0, rect.height, rect.width)
        else:
            temp_rect = Rect(0, 0, rect.width, rect.height)

        # use a small border by default
        mycss = "body {margin:1px;}" + css  # append user CSS

        # either make a story, or accept a given one
        if isinstance(text, str):  # if a string, convert to a Story
            story = Story(html=text, user_css=mycss, archive=archive)
        elif isinstance(text, Story):
            story = text
        else:
            raise ValueError("'text' must be a string or a Story")
        
        # ----------------------------------------------------------------
        # Find a scaling factor that lets our story fit in. Instead of scaling
        # the text smaller, we instead look at how much bigger the rect needs
        # to be to fit the text, then reverse the scaling to get how much we
        # need to scale down the text.
        # ----------------------------------------------------------------
        rect_scale_max = None if scale_low == 0 else 1 / scale_low

        fit = story.fit_scale(
                temp_rect,
                scale_min=1,
                scale_max=rect_scale_max,
                flags=mupdf.FZ_PLACE_STORY_FLAG_NO_OVERFLOW if _scale_word_width else 0,
                verbose=_verbose,
                )
        
        if not fit.big_enough:  # there was no fit
            scale = 1 / fit.parameter
            return (-1, scale)

        # fit.filled is a tuple; we convert it in place to a Rect for
        # convenience. (fit.rect is already a Rect.)
        fit.filled = Rect(fit.filled)
        assert (fit.rect.x0, fit.rect.y0) == (0, 0)
        assert (fit.filled.x0, fit.filled.y0) == (0, 0)
        
        scale = 1 / fit.parameter
        assert scale >= scale_low, f'{scale_low=} {scale=}'
        
        spare_height = max((fit.rect.y1 - fit.filled.y1) * scale, 0)

        def rect_function(*args):
            return fit.rect, fit.rect, None

        # draw story on temp PDF page
        doc = story.write_with_links(rect_function)

        # Insert opacity if requested.
        # For this, we prepend a command to the /Contents.
        if 0 <= opacity < 1:
            tpage = doc[0]  # load page
            # generate /ExtGstate for the page
            alp0 = tpage._set_opacity(CA=opacity, ca=opacity)
            s = f"/{alp0} gs\n"  # generate graphic state command
            TOOLS._insert_contents(tpage, s.encode(), 0)

        # put result in target page
        page.show_pdf_page(rect, doc, 0, rotate=rotate, oc=oc, overlay=overlay)

        # -------------------------------------------------------------------------
        # re-insert links in target rect (show_pdf_page cannot copy annotations)
        # -------------------------------------------------------------------------
        # scaled center point of fit.rect
        mp1 = (fit.rect.tl + fit.rect.br) / 2 * scale

        # center point of target rect
        mp2 = (rect.tl + rect.br) / 2

        # compute link positioning matrix:
        # - move center of scaled-down fit.rect to (0,0)
        # - rotate
        # - move (0,0) to center of target rect
        mat = (
            Matrix(scale, 0, 0, scale, -mp1.x, -mp1.y)
            * Matrix(-rotate)
            * Matrix(1, 0, 0, 1, mp2.x, mp2.y)
        )

        # copy over links
        for link in doc[0].get_links():
            link["from"] *= mat
            page.insert_link(link)

        return spare_height, scale

    def insert_image(
            page,
            rect,
            *,
            alpha=-1,
            filename=None,
            height=0,
            keep_proportion=True,
            mask=None,
            oc=0,
            overlay=True,
            pixmap=None,
            rotate=0,
            stream=None,
            width=0,
            xref=0,
            ):
        """Insert an image for display in a rectangle.

        Args:
            rect: (rect_like) position of image on the page.
            alpha: (int, optional) set to 0 if image has no transparency.
            filename: (str, Path, file object) image filename.
            height: (int)
            keep_proportion: (bool) keep width / height ratio (default).
            mask: (bytes, optional) image consisting of alpha values to use.
            oc: (int) xref of OCG or OCMD to declare as Optional Content.
            overlay: (bool) put in foreground (default) or background.
            pixmap: (pymupdf.Pixmap) use this as image.
            rotate: (int) rotate by 0, 90, 180 or 270 degrees.
            stream: (bytes) use this as image.
            width: (int)
            xref: (int) use this as image.

        'page' and 'rect' are positional, all other parameters are keywords.

        If 'xref' is given, that image is used. Other input options are ignored.
        Else, exactly one of pixmap, stream or filename must be given.

        'alpha=0' for non-transparent images improves performance significantly.
        Affects stream and filename only.

        Optimum transparent insertions are possible by using filename / stream in
        conjunction with a 'mask' image of alpha values.

        Returns:
            xref (int) of inserted image. Re-use as argument for multiple insertions.
        """
        CheckParent(page)
        doc = page.parent
        if not doc.is_pdf:
            raise ValueError("is no PDF")

        if xref == 0 and (bool(filename) + bool(stream) + bool(pixmap) != 1):
            raise ValueError("xref=0 needs exactly one of filename, pixmap, stream")

        if filename:
            if type(filename) is str:
                pass
            elif hasattr(filename, "absolute"):
                filename = str(filename)
            elif hasattr(filename, "name"):
                filename = filename.name
            else:
                raise ValueError("bad filename")

        if filename and not os.path.exists(filename):
            raise FileNotFoundError("No such file: '%s'" % filename)
        elif stream and type(stream) not in (bytes, bytearray, io.BytesIO):
            raise ValueError("stream must be bytes-like / BytesIO")
        elif pixmap and type(pixmap) is not Pixmap:
            raise ValueError("pixmap must be a Pixmap")
        if mask and not (stream or filename):
            raise ValueError("mask requires stream or filename")
        if mask and type(mask) not in (bytes, bytearray, io.BytesIO):
            raise ValueError("mask must be bytes-like / BytesIO")
        while rotate < 0:
            rotate += 360
        while rotate >= 360:
            rotate -= 360
        if rotate not in (0, 90, 180, 270):
            raise ValueError("bad rotate value")

        r = Rect(rect)
        if r.is_empty or r.is_infinite:
            raise ValueError("rect must be finite and not empty")
        clip = r * ~page.transformation_matrix

        # Create a unique image reference name.
        ilst = [i[7] for i in doc.get_page_images(page.number)]
        ilst += [i[1] for i in doc.get_page_xobjects(page.number)]
        ilst += [i[4] for i in doc.get_page_fonts(page.number)]
        n = "fzImg"  # 'pymupdf image'
        i = 0
        _imgname = n + "0"  # first name candidate
        while _imgname in ilst:
            i += 1
            _imgname = n + str(i)  # try new name

        if overlay:
            page.wrap_contents()  # ensure a balanced graphics state
        digests = doc.InsertedImages
        xref, digests = page._insert_image(
            filename=filename,
            pixmap=pixmap,
            stream=stream,
            imask=mask,
            clip=clip,
            overlay=overlay,
            oc=oc,
            xref=xref,
            rotate=rotate,
            keep_proportion=keep_proportion,
            width=width,
            height=height,
            alpha=alpha,
            _imgname=_imgname,
            digests=digests,
        )
        if digests is not None:
            doc.InsertedImages = digests

        return xref

    def insert_link(page: 'Page', lnk: dict, mark: bool = True) -> None:
        """Insert a new link for the current page."""
        CheckParent(page)
        annot = utils.getLinkText(page, lnk)
        if annot == "":
            raise ValueError("link kind not supported")
        page._addAnnot_FromString((annot,))

    def insert_text(
            page: 'Page',
            point: point_like,
            text: typing.Union[str, list],
            *,
            fontsize: float = 11,
            lineheight: OptFloat = None,
            fontname: str = "helv",
            fontfile: OptStr = None,
            set_simple: int = 0,
            encoding: int = 0,
            color: OptSeq = None,
            fill: OptSeq = None,
            border_width: float = 0.05,
            miter_limit: float = 1,
            render_mode: int = 0,
            rotate: int = 0,
            morph: OptSeq = None,
            overlay: bool = True,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc: int = 0,
            ):

        img = page.new_shape()
        rc = img.insert_text(
            point,
            text,
            fontsize=fontsize,
            lineheight=lineheight,
            fontname=fontname,
            fontfile=fontfile,
            set_simple=set_simple,
            encoding=encoding,
            color=color,
            fill=fill,
            border_width=border_width,
            render_mode=render_mode,
            miter_limit=miter_limit,
            rotate=rotate,
            morph=morph,
            stroke_opacity=stroke_opacity,
            fill_opacity=fill_opacity,
            oc=oc,
        )
        if rc >= 0:
            img.commit(overlay)
        return rc

    def insert_textbox(
            page: 'Page',
            rect: rect_like,
            buffer: typing.Union[str, list],
            *,
            fontname: str = "helv",
            fontfile: OptStr = None,
            set_simple: int = 0,
            encoding: int = 0,
            fontsize: float = 11,
            lineheight: OptFloat = None,
            color: OptSeq = None,
            fill: OptSeq = None,
            expandtabs: int = 1,
            align: int = 0,
            rotate: int = 0,
            render_mode: int = 0,
            miter_limit: float = 1,
            border_width: float = 0.05,
            morph: OptSeq = None,
            overlay: bool = True,
            stroke_opacity: float = 1,
            fill_opacity: float = 1,
            oc: int = 0,
            ) -> float:
        """Insert text into a given rectangle.

        Notes:
            Creates a Shape object, uses its same-named method and commits it.
        Parameters:
            rect: (rect-like) area to use for text.
            buffer: text to be inserted
            fontname: a Base-14 font, font name or '/name'
            fontfile: name of a font file
            fontsize: font size
            lineheight: overwrite the font property
            color: RGB color triple
            expandtabs: handles tabulators with string function
            align: left, center, right, justified
            rotate: 0, 90, 180, or 270 degrees
            morph: morph box with a matrix and a fixpoint
            overlay: put text in foreground or background
        Returns:
            unused or deficit rectangle area (float)
        """
        img = page.new_shape()
        rc = img.insert_textbox(
            rect,
            buffer,
            fontsize=fontsize,
            lineheight=lineheight,
            fontname=fontname,
            fontfile=fontfile,
            set_simple=set_simple,
            encoding=encoding,
            color=color,
            fill=fill,
            expandtabs=expandtabs,
            render_mode=render_mode,
            miter_limit=miter_limit,
            border_width=border_width,
            align=align,
            rotate=rotate,
            morph=morph,
            stroke_opacity=stroke_opacity,
            fill_opacity=fill_opacity,
            oc=oc,
        )
        if rc >= 0:
            img.commit(overlay)
        return rc

    @property
    def is_wrapped(self):
        """Check if /Contents is in a balanced graphics state."""
        return self._count_q_balance() == (0, 0)

    @property
    def language(self):
        """Page language."""
        pdfpage = _as_pdf_page(self.this, required=False)
        if not pdfpage.m_internal:
            return
        lang = mupdf.pdf_dict_get_inheritable(pdfpage.obj(), PDF_NAME('Lang'))
        if not lang.m_internal:
            return
        return mupdf.pdf_to_str_buf(lang)

    def links(self, kinds=None):
        """ Generator over the links of a page.

        Args:
            kinds: (list) link kinds to subselect from. If none,
                   all links are returned. E.g. kinds=[LINK_URI]
                   will only yield URI links.
        """
        all_links = self.get_links()
        for link in all_links:
            if kinds is None or link["kind"] in kinds:
                yield (link)

    def load_annot(self, ident: typing.Union[str, int]) -> Annot:
        """Load an annot by name (/NM key) or xref.

        Args:
            ident: identifier, either name (str) or xref (int).
        """
        CheckParent(self)
        if type(ident) is str:
            xref = 0
            name = ident
        elif type(ident) is int:
            xref = ident
            name = None
        else:
            raise ValueError("identifier must be a string or integer")
        val = self._load_annot(name, xref)
        if not val:
            return val
        val.thisown = True
        val.parent = weakref.proxy(self)
        self._annot_refs[id(val)] = val
        return val

    def load_links(self):
        """Get first Link."""
        CheckParent(self)
        val = mupdf.fz_load_links( self.this)
        if not val.m_internal:
            return
        val = Link( val)
        val.thisown = True
        val.parent = weakref.proxy(self) # owning page object
        self._annot_refs[id(val)] = val
        val.xref = 0
        val.id = ""
        if self.parent.is_pdf:
            xrefs = self.annot_xrefs()
            xrefs = [x for x in xrefs if x[1] == mupdf.PDF_ANNOT_LINK]
            if xrefs:
                link_id = xrefs[0]
                val.xref = link_id[0]
                val.id = link_id[2]
        else:
            val.xref = 0
            val.id = ""
        return val

    #----------------------------------------------------------------
    # page load widget by xref
    #----------------------------------------------------------------
    def load_widget( self, xref):
        """Load a widget by its xref."""
        CheckParent(self)

        page = _as_pdf_page(self.this)
        annot = JM_get_widget_by_xref( page, xref)
        #log( '{=type(annot)}')
        val = annot
        if not val:
            return val
        val.thisown = True
        val.parent = weakref.proxy(self)
        self._annot_refs[id(val)] = val
        widget = Widget()
        TOOLS._fill_widget(val, widget)
        val = widget
        return val

    @property
    def mediabox(self):
        """The MediaBox."""
        CheckParent(self)
        page = self._pdf_page(required=False)
        if not page.m_internal:
            rect = mupdf.fz_bound_page( self.this)
        else:
            rect = JM_mediabox( page.obj())
        return Rect(rect)

    @property
    def mediabox_size(self):
        return Point(self.mediabox.x1, self.mediabox.y1)

    def new_shape(self):
        return Shape(self)

    #@property
    #def parent( self):
    #    assert self._parent
    #    if self._parent:
    #        return self._parent
    #    return Document( self.this.document())

    def read_contents(self):
        """All /Contents streams concatenated to one bytes object."""
        return TOOLS._get_all_contents(self)

    def refresh(self):
        """Refresh page after link/annot/widget updates."""
        CheckParent(self)
        doc = self.parent
        page = doc.reload_page(self)
        # fixme this looks wrong.
        self.this = page

    def replace_image(
            page: 'Page',
            xref: int,
            *,
            filename=None,
            pixmap=None,
            stream=None,
            ):
        """Replace the image referred to by xref.

        Replace the image by changing the object definition stored under xref. This
        will leave the pages appearance instructions intact, so the new image is
        being displayed with the same bbox, rotation etc.
        By providing a small fully transparent image, an effect as if the image had
        been deleted can be achieved.
        A typical use may include replacing large images by a smaller version,
        e.g. with a lower resolution or graylevel instead of colored.

        Args:
            xref: the xref of the image to replace.
            filename, pixmap, stream: exactly one of these must be provided. The
                meaning being the same as in Page.insert_image.
        """
        doc = page.parent  # the owning document
        if not doc.xref_is_image(xref):
            raise ValueError("xref not an image")  # insert new image anywhere in page
        if bool(filename) + bool(stream) + bool(pixmap) != 1:
            raise ValueError("Exactly one of filename/stream/pixmap must be given")
        new_xref = page.insert_image(
            page.rect, filename=filename, stream=stream, pixmap=pixmap
        )
        doc.xref_copy(new_xref, xref)  # copy over new to old
        last_contents_xref = page.get_contents()[-1]
        # new image insertion has created a new /Contents source,
        # which we will set to spaces now
        doc.update_stream(last_contents_xref, b" ")
        page._image_info = None  # clear cache of extracted image information

    @property
    def rotation(self):
        """Page rotation."""
        CheckParent(self)
        page = _as_pdf_page(self.this, required=0)
        if not page.m_internal:
            return 0
        return JM_page_rotation(page)

    @property
    def rotation_matrix(self) -> Matrix:
        """Reflects page rotation."""
        return Matrix(TOOLS._rotate_matrix(self))

    def run(self, dw, m):
        """Run page through a device.
        dw: DeviceWrapper
        """
        CheckParent(self)
        mupdf.fz_run_page(self.this, dw.device, JM_matrix_from_py(m), mupdf.FzCookie())

    def search_for(
            page,
            text,
            *,
            clip=None,
            quads=False,
            flags=None,
            textpage=None,
            ) -> list:
        """Search for a string on a page.

        Args:
            text: string to be searched for
            clip: restrict search to this rectangle
            quads: (bool) return quads instead of rectangles
            flags: bit switches, default: join hyphened words
            textpage: a pre-created pymupdf.TextPage
        Returns:
            a list of rectangles or quads, each containing one occurrence.
        """
        if flags is None:
            flags=(0
                | TEXT_DEHYPHENATE
                | TEXT_PRESERVE_WHITESPACE
                | TEXT_PRESERVE_LIGATURES
                | TEXT_MEDIABOX_CLIP
                )
        if clip is not None:
            clip = Rect(clip)

        CheckParent(page)
        tp = textpage
        if tp is None:
            tp = page.get_textpage(clip=clip, flags=flags)  # create pymupdf.TextPage
        elif getattr(tp, "parent") != page:
            raise ValueError("not a textpage of this page")
        rlist = tp.search(text, quads=quads)
        if textpage is None:
            del tp
        return rlist

    def set_artbox(self, rect):
        """Set the ArtBox."""
        return self._set_pagebox("ArtBox", rect)

    def set_bleedbox(self, rect):
        """Set the BleedBox."""
        return self._set_pagebox("BleedBox", rect)

    def set_contents(self, xref):
        """Set object at 'xref' as the page's /Contents."""
        CheckParent(self)
        doc = self.parent
        if doc.is_closed:
            raise ValueError("document closed")
        if not doc.is_pdf:
            raise ValueError("is no PDF")
        if xref not in range(1, doc.xref_length()):
            raise ValueError("bad xref")
        if not doc.xref_is_stream(xref):
            raise ValueError("xref is no stream")
        doc.xref_set_key(self.xref, "Contents", "%i 0 R" % xref)

    def set_cropbox(self, rect):
        """Set the CropBox. Will also change Page.rect."""
        return self._set_pagebox("CropBox", rect)

    def set_language(self, language=None):
        """Set PDF page default language."""
        CheckParent(self)
        pdfpage = _as_pdf_page(self.this)
        if not language:
            mupdf.pdf_dict_del(pdfpage.obj(), PDF_NAME('Lang'))
        else:
            lang = mupdf.fz_text_language_from_string(language)
            assert hasattr(mupdf, 'fz_string_from_text_language2')
            mupdf.pdf_dict_put_text_string(
                    pdfpage.obj,
                    PDF_NAME('Lang'),
                    mupdf.fz_string_from_text_language2(lang)
                    )

    def set_mediabox(self, rect):
        """Set the MediaBox."""
        CheckParent(self)
        page = self._pdf_page()
        mediabox = JM_rect_from_py(rect)
        if (mupdf.fz_is_empty_rect(mediabox)
                or mupdf.fz_is_infinite_rect(mediabox)
                ):
            raise ValueError( MSG_BAD_RECT)
        mupdf.pdf_dict_put_rect( page.obj(), PDF_NAME('MediaBox'), mediabox)
        mupdf.pdf_dict_del( page.obj(), PDF_NAME('CropBox'))
        mupdf.pdf_dict_del( page.obj(), PDF_NAME('ArtBox'))
        mupdf.pdf_dict_del( page.obj(), PDF_NAME('BleedBox'))
        mupdf.pdf_dict_del( page.obj(), PDF_NAME('TrimBox'))

    def set_rotation(self, rotation):
        """Set page rotation."""
        CheckParent(self)
        page = _as_pdf_page(self.this)
        rot = JM_norm_rotation(rotation)
        mupdf.pdf_dict_put_int( page.obj(), PDF_NAME('Rotate'), rot)

    def set_trimbox(self, rect):
        """Set the TrimBox."""
        return self._set_pagebox("TrimBox", rect)

    def show_pdf_page(
            page,
            rect,
            docsrc,
            pno=0,
            keep_proportion=True,
            overlay=True,
            oc=0,
            rotate=0,
            clip=None,
            ) -> int:
        """Show page number 'pno' of PDF 'docsrc' in rectangle 'rect'.

        Args:
            rect: (rect-like) where to place the source image
            docsrc: (document) source PDF
            pno: (int) source page number
            keep_proportion: (bool) do not change width-height-ratio
            overlay: (bool) put in foreground
            oc: (xref) make visibility dependent on this OCG / OCMD (which must be defined in the target PDF)
            rotate: (int) degrees (multiple of 90)
            clip: (rect-like) part of source page rectangle
        Returns:
            xref of inserted object (for reuse)
        """
        def calc_matrix(sr, tr, keep=True, rotate=0):
            """Calculate transformation matrix from source to target rect.

            Notes:
                The product of four matrices in this sequence: (1) translate correct
                source corner to origin, (2) rotate, (3) scale, (4) translate to
                target's top-left corner.
            Args:
                sr: source rect in PDF (!) coordinate system
                tr: target rect in PDF coordinate system
                keep: whether to keep source ratio of width to height
                rotate: rotation angle in degrees
            Returns:
                Transformation matrix.
            """
            # calc center point of source rect
            smp = (sr.tl + sr.br) / 2.0
            # calc center point of target rect
            tmp = (tr.tl + tr.br) / 2.0

            # m moves to (0, 0), then rotates
            m = Matrix(1, 0, 0, 1, -smp.x, -smp.y) * Matrix(rotate)

            sr1 = sr * m  # resulting source rect to calculate scale factors

            fw = tr.width / sr1.width  # scale the width
            fh = tr.height / sr1.height  # scale the height
            if keep:
                fw = fh = min(fw, fh)  # take min if keeping aspect ratio

            m *= Matrix(fw, fh)  # concat scale matrix
            m *= Matrix(1, 0, 0, 1, tmp.x, tmp.y)  # concat move to target center
            return JM_TUPLE(m)

        CheckParent(page)
        doc = page.parent

        if not doc.is_pdf or not docsrc.is_pdf:
            raise ValueError("is no PDF")

        if rect.is_empty or rect.is_infinite:
            raise ValueError("rect must be finite and not empty")

        while pno < 0:  # support negative page numbers
            pno += docsrc.page_count
        src_page = docsrc[pno]  # load source page

        tar_rect = rect * ~page.transformation_matrix  # target rect in PDF coordinates

        src_rect = src_page.rect if not clip else src_page.rect & clip  # source rect
        if src_rect.is_empty or src_rect.is_infinite:
            raise ValueError("clip must be finite and not empty")
        src_rect = src_rect * ~src_page.transformation_matrix  # ... in PDF coord

        matrix = calc_matrix(src_rect, tar_rect, keep=keep_proportion, rotate=rotate)

        # list of existing /Form /XObjects
        ilst = [i[1] for i in doc.get_page_xobjects(page.number)]
        ilst += [i[7] for i in doc.get_page_images(page.number)]
        ilst += [i[4] for i in doc.get_page_fonts(page.number)]

        # create a name not in that list
        n = "fzFrm"
        i = 0
        _imgname = n + "0"
        while _imgname in ilst:
            i += 1
            _imgname = n + str(i)

        isrc = docsrc._graft_id  # used as key for graftmaps
        if doc._graft_id == isrc:
            raise ValueError("source document must not equal target")

        # retrieve / make Graftmap for source PDF
        gmap = doc.Graftmaps.get(isrc, None)
        if gmap is None:
            gmap = Graftmap(doc)
            doc.Graftmaps[isrc] = gmap

        # take note of generated xref for automatic reuse
        pno_id = (isrc, pno)  # id of docsrc[pno]
        xref = doc.ShownPages.get(pno_id, 0)

        if overlay:
            page.wrap_contents()  # ensure a balanced graphics state
        xref = page._show_pdf_page(
            src_page,
            overlay=overlay,
            matrix=matrix,
            xref=xref,
            oc=oc,
            clip=src_rect,
            graftmap=gmap,
            _imgname=_imgname,
        )
        doc.ShownPages[pno_id] = xref

        return xref

    @property
    def transformation_matrix(self):
        """Page transformation matrix."""
        CheckParent(self)

        ctm = mupdf.FzMatrix()
        page = self._pdf_page(required=False)
        if not page.m_internal:
            return JM_py_from_matrix(ctm)
        mediabox = mupdf.FzRect(mupdf.FzRect.Fixed_UNIT)    # fixme: original code passed mediabox=NULL.
        mupdf.pdf_page_transform(page, mediabox, ctm)
        val = JM_py_from_matrix(ctm)

        if self.rotation % 360 == 0:
            val = Matrix(val)
        else:
            val = Matrix(1, 0, 0, -1, 0, self.cropbox.height)
        return val

    @property
    def trimbox(self):
        """The TrimBox"""
        rect = self._other_box("TrimBox")
        if rect is None:
            return self.cropbox
        mb = self.mediabox
        return Rect(rect[0], mb.y1 - rect[3], rect[2], mb.y1 - rect[1])

    def update_link(page: 'Page', lnk: dict) -> None:
        """Update a link on the current page."""
        CheckParent(page)
        annot = utils.getLinkText(page, lnk)
        if annot == "":
            raise ValueError("link kind not supported")

        page.parent.update_object(lnk["xref"], annot, page=page)

    def widgets(self, types=None):
        """ Generator over the widgets of a page.

        Args:
            types: (list) field types to subselect from. If none,
                    all fields are returned. E.g. types=[PDF_WIDGET_TYPE_TEXT]
                    will only yield text fields.
        """
        #for a in self.annot_xrefs():
        #    log( '{a=}')
        widget_xrefs = [a[0] for a in self.annot_xrefs() if a[1] == mupdf.PDF_ANNOT_WIDGET]
        #log(f'widgets(): {widget_xrefs=}')
        for xref in widget_xrefs:
            widget = self.load_widget(xref)
            if types is None or widget.field_type in types:
                yield (widget)

    def wrap_contents(self):
        """Ensure page is in a balanced graphics state."""
        push, pop = self._count_q_balance()  # count missing "q"/"Q" commands
        if push > 0:  # prepend required push commands
            prepend = b"q\n" * push
            TOOLS._insert_contents(self, prepend, False)
        if pop > 0:  # append required pop commands
            append = b"\nQ" * pop + b"\n"
            TOOLS._insert_contents(self, append, True)

    def write_text(
            page: 'Page',
            rect=None,
            writers=None,
            overlay=True,
            color=None,
            opacity=None,
            keep_proportion=True,
            rotate=0,
            oc=0,
            ) -> None:
        """Write the text of one or more pymupdf.TextWriter objects.

        Args:
            rect: target rectangle. If None, the union of the text writers is used.
            writers: one or more pymupdf.TextWriter objects.
            overlay: put in foreground or background.
            keep_proportion: maintain aspect ratio of rectangle sides.
            rotate: arbitrary rotation angle.
            oc: the xref of an optional content object
        """
        assert isinstance(page, Page)
        if not writers:
            raise ValueError("need at least one pymupdf.TextWriter")
        if type(writers) is TextWriter:
            if rotate == 0 and rect is None:
                writers.write_text(page, opacity=opacity, color=color, overlay=overlay)
                return None
            else:
                writers = (writers,)
        clip = writers[0].text_rect
        textdoc = Document()
        tpage = textdoc.new_page(width=page.rect.width, height=page.rect.height)
        for writer in writers:
            clip |= writer.text_rect
            writer.write_text(tpage, opacity=opacity, color=color)
        if rect is None:
            rect = clip
        page.show_pdf_page(
            rect,
            textdoc,
            0,
            overlay=overlay,
            keep_proportion=keep_proportion,
            rotate=rotate,
            clip=clip,
            oc=oc,
        )
        textdoc = None
        tpage = None

    @property
    def xref(self):
        """PDF xref number of page."""
        CheckParent(self)
        return self.parent.page_xref(self.number)

    rect = property(bound, doc="page rectangle")

    # any result of layout analysis is stored here
    layout_information = None

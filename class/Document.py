"""
Class: fitz.Document

Description: No docstring available.

Inheritance (MRO): Document -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Document =====

# FormFonts = <property object at 0x000002052DE31530>  [property]

# __contains__(self, loc) -> bool  [function]

# __enter__(self)  [function]

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __exit__(self, *args)  [function]

# __getitem__(self, i=0)  [function]

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, filename=None, stream=None, filetype=None, rect=None, width=0, height=0, fontsize=11)  [function]
#     -> Creates a document. Use 'open' as a synonym.

# __len__(self) -> int  [function]

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self) -> str  [function]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# add_layer(self, name, creator=None, on=None)  [function]
#     -> Add a new OC layer.

# add_ocg(self, name, config=-1, on=1, intent=None, usage=None)  [function]
#     -> Add new optional content group.

# authenticate(self, password)  [function]
#     -> Decrypt document.

# bake(self, *, annots: bool = True, widgets: bool = True) -> None  [function]
#     -> Convert annotations or fields to permanent content.

# can_save_incrementally(self)  [function]
#     -> Check whether incremental saves are possible.

# chapter_count = <property object at 0x000002052DE31670>  [property]

# chapter_page_count(self, chapter)  [function]
#     -> Page count of chapter.

# close(self)  [function]
#     -> Close document.

# convert_to_pdf(self, from_page=0, to_page=-1, rotate=0)  [function]
#     -> Convert document to a PDF, selecting page range and optional rotation. Output bytes object.

# copy_page(self, pno: int, to: int = -1)  [function]
#     -> Copy a page within a PDF document.

# del_toc_item(self, idx: int) -> None  [function]
#     -> Delete TOC / bookmark item by index.

# del_xml_metadata(self)  [function]
#     -> Delete XML metadata.

# delete_page(self, pno: int = -1)  [function]
#     -> Delete one page from a PDF.

# delete_pages(self, *args, **kw)  [function]
#     -> Delete pages from a PDF.

# embfile_add(self, name: str, buffer_: ByteString, filename: Optional[str] = None, ufilename: Optional[str] = None, desc: Optional[str] = None) -> None  [function]
#     -> Add an item to the EmbeddedFiles array.

# embfile_count(self) -> int  [function]
#     -> Get number of EmbeddedFiles.

# embfile_del(self, item: Union[int, str])  [function]
#     -> Delete an entry from EmbeddedFiles.

# embfile_get(self, item: Union[int, str]) -> bytes  [function]
#     -> Get the content of an item in the EmbeddedFiles array.

# embfile_info(self, item: Union[int, str]) -> dict  [function]
#     -> Get information of an item in the EmbeddedFiles array.

# embfile_names(self) -> list  [function]
#     -> Get list of names of EmbeddedFiles.

# embfile_upd(self, item: Union[int, str], buffer_: Optional[ByteString] = None, filename: Optional[str] = None, ufilename: Optional[str] = None, desc: Optional[str] = None) -> None  [function]
#     -> Change an item of the EmbeddedFiles array.

# extract_font(self, xref=0, info_only=0, named=None)  [function]
#     -> Get a font by xref. Returns a tuple or dictionary.

# extract_image(self, xref)  [function]
#     -> Get image by xref. Returns a dictionary.

# ez_save(self, filename, garbage=3, clean=False, deflate=True, deflate_images=True, deflate_fonts=True, incremental=False, ascii=False, expand=False, linear=False, pretty=False, encryption=1, permissions=4095, owner_pw=None, user_pw=None, no_new_id=True, preserve_metadata=1, use_objstms=1, compression_effort=0, raise_on_repair=False)  [function]
#     -> Save PDF using some different defaults

# find_bookmark(self, bm)  [function]
#     -> Find new location after layouting a document.

# fullcopy_page(self, pno, to=-1)  [function]
#     -> Make a full page duplicate.

# get_char_widths(doc: 'Document', xref: int, limit: int = 256, idx: int = 0, fontdict: Optional[dict] = None) -> list  [function]
#     -> Get list of glyph information of a font.

# get_layer(self, config=-1)  [function]
#     -> Content of ON, OFF, RBGroups of an OC layer.

# get_layers(self)  [function]
#     -> Show optional OC layers.

# get_new_xref(self)  [function]
#     -> Make new xref.

# get_oc(doc: 'Document', xref: int) -> int  [function]
#     -> Return optional content object xref for an image or form xobject.

# get_ocgs(self)  [function]
#     -> Show existing optional content groups.

# get_ocmd(doc: 'Document', xref: int) -> dict  [function]
#     -> Return the definition of an OCMD (optional content membership dictionary).

# get_outline_xrefs(self)  [function]
#     -> Get list of outline xref numbers.

# get_page_fonts(self, pno: int, full: bool = False) -> list  [function]
#     -> Retrieve a list of fonts used on a page.

# get_page_images(self, pno: int, full: bool = False) -> list  [function]
#     -> Retrieve a list of images used on a page.

# get_page_labels(self)  [function]
#     -> Return page label definitions in PDF document.

# get_page_numbers(doc, label, only_one=False)  [function]
#     -> Return a list of page numbers with the given label.

# get_page_pixmap(doc: 'Document', pno: int, *, matrix: 'matrix_like' = None, dpi=None, colorspace: pymupdf.Colorspace = None, clip: 'rect_like' = None, alpha: bool = False, annots: bool = True) -> 'Pixmap'  [function]
#     -> Create pixmap of document page by page number.

# get_page_text(doc: 'Document', pno: int, option: str = 'text', clip: 'rect_like' = None, flags: Optional[int] = None, textpage: 'TextPage' = None, sort: bool = False) -> Any  [function]
#     -> Extract a document page's text by page number.

# get_page_xobjects(self, pno: int) -> list  [function]
#     -> Retrieve a list of XObjects used on a page.

# get_sigflags(self)  [function]
#     -> Get the /SigFlags value.

# get_toc(doc: 'Document', simple: bool = True) -> list  [function]
#     -> Create a table of contents.

# get_xml_metadata(self)  [function]
#     -> Get document XML metadata.

# has_annots(doc: 'Document') -> bool  [function]
#     -> Check whether there are annotations on any page.

# has_links(doc: 'Document') -> bool  [function]
#     -> Check whether there are links on any page.

# init_doc(self)  [function]

# insert_file(self, infile, from_page=-1, to_page=-1, start_at=-1, rotate=-1, links=True, annots=True, show_progress=0, final=1)  [function]
#     -> Insert an arbitrary supported document to an existing PDF.

# insert_page(doc: 'Document', pno: int, text: Union[str, list, NoneType] = None, fontsize: float = 11, width: float = 595, height: float = 842, fontname: str = 'helv', fontfile: Optional[str] = None, color: Optional[Sequence] = (0,)) -> int  [function]
#     -> Create a new PDF page and insert some text.

# insert_pdf(self, docsrc, *, from_page=-1, to_page=-1, start_at=-1, rotate=-1, links=1, annots=1, widgets=1, join_duplicates=0, show_progress=0, final=1, _gmap=None)  [function]
#     -> Insert a page range from another PDF.

# is_dirty = <property object at 0x000002052DE316C0>  [property]

# is_fast_webaccess = <property object at 0x000002052DE31710>  [property]

# is_form_pdf = <property object at 0x000002052DE31760>  [property]

# is_pdf = <property object at 0x000002052DE317B0>  [property]

# is_reflowable = <property object at 0x000002052DE31800>  [property]

# is_repaired = <property object at 0x000002052DE31850>  [property]

# is_stream(self, xref=0)  [function]
#     -> Check if xref is a stream object.

# journal_can_do(self)  [function]
#     -> Show if undo and / or redo are possible.

# journal_enable(self)  [function]
#     -> Activate document journalling.

# journal_is_enabled(self)  [function]
#     -> Check if journalling is enabled.

# journal_load(self, filename)  [function]
#     -> Load a journal from a file.

# journal_op_name(self, step)  [function]
#     -> Show operation name for given step.

# journal_position(self)  [function]
#     -> Show journalling state.

# journal_redo(self)  [function]
#     -> Move forward in the journal.

# journal_save(self, filename)  [function]
#     -> Save journal to a file.

# journal_start_op(self, name=None)  [function]
#     -> Begin a journalling operation.

# journal_stop_op(self)  [function]
#     -> End a journalling operation.

# journal_undo(self)  [function]
#     -> Move backwards in the journal.

# language = <property object at 0x000002052DE318A0>  [property]

# last_location = <property object at 0x000002052DE318F0>  [property]

# layer_ui_configs(self)  [function]
#     -> Show OC visibility status modifiable by user.

# layout(self, rect=None, width=0, height=0, fontsize=11)  [function]
#     -> Re-layout a reflowable document.

# load_page(self, page_id)  [function]
#     -> Load a page.

# location_from_page_number(self, pno)  [function]
#     -> Convert pno to (chapter, page).

# make_bookmark(self, loc)  [function]
#     -> Make a page pointer before layouting document.

# markinfo = <property object at 0x000002052DE31940>  [property]

# move_page(self, pno: int, to: int = -1)  [function]
#     -> Move a page within a PDF document.

# name = <property object at 0x000002052DE31990>  [property]

# need_appearances(self, value=None)  [function]
#     -> Get/set the NeedAppearances value.

# needs_pass = <property object at 0x000002052DE319E0>  [property]

# new_page(doc: 'Document', pno: int = -1, width: float = 595, height: float = 842) -> 'Page_forward_decl'  [function]
#     -> Create and return a new page object.

# next_location(self, page_id)  [function]
#     -> Get (chapter, page) of next page.

# outline = <property object at 0x000002052DE31C60>  [property]

# page_annot_xrefs(self, n)  [function]

# page_count = <property object at 0x000002052DE31A30>  [property]

# page_count2 = <member 'page_count2' of 'Document' objects>  [member_descriptor]

# page_cropbox(self, pno)  [function]
#     -> Get CropBox of page number (without loading page).

# page_number_from_location(self, page_id)  [function]
#     -> Convert (chapter, pno) to page number.

# page_xref(self, pno)  [function]
#     -> Get xref of page number.

# pagelayout = <property object at 0x000002052DE31A80>  [property]

# pagemode = <property object at 0x000002052DE31AD0>  [property]

# pages(self, start: Optional[int] = None, stop: Optional[int] = None, step: Optional[int] = None) -> collections.abc.Iterable['Page_forward_decl']  [function]
#     -> Return a generator iterator over a page range.

# pdf_catalog(self)  [function]
#     -> Get xref of PDF catalog.

# pdf_trailer(self, compressed=0, ascii=0)  [function]
#     -> Get PDF trailer as a string.

# permissions = <property object at 0x000002052DE31B70>  [property]

# prev_location(self, page_id)  [function]
#     -> Get (chapter, page) of previous page.

# recolor(self, components=1)  [function]
#     -> Change the color component count on all pages.

# reload_page(self, page: 'Page_forward_decl') -> 'Page_forward_decl'  [function]
#     -> Make a fresh copy of a page.

# repair(self)  [function]
#     -> If we are a PDF document, does repair.

# resolve_link(self, uri=None, chapters=0)  [function]
#     -> Calculate internal link destination.

# resolve_names(self)  [function]
#     -> Convert the PDF's destination names into a Python dict.

# rewrite_images(self, dpi_threshold=None, dpi_target=0, quality=0, lossy=True, lossless=True, bitonal=True, color=True, gray=True, set_to_gray=False, options=None)  [function]
#     -> Rewrite images in a PDF document.

# save(self, filename, garbage=0, clean=0, deflate=0, deflate_images=0, deflate_fonts=0, incremental=0, ascii=0, expand=0, linear=0, no_new_id=0, appearance=0, pretty=0, encryption=1, permissions=4095, owner_pw=None, user_pw=None, preserve_metadata=1, use_objstms=0, compression_effort=0, raise_on_repair=False)  [function]

# saveIncr(self)  [function]
#     -> Save PDF incrementally

# save_snapshot(self, filename)  [function]
#     -> Save a file snapshot suitable for journalling.

# scrub(doc: 'Document', attached_files: bool = True, clean_pages: bool = True, embedded_files: bool = True, hidden_text: bool = True, javascript: bool = True, metadata: bool = True, redactions: bool = True, redact_images: int = 0, remove_links: bool = True, reset_fields: bool = True, reset_responses: bool = True, thumbnails: bool = True, xml_metadata: bool = True) -> None  [function]

# search_page_for(doc: 'Document', pno: int, text: str, quads: bool = False, clip: 'rect_like' = None, flags: int = None, textpage: 'TextPage' = None) -> list  [function]
#     -> Search for a string on a page.

# select(self, pyliste)  [function]
#     -> Build sub-pdf with page numbers in the list.

# set_language(self, language=None)  [function]

# set_layer(self, config, basestate=None, on=None, off=None, rbgroups=None, locked=None)  [function]
#     -> Set the PDF keys /ON, /OFF, /RBGroups of an OC layer.

# set_layer_ui_config(self, number, action=0)  [function]
#     -> Set / unset OC intent configuration.

# set_markinfo(self, markinfo: dict) -> bool  [function]
#     -> Set the PDF MarkInfo values.

# set_metadata(doc: 'Document', m: dict = None) -> None  [function]
#     -> Update the PDF /Info object.

# set_oc(doc: 'Document', xref: int, oc: int) -> None  [function]
#     -> Attach optional content object to image or form xobject.

# set_ocmd(doc: 'Document', xref: int = 0, ocgs: Optional[list] = None, policy: Optional[str] = None, ve: Optional[list] = None) -> int  [function]
#     -> Create or update an OCMD object in a PDF document.

# set_page_labels(doc, labels)  [function]
#     -> Add / replace page label definitions in PDF document.

# set_pagelayout(self, pagelayout: str)  [function]
#     -> Set the PDF PageLayout value.

# set_pagemode(self, pagemode: str)  [function]
#     -> Set the PDF PageMode value.

# set_toc(doc: 'Document', toc: list, collapse: int = 1) -> int  [function]
#     -> Create new outline tree (table of contents, TOC).

# set_toc_item(doc: 'Document', idx: int, dest_dict: Optional[dict] = None, kind: Optional[int] = None, pno: Optional[int] = None, uri: Optional[str] = None, title: Optional[str] = None, to: 'point_like' = None, filename: Optional[str] = None, zoom: float = 0) -> None  [function]
#     -> Update TOC item by index.

# set_xml_metadata(self, metadata)  [function]
#     -> Store XML document level metadata.

# subset_fonts(doc: 'Document', verbose: bool = False, fallback: bool = False) -> Optional[int]  [function]
#     -> Build font subsets in a PDF.

# switch_layer(self, config, as_default=0)  [function]
#     -> Activate an OC layer.

# this = <member 'this' of 'Document' objects>  [member_descriptor]

# this_is_pdf = <member 'this_is_pdf' of 'Document' objects>  [member_descriptor]

# tobytes(self, *args, **kwargs)  [function]

# update_object(self, xref, text, page=None)  [function]
#     -> Replace object definition source.

# update_stream(self, xref=0, stream=None, new=1, compress=1)  [function]
#     -> Replace xref stream part.

# version_count = <property object at 0x000002052DE31BC0>  [property]

# write(self, garbage=False, clean=False, deflate=False, deflate_images=False, deflate_fonts=False, incremental=False, ascii=False, expand=False, linear=False, no_new_id=False, appearance=False, pretty=False, encryption=1, permissions=4095, owner_pw=None, user_pw=None, preserve_metadata=1, use_objstms=0, compression_effort=0, raise_on_repair=False)  [function]

# xref = <property object at 0x000002052DE31C10>  [property]

# xref_copy(doc: 'Document', source: int, target: int, *, keep: list = None) -> None  [function]
#     -> Copy a PDF dictionary object to another one given their xref numbers.

# xref_get_key(self, xref, key)  [function]
#     -> Get PDF dict key value of object at 'xref'.

# xref_get_keys(self, xref)  [function]
#     -> Get the keys of PDF dict object at 'xref'. Use -1 for the PDF trailer.

# xref_is_font(self, xref)  [function]
#     -> Check if xref is a font object.

# xref_is_image(self, xref)  [function]
#     -> Check if xref is an image object.

# xref_is_stream(self, xref=0)  [function]
#     -> Check if xref is a stream object.

# xref_is_xobject(self, xref)  [function]
#     -> Check if xref is a form xobject.

# xref_length(self)  [function]
#     -> Get length of xref table.

# xref_object(self, xref, compressed=0, ascii=0)  [function]
#     -> Get xref object source as a string.

# xref_set_key(self, xref, key, value)  [function]
#     -> Set the value of a PDF dictionary key.

# xref_stream(self, xref)  [function]
#     -> Get decompressed xref stream.

# xref_stream_raw(self, xref)  [function]
#     -> Get xref stream without decompression.

# xref_xml_metadata(self)  [function]
#     -> Get xref of document XML metadata.


# ===== Source Code =====
class Document:

    def __contains__(self, loc) -> bool:
        if type(loc) is int:
            if loc < self.page_count:
                return True
            return False
        if type(loc) not in (tuple, list) or len(loc) != 2:
            return False
        chapter, pno = loc
        if (0
                or not isinstance(chapter, int)
                or chapter < 0
                or chapter >= self.chapter_count
                ):
            return False
        if (0
                or not isinstance(pno, int)
                or pno < 0
                or pno >= self.chapter_page_count(chapter)
                ):
            return False
        return True

    def __delitem__(self, i)->None:
        if not self.is_pdf:
            raise ValueError("is no PDF")
        if type(i) is int:
            return self.delete_page(i)
        if type(i) in (list, tuple, range):
            return self.delete_pages(i)
        if type(i) is not slice:
            raise ValueError("bad argument type")
        pc = self.page_count
        start = i.start if i.start else 0
        stop = i.stop if i.stop else pc
        step = i.step if i.step else 1
        while start < 0:
            start += pc
        if start >= pc:
            raise ValueError("bad page number(s)")
        while stop < 0:
            stop += pc
        if stop > pc:
            raise ValueError("bad page number(s)")
        return self.delete_pages(range(start, stop, step))

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    @typing.overload
    def __getitem__(self, i: int = 0) -> Page:
        ...
    
    if sys.version_info >= (3, 9):
        @typing.overload
        def __getitem__(self, i: slice) -> list[Page]:
            ...
        
        @typing.overload
        def __getitem__(self, i: tuple[int, int]) -> Page:
            ...
    
    def __getitem__(self, i=0):
        if isinstance(i, slice):
            return [self[j] for j in range(*i.indices(len(self)))]
        assert isinstance(i, int) or (isinstance(i, tuple) and len(i) == 2 and all(isinstance(x, int) for x in i)), \
                f'Invalid item number: {i=}.'
        if i not in self:
            raise IndexError(f"page {i} not in document")
        return self.load_page(i)

    def __init__(self, filename=None, stream=None, filetype=None, rect=None, width=0, height=0, fontsize=11):
        """Creates a document. Use 'open' as a synonym.

        Notes:
            Basic usages:
            open() - new PDF document
            open(filename) - string or pathlib.Path, must have supported
                    file extension.
            open(type, buffer) - type: valid extension, buffer: bytes object.
            open(stream=buffer, filetype=type) - keyword version of previous.
            open(filename, fileype=type) - filename with unrecognized extension.
            rect, width, height, fontsize: layout reflowable document
            on open (e.g. EPUB). Ignored if n/a.
        """
        # We temporarily set JM_mupdf_show_errors=0 while we are constructing,
        # then restore its original value in a `finally:` block.
        #
        global JM_mupdf_show_errors
        JM_mupdf_show_errors_old = JM_mupdf_show_errors
        JM_mupdf_show_errors = 0
        
        try:
            self.is_closed    = False
            self.is_encrypted = False
            self.is_encrypted = False
            self.metadata    = None
            self.FontInfos   = []
            self.Graftmaps   = {}
            self.ShownPages  = {}
            self.InsertedImages  = {}
            self._page_refs  = weakref.WeakValueDictionary()
            if isinstance(filename, mupdf.PdfDocument):
                pdf_document = filename
                self.this = pdf_document
                self.this_is_pdf = True
                return
        
            w = width
            h = height
            r = JM_rect_from_py(rect)
            if not mupdf.fz_is_infinite_rect(r):
                w = r.x1 - r.x0
                h = r.y1 - r.y0

            self._name = filename
            self.stream = stream
            
            if stream is not None:
                if filename is not None and filetype is None:
                    # 2025-05-06: Use <filename> as the filetype. This is
                    # reversing precedence - we used to use <filename> if both
                    # were set.
                    filetype = filename
                if isinstance(stream, (bytes, memoryview)):
                    pass
                elif isinstance(stream, bytearray):
                    stream = bytes(stream)
                elif isinstance(stream, io.BytesIO):
                    stream = stream.getvalue()
                else:
                    raise TypeError(f"bad stream: {type(stream)=}.")
                self.stream = stream
                
                assert isinstance(stream, (bytes, memoryview))
                if len(stream) == 0:
                    # MuPDF raise an exception for this but also generates
                    # warnings, which is not very helpful for us. So instead we
                    # raise a specific exception.
                    raise EmptyFileError('Cannot open empty stream.')
                    
                stream2 = mupdf.fz_open_memory(mupdf.python_buffer_data(stream), len(stream))
                try:
                    doc = mupdf.fz_open_document_with_stream(filetype if filetype else '', stream2)
                except Exception as e:
                    if g_exceptions_verbose > 1:    exception_info()
                    raise FileDataError('Failed to open stream') from e
            
            elif filename:
                assert not stream
                if isinstance(filename, str):
                    pass
                elif hasattr(filename, "absolute"):
                    filename = str(filename)
                elif hasattr(filename, "name"):
                    filename = filename.name
                else:
                    raise TypeError(f"bad filename: {type(filename)=} {filename=}.")
                self._name = filename
                
                # Generate our own specific exceptions. This avoids MuPDF
                # generating warnings etc.
                if not os.path.exists(filename):
                    raise FileNotFoundError(f"no such file: '{filename}'")
                elif not os.path.isfile(filename):
                    raise FileDataError(f"'{filename}' is no file")
                elif os.path.getsize(filename) == 0:
                    raise EmptyFileError(f'Cannot open empty file: {filename=}.')
                
                if filetype:
                    # Override the type implied by <filename>. MuPDF does not
                    # have a way to do this directly so we open via a stream.
                    try:
                        fz_stream = mupdf.fz_open_file(filename)
                        doc = mupdf.fz_open_document_with_stream(filetype, fz_stream)
                    except Exception as e:
                        if g_exceptions_verbose > 1:    exception_info()
                        raise FileDataError(f'Failed to open file {filename!r} as type {filetype!r}.') from e
                else:
                    try:
                        doc = mupdf.fz_open_document(filename)
                    except Exception as e:
                        if g_exceptions_verbose > 1:    exception_info()
                        raise FileDataError(f'Failed to open file {filename!r}.') from e

            else:
                pdf = mupdf.PdfDocument()
                doc = mupdf.FzDocument(pdf)
            
            if w > 0 and h > 0:
                mupdf.fz_layout_document(doc, w, h, fontsize)
            elif mupdf.fz_is_document_reflowable(doc):
                mupdf.fz_layout_document(doc, 400, 600, 11)

            self.this = doc

            # fixme: not sure where self.thisown gets initialised in PyMuPDF.
            #
            self.thisown = True

            if self.thisown:
                self._graft_id = TOOLS.gen_id()
                if self.needs_pass:
                    self.is_encrypted = True
                else: # we won't init until doc is decrypted
                    self.init_doc()
                # the following hack detects invalid/empty SVG files, which else may lead
                # to interpreter crashes
                if filename and filename.lower().endswith("svg") or filetype and "svg" in filetype.lower():
                    try:
                        _ = self.convert_to_pdf()  # this seems to always work
                    except Exception as e:
                        if g_exceptions_verbose > 1:    exception_info()
                        raise FileDataError("cannot open broken document") from e

            if g_use_extra:
                self.this_is_pdf = isinstance( self.this, mupdf.PdfDocument)
                if self.this_is_pdf:
                    self.page_count2 = extra.page_count_pdf
                else:
                    self.page_count2 = extra.page_count_fz
        finally:
            JM_mupdf_show_errors = JM_mupdf_show_errors_old
    
    def __len__(self) -> int:
        return self.page_count

    def __repr__(self) -> str:
        m = "closed " if self.is_closed else ""
        if self.stream is None:
            if self.name == "":
                return m + "Document(<new PDF, doc# %i>)" % self._graft_id
            return m + "Document('%s')" % (self.name,)
        return m + "Document('%s', <memory, doc# %i>)" % (self.name, self._graft_id)

    def _addFormFont(self, name, font):
        """Add new form font."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self, required=0)
        if not pdf.m_internal:
            return
        fonts = mupdf.pdf_dict_getl(
                mupdf.pdf_trailer( pdf),
                PDF_NAME('Root'),
                PDF_NAME('AcroForm'),
                PDF_NAME('DR'),
                PDF_NAME('Font'),
                )
        if not fonts.m_internal or not mupdf.pdf_is_dict( fonts):
            raise RuntimeError( "PDF has no form fonts yet")
        k = mupdf.pdf_new_name( name)
        v = JM_pdf_obj_from_str( pdf, font)
        mupdf.pdf_dict_put( fonts, k, v)

    def del_toc_item(
            self,
            idx: int,
            ) -> None:
        """Delete TOC / bookmark item by index."""
        xref = self.get_outline_xrefs()[idx]
        self._remove_toc_item(xref)

    def _delToC(self):
        """Delete the TOC."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        xrefs = []  # create Python list
        pdf = _as_pdf_document(self, required=0)
        if not pdf.m_internal:
            return xrefs    # not a pdf
        # get the main root
        root = mupdf.pdf_dict_get(mupdf.pdf_trailer(pdf), PDF_NAME('Root'))
        # get the outline root
        olroot = mupdf.pdf_dict_get(root, PDF_NAME('Outlines'))
        if not olroot.m_internal:
            return xrefs    # no outlines or some problem

        first = mupdf.pdf_dict_get(olroot, PDF_NAME('First'))  # first outline

        xrefs = JM_outline_xrefs(first, xrefs)
        xref_count = len(xrefs)

        olroot_xref = mupdf.pdf_to_num(olroot) # delete OL root
        mupdf.pdf_delete_object(pdf, olroot_xref)  # delete OL root
        mupdf.pdf_dict_del(root, PDF_NAME('Outlines')) # delete OL root

        for i in range(xref_count):
            _, xref = JM_INT_ITEM(xrefs, i)
            mupdf.pdf_delete_object(pdf, xref) # delete outline item
        xrefs.append(olroot_xref)
        val = xrefs
        self.init_doc()
        return val

    def _delete_page(self, pno):
        pdf = _as_pdf_document(self)
        mupdf.pdf_delete_page( pdf, pno)
        if pdf.m_internal.rev_page_map:
            mupdf.ll_pdf_drop_page_tree( pdf.m_internal)

    def _deleteObject(self, xref):
        """Delete object."""
        pdf = _as_pdf_document(self)
        if not _INRANGE(xref, 1, mupdf.pdf_xref_len(pdf)-1):
            raise ValueError( MSG_BAD_XREF)
        mupdf.pdf_delete_object(pdf, xref)

    def _do_links(
            doc1: 'Document',
            doc2: 'Document',
            from_page: int = -1,
            to_page: int = -1,
            start_at: int = -1,
            ) -> None:
        """Insert links contained in copied page range into destination PDF.

        Parameter values **must** equal those of method insert_pdf(), which must
        have been previously executed.
        """
        #pymupdf.log( 'utils.do_links()')
        # --------------------------------------------------------------------------
        # internal function to create the actual "/Annots" object string
        # --------------------------------------------------------------------------
        def cre_annot(lnk, xref_dst, pno_src, ctm):
            """Create annotation object string for a passed-in link."""

            r = lnk["from"] * ctm  # rect in PDF coordinates
            rect = _format_g(tuple(r))
            if lnk["kind"] == LINK_GOTO:
                txt = annot_skel["goto1"]  # annot_goto
                idx = pno_src.index(lnk["page"])
                p = lnk["to"] * ctm  # target point in PDF coordinates
                annot = txt(xref_dst[idx], p.x, p.y, lnk["zoom"], rect)

            elif lnk["kind"] == LINK_GOTOR:
                if lnk["page"] >= 0:
                    txt = annot_skel["gotor1"]  # annot_gotor
                    pnt = lnk.get("to", Point(0, 0))  # destination point
                    if type(pnt) is not Point:
                        pnt = Point(0, 0)
                    annot = txt(
                        lnk["page"],
                        pnt.x,
                        pnt.y,
                        lnk["zoom"],
                        lnk["file"],
                        lnk["file"],
                        rect,
                    )
                else:
                    txt = annot_skel["gotor2"]  # annot_gotor_n
                    to = get_pdf_str(lnk["to"])
                    to = to[1:-1]
                    f = lnk["file"]
                    annot = txt(to, f, rect)

            elif lnk["kind"] == LINK_LAUNCH:
                txt = annot_skel["launch"]  # annot_launch
                annot = txt(lnk["file"], lnk["file"], rect)

            elif lnk["kind"] == LINK_URI:
                txt = annot_skel["uri"]  # annot_uri
                annot = txt(lnk["uri"], rect)

            else:
                annot = ""

            return annot

        # --------------------------------------------------------------------------

        # validate & normalize parameters
        if from_page < 0:
            fp = 0
        elif from_page >= doc2.page_count:
            fp = doc2.page_count - 1
        else:
            fp = from_page

        if to_page < 0 or to_page >= doc2.page_count:
            tp = doc2.page_count - 1
        else:
            tp = to_page

        if start_at < 0:
            raise ValueError("'start_at' must be >= 0")
        sa = start_at

        incr = 1 if fp <= tp else -1  # page range could be reversed

        # lists of source / destination page numbers
        pno_src = list(range(fp, tp + incr, incr))
        pno_dst = [sa + i for i in range(len(pno_src))]

        # lists of source / destination page xrefs
        xref_src = []
        xref_dst = []
        for i in range(len(pno_src)):
            p_src = pno_src[i]
            p_dst = pno_dst[i]
            old_xref = doc2.page_xref(p_src)
            new_xref = doc1.page_xref(p_dst)
            xref_src.append(old_xref)
            xref_dst.append(new_xref)

        # create the links for each copied page in destination PDF
        for i in range(len(xref_src)):
            page_src = doc2[pno_src[i]]  # load source page
            links = page_src.get_links()  # get all its links
            #log( '{pno_src=}')
            #log( '{type(page_src)=}')
            #log( '{page_src=}')
            #log( '{=i len(links)}')
            if len(links) == 0:  # no links there
                page_src = None
                continue
            ctm = ~page_src.transformation_matrix  # calc page transformation matrix
            page_dst = doc1[pno_dst[i]]  # load destination page
            link_tab = []  # store all link definitions here
            for l in links:
                if l["kind"] == LINK_GOTO and (l["page"] not in pno_src):
                    continue  # GOTO link target not in copied pages
                annot_text = cre_annot(l, xref_dst, pno_src, ctm)
                if annot_text:
                    link_tab.append(annot_text)
            if link_tab != []:
                page_dst._addAnnot_FromString( tuple(link_tab))
        #log( 'utils.do_links() returning.')

    def _do_widgets(
            tar: 'Document',
            src: 'Document',
            graftmap,
            from_page: int = -1,
            to_page: int = -1,
            start_at: int = -1,
            join_duplicates=0,
            ) -> None:
        """Insert widgets of copied page range into target PDF.

        Parameter values **must** equal those of method insert_pdf() which
        must have been previously executed.
        """
        if not src.is_form_pdf:  # nothing to do: source PDF has no fields
            return

        def clean_kid_parents(acro_fields):
            """ Make sure all kids have correct "Parent" pointers."""
            for i in range(acro_fields.pdf_array_len()):
                parent = acro_fields.pdf_array_get(i)
                kids = parent.pdf_dict_get(PDF_NAME("Kids"))
                for j in range(kids.pdf_array_len()):
                    kid = kids.pdf_array_get(j)
                    kid.pdf_dict_put(PDF_NAME("Parent"), parent)

        def join_widgets(pdf, acro_fields, xref1, xref2, name):
            """Called for each pair of widgets having the same name.

            Args:
                pdf: target MuPDF document
                acro_fields: object Root/AcroForm/Fields
                xref1, xref2: widget xrefs having same names
                name: (str) the name

            Result:
                Defined or updated widget parent that points to both widgets.
            """

            def re_target(pdf, acro_fields, xref1, kids1, xref2, kids2):
                """Merge widget in xref2 into "Kids" list of widget xref1.

                Args:
                    xref1, kids1: target widget and its "Kids" array.
                    xref2, kids2: source wwidget and its "Kids" array (may be empty).
                """
                # make indirect objects from widgets
                w1_ind = mupdf.pdf_new_indirect(pdf, xref1, 0)
                w2_ind = mupdf.pdf_new_indirect(pdf, xref2, 0)
                # find source widget in "Fields" array
                idx = acro_fields.pdf_array_find(w2_ind)
                acro_fields.pdf_array_delete(idx)

                if not kids2.pdf_is_array():  # source widget has no kids
                    widget = mupdf.pdf_load_object(pdf, xref2)

                    # delete name from widget and insert target as parent
                    widget.pdf_dict_del(PDF_NAME("T"))
                    widget.pdf_dict_put(PDF_NAME("Parent"), w1_ind)

                    # put in target Kids
                    kids1.pdf_array_push(w2_ind)
                else:  # copy source kids to target kids
                    for i in range(kids2.pdf_array_len()):
                        kid = kids2.pdf_array_get(i)
                        kid.pdf_dict_put(PDF_NAME("Parent"), w1_ind)
                        kid_ind = mupdf.pdf_new_indirect(pdf, kid.pdf_to_num(), 0)
                        kids1.pdf_array_push(kid_ind)

            def new_target(pdf, acro_fields, xref1, w1, xref2, w2, name):
                """Make new "Parent" for two widgets with same name.

                Args:
                    xref1, w1: first widget
                    xref2, w2: second widget
                    name: field name

                Result:
                    Both widgets have no "Kids". We create a new object with the
                    name and a "Kids" array containing the widgets.
                    Original widgets must be removed from AcroForm/Fields.
                """
                # make new "Parent" object
                new = mupdf.pdf_new_dict(pdf, 5)
                new.pdf_dict_put_text_string(PDF_NAME("T"), name)
                kids = new.pdf_dict_put_array(PDF_NAME("Kids"), 2)
                new_obj = mupdf.pdf_add_object(pdf, new)
                new_obj_xref = new_obj.pdf_to_num()
                new_ind = mupdf.pdf_new_indirect(pdf, new_obj_xref, 0)

                # copy over some required source widget properties
                ft = w1.pdf_dict_get(PDF_NAME("FT"))
                w1.pdf_dict_del(PDF_NAME("FT"))
                new_obj.pdf_dict_put(PDF_NAME("FT"), ft)

                aa = w1.pdf_dict_get(PDF_NAME("AA"))
                w1.pdf_dict_del(PDF_NAME("AA"))
                new_obj.pdf_dict_put(PDF_NAME("AA"), aa)

                # remove name field, insert "Parent" field in source widgets
                w1.pdf_dict_del(PDF_NAME("T"))
                w1.pdf_dict_put(PDF_NAME("Parent"), new_ind)
                w2.pdf_dict_del(PDF_NAME("T"))
                w2.pdf_dict_put(PDF_NAME("Parent"), new_ind)

                # put source widgets in "kids" array
                ind1 = mupdf.pdf_new_indirect(pdf, xref1, 0)
                ind2 = mupdf.pdf_new_indirect(pdf, xref2, 0)
                kids.pdf_array_push(ind1)
                kids.pdf_array_push(ind2)

                # remove source widgets from "AcroForm/Fields"
                idx = acro_fields.pdf_array_find(ind1)
                acro_fields.pdf_array_delete(idx)
                idx = acro_fields.pdf_array_find(ind2)
                acro_fields.pdf_array_delete(idx)

                acro_fields.pdf_array_push(new_ind)

            w1 = mupdf.pdf_load_object(pdf, xref1)
            w2 = mupdf.pdf_load_object(pdf, xref2)
            kids1 = w1.pdf_dict_get(PDF_NAME("Kids"))
            kids2 = w2.pdf_dict_get(PDF_NAME("Kids"))

            # check which widget has a suitable "Kids" array
            if kids1.pdf_is_array():
                re_target(pdf, acro_fields, xref1, kids1, xref2, kids2)  # pylint: disable=arguments-out-of-order
            elif kids2.pdf_is_array():
                re_target(pdf, acro_fields, xref2, kids2, xref1, kids1)  # pylint: disable=arguments-out-of-order
            else:
                new_target(pdf, acro_fields, xref1, w1, xref2, w2, name)  # pylint: disable=arguments-out-of-order

        def get_kids(parent, kids_list):
            """Return xref list of leaf kids for a parent.

            Call with an empty list.
            """
            kids = mupdf.pdf_dict_get(parent, PDF_NAME("Kids"))
            if not kids.pdf_is_array():
                return kids_list
            for i in range(kids.pdf_array_len()):
                kid = kids.pdf_array_get(i)
                if mupdf.pdf_is_dict(mupdf.pdf_dict_get(kid, PDF_NAME("Kids"))):
                    kids_list = get_kids(kid, kids_list)
                else:
                    kids_list.append(kid.pdf_to_num())
            return kids_list

        def kids_xrefs(widget):
            """Get the xref of top "Parent" and the list of leaf widgets."""
            kids_list = []
            parent = mupdf.pdf_dict_get(widget, PDF_NAME("Parent"))
            parent_xref = parent.pdf_to_num()
            if parent_xref == 0:
                return parent_xref, kids_list
            kids_list = get_kids(parent, kids_list)
            return parent_xref, kids_list

        def deduplicate_names(pdf, acro_fields, join_duplicates=False):
            """Handle any widget name duplicates caused by the merge."""
            names = {}  # key is a widget name, value a list of widgets having it.

            # extract all names and widgets in "AcroForm/Fields"
            for i in range(mupdf.pdf_array_len(acro_fields)):
                wobject = mupdf.pdf_array_get(acro_fields, i)
                xref = wobject.pdf_to_num()

                # extract widget name and collect widget(s) using it
                T = mupdf.pdf_dict_get_text_string(wobject, PDF_NAME("T"))
                xrefs = names.get(T, [])
                xrefs.append(xref)
                names[T] = xrefs

            for name, xrefs in names.items():
                if len(xrefs) < 2:
                    continue
                xref0, xref1 = xrefs[:2]  # only exactly 2 should occur!
                if join_duplicates:  # combine fields with equal names
                    join_widgets(pdf, acro_fields, xref0, xref1, name)
                else:  # make field names unique
                    newname = name + f" [{xref1}]"  # append this to the name
                    wobject = mupdf.pdf_load_object(pdf, xref1)
                    wobject.pdf_dict_put_text_string(PDF_NAME("T"), newname)

            clean_kid_parents(acro_fields)

        def get_acroform(doc):
            """Retrieve the AcroForm dictionary form a PDF."""
            pdf = mupdf.pdf_document_from_fz_document(doc)
            # AcroForm (= central form field info)
            return mupdf.pdf_dict_getp(mupdf.pdf_trailer(pdf), "Root/AcroForm")

        tarpdf = mupdf.pdf_document_from_fz_document(tar)
        srcpdf = mupdf.pdf_document_from_fz_document(src)

        if tar.is_form_pdf:
            # target is a Form PDF, so use it to include source fields
            acro = get_acroform(tar)
            # Important arrays in AcroForm
            acro_fields = acro.pdf_dict_get(PDF_NAME("Fields"))
            tar_co = acro.pdf_dict_get(PDF_NAME("CO"))
            if not tar_co.pdf_is_array():
                tar_co = acro.pdf_dict_put_array(PDF_NAME("CO"), 5)
        else:
            # target is no Form PDF, so copy over source AcroForm
            acro = mupdf.pdf_deep_copy_obj(get_acroform(src))  # make a copy

            # Clear "Fields" and "CO" arrays: will be populated by page fields.
            # This is required to avoid copying unneeded objects.
            acro.pdf_dict_del(PDF_NAME("Fields"))
            acro.pdf_dict_put_array(PDF_NAME("Fields"), 5)
            acro.pdf_dict_del(PDF_NAME("CO"))
            acro.pdf_dict_put_array(PDF_NAME("CO"), 5)

            # Enrich AcroForm for copying to target
            acro_graft = mupdf.pdf_graft_mapped_object(graftmap, acro)

            # Insert AcroForm into target PDF
            acro_tar = mupdf.pdf_add_object(tarpdf, acro_graft)
            acro_fields = acro_tar.pdf_dict_get(PDF_NAME("Fields"))
            tar_co = acro_tar.pdf_dict_get(PDF_NAME("CO"))

            # get its xref and insert it into target catalog
            tar_xref = acro_tar.pdf_to_num()
            acro_tar_ind = mupdf.pdf_new_indirect(tarpdf, tar_xref, 0)
            root = mupdf.pdf_dict_get(mupdf.pdf_trailer(tarpdf), PDF_NAME("Root"))
            root.pdf_dict_put(PDF_NAME("AcroForm"), acro_tar_ind)

        if from_page <= to_page:
            src_range = range(from_page, to_page + 1)
        else:
            src_range = range(from_page, to_page - 1, -1)

        parents = {}  # information about widget parents

        # remove "P" owning page reference from all widgets of all source pages
        for i in src_range:
            src_page = src[i]
            for xref in [
                xref
                for xref, wtype, _ in src_page.annot_xrefs()
                if wtype == mupdf.PDF_ANNOT_WIDGET  # pylint: disable=no-member
            ]:
                w_obj = mupdf.pdf_load_object(srcpdf, xref)
                w_obj.pdf_dict_del(PDF_NAME("P"))

                # get the widget's parent structure
                parent_xref, old_kids = kids_xrefs(w_obj)
                if parent_xref:
                    parents[parent_xref] = {
                        "new_xref": 0,
                        "old_kids": old_kids,
                        "new_kids": [],
                    }
        # Copy over Parent widgets first - they are not page-dependent
        for xref in parents.keys():  # pylint: disable=consider-using-dict-items
            parent = mupdf.pdf_load_object(srcpdf, xref)
            parent_graft = mupdf.pdf_graft_mapped_object(graftmap, parent)
            parent_tar = mupdf.pdf_add_object(tarpdf, parent_graft)
            kids_xrefs_new = get_kids(parent_tar, [])
            parent_xref_new = parent_tar.pdf_to_num()
            parent_ind = mupdf.pdf_new_indirect(tarpdf, parent_xref_new, 0)
            acro_fields.pdf_array_push(parent_ind)
            parents[xref]["new_xref"] = parent_xref_new
            parents[xref]["new_kids"] = kids_xrefs_new

        for i in range(len(src_range)):
            # read first copied over page in target
            tar_page = tar[start_at + i]

            # read the original page in the source PDF
            src_page = src[src_range[i]]

            # now walk through source page widgets and copy over
            w_xrefs = [  # widget xrefs of the source page
                xref
                for xref, wtype, _ in src_page.annot_xrefs()
                if wtype == mupdf.PDF_ANNOT_WIDGET  # pylint: disable=no-member
            ]
            if not w_xrefs:  # no widgets on this source page
                continue

            # convert to formal PDF page
            tar_page_pdf = mupdf.pdf_page_from_fz_page(tar_page)

            # extract annotations array
            tar_annots = mupdf.pdf_dict_get(tar_page_pdf.obj(), PDF_NAME("Annots"))
            if not mupdf.pdf_is_array(tar_annots):
                tar_annots = mupdf.pdf_dict_put_array(
                    tar_page_pdf.obj(), PDF_NAME("Annots"), 5
                )

            for xref in w_xrefs:
                w_obj = mupdf.pdf_load_object(srcpdf, xref)

                # check if field takes part in inter-field validations
                is_aac = mupdf.pdf_is_dict(mupdf.pdf_dict_getp(w_obj, "AA/C"))

                # check if parent of widget already in target
                parent_xref = mupdf.pdf_to_num(
                    w_obj.pdf_dict_get(PDF_NAME("Parent"))
                )
                if parent_xref == 0:  # parent not in target yet
                    try:
                        w_obj_graft = mupdf.pdf_graft_mapped_object(graftmap, w_obj)
                    except Exception as e:
                        message_warning(f"cannot copy widget at {xref=}: {e}")
                        continue
                    w_obj_tar = mupdf.pdf_add_object(tarpdf, w_obj_graft)
                    tar_xref = w_obj_tar.pdf_to_num()
                    w_obj_tar_ind = mupdf.pdf_new_indirect(tarpdf, tar_xref, 0)
                    mupdf.pdf_array_push(tar_annots, w_obj_tar_ind)
                    mupdf.pdf_array_push(acro_fields, w_obj_tar_ind)
                else:
                    parent = parents[parent_xref]
                    idx = parent["old_kids"].index(xref)  # search for xref in parent
                    tar_xref = parent["new_kids"][idx]
                    w_obj_tar_ind = mupdf.pdf_new_indirect(tarpdf, tar_xref, 0)
                    mupdf.pdf_array_push(tar_annots, w_obj_tar_ind)

                # Into "AcroForm/CO" if a computation field.
                if is_aac:
                    mupdf.pdf_array_push(tar_co, w_obj_tar_ind)

        deduplicate_names(tarpdf, acro_fields, join_duplicates=join_duplicates)

    def _embeddedFileGet(self, idx):
        pdf = _as_pdf_document(self)
        names = mupdf.pdf_dict_getl(
                mupdf.pdf_trailer(pdf),
                PDF_NAME('Root'),
                PDF_NAME('Names'),
                PDF_NAME('EmbeddedFiles'),
                PDF_NAME('Names'),
                )
        entry = mupdf.pdf_array_get(names, 2*idx+1)
        filespec = mupdf.pdf_dict_getl(entry, PDF_NAME('EF'), PDF_NAME('F'))
        buf = mupdf.pdf_load_stream(filespec)
        cont = JM_BinFromBuffer(buf)
        return cont

    def _embeddedFileIndex(self, item: typing.Union[int, str]) -> int:
        filenames = self.embfile_names()
        msg = "'%s' not in EmbeddedFiles array." % str(item)
        if item in filenames:
            idx = filenames.index(item)
        elif item in range(len(filenames)):
            idx = item
        else:
            raise ValueError(msg)
        return idx

    def _embfile_add(self, name, buffer_, filename=None, ufilename=None, desc=None):
        pdf = _as_pdf_document(self)
        data = JM_BufferFromBytes(buffer_)
        if not data.m_internal:
            raise TypeError( MSG_BAD_BUFFER)

        names = mupdf.pdf_dict_getl(
                mupdf.pdf_trailer(pdf),
                PDF_NAME('Root'),
                PDF_NAME('Names'),
                PDF_NAME('EmbeddedFiles'),
                PDF_NAME('Names'),
                )
        if not mupdf.pdf_is_array(names):
            root = mupdf.pdf_dict_get(mupdf.pdf_trailer(pdf), PDF_NAME('Root'))
            names = mupdf.pdf_new_array(pdf, 6)    # an even number!
            mupdf.pdf_dict_putl(
                    root,
                    names,
                    PDF_NAME('Names'),
                    PDF_NAME('EmbeddedFiles'),
                    PDF_NAME('Names'),
                    )
        fileentry = JM_embed_file(pdf, data, filename, ufilename, desc, 1)
        xref = mupdf.pdf_to_num(
                mupdf.pdf_dict_getl(fileentry, PDF_NAME('EF'), PDF_NAME('F'))
                )
        mupdf.pdf_array_push(names, mupdf.pdf_new_text_string(name))
        mupdf.pdf_array_push(names, fileentry)
        return xref

    def _embfile_del(self, idx):
        pdf = _as_pdf_document(self)
        names = mupdf.pdf_dict_getl(
                mupdf.pdf_trailer(pdf),
                PDF_NAME('Root'),
                PDF_NAME('Names'),
                PDF_NAME('EmbeddedFiles'),
                PDF_NAME('Names'),
                )
        mupdf.pdf_array_delete(names, idx + 1)
        mupdf.pdf_array_delete(names, idx)

    def _embfile_info(self, idx, infodict):
        pdf = _as_pdf_document(self)
        xref = 0
        ci_xref=0

        trailer = mupdf.pdf_trailer(pdf)

        names = mupdf.pdf_dict_getl(
                trailer,
                PDF_NAME('Root'),
                PDF_NAME('Names'),
                PDF_NAME('EmbeddedFiles'),
                PDF_NAME('Names'),
                )
        o = mupdf.pdf_array_get(names, 2*idx+1)
        ci = mupdf.pdf_dict_get(o, PDF_NAME('CI'))
        if ci.m_internal:
            ci_xref = mupdf.pdf_to_num(ci)
        infodict["collection"] = ci_xref
        name = mupdf.pdf_to_text_string(mupdf.pdf_dict_get(o, PDF_NAME('F')))
        infodict[dictkey_filename] = JM_EscapeStrFromStr(name)

        name = mupdf.pdf_to_text_string(mupdf.pdf_dict_get(o, PDF_NAME('UF')))
        infodict[dictkey_ufilename] = JM_EscapeStrFromStr(name)

        name = mupdf.pdf_to_text_string(mupdf.pdf_dict_get(o, PDF_NAME('Desc')))
        infodict[dictkey_descr] = JM_UnicodeFromStr(name)

        len_ = -1
        DL = -1
        fileentry = mupdf.pdf_dict_getl(o, PDF_NAME('EF'), PDF_NAME('F'))
        xref = mupdf.pdf_to_num(fileentry)
        o = mupdf.pdf_dict_get(fileentry, PDF_NAME('Length'))
        if o.m_internal:
            len_ = mupdf.pdf_to_int(o)

        o = mupdf.pdf_dict_get(fileentry, PDF_NAME('DL'))
        if o.m_internal:
            DL = mupdf.pdf_to_int(o)
        else:
            o = mupdf.pdf_dict_getl(fileentry, PDF_NAME('Params'), PDF_NAME('Size'))
            if o.m_internal:
                DL = mupdf.pdf_to_int(o)
        infodict[dictkey_size] = DL
        infodict[dictkey_length] = len_
        return xref

    def _embfile_names(self, namelist):
        """Get list of embedded file names."""
        pdf = _as_pdf_document(self)
        names = mupdf.pdf_dict_getl(
                mupdf.pdf_trailer(pdf),
                PDF_NAME('Root'),
                PDF_NAME('Names'),
                PDF_NAME('EmbeddedFiles'),
                PDF_NAME('Names'),
                )
        if mupdf.pdf_is_array(names):
            n = mupdf.pdf_array_len(names)
            for i in range(0, n, 2):
                val = JM_EscapeStrFromStr(
                        mupdf.pdf_to_text_string(
                            mupdf.pdf_array_get(names, i)
                            )
                        )
                namelist.append(val)

    def _embfile_upd(self, idx, buffer_=None, filename=None, ufilename=None, desc=None):
        pdf = _as_pdf_document(self)
        xref = 0
        names = mupdf.pdf_dict_getl(
                mupdf.pdf_trailer(pdf),
                PDF_NAME('Root'),
                PDF_NAME('Names'),
                PDF_NAME('EmbeddedFiles'),
                PDF_NAME('Names'),
                )
        entry = mupdf.pdf_array_get(names, 2*idx+1)

        filespec = mupdf.pdf_dict_getl(entry, PDF_NAME('EF'), PDF_NAME('F'))
        if not filespec.m_internal:
            RAISEPY( "bad PDF: no /EF object", JM_Exc_FileDataError)
        res = JM_BufferFromBytes(buffer_)
        if buffer_ and buffer_.m_internal and not res.m_internal:
            raise TypeError( MSG_BAD_BUFFER)
        if res.m_internal and buffer_ and buffer_.m_internal:
            JM_update_stream(pdf, filespec, res, 1)
            # adjust /DL and /Size parameters
            len, _ = mupdf.fz_buffer_storage(res)
            l = mupdf.pdf_new_int(len)
            mupdf.pdf_dict_put(filespec, PDF_NAME('DL'), l)
            mupdf.pdf_dict_putl(filespec, l, PDF_NAME('Params'), PDF_NAME('Size'))
        xref = mupdf.pdf_to_num(filespec)
        if filename:
            mupdf.pdf_dict_put_text_string(entry, PDF_NAME('F'), filename)

        if ufilename:
            mupdf.pdf_dict_put_text_string(entry, PDF_NAME('UF'), ufilename)

        if desc:
            mupdf.pdf_dict_put_text_string(entry, PDF_NAME('Desc'), desc)
        return xref

    def _extend_toc_items(self, items):
        """Add color info to all items of an extended TOC list."""
        if self.is_closed:
            raise ValueError("document closed")
        if g_use_extra:
            return extra.Document_extend_toc_items( self.this, items)
        pdf = _as_pdf_document(self)
        zoom = "zoom"
        bold = "bold"
        italic = "italic"
        collapse = "collapse"

        root = mupdf.pdf_dict_get(mupdf.pdf_trailer(pdf), PDF_NAME('Root'))
        if not root.m_internal:
            return
        olroot = mupdf.pdf_dict_get(root, PDF_NAME('Outlines'))
        if not olroot.m_internal:
            return
        first = mupdf.pdf_dict_get(olroot, PDF_NAME('First'))
        if not first.m_internal:
            return
        xrefs = []
        xrefs = JM_outline_xrefs(first, xrefs)
        n = len(xrefs)
        m = len(items)
        if not n:
            return
        if n != m:
            raise IndexError( "internal error finding outline xrefs")

        # update all TOC item dictionaries
        for i in range(n):
            xref = int(xrefs[i])
            item = items[i]
            itemdict = item[3]
            if not isinstance(itemdict, dict):
                raise ValueError( "need non-simple TOC format")
            itemdict[dictkey_xref] = xrefs[i]
            bm = mupdf.pdf_load_object(pdf, xref)
            flags = mupdf.pdf_to_int( mupdf.pdf_dict_get(bm, PDF_NAME('F')))
            if flags == 1:
                itemdict[italic] = True
            elif flags == 2:
                itemdict[bold] = True
            elif flags == 3:
                itemdict[italic] = True
                itemdict[bold] = True
            count = mupdf.pdf_to_int( mupdf.pdf_dict_get(bm, PDF_NAME('Count')))
            if count < 0:
                itemdict[collapse] = True
            elif count > 0:
                itemdict[collapse] = False
            col = mupdf.pdf_dict_get(bm, PDF_NAME('C'))
            if mupdf.pdf_is_array(col) and mupdf.pdf_array_len(col) == 3:
                color = (
                        mupdf.pdf_to_real(mupdf.pdf_array_get(col, 0)),
                        mupdf.pdf_to_real(mupdf.pdf_array_get(col, 1)),
                        mupdf.pdf_to_real(mupdf.pdf_array_get(col, 2)),
                        )
                itemdict[dictkey_color] = color
            z=0
            obj = mupdf.pdf_dict_get(bm, PDF_NAME('Dest'))
            if not obj.m_internal or not mupdf.pdf_is_array(obj):
                obj = mupdf.pdf_dict_getl(bm, PDF_NAME('A'), PDF_NAME('D'))
            if mupdf.pdf_is_array(obj) and mupdf.pdf_array_len(obj) == 5:
                z = mupdf.pdf_to_real(mupdf.pdf_array_get(obj, 4))
            itemdict[zoom] = float(z)
            item[3] = itemdict
            items[i] = item

    def _forget_page(self, page: Page):
        """Remove a page from document page dict."""
        pid = id(page)
        if pid in self._page_refs:
            #self._page_refs[pid] = None
            del self._page_refs[pid]

    def _get_char_widths(self, xref: int, bfname: str, ext: str, ordering: int, limit: int, idx: int = 0):
        pdf = _as_pdf_document(self)
        mylimit = limit
        if mylimit < 256:
            mylimit = 256
        if ordering >= 0:
            data, size, index = mupdf.fz_lookup_cjk_font(ordering)
            font = mupdf.fz_new_font_from_memory(None, data, size, index, 0)
        else:
            data, size = mupdf.fz_lookup_base14_font(bfname)
            if data:
                font = mupdf.fz_new_font_from_memory(bfname, data, size, 0, 0)
            else:
                buf = JM_get_fontbuffer(pdf, xref)
                if not buf.m_internal:
                    raise Exception("font at xref %d is not supported" % xref)

                font = mupdf.fz_new_font_from_buffer(None, buf, idx, 0)
        wlist = []
        for i in range(mylimit):
            glyph = mupdf.fz_encode_character(font, i)
            adv = mupdf.fz_advance_glyph(font, glyph, 0)
            if ordering >= 0:
                glyph = i
            if glyph > 0:
                wlist.append( (glyph, adv))
            else:
                wlist.append( (glyph, 0.0))
        return wlist

    def _get_page_labels(self):
        pdf = _as_pdf_document(self)
        rc = []
        pagelabels = mupdf.pdf_new_name("PageLabels")
        obj = mupdf.pdf_dict_getl( mupdf.pdf_trailer(pdf), PDF_NAME('Root'), pagelabels)
        if not obj.m_internal:
            return rc
        # simple case: direct /Nums object
        nums = mupdf.pdf_resolve_indirect( mupdf.pdf_dict_get( obj, PDF_NAME('Nums')))
        if nums.m_internal:
            JM_get_page_labels(rc, nums)
            return rc
        # case: /Kids/Nums
        nums = mupdf.pdf_resolve_indirect( mupdf.pdf_dict_getl(obj, PDF_NAME('Kids'), PDF_NAME('Nums')))
        if nums.m_internal:
            JM_get_page_labels(rc, nums)
            return rc
        # case: /Kids is an array of multiple /Nums
        kids = mupdf.pdf_resolve_indirect( mupdf.pdf_dict_get( obj, PDF_NAME('Kids')))
        if not kids.m_internal or not mupdf.pdf_is_array(kids):
            return rc
        n = mupdf.pdf_array_len(kids)
        for i in range(n):
            nums = mupdf.pdf_resolve_indirect(
                    mupdf.pdf_dict_get(
                        mupdf.pdf_array_get(kids, i),
                        PDF_NAME('Nums'),
                        )
                    )
            JM_get_page_labels(rc, nums)
        return rc

    def _getMetadata(self, key):
        """Get metadata."""
        try:
            return mupdf.fz_lookup_metadata2( self.this, key)
        except Exception:
            if g_exceptions_verbose > 2:    exception_info()
            return ''

    def _getOLRootNumber(self):
        """Get xref of Outline Root, create it if missing."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        # get main root
        root = mupdf.pdf_dict_get( mupdf.pdf_trailer( pdf), PDF_NAME('Root'))
        # get outline root
        olroot = mupdf.pdf_dict_get( root, PDF_NAME('Outlines'))
        if not olroot.m_internal:
            olroot = mupdf.pdf_new_dict( pdf, 4)
            mupdf.pdf_dict_put( olroot, PDF_NAME('Type'), PDF_NAME('Outlines'))
            ind_obj = mupdf.pdf_add_object( pdf, olroot)
            mupdf.pdf_dict_put( root, PDF_NAME('Outlines'), ind_obj)
            olroot = mupdf.pdf_dict_get( root, PDF_NAME('Outlines'))
        return mupdf.pdf_to_num( olroot)

    def _getPDFfileid(self):
        """Get PDF file id."""
        pdf = _as_pdf_document(self, required=0)
        if not pdf.m_internal:
            return
        idlist = []
        identity = mupdf.pdf_dict_get(mupdf.pdf_trailer(pdf), PDF_NAME('ID'))
        if identity.m_internal:
            n = mupdf.pdf_array_len(identity)
            for i in range(n):
                o = mupdf.pdf_array_get(identity, i)
                text = mupdf.pdf_to_text_string(o)
                hex_ = binascii.hexlify(text)
                idlist.append(hex_)
        return idlist

    def _getPageInfo(self, pno, what):
        """List fonts, images, XObjects used on a page."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        doc = self.this
        pageCount = mupdf.pdf_count_pages(doc) if isinstance(doc, mupdf.PdfDocument) else mupdf.fz_count_pages(doc)
        n = pno  # pno < 0 is allowed
        while n < 0:
            n += pageCount  # make it non-negative
        if n >= pageCount:
            raise ValueError( MSG_BAD_PAGENO)
        pdf = _as_pdf_document(self)
        pageref = mupdf.pdf_lookup_page_obj(pdf, n)
        rsrc = mupdf.pdf_dict_get_inheritable(pageref, mupdf.PDF_ENUM_NAME_Resources)
        liste = []
        tracer = []
        if rsrc.m_internal:
            JM_scan_resources(pdf, rsrc, liste, what, 0, tracer)
        return liste

    def _insert_font(self, fontfile=None, fontbuffer=None):
        '''
        Utility: insert font from file or binary.
        '''
        pdf = _as_pdf_document(self)
        if not fontfile and not fontbuffer:
            raise ValueError( MSG_FILE_OR_BUFFER)
        value = JM_insert_font(pdf, None, fontfile, fontbuffer, 0, 0, 0, 0, 0, -1)
        return value

    def _loadOutline(self):
        """Load first outline."""
        doc = self.this
        assert isinstance( doc, mupdf.FzDocument)
        try:
            ol = mupdf.fz_load_outline( doc)
        except Exception:
            if g_exceptions_verbose > 1:    exception_info()
            return
        return Outline( ol)

    def _make_page_map(self):
        """Make an array page number -> page object."""
        if self.is_closed:
            raise ValueError("document closed")
        assert 0, f'_make_page_map() is no-op'

    def _move_copy_page(self, pno, nb, before, copy):
        """Move or copy a PDF page reference."""
        pdf = _as_pdf_document(self)
        same = 0
        # get the two page objects -----------------------------------
        # locate the /Kids arrays and indices in each

        page1, parent1, i1 = pdf_lookup_page_loc( pdf, pno)

        kids1 = mupdf.pdf_dict_get( parent1, PDF_NAME('Kids'))

        page2, parent2, i2 = pdf_lookup_page_loc( pdf, nb)
        kids2 = mupdf.pdf_dict_get( parent2, PDF_NAME('Kids'))
        if before:  # calc index of source page in target /Kids
            pos = i2
        else:
            pos = i2 + 1

        # same /Kids array? ------------------------------------------
        same = mupdf.pdf_objcmp( kids1, kids2)

        # put source page in target /Kids array ----------------------
        if not copy and same != 0:  # update parent in page object
            mupdf.pdf_dict_put( page1, PDF_NAME('Parent'), parent2)
        mupdf.pdf_array_insert( kids2, page1, pos)

        if same != 0:   # different /Kids arrays ----------------------
            parent = parent2
            while parent.m_internal:    # increase /Count objects in parents
                count = mupdf.pdf_dict_get_int( parent, PDF_NAME('Count'))
                mupdf.pdf_dict_put_int( parent, PDF_NAME('Count'), count + 1)
                parent = mupdf.pdf_dict_get( parent, PDF_NAME('Parent'))
            if not copy:    # delete original item
                mupdf.pdf_array_delete( kids1, i1)
                parent = parent1
                while parent.m_internal:    # decrease /Count objects in parents
                    count = mupdf.pdf_dict_get_int( parent, PDF_NAME('Count'))
                    mupdf.pdf_dict_put_int( parent, PDF_NAME('Count'), count - 1)
                    parent = mupdf.pdf_dict_get( parent, PDF_NAME('Parent'))
        else:   # same /Kids array
            if copy:    # source page is copied
                parent = parent2
                while parent.m_internal:    # increase /Count object in parents
                    count = mupdf.pdf_dict_get_int( parent, PDF_NAME('Count'))
                    mupdf.pdf_dict_put_int( parent, PDF_NAME('Count'), count + 1)
                    parent = mupdf.pdf_dict_get( parent, PDF_NAME('Parent'))
            else:
                if i1 < pos:
                    mupdf.pdf_array_delete( kids1, i1)
                else:
                    mupdf.pdf_array_delete( kids1, i1 + 1)
        if pdf.m_internal.rev_page_map: # page map no longer valid: drop it
            mupdf.ll_pdf_drop_page_tree( pdf.m_internal)

        self._reset_page_refs()

    def _newPage(self, pno=-1, width=595, height=842):
        """Make a new PDF page."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if g_use_extra:
            extra._newPage( self.this, pno, width, height)
        else:
            pdf = _as_pdf_document(self)
            mediabox = mupdf.FzRect(mupdf.FzRect.Fixed_UNIT)
            mediabox.x1 = width
            mediabox.y1 = height
            contents = mupdf.FzBuffer()
            if pno < -1:
                raise ValueError( MSG_BAD_PAGENO)
            # create /Resources and /Contents objects
            #resources = pdf.add_object(pdf.new_dict(1))
            resources = mupdf.pdf_add_new_dict(pdf, 1)
            page_obj = mupdf.pdf_add_page( pdf, mediabox, 0, resources, contents)
            mupdf.pdf_insert_page( pdf, pno, page_obj)
        # fixme: pdf->dirty = 1;

        self._reset_page_refs()
        return self[pno]

    def _remove_links_to(self, numbers):
        pdf = _as_pdf_document(self)
        _remove_dest_range(pdf, numbers)

    def _remove_toc_item(self, xref):
        # "remove" bookmark by letting it point to nowhere
        pdf = _as_pdf_document(self)
        item = mupdf.pdf_new_indirect(pdf, xref, 0)
        mupdf.pdf_dict_del( item, PDF_NAME('Dest'))
        mupdf.pdf_dict_del( item, PDF_NAME('A'))
        color = mupdf.pdf_new_array( pdf, 3)
        for i in range(3):
            mupdf.pdf_array_push_real( color, 0.8)
        mupdf.pdf_dict_put( item, PDF_NAME('C'), color)

    def _reset_page_refs(self):
        """Invalidate all pages in document dictionary."""
        if getattr(self, "is_closed", True):
            return
        pages = [p for p in self._page_refs.values()]
        for page in pages:
            if page:
                page._erase()
                page = None
        self._page_refs.clear()

    def _set_page_labels(self, labels):
        pdf = _as_pdf_document(self)
        pagelabels = mupdf.pdf_new_name("PageLabels")
        root = mupdf.pdf_dict_get(mupdf.pdf_trailer(pdf), PDF_NAME('Root'))
        mupdf.pdf_dict_del(root, pagelabels)
        mupdf.pdf_dict_putl(root, mupdf.pdf_new_array(pdf, 0), pagelabels, PDF_NAME('Nums'))

        xref = self.pdf_catalog()
        text = self.xref_object(xref, compressed=True)
        text = text.replace("/Nums[]", "/Nums[%s]" % labels)
        self.update_object(xref, text)

    def _update_toc_item(self, xref, action=None, title=None, flags=0, collapse=None, color=None):
        '''
        "update" bookmark by letting it point to nowhere
        '''
        pdf = _as_pdf_document(self)
        item = mupdf.pdf_new_indirect( pdf, xref, 0)
        if title:
            mupdf.pdf_dict_put_text_string( item, PDF_NAME('Title'), title)
        if action:
            mupdf.pdf_dict_del( item, PDF_NAME('Dest'))
            obj = JM_pdf_obj_from_str( pdf, action)
            mupdf.pdf_dict_put( item, PDF_NAME('A'), obj)
        mupdf.pdf_dict_put_int( item, PDF_NAME('F'), flags)
        if color:
            c = mupdf.pdf_new_array( pdf, 3)
            for i in range(3):
                f = color[i]
                mupdf.pdf_array_push_real( c, f)
            mupdf.pdf_dict_put( item, PDF_NAME('C'), c)
        elif color is not None:
            mupdf.pdf_dict_del( item, PDF_NAME('C'))
        if collapse is not None:
            if mupdf.pdf_dict_get( item, PDF_NAME('Count')).m_internal:
                i = mupdf.pdf_dict_get_int( item, PDF_NAME('Count'))
                if (i < 0 and collapse is False) or (i > 0 and collapse is True):
                    i = i * (-1)
                    mupdf.pdf_dict_put_int( item, PDF_NAME('Count'), i)

    @property
    def FormFonts(self):
        """Get list of field font resource names."""
        pdf = _as_pdf_document(self, required=0)
        if not pdf.m_internal:
            return
        fonts = mupdf.pdf_dict_getl(
                mupdf.pdf_trailer(pdf),
                PDF_NAME('Root'),
                PDF_NAME('AcroForm'),
                PDF_NAME('DR'),
                PDF_NAME('Font'),
                )
        liste = list()
        if fonts.m_internal and mupdf.pdf_is_dict(fonts):   # fonts exist
            n = mupdf.pdf_dict_len(fonts)
            for i in range(n):
                f = mupdf.pdf_dict_get_key(fonts, i)
                liste.append(JM_UnicodeFromStr(mupdf.pdf_to_name(f)))
        return liste

    def add_layer(self, name, creator=None, on=None):
        """Add a new OC layer."""
        pdf = _as_pdf_document(self)
        JM_add_layer_config( pdf, name, creator, on)
        mupdf.ll_pdf_read_ocg( pdf.m_internal)

    def add_ocg(self, name, config=-1, on=1, intent=None, usage=None):
        """Add new optional content group."""
        xref = 0
        pdf = _as_pdf_document(self)

        # make the OCG
        ocg = mupdf.pdf_add_new_dict(pdf, 3)
        mupdf.pdf_dict_put(ocg, PDF_NAME('Type'), PDF_NAME('OCG'))
        mupdf.pdf_dict_put_text_string(ocg, PDF_NAME('Name'), name)
        intents = mupdf.pdf_dict_put_array(ocg, PDF_NAME('Intent'), 2)
        if not intent:
            mupdf.pdf_array_push(intents, PDF_NAME('View'))
        elif not isinstance(intent, str):
            assert 0, f'fixme: intent is not a str. {type(intent)=} {type=}'
            #n = len(intent)
            #for i in range(n):
            #    item = intent[i]
            #    c = JM_StrAsChar(item);
            #    if (c) {
            #        pdf_array_push(gctx, intents, pdf_new_name(gctx, c));
            #    }
            #    Py_DECREF(item);
            #}
        else:
            mupdf.pdf_array_push(intents, mupdf.pdf_new_name(intent))
        use_for = mupdf.pdf_dict_put_dict(ocg, PDF_NAME('Usage'), 3)
        ci_name = mupdf.pdf_new_name("CreatorInfo")
        cre_info = mupdf.pdf_dict_put_dict(use_for, ci_name, 2)
        mupdf.pdf_dict_put_text_string(cre_info, PDF_NAME('Creator'), "PyMuPDF")
        if usage:
            mupdf.pdf_dict_put_name(cre_info, PDF_NAME('Subtype'), usage)
        else:
            mupdf.pdf_dict_put_name(cre_info, PDF_NAME('Subtype'), "Artwork")
        indocg = mupdf.pdf_add_object(pdf, ocg)

        # Insert OCG in the right config
        ocp = JM_ensure_ocproperties(pdf)
        obj = mupdf.pdf_dict_get(ocp, PDF_NAME('OCGs'))
        mupdf.pdf_array_push(obj, indocg)

        if config > -1:
            obj = mupdf.pdf_dict_get(ocp, PDF_NAME('Configs'))
            if not mupdf.pdf_is_array(obj):
                raise ValueError( MSG_BAD_OC_CONFIG)
            cfg = mupdf.pdf_array_get(obj, config)
            if not cfg.m_internal:
                raise ValueError( MSG_BAD_OC_CONFIG)
        else:
            cfg = mupdf.pdf_dict_get(ocp, PDF_NAME('D'))

        obj = mupdf.pdf_dict_get(cfg, PDF_NAME('Order'))
        if not obj.m_internal:
            obj = mupdf.pdf_dict_put_array(cfg, PDF_NAME('Order'), 1)
        mupdf.pdf_array_push(obj, indocg)
        if on:
            obj = mupdf.pdf_dict_get(cfg, PDF_NAME('ON'))
            if not obj.m_internal:
                obj = mupdf.pdf_dict_put_array(cfg, PDF_NAME('ON'), 1)
        else:
            obj =mupdf.pdf_dict_get(cfg, PDF_NAME('OFF'))
            if not obj.m_internal:
                obj =mupdf.pdf_dict_put_array(cfg, PDF_NAME('OFF'), 1)
        mupdf.pdf_array_push(obj, indocg)

        # let MuPDF take note: re-read OCProperties
        mupdf.ll_pdf_read_ocg(pdf.m_internal)

        xref = mupdf.pdf_to_num(indocg)
        return xref

    def authenticate(self, password):
        """Decrypt document."""
        if self.is_closed:
            raise ValueError("document closed")
        val = mupdf.fz_authenticate_password(self.this, password)
        if val:  # the doc is decrypted successfully and we init the outline
            self.is_encrypted = False
            self.is_encrypted = False
            self.init_doc()
            self.thisown = True
        return val

    def can_save_incrementally(self):
        """Check whether incremental saves are possible."""
        pdf = _as_pdf_document(self, required=0)
        if not pdf.m_internal:
            return False
        return mupdf.pdf_can_be_saved_incrementally(pdf)

    def bake(self, *, annots: bool = True, widgets: bool = True) -> None:
        """Convert annotations or fields to permanent content.

        Notes:
            Converts annotations or widgets to permanent page content, like
            text and vector graphics, as appropriate.
            After execution, pages will still look the same, but no longer
            have annotations, respectively no fields.
            If widgets are selected the PDF will no longer be a Form PDF.

        Args:
            annots: convert annotations
            widgets: convert form fields

        """
        pdf = _as_pdf_document(self)
        mupdf.pdf_bake_document(pdf, int(annots), int(widgets))

    @property
    def chapter_count(self):
        """Number of chapters."""
        if self.is_closed:
            raise ValueError("document closed")
        return mupdf.fz_count_chapters( self.this)

    def chapter_page_count(self, chapter):
        """Page count of chapter."""
        if self.is_closed:
            raise ValueError("document closed")
        chapters = mupdf.fz_count_chapters( self.this)
        if chapter < 0 or chapter >= chapters:
            raise ValueError( "bad chapter number")
        pages = mupdf.fz_count_chapter_pages( self.this, chapter)
        return pages

    def close(self):
        """Close document."""
        if getattr(self, "is_closed", True):
            raise ValueError("document closed")
        # self._cleanup()
        if hasattr(self, "_outline") and self._outline:
            self._outline = None
        self._reset_page_refs()
        #self.metadata    = None
        #self.stream      = None
        self.is_closed    = True
        #self.FontInfos   = []
        self.Graftmaps = {} # Fixes test_3140().
        #self.ShownPages = {}
        #self.InsertedImages  = {}
        #self.this = None
        self.this = None

    def convert_to_pdf(self, from_page=0, to_page=-1, rotate=0):
        """Convert document to a PDF, selecting page range and optional rotation. Output bytes object."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        fz_doc = self.this
        fp = from_page
        tp = to_page
        srcCount = mupdf.fz_count_pages(fz_doc)
        if fp < 0:
            fp = 0
        if fp > srcCount - 1:
            fp = srcCount - 1
        if tp < 0:
            tp = srcCount - 1
        if tp > srcCount - 1:
            tp = srcCount - 1
        len0 = len(JM_mupdf_warnings_store)
        doc = JM_convert_to_pdf(fz_doc, fp, tp, rotate)
        len1 = len(JM_mupdf_warnings_store)
        for i in range(len0, len1):
            message(f'{JM_mupdf_warnings_store[i]}')
        return doc

    def copy_page(self, pno: int, to: int =-1):
        """Copy a page within a PDF document.

        This will only create another reference of the same page object.
        Args:
            pno: source page number
            to: put before this page, '-1' means after last page.
        """
        if self.is_closed:
            raise ValueError("document closed")

        page_count = len(self)
        if (
                pno not in range(page_count)
                or to not in range(-1, page_count)
                ):
            raise ValueError("bad page number(s)")
        before = 1
        copy = 1
        if to == -1:
            to = page_count - 1
            before = 0

        return self._move_copy_page(pno, to, before, copy)

    def del_xml_metadata(self):
        """Delete XML metadata."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        root = mupdf.pdf_dict_get( mupdf.pdf_trailer( pdf), PDF_NAME('Root'))
        if root.m_internal:
            mupdf.pdf_dict_del( root, PDF_NAME('Metadata'))

    def delete_page(self, pno: int =-1):
        """ Delete one page from a PDF.
        """
        return self.delete_pages(pno)

    def delete_pages(self, *args, **kw):
        """Delete pages from a PDF.

        Args:
            Either keywords 'from_page'/'to_page', or two integers to
            specify the first/last page to delete.
            Or a list/tuple/range object, which can contain arbitrary
            page numbers.
            Or a single integer page number.
        """
        if not self.is_pdf:
            raise ValueError("is no PDF")
        if self.is_closed:
            raise ValueError("document closed")

        page_count = self.page_count  # page count of document
        f = t = -1
        if kw:  # check if keywords were used
            if args:  # then no positional args are allowed
                raise ValueError("cannot mix keyword and positional argument")
            f = kw.get("from_page", -1)  # first page to delete
            t = kw.get("to_page", -1)  # last page to delete
            while f < 0:
                f += page_count
            while t < 0:
                t += page_count
            if not f <= t < page_count:
                raise ValueError("bad page number(s)")
            numbers = tuple(range(f, t + 1))
        else:
            if len(args) > 2 or args == []:
                raise ValueError("need 1 or 2 positional arguments")
            if len(args) == 2:
                f, t = args
                if not (type(f) is int and type(t) is int):
                    raise ValueError("both arguments must be int")
                if f > t:
                    f, t = t, f
                if not f <= t < page_count:
                    raise ValueError("bad page number(s)")
                numbers = tuple(range(f, t + 1))
            elif isinstance(args[0], int):
                pno = args[0]
                while pno < 0:
                    pno += page_count
                numbers = (pno,)
            else:
                numbers = tuple(args[0])

        numbers = list(map(int, set(numbers)))  # ensure unique integers
        if numbers == []:
            message("nothing to delete")
            return
        numbers.sort()
        if numbers[0] < 0 or numbers[-1] >= page_count:
            raise ValueError("bad page number(s)")
        frozen_numbers = frozenset(numbers)
        toc = self.get_toc()
        for i, xref in enumerate(self.get_outline_xrefs()):
            if toc[i][2] - 1 in frozen_numbers:
                self._remove_toc_item(xref)  # remove target in PDF object

        self._remove_links_to(frozen_numbers)

        for i in reversed(numbers):  # delete pages, last to first
            self._delete_page(i)

        self._reset_page_refs()

    def embfile_add(self,
            name: str,
            buffer_: ByteString,
            filename: OptStr =None,
            ufilename: OptStr =None,
            desc: OptStr =None,
            ) -> None:
        """Add an item to the EmbeddedFiles array.

        Args:
            name: name of the new item, must not already exist.
            buffer_: (binary data) the file content.
            filename: (str) the file name, default: the name
            ufilename: (unicode) the file name, default: filename
            desc: (str) the description.
        """
        filenames = self.embfile_names()
        msg = "Name '%s' already exists." % str(name)
        if name in filenames:
            raise ValueError(msg)

        if filename is None:
            filename = name
        if ufilename is None:
            ufilename = filename
        if desc is None:
            desc = name
        xref = self._embfile_add(
                name,
                buffer_=buffer_,
                filename=filename,
                ufilename=ufilename,
                desc=desc,
                )
        date = get_pdf_now()
        self.xref_set_key(xref, "Type", "/EmbeddedFile")
        self.xref_set_key(xref, "Params/CreationDate", get_pdf_str(date))
        self.xref_set_key(xref, "Params/ModDate", get_pdf_str(date))
        return xref

    def embfile_count(self) -> int:
        """Get number of EmbeddedFiles."""
        return len(self.embfile_names())

    def embfile_del(self, item: typing.Union[int, str]):
        """Delete an entry from EmbeddedFiles.

        Notes:
            The argument must be name or index of an EmbeddedFiles item.
            Physical deletion of data will happen on save to a new
            file with appropriate garbage option.
        Args:
            item: name or number of item.
        Returns:
            None
        """
        idx = self._embeddedFileIndex(item)
        return self._embfile_del(idx)

    def embfile_get(self, item: typing.Union[int, str]) -> bytes:
        """Get the content of an item in the EmbeddedFiles array.

        Args:
            item: number or name of item.
        Returns:
            (bytes) The file content.
        """
        idx = self._embeddedFileIndex(item)
        return self._embeddedFileGet(idx)

    def embfile_info(self, item: typing.Union[int, str]) -> dict:
        """Get information of an item in the EmbeddedFiles array.

        Args:
            item: number or name of item.
        Returns:
            Information dictionary.
        """
        idx = self._embeddedFileIndex(item)
        infodict = {"name": self.embfile_names()[idx]}
        xref = self._embfile_info(idx, infodict)
        t, date = self.xref_get_key(xref, "Params/CreationDate")
        if t != "null":
            infodict["creationDate"] = date
        t, date = self.xref_get_key(xref, "Params/ModDate")
        if t != "null":
            infodict["modDate"] = date
        t, md5 = self.xref_get_key(xref, "Params/CheckSum")
        if t != "null":
            infodict["checksum"] = binascii.hexlify(md5.encode()).decode()
        return infodict

    def embfile_names(self) -> list:
        """Get list of names of EmbeddedFiles."""
        filenames = []
        self._embfile_names(filenames)
        return filenames

    def embfile_upd(self,
            item: typing.Union[int, str],
            buffer_: OptBytes =None,
            filename: OptStr =None,
            ufilename: OptStr =None,
            desc: OptStr =None,
            ) -> None:
        """Change an item of the EmbeddedFiles array.

        Notes:
            Only provided parameters are changed. If all are omitted,
            the method is a no-op.
        Args:
            item: number or name of item.
            buffer_: (binary data) the new file content.
            filename: (str) the new file name.
            ufilename: (unicode) the new filen ame.
            desc: (str) the new description.
        """
        idx = self._embeddedFileIndex(item)
        xref = self._embfile_upd(
                idx,
                buffer_=buffer_,
                filename=filename,
                ufilename=ufilename,
                desc=desc,
                )
        date = get_pdf_now()
        self.xref_set_key(xref, "Params/ModDate", get_pdf_str(date))
        return xref

    def extract_font(self, xref=0, info_only=0, named=None):
        '''
        Get a font by xref. Returns a tuple or dictionary.
        '''
        #log( '{=xref info_only}')
        pdf = _as_pdf_document(self)
        obj = mupdf.pdf_load_object(pdf, xref)
        type_ = mupdf.pdf_dict_get(obj, PDF_NAME('Type'))
        subtype = mupdf.pdf_dict_get(obj, PDF_NAME('Subtype'))
        if (mupdf.pdf_name_eq(type_, PDF_NAME('Font'))
                and not mupdf.pdf_to_name( subtype).startswith('CIDFontType')
                ):
            basefont = mupdf.pdf_dict_get(obj, PDF_NAME('BaseFont'))
            if not basefont.m_internal or mupdf.pdf_is_null(basefont):
                bname = mupdf.pdf_dict_get(obj, PDF_NAME('Name'))
            else:
                bname = basefont
            ext = JM_get_fontextension(pdf, xref)
            if ext != 'n/a' and not info_only:
                buffer_ = JM_get_fontbuffer(pdf, xref)
                bytes_ = JM_BinFromBuffer(buffer_)
            else:
                bytes_ = b''
            if not named:
                rc = (
                        JM_EscapeStrFromStr(mupdf.pdf_to_name(bname)),
                        JM_UnicodeFromStr(ext),
                        JM_UnicodeFromStr(mupdf.pdf_to_name(subtype)),
                        bytes_,
                        )
            else:
                rc = {
                        dictkey_name: JM_EscapeStrFromStr(mupdf.pdf_to_name(bname)),
                        dictkey_ext: JM_UnicodeFromStr(ext),
                        dictkey_type: JM_UnicodeFromStr(mupdf.pdf_to_name(subtype)),
                        dictkey_content: bytes_,
                        }
        else:
            if not named:
                rc = '', '', '', b''
            else:
                rc = {
                        dictkey_name: '',
                        dictkey_ext: '',
                        dictkey_type: '',
                        dictkey_content: b'',
                        }
        return rc

    def extract_image(self, xref):
        """Get image by xref. Returns a dictionary."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")

        pdf = _as_pdf_document(self)

        if not _INRANGE(xref, 1, mupdf.pdf_xref_len(pdf)-1):
            raise ValueError( MSG_BAD_XREF)

        obj = mupdf.pdf_new_indirect(pdf, xref, 0)
        subtype = mupdf.pdf_dict_get(obj, PDF_NAME('Subtype'))

        if not mupdf.pdf_name_eq(subtype, PDF_NAME('Image')):
            raise ValueError( "not an image")

        o = mupdf.pdf_dict_geta(obj, PDF_NAME('SMask'), PDF_NAME('Mask'))
        if o.m_internal:
            smask = mupdf.pdf_to_num(o)
        else:
            smask = 0

        # load the image
        img = mupdf.pdf_load_image(pdf, obj)
        rc = dict()
        _make_image_dict(img, rc)
        rc[dictkey_smask] = smask
        rc[dictkey_cs_name] = mupdf.fz_colorspace_name(img.colorspace())
        return rc

    def ez_save(
            self,
            filename,
            garbage=3,
            clean=False,
            deflate=True,
            deflate_images=True,
            deflate_fonts=True,
            incremental=False,
            ascii=False,
            expand=False,
            linear=False,
            pretty=False,
            encryption=1,
            permissions=4095,
            owner_pw=None,
            user_pw=None,
            no_new_id=True,
            preserve_metadata=1,
            use_objstms=1,
            compression_effort=0,
            raise_on_repair=False,
            ):
        '''
        Save PDF using some different defaults
        '''
        return self.save(
                filename,
                garbage=garbage,
                clean=clean,
                deflate=deflate,
                deflate_images=deflate_images,
                deflate_fonts=deflate_fonts,
                incremental=incremental,
                ascii=ascii,
                expand=expand,
                linear=linear,
                pretty=pretty,
                encryption=encryption,
                permissions=permissions,
                owner_pw=owner_pw,
                user_pw=user_pw,
                no_new_id=no_new_id,
                preserve_metadata=preserve_metadata,
                use_objstms=use_objstms,
                compression_effort=compression_effort,
                raise_on_repair=raise_on_repair,
                )

    def find_bookmark(self, bm):
        """Find new location after layouting a document."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        location = mupdf.fz_lookup_bookmark2( self.this, bm)
        return location.chapter, location.page

    def fullcopy_page(self, pno, to=-1):
        """Make a full page duplicate."""
        pdf = _as_pdf_document(self)
        page_count = mupdf.pdf_count_pages( pdf)
        try:
            if (not _INRANGE(pno, 0, page_count - 1)
                    or not _INRANGE(to, -1, page_count - 1)
                    ):
                raise ValueError( MSG_BAD_PAGENO)

            page1 = mupdf.pdf_resolve_indirect( mupdf.pdf_lookup_page_obj( pdf, pno))

            page2 = mupdf.pdf_deep_copy_obj( page1)
            old_annots = mupdf.pdf_dict_get( page2, PDF_NAME('Annots'))

            # copy annotations, but remove Popup and IRT types
            if old_annots.m_internal:
                n = mupdf.pdf_array_len( old_annots)
                new_annots = mupdf.pdf_new_array( pdf, n)
                for i in range(n):
                    o = mupdf.pdf_array_get( old_annots, i)
                    subtype = mupdf.pdf_dict_get( o, PDF_NAME('Subtype'))
                    if mupdf.pdf_name_eq( subtype, PDF_NAME('Popup')):
                        continue
                    if mupdf.pdf_dict_gets( o, "IRT").m_internal:
                        continue
                    copy_o = mupdf.pdf_deep_copy_obj( mupdf.pdf_resolve_indirect( o))
                    xref = mupdf.pdf_create_object( pdf)
                    mupdf.pdf_update_object( pdf, xref, copy_o)
                    copy_o = mupdf.pdf_new_indirect( pdf, xref, 0)
                    mupdf.pdf_dict_del( copy_o, PDF_NAME('Popup'))
                    mupdf.pdf_dict_del( copy_o, PDF_NAME('P'))
                    mupdf.pdf_array_push( new_annots, copy_o)
                mupdf.pdf_dict_put( page2, PDF_NAME('Annots'), new_annots)

            # copy the old contents stream(s)
            res = JM_read_contents( page1)

            # create new /Contents object for page2
            if res and res.m_internal:
                #contents = mupdf.pdf_add_stream( pdf, mupdf.fz_new_buffer_from_copied_data( b"  ", 1), NULL, 0)
                contents = mupdf.pdf_add_stream( pdf, mupdf.fz_new_buffer_from_copied_data( b" "), mupdf.PdfObj(), 0)
                JM_update_stream( pdf, contents, res, 1)
                mupdf.pdf_dict_put( page2, PDF_NAME('Contents'), contents)

            # now insert target page, making sure it is an indirect object
            xref = mupdf.pdf_create_object( pdf)   # get new xref
            mupdf.pdf_update_object( pdf, xref, page2) # store new page

            page2 = mupdf.pdf_new_indirect( pdf, xref, 0)  # reread object
            mupdf.pdf_insert_page( pdf, to, page2) # and store the page
        finally:
            mupdf.ll_pdf_drop_page_tree( pdf.m_internal)

        self._reset_page_refs()

    def get_char_widths(
            doc: 'Document',
            xref: int,
            limit: int = 256,
            idx: int = 0,
            fontdict: OptDict = None,
            ) -> list:
        """Get list of glyph information of a font.

        Notes:
            Must be provided by its XREF number. If we already dealt with the
            font, it will be recorded in doc.FontInfos. Otherwise we insert an
            entry there.
            Finally we return the glyphs for the font. This is a list of
            (glyph, width) where glyph is an integer controlling the char
            appearance, and width is a float controlling the char's spacing:
            width * fontsize is the actual space.
            For 'simple' fonts, glyph == ord(char) will usually be true.
            Exceptions are 'Symbol' and 'ZapfDingbats'. We are providing data for these directly here.
        """
        fontinfo = CheckFontInfo(doc, xref)
        if fontinfo is None:  # not recorded yet: create it
            if fontdict is None:
                name, ext, stype, asc, dsc = utils._get_font_properties(doc, xref)
                fontdict = {
                    "name": name,
                    "type": stype,
                    "ext": ext,
                    "ascender": asc,
                    "descender": dsc,
                }
            else:
                name = fontdict["name"]
                ext = fontdict["ext"]
                stype = fontdict["type"]
                ordering = fontdict["ordering"]
                simple = fontdict["simple"]

            if ext == "":
                raise ValueError("xref is not a font")

            # check for 'simple' fonts
            if stype in ("Type1", "MMType1", "TrueType"):
                simple = True
            else:
                simple = False

            # check for CJK fonts
            if name in ("Fangti", "Ming"):
                ordering = 0
            elif name in ("Heiti", "Song"):
                ordering = 1
            elif name in ("Gothic", "Mincho"):
                ordering = 2
            elif name in ("Dotum", "Batang"):
                ordering = 3
            else:
                ordering = -1

            fontdict["simple"] = simple

            if name == "ZapfDingbats":
                glyphs = zapf_glyphs
            elif name == "Symbol":
                glyphs = symbol_glyphs
            else:
                glyphs = None

            fontdict["glyphs"] = glyphs
            fontdict["ordering"] = ordering
            fontinfo = [xref, fontdict]
            doc.FontInfos.append(fontinfo)
        else:
            fontdict = fontinfo[1]
            glyphs = fontdict["glyphs"]
            simple = fontdict["simple"]
            ordering = fontdict["ordering"]

        if glyphs is None:
            oldlimit = 0
        else:
            oldlimit = len(glyphs)

        mylimit = max(256, limit)

        if mylimit <= oldlimit:
            return glyphs

        if ordering < 0:  # not a CJK font
            glyphs = doc._get_char_widths(
                xref, fontdict["name"], fontdict["ext"], fontdict["ordering"], mylimit, idx
            )
        else:  # CJK fonts use char codes and width = 1
            glyphs = None

        fontdict["glyphs"] = glyphs
        fontinfo[1] = fontdict
        UpdateFontInfo(doc, fontinfo)

        return glyphs

    def get_layer(self, config=-1):
        """Content of ON, OFF, RBGroups of an OC layer."""
        pdf = _as_pdf_document(self)
        ocp = mupdf.pdf_dict_getl(
                mupdf.pdf_trailer( pdf),
                PDF_NAME('Root'),
                PDF_NAME('OCProperties'),
                )
        if not ocp.m_internal:
            return
        if config == -1:
            obj = mupdf.pdf_dict_get( ocp, PDF_NAME('D'))
        else:
            obj = mupdf.pdf_array_get(
                    mupdf.pdf_dict_get( ocp, PDF_NAME('Configs')),
                    config,
                    )
        if not obj.m_internal:
            raise ValueError( MSG_BAD_OC_CONFIG)
        rc = JM_get_ocg_arrays( obj)
        return rc

    def get_layers(self):
        """Show optional OC layers."""
        pdf = _as_pdf_document(self)
        n = mupdf.pdf_count_layer_configs( pdf)
        if n == 1:
            obj = mupdf.pdf_dict_getl(
                    mupdf.pdf_trailer( pdf),
                    PDF_NAME('Root'),
                    PDF_NAME('OCProperties'),
                    PDF_NAME('Configs'),
                    )
            if not mupdf.pdf_is_array( obj):
                n = 0
        rc = []
        info = mupdf.PdfLayerConfig()
        for i in range(n):
            mupdf.pdf_layer_config_info( pdf, i, info)
            item = {
                    "number": i,
                    "name": info.name,
                    "creator": info.creator,
                    }
            rc.append( item)
        return rc

    def get_new_xref(self):
        """Make new xref."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        xref = 0
        ENSURE_OPERATION(pdf)
        xref = mupdf.pdf_create_object(pdf)
        return xref

    def get_oc(doc: 'Document', xref: int) -> int:
        """Return optional content object xref for an image or form xobject.

        Args:
            xref: (int) xref number of an image or form xobject.
        """
        if doc.is_closed or doc.is_encrypted:
            raise ValueError("document close or encrypted")
        t, name = doc.xref_get_key(xref, "Subtype")
        if t != "name" or name not in ("/Image", "/Form"):
            raise ValueError("bad object type at xref %i" % xref)
        t, oc = doc.xref_get_key(xref, "OC")
        if t != "xref":
            return 0
        rc = int(oc.replace("0 R", ""))
        return rc
    
    def get_ocgs(self):
        """Show existing optional content groups."""
        ci = mupdf.pdf_new_name( "CreatorInfo")
        pdf = _as_pdf_document(self)
        ocgs = mupdf.pdf_dict_getl(
                mupdf.pdf_dict_get( mupdf.pdf_trailer( pdf), PDF_NAME('Root')),
                PDF_NAME('OCProperties'),
                PDF_NAME('OCGs'),
                )
        rc = dict()
        if not mupdf.pdf_is_array( ocgs):
            return rc
        n = mupdf.pdf_array_len( ocgs)
        for i in range(n):
            ocg = mupdf.pdf_array_get( ocgs, i)
            xref = mupdf.pdf_to_num( ocg)
            name = mupdf.pdf_to_text_string( mupdf.pdf_dict_get( ocg, PDF_NAME('Name')))
            obj = mupdf.pdf_dict_getl( ocg, PDF_NAME('Usage'), ci, PDF_NAME('Subtype'))
            usage = None
            if obj.m_internal:
                usage = mupdf.pdf_to_name( obj)
            intents = list()
            intent = mupdf.pdf_dict_get( ocg, PDF_NAME('Intent'))
            if intent.m_internal:
                if mupdf.pdf_is_name( intent):
                    intents.append( mupdf.pdf_to_name( intent))
                elif mupdf.pdf_is_array( intent):
                    m = mupdf.pdf_array_len( intent)
                    for j in range(m):
                        o = mupdf.pdf_array_get( intent, j)
                        if mupdf.pdf_is_name( o):
                            intents.append( mupdf.pdf_to_name( o))
            if mupdf_version_tuple >= (1, 26, 11):
                resource_stack = mupdf.PdfResourceStack()
                hidden = mupdf.pdf_is_ocg_hidden( pdf, resource_stack, usage, ocg)
            else:
                hidden = mupdf.pdf_is_ocg_hidden( pdf, mupdf.PdfObj(), usage, ocg)
            item = {
                    "name": name,
                    "intent": intents,
                    "on": not hidden,
                    "usage": usage,
                    }
            temp = xref
            rc[ temp] = item
        return rc

    def get_ocmd(doc: 'Document', xref: int) -> dict:
        """Return the definition of an OCMD (optional content membership dictionary).

        Recognizes PDF dict keys /OCGs (PDF array of OCGs), /P (policy string) and
        /VE (visibility expression, PDF array). Via string manipulation, this
        info is converted to a Python dictionary with keys "xref", "ocgs", "policy"
        and "ve" - ready to recycle as input for 'set_ocmd()'.
        """

        if xref not in range(doc.xref_length()):
            raise ValueError("bad xref")
        text = doc.xref_object(xref, compressed=True)
        if "/Type/OCMD" not in text:
            raise ValueError("bad object type")
        textlen = len(text)

        p0 = text.find("/OCGs[")  # look for /OCGs key
        p1 = text.find("]", p0)
        if p0 < 0 or p1 < 0:  # no OCGs found
            ocgs = None
        else:
            ocgs = text[p0 + 6 : p1].replace("0 R", " ").split()
            ocgs = list(map(int, ocgs))

        p0 = text.find("/P/")  # look for /P policy key
        if p0 < 0:
            policy = None
        else:
            p1 = text.find("ff", p0)
            if p1 < 0:
                p1 = text.find("on", p0)
            if p1 < 0:  # some irregular syntax
                raise ValueError("bad object at xref")
            else:
                policy = text[p0 + 3 : p1 + 2]

        p0 = text.find("/VE[")  # look for /VE visibility expression key
        if p0 < 0:  # no visibility expression found
            ve = None
        else:
            lp = rp = 0  # find end of /VE by finding last ']'.
            p1 = p0
            while lp < 1 or lp != rp:
                p1 += 1
                if not p1 < textlen:  # some irregular syntax
                    raise ValueError("bad object at xref")
                if text[p1] == "[":
                    lp += 1
                if text[p1] == "]":
                    rp += 1
            # p1 now positioned at the last "]"
            ve = text[p0 + 3 : p1 + 1]  # the PDF /VE array
            ve = (
                ve.replace("/And", '"and",')
                .replace("/Not", '"not",')
                .replace("/Or", '"or",')
            )
            ve = ve.replace(" 0 R]", "]").replace(" 0 R", ",").replace("][", "],[")
            import json
            try:
                ve = json.loads(ve)
            except Exception:
                exception_info()
                message(f"bad /VE key: {ve!r}")
                raise
        return {"xref": xref, "ocgs": ocgs, "policy": policy, "ve": ve}

    def get_outline_xrefs(self):
        """Get list of outline xref numbers."""
        xrefs = []
        pdf = _as_pdf_document(self, required=0)
        if not pdf.m_internal:
            return xrefs
        root = mupdf.pdf_dict_get(mupdf.pdf_trailer(pdf), PDF_NAME('Root'))
        if not root.m_internal:
            return xrefs
        olroot = mupdf.pdf_dict_get(root, PDF_NAME('Outlines'))
        if not olroot.m_internal:
            return xrefs
        first = mupdf.pdf_dict_get(olroot, PDF_NAME('First'))
        if not first.m_internal:
            return xrefs
        xrefs = JM_outline_xrefs(first, xrefs)
        return xrefs

    def get_page_fonts(self, pno: int, full: bool =False) -> list:
        """Retrieve a list of fonts used on a page.
        """
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if not self.is_pdf:
            return ()
        if type(pno) is not int:
            try:
                pno = pno.number
            except Exception:
                exception_info()
                raise ValueError("need a Page or page number")
        val = self._getPageInfo(pno, 1)
        if not full:
            return [v[:-1] for v in val]
        return val

    def get_page_images(self, pno: int, full: bool =False) -> list:
        """Retrieve a list of images used on a page.
        """
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if not self.is_pdf:
            return ()
        val = self._getPageInfo(pno, 2)
        if not full:
            return [v[:-1] for v in val]
        return val

    def get_page_labels(self):
        """Return page label definitions in PDF document.

        Returns:
            A list of dictionaries with the following format:
            {'startpage': int, 'prefix': str, 'style': str, 'firstpagenum': int}.
        """
        # Jorj McKie, 2021-01-10
        return [utils.rule_dict(item) for item in self._get_page_labels()]

    def get_page_numbers(doc, label, only_one=False):
        """Return a list of page numbers with the given label.

        Args:
            doc: PDF document object (resp. 'self').
            label: (str) label.
            only_one: (bool) stop searching after first hit.
        Returns:
            List of page numbers having this label.
        """
        # Jorj McKie, 2021-01-06

        numbers = []
        if not label:
            return numbers
        labels = doc._get_page_labels()
        if labels == []:
            return numbers
        for i in range(doc.page_count):
            plabel = utils.get_label_pno(i, labels)
            if plabel == label:
                numbers.append(i)
                if only_one:
                    break
        return numbers
    
    def get_page_pixmap(
            doc: 'Document',
            pno: int,
            *,
            matrix: matrix_like = None,
            dpi=None,
            colorspace: Colorspace = None,
            clip: rect_like = None,
            alpha: bool = False,
            annots: bool = True,
            ) -> 'Pixmap':
        """Create pixmap of document page by page number.

        Notes:
            Convenience function calling page.get_pixmap.
        Args:
            pno: (int) page number
            matrix: pymupdf.Matrix for transformation (default: pymupdf.Identity).
            colorspace: (str,pymupdf.Colorspace) rgb, rgb, gray - case ignored, default csRGB.
            clip: (irect-like) restrict rendering to this area.
            alpha: (bool) include alpha channel
            annots: (bool) also render annotations
        """
        if matrix is None:
            matrix = Identity
        if colorspace is None:
            colorspace = csRGB
        return doc[pno].get_pixmap(
                matrix=matrix,
                dpi=dpi, colorspace=colorspace,
                clip=clip,
                alpha=alpha,
                annots=annots
                )
    
    def get_page_text(
            doc: 'Document',
            pno: int,
            option: str = "text",
            clip: rect_like = None,
            flags: OptInt = None,
            textpage: 'TextPage' = None,
            sort: bool = False,
            ) -> typing.Any:
        """Extract a document page's text by page number.

        Notes:
            Convenience function calling page.get_text().
        Args:
            pno: page number
            option: (str) text, words, blocks, html, dict, json, rawdict, xhtml or xml.
        Returns:
            output from page.TextPage().
        """
        return doc[pno].get_text(option, clip=clip, flags=flags, sort=sort)
    
    def get_page_xobjects(self, pno: int) -> list:
        """Retrieve a list of XObjects used on a page.
        """
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if not self.is_pdf:
            return ()
        val = self._getPageInfo(pno, 3)
        return val

    def get_sigflags(self):
        """Get the /SigFlags value."""
        pdf = _as_pdf_document(self, required=0)
        if not pdf.m_internal:
            return -1   # not a PDF
        sigflags = mupdf.pdf_dict_getl(
                mupdf.pdf_trailer(pdf),
                PDF_NAME('Root'),
                PDF_NAME('AcroForm'),
                PDF_NAME('SigFlags'),
                )
        sigflag = -1
        if sigflags.m_internal:
            sigflag = mupdf.pdf_to_int(sigflags)
        return sigflag

    def get_toc(
            doc: 'Document',
            simple: bool = True,
            ) -> list:
        """Create a table of contents.

        Args:
            simple: a bool to control output. Returns a list, where each entry consists of outline level, title, page number and link destination (if simple = False). For details see PyMuPDF's documentation.
        """
        def recurse(olItem, liste, lvl):
            """Recursively follow the outline item chain and record item information in a list."""
            while olItem and olItem.this.m_internal:
                if olItem.title:
                    title = olItem.title
                else:
                    title = " "

                if not olItem.is_external:
                    if olItem.uri:
                        if olItem.page == -1:
                            resolve = doc.resolve_link(olItem.uri)
                            page = resolve[0] + 1
                        else:
                            page = olItem.page + 1
                    else:
                        page = -1
                else:
                    page = -1

                if not simple:
                    link = utils.getLinkDict(olItem, doc)
                    liste.append([lvl, title, page, link])
                else:
                    liste.append([lvl, title, page])

                if olItem.down:
                    liste = recurse(olItem.down, liste, lvl + 1)
                olItem = olItem.next
            return liste

        # ensure document is open
        if doc.is_closed:
            raise ValueError("document closed")
        doc.init_doc()
        olItem = doc.outline
        if not olItem:
            return []
        lvl = 1
        liste = []
        toc = recurse(olItem, liste, lvl)
        if doc.is_pdf and not simple:
            doc._extend_toc_items(toc)
        return toc
    
    def get_xml_metadata(self):
        """Get document XML metadata."""
        xml = None
        pdf = _as_pdf_document(self, required=0)
        if pdf.m_internal:
            xml = mupdf.pdf_dict_getl(
                    mupdf.pdf_trailer(pdf),
                    PDF_NAME('Root'),
                    PDF_NAME('Metadata'),
                    )
        if xml is not None and xml.m_internal:
            buff = mupdf.pdf_load_stream(xml)
            rc = JM_UnicodeFromBuffer(buff)
        else:
            rc = ''
        return rc

    def has_annots(doc: 'Document') -> bool:
        """Check whether there are annotations on any page."""
        if doc.is_closed:
            raise ValueError("document closed")
        if not doc.is_pdf:
            raise ValueError("is no PDF")
        for i in range(doc.page_count):
            for item in doc.page_annot_xrefs(i):
                # pylint: disable=no-member
                if not (item[1] == mupdf.PDF_ANNOT_LINK or item[1] == mupdf.PDF_ANNOT_WIDGET):  # pylint: disable=no-member
                    return True
        return False
    
    def has_links(doc: 'Document') -> bool:
        """Check whether there are links on any page."""
        if doc.is_closed:
            raise ValueError("document closed")
        if not doc.is_pdf:
            raise ValueError("is no PDF")
        for i in range(doc.page_count):
            for item in doc.page_annot_xrefs(i):
                if item[1] == mupdf.PDF_ANNOT_LINK:  # pylint: disable=no-member
                    return True
        return False
    
    def init_doc(self):
        if self.is_encrypted:
            raise ValueError("cannot initialize - document still encrypted")
        self._outline = self._loadOutline()
        self.metadata = dict(
                    [
                        (k,self._getMetadata(v)) for k,v in {
                            'format':'format',
                            'title':'info:Title',
                            'author':'info:Author',
                            'subject':'info:Subject',
                            'keywords':'info:Keywords',
                            'creator':'info:Creator',
                            'producer':'info:Producer',
                            'creationDate':'info:CreationDate',
                            'modDate':'info:ModDate',
                            'trapped':'info:Trapped'
                            }.items()
                    ]
                )
        self.metadata['encryption'] = None if self._getMetadata('encryption')=='None' else self._getMetadata('encryption')

    def insert_file(self,
            infile,
            from_page=-1,
            to_page=-1,
            start_at=-1,
            rotate=-1,
            links=True,
            annots=True,
            show_progress=0,
            final=1,
            ):
        '''
        Insert an arbitrary supported document to an existing PDF.

        The infile may be given as a filename, a Document or a Pixmap. Other
        parameters - where applicable - equal those of insert_pdf().
        '''
        src = None
        if isinstance(infile, Pixmap):
            if infile.colorspace.n > 3:
                infile = Pixmap(csRGB, infile)
            src = Document("png", infile.tobytes())
        elif isinstance(infile, Document):
            src = infile
        else:
            src = Document(infile)
        if not src:
            raise ValueError("bad infile parameter")
        if not src.is_pdf:
            pdfbytes = src.convert_to_pdf()
            src = Document("pdf", pdfbytes)
        return self.insert_pdf(
                src,
                from_page=from_page,
                to_page=to_page,
                start_at=start_at,
                rotate=rotate,
                links=links,
                annots=annots,
                show_progress=show_progress,
                final=final,
                )

    def insert_page(
            doc: 'Document',
            pno: int,
            text: typing.Union[str, list, None] = None,
            fontsize: float = 11,
            width: float = 595,
            height: float = 842,
            fontname: str = "helv",
            fontfile: OptStr = None,
            color: OptSeq = (0,),
            ) -> int:
        """Create a new PDF page and insert some text.

        Notes:
            Function combining pymupdf.Document.new_page() and pymupdf.Page.insert_text().
            For parameter details see these methods.
        """
        page = doc.new_page(pno=pno, width=width, height=height)
        if not bool(text):
            return 0
        rc = page.insert_text(
            (50, 72),
            text,
            fontsize=fontsize,
            fontname=fontname,
            fontfile=fontfile,
            color=color,
        )
        return rc
    
    def insert_pdf(
            self,
            docsrc,
            *,
            from_page=-1,
            to_page=-1,
            start_at=-1,
            rotate=-1,
            links=1,
            annots=1,
            widgets=1,
            join_duplicates=0,
            show_progress=0,
            final=1,
            _gmap=None,
            ):
        """Insert a page range from another PDF.

        Args:
            docsrc: PDF to copy from. Must be different object, but may be same file.
            from_page: (int) first source page to copy, 0-based, default 0.
            to_page: (int) last source page to copy, 0-based, default last page.
            start_at: (int) from_page will become this page number in target.
            rotate: (int) rotate copied pages, default -1 is no change.
            links: (int/bool) whether to also copy links.
            annots: (int/bool) whether to also copy annotations.
            widgets: (int/bool) whether to also copy form fields.
            join_duplicates: (int/bool) join or rename duplicate widget names.
            show_progress: (int) progress message interval, 0 is no messages.
            final: (bool) indicates last insertion from this source PDF.
            _gmap: internal use only

        Copy sequence reversed if from_page > to_page."""

        # Insert pages from a source PDF into this PDF.
        # For reconstructing the links (_do_links method), we must save the
        # insertion point (start_at) if it was specified as -1.
        #log( 'insert_pdf(): start')
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if self._graft_id == docsrc._graft_id:
            raise ValueError("source and target cannot be same object")
        sa = start_at
        if sa < 0:
            sa = self.page_count
        outCount = self.page_count
        srcCount = docsrc.page_count

        # local copies of page numbers
        fp = from_page
        tp = to_page
        sa = start_at

        # normalize page numbers
        fp = max(fp, 0) # -1 = first page
        fp = min(fp, srcCount - 1)  # but do not exceed last page

        if tp < 0:
            tp = srcCount - 1   # -1 = last page
        tp = min(tp, srcCount - 1)  # but do not exceed last page

        if sa < 0:
            sa = outCount   # -1 = behind last page
        sa = min(sa, outCount)  # but that is also the limit

        if len(docsrc) > show_progress > 0:
            inname = os.path.basename(docsrc.name)
            if not inname:
                inname = "memory PDF"
            outname = os.path.basename(self.name)
            if not outname:
                outname = "memory PDF"
            message("Inserting '%s' at '%s'" % (inname, outname))

        # retrieve / make a Graftmap to avoid duplicate objects
        #log( 'insert_pdf(): Graftmaps')
        isrt = docsrc._graft_id
        _gmap = self.Graftmaps.get(isrt, None)
        if _gmap is None:
            #log( 'insert_pdf(): Graftmaps2')
            _gmap = Graftmap(self)
            self.Graftmaps[isrt] = _gmap

        if g_use_extra:
            #log( 'insert_pdf(): calling extra_FzDocument_insert_pdf()')
            extra_FzDocument_insert_pdf(
                    self.this,
                    docsrc.this,
                    from_page,
                    to_page,
                    start_at,
                    rotate,
                    links,
                    annots,
                    show_progress,
                    final,
                    _gmap,
                    )
            #log( 'insert_pdf(): extra_FzDocument_insert_pdf() returned.')
        else:
            pdfout = _as_pdf_document(self)
            pdfsrc = _as_pdf_document(docsrc)

            if not pdfout.m_internal or not pdfsrc.m_internal:
                raise TypeError( "source or target not a PDF")
            ENSURE_OPERATION(pdfout)
            JM_merge_range(pdfout, pdfsrc, fp, tp, sa, rotate, links, annots, show_progress, _gmap)
        
        #log( 'insert_pdf(): calling self._reset_page_refs()')
        self._reset_page_refs()
        if links:
            #log( 'insert_pdf(): calling self._do_links()')
            self._do_links(docsrc, from_page=fp, to_page=tp, start_at=sa)
        if widgets:
            self._do_widgets(docsrc, _gmap, from_page=fp, to_page=tp, start_at=sa, join_duplicates=join_duplicates)
        if final == 1:
            self.Graftmaps[isrt] = None
        #log( 'insert_pdf(): returning')

    @property
    def is_dirty(self):
        pdf = _as_pdf_document(self, required=0)
        if not pdf.m_internal:
            return False
        r = mupdf.pdf_has_unsaved_changes(pdf)
        return True if r else False

    @property
    def is_fast_webaccess(self):
        '''
        Check whether we have a linearized PDF.
        '''
        pdf = _as_pdf_document(self, required=0)
        if pdf.m_internal:
            return mupdf.pdf_doc_was_linearized(pdf)
        return False    # gracefully handle non-PDF

    @property
    def is_form_pdf(self):
        """Either False or PDF field count."""
        pdf = _as_pdf_document(self, required=0)
        if not pdf.m_internal:
            return False
        count = -1
        try:
            fields = mupdf.pdf_dict_getl(
                    mupdf.pdf_trailer(pdf),
                    mupdf.PDF_ENUM_NAME_Root,
                    mupdf.PDF_ENUM_NAME_AcroForm,
                    mupdf.PDF_ENUM_NAME_Fields,
                    )
            if mupdf.pdf_is_array(fields):
                count = mupdf.pdf_array_len(fields)
        except Exception:
            if g_exceptions_verbose:    exception_info()
            return False
        if count >= 0:
            return count
        return False

    @property
    def is_pdf(self):
        """Check for PDF."""
        if isinstance(self.this, mupdf.PdfDocument):
            return True
        # Avoid calling smupdf.pdf_specifics because it will end up creating
        # a new PdfDocument which will call pdf_create_document(), which is ok
        # but a little unnecessary.
        #
        if mupdf.ll_pdf_specifics(self.this.m_internal):
            ret = True
        else:
            ret = False
        return ret

    @property
    def is_reflowable(self):
        """Check if document is layoutable."""
        if self.is_closed:
            raise ValueError("document closed")
        return bool(mupdf.fz_is_document_reflowable(self))

    @property
    def is_repaired(self):
        """Check whether PDF was repaired."""
        pdf = _as_pdf_document(self, required=0)
        if not pdf.m_internal:
            return False
        r = mupdf.pdf_was_repaired(pdf)
        if r:
            return True
        return False

    def journal_can_do(self):
        """Show if undo and / or redo are possible."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        undo=0
        redo=0
        pdf = _as_pdf_document(self)
        undo = mupdf.pdf_can_undo(pdf)
        redo = mupdf.pdf_can_redo(pdf)
        return {'undo': bool(undo), 'redo': bool(redo)}

    def journal_enable(self):
        """Activate document journalling."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        mupdf.pdf_enable_journal(pdf)

    def journal_is_enabled(self):
        """Check if journalling is enabled."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        enabled = pdf.m_internal and pdf.m_internal.journal
        return enabled

    def journal_load(self, filename):
        """Load a journal from a file."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        if isinstance(filename, str):
            mupdf.pdf_load_journal(pdf, filename)
        else:
            res = JM_BufferFromBytes(filename)
            stm = mupdf.fz_open_buffer(res)
            mupdf.pdf_deserialise_journal(pdf, stm)
        if not pdf.m_internal.journal:
            RAISEPY( "Journal and document do not match", JM_Exc_FileDataError)

    def journal_op_name(self, step):
        """Show operation name for given step."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        name = mupdf.pdf_undoredo_step(pdf, step)
        return name

    def journal_position(self):
        """Show journalling state."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        steps=0
        pdf = _as_pdf_document(self)
        rc, steps = mupdf.pdf_undoredo_state(pdf)
        return rc, steps

    def journal_redo(self):
        """Move forward in the journal."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        mupdf.pdf_redo(pdf)
        return True

    def journal_save(self, filename):
        """Save journal to a file."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        if isinstance(filename, str):
            mupdf.pdf_save_journal(pdf, filename)
        else:
            out = JM_new_output_fileptr(filename)
            mupdf.pdf_write_journal(pdf, out)
            out.fz_close_output()

    def journal_start_op(self, name=None):
        """Begin a journalling operation."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        if not pdf.m_internal.journal:
            raise RuntimeError( "Journalling not enabled")
        if name:
            mupdf.pdf_begin_operation(pdf, name)
        else:
            mupdf.pdf_begin_implicit_operation(pdf)

    def journal_stop_op(self):
        """End a journalling operation."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        mupdf.pdf_end_operation(pdf)

    def journal_undo(self):
        """Move backwards in the journal."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        mupdf.pdf_undo(pdf)
        return True

    @property
    def language(self):
        """Document language."""
        pdf = _as_pdf_document(self, required=0)
        if not pdf.m_internal:
            return
        lang = mupdf.pdf_document_language(pdf)
        if lang == mupdf.FZ_LANG_UNSET:
            return
        return mupdf.fz_string_from_text_language2(lang)

    @property
    def last_location(self):
        """Id (chapter, page) of last page."""
        if self.is_closed:
            raise ValueError("document closed")
        last_loc = mupdf.fz_last_page(self.this)
        return last_loc.chapter, last_loc.page

    def layer_ui_configs(self):
        """Show OC visibility status modifiable by user."""
        pdf = _as_pdf_document(self)
        info = mupdf.PdfLayerConfigUi()
        n = mupdf.pdf_count_layer_config_ui( pdf)
        rc = []
        for i in range(n):
            mupdf.pdf_layer_config_ui_info( pdf, i, info)
            if info.type == 1:
                type_ = "checkbox"
            elif info.type == 2:
                type_ = "radiobox"
            else:
                type_ = "label"
            item = {
                    "number": i,
                    "text": info.text,
                    "depth": info.depth,
                    "type": type_,
                    "on": info.selected,
                    "locked": info.locked,
                    }
            rc.append(item)
        return rc

    def layout(self, rect=None, width=0, height=0, fontsize=11):
        """Re-layout a reflowable document."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        doc = self.this
        if not mupdf.fz_is_document_reflowable( doc):
            return
        w = width
        h = height
        r = JM_rect_from_py(rect)
        if not mupdf.fz_is_infinite_rect(r):
            w = r.x1 - r.x0
            h = r.y1 - r.y0
        if w <= 0.0 or h <= 0.0:
            raise ValueError( "bad page size")
        mupdf.fz_layout_document( doc, w, h, fontsize)

        self._reset_page_refs()
        self.init_doc()

    def load_page(self, page_id):
        """Load a page.

        'page_id' is either a 0-based page number or a tuple (chapter, pno),
        with chapter number and page number within that chapter.
        """
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if page_id is None:
            page_id = 0
        if page_id not in self:
            raise ValueError("page not in document")
        if type(page_id) is int and page_id < 0:
            np = self.page_count
            while page_id < 0:
                page_id += np
        if isinstance(page_id, int):
            page = mupdf.fz_load_page(self.this, page_id)
        else:
            chapter, pagenum = page_id
            page = mupdf.fz_load_chapter_page(self.this, chapter, pagenum)
        val = Page(page, self)

        val.thisown = True
        val.parent = self
        self._page_refs[id(val)] = val
        val._annot_refs = weakref.WeakValueDictionary()
        val.number = page_id
        return val

    def location_from_page_number(self, pno):
        """Convert pno to (chapter, page)."""
        if self.is_closed:
            raise ValueError("document closed")
        this_doc = self.this
        loc = mupdf.fz_make_location(-1, -1)
        page_count = mupdf.fz_count_pages(this_doc)
        while pno < 0:
            pno += page_count
        if pno >= page_count:
            raise ValueError( MSG_BAD_PAGENO)
        loc = mupdf.fz_location_from_page_number(this_doc, pno)
        return loc.chapter, loc.page

    def make_bookmark(self, loc):
        """Make a page pointer before layouting document."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        loc = mupdf.FzLocation(*loc)
        mark = mupdf.ll_fz_make_bookmark2( self.this.m_internal, loc.internal())
        return mark

    @property
    def markinfo(self) -> dict:
        """Return the PDF MarkInfo value."""
        xref = self.pdf_catalog()
        if xref == 0:
            return None
        rc = self.xref_get_key(xref, "MarkInfo")
        if rc[0] == "null":
            return {}
        if rc[0] == "xref":
            xref = int(rc[1].split()[0])
            val = self.xref_object(xref, compressed=True)
        elif rc[0] == "dict":
            val = rc[1]
        else:
            val = None
        if val is None or not (val[:2] == "<<" and val[-2:] == ">>"):
            return {}
        valid = {"Marked": False, "UserProperties": False, "Suspects": False}
        val = val[2:-2].split("/")
        for v in val[1:]:
            try:
                key, value = v.split()
            except Exception:
                if g_exceptions_verbose > 1:    exception_info()
                return valid
            if value == "true":
                valid[key] = True
        return valid

    def move_page(self, pno: int, to: int =-1):
        """Move a page within a PDF document.

        Args:
            pno: source page number.
            to: put before this page, '-1' means after last page.
        """
        if self.is_closed:
            raise ValueError("document closed")
        page_count = len(self)
        if (pno not in range(page_count) or to not in range(-1, page_count)):
            raise ValueError("bad page number(s)")
        before = 1
        copy = 0
        if to == -1:
            to = page_count - 1
            before = 0

        return self._move_copy_page(pno, to, before, copy)

    @property
    def name(self):
        return self._name
    
    def need_appearances(self, value=None):
        """Get/set the NeedAppearances value."""
        if not self.is_form_pdf:
            return None
        
        pdf = _as_pdf_document(self)
        oldval = -1
        appkey = "NeedAppearances"
        
        form = mupdf.pdf_dict_getp(
                mupdf.pdf_trailer(pdf),
                "Root/AcroForm",
                )
        app = mupdf.pdf_dict_gets(form, appkey)
        if mupdf.pdf_is_bool(app):
            oldval = mupdf.pdf_to_bool(app)
        if value:
            mupdf.pdf_dict_puts(form, appkey, mupdf.PDF_TRUE)
        else:
            mupdf.pdf_dict_puts(form, appkey, mupdf.PDF_FALSE)
        if value is None:
            return oldval >= 0
        return value

    @property
    def needs_pass(self):
        """Indicate password required."""
        if self.is_closed:
            raise ValueError("document closed")
        document = self.this if isinstance(self.this, mupdf.FzDocument) else self.this.super()
        ret = mupdf.fz_needs_password( document)
        return ret

    def new_page(
            doc: 'Document',
            pno: int = -1,
            width: float = 595,
            height: float = 842,
            ) -> Page:
        """Create and return a new page object.

        Args:
            pno: (int) insert before this page. Default: after last page.
            width: (float) page width in points. Default: 595 (ISO A4 width).
            height: (float) page height in points. Default 842 (ISO A4 height).
        Returns:
            A pymupdf.Page object.
        """
        doc._newPage(pno, width=width, height=height)
        return doc[pno]
    
    def next_location(self, page_id):
        """Get (chapter, page) of next page."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if type(page_id) is int:
            page_id = (0, page_id)
        if page_id not in self:
            raise ValueError("page id not in document")
        if tuple(page_id) == self.last_location:
            return ()
        this_doc = _as_fz_document(self)
        val = page_id[ 0]
        if not isinstance(val, int):
            RAISEPY(MSG_BAD_PAGEID, PyExc_ValueError)
        chapter = val
        val = page_id[ 1]
        pno = val
        loc = mupdf.fz_make_location(chapter, pno)
        next_loc = mupdf.fz_next_page( this_doc, loc)
        return next_loc.chapter, next_loc.page

    def page_annot_xrefs(self, n):
        if g_use_extra:
            return extra.page_annot_xrefs( self.this, n)
        
        if isinstance(self.this, mupdf.PdfDocument):
            page_count = mupdf.pdf_count_pages(self.this)
            pdf_document = self.this
        else:
            page_count = mupdf.fz_count_pages(self.this)
            pdf_document = _as_pdf_document(self)
        while n < 0:
            n += page_count
        if n > page_count:
            raise ValueError( MSG_BAD_PAGENO)
        page_obj = mupdf.pdf_lookup_page_obj(pdf_document, n)
        annots = JM_get_annot_xref_list(page_obj)
        return annots

    @property
    def page_count(self):
        """Number of pages."""
        if self.is_closed:
            raise ValueError('document closed')
        if g_use_extra:
            return self.page_count2(self)
        if isinstance( self.this, mupdf.FzDocument):
            return mupdf.fz_count_pages( self.this)
        else:
            return mupdf.pdf_count_pages( self.this)

    def page_cropbox(self, pno):
        """Get CropBox of page number (without loading page)."""
        if self.is_closed:
            raise ValueError("document closed")
        this_doc = self.this
        page_count = mupdf.fz_count_pages( this_doc)
        n = pno
        while n < 0:
            n += page_count
        pdf = _as_pdf_document(self)
        if n >= page_count:
            raise ValueError( MSG_BAD_PAGENO)
        pageref = mupdf.pdf_lookup_page_obj( pdf, n)
        cropbox = JM_cropbox(pageref)
        val = JM_py_from_rect(cropbox)

        val = Rect(val)

        return val

    def page_number_from_location(self, page_id):
        """Convert (chapter, pno) to page number."""
        if type(page_id) is int:
            np = self.page_count
            while page_id < 0:
                page_id += np
            page_id = (0, page_id)
        if page_id not in self:
            raise ValueError("page id not in document")
        chapter, pno = page_id
        loc = mupdf.fz_make_location( chapter, pno)
        page_n = mupdf.fz_page_number_from_location( self.this, loc)
        return page_n

    def page_xref(self, pno):
        """Get xref of page number."""
        if g_use_extra:
            return extra.page_xref( self.this, pno)
        if self.is_closed:
            raise ValueError("document closed")
        page_count = mupdf.fz_count_pages(self.this)
        n = pno
        while n < 0:
            n += page_count
        pdf = _as_pdf_document(self)
        xref = 0
        if n >= page_count:
            raise ValueError( MSG_BAD_PAGENO)
        xref = mupdf.pdf_to_num(mupdf.pdf_lookup_page_obj(pdf, n))
        return xref

    @property
    def pagelayout(self) -> str:
        """Return the PDF PageLayout value.
        """
        xref = self.pdf_catalog()
        if xref == 0:
            return None
        rc = self.xref_get_key(xref, "PageLayout")
        if rc[0] == "null":
            return "SinglePage"
        if rc[0] == "name":
            return rc[1][1:]
        return "SinglePage"

    @property
    def pagemode(self) -> str:
        """Return the PDF PageMode value.
        """
        xref = self.pdf_catalog()
        if xref == 0:
            return None
        rc = self.xref_get_key(xref, "PageMode")
        if rc[0] == "null":
            return "UseNone"
        if rc[0] == "name":
            return rc[1][1:]
        return "UseNone"

    if sys.implementation.version < (3, 9):
        # Appending `[Page]` causes `TypeError: 'ABCMeta' object is not subscriptable`.
        _pages_ret = collections.abc.Iterable
    else:
        _pages_ret = collections.abc.Iterable[Page]

    def pages(self, start: OptInt =None, stop: OptInt =None, step: OptInt =None) -> _pages_ret:
        """Return a generator iterator over a page range.

        Arguments have the same meaning as for the range() built-in.
        """
        if not self.page_count:
            return
        # set the start value
        start = start or 0
        while start < 0:
            start += self.page_count
        if start not in range(self.page_count):
            raise ValueError("bad start page number")

        # set the stop value
        stop = stop if stop is not None and stop <= self.page_count else self.page_count

        # set the step value
        if step == 0:
            raise ValueError("arg 3 must not be zero")
        if step is None:
            if start > stop:
                step = -1
            else:
                step = 1

        for pno in range(start, stop, step):
            yield (self.load_page(pno))

    def pdf_catalog(self):
        """Get xref of PDF catalog."""
        pdf = _as_pdf_document(self, required=0)
        xref = 0
        if not pdf.m_internal:
            return xref
        root = mupdf.pdf_dict_get(mupdf.pdf_trailer(pdf), PDF_NAME('Root'))
        xref = mupdf.pdf_to_num(root)
        return xref

    def pdf_trailer(self, compressed=0, ascii=0):
        """Get PDF trailer as a string."""
        return self.xref_object(-1, compressed=compressed, ascii=ascii)

    @property
    def permissions(self):
        """Document permissions."""
        if self.is_encrypted:
            return 0
        doc =self.this
        pdf = mupdf.pdf_document_from_fz_document(doc)

        # for PDF return result of standard function
        if pdf.m_internal:
            return mupdf.pdf_document_permissions(pdf)

        # otherwise simulate the PDF return value
        perm = 0xFFFFFFFC   # all permissions granted
        # now switch off where needed
        if not mupdf.fz_has_permission(doc, mupdf.FZ_PERMISSION_PRINT):
            perm = perm ^ mupdf.PDF_PERM_PRINT
        if not mupdf.fz_has_permission(doc, mupdf.FZ_PERMISSION_EDIT):
            perm = perm ^ mupdf.PDF_PERM_MODIFY
        if not mupdf.fz_has_permission(doc, mupdf.FZ_PERMISSION_COPY):
            perm = perm ^ mupdf.PDF_PERM_COPY
        if not mupdf.fz_has_permission(doc, mupdf.FZ_PERMISSION_ANNOTATE):
            perm = perm ^ mupdf.PDF_PERM_ANNOTATE
        return perm

    def prev_location(self, page_id):

        """Get (chapter, page) of previous page."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if type(page_id) is int:
            page_id = (0, page_id)
        if page_id not in self:
            raise ValueError("page id not in document")
        if page_id  == (0, 0):
            return ()
        chapter, pno = page_id
        loc = mupdf.fz_make_location(chapter, pno)
        prev_loc = mupdf.fz_previous_page(self.this, loc)
        return prev_loc.chapter, prev_loc.page

    def reload_page(self, page: Page) -> Page:
        """Make a fresh copy of a page."""
        old_annots = {}  # copy annot references to here
        pno = page.number  # save the page number
        for k, v in page._annot_refs.items():  # save the annot dictionary
            old_annots[k] = v
        
        # When we call `self.load_page()` below, it will end up in
        # fz_load_chapter_page(), which will return any matching page in the
        # document's list of non-ref-counted loaded pages, instead of actually
        # reloading the page.
        #
        # We want to assert that we have actually reloaded the fz_page, and not
        # simply returned the same `fz_page*` pointer from the document's list
        # of non-ref-counted loaded pages.
        #
        # So we first remove our reference to the `fz_page*`. This will
        # decrement .refs, and if .refs was 1, this is guaranteed to free the
        # `fz_page*` and remove it from the document's list if it was there. So
        # we are guaranteed that our returned `fz_page*` is from a genuine
        # reload, even if it happens to reuse the original block of memory.
        #
        # However if the original .refs is greater than one, there must be
        # other references to the `fz_page` somewhere, and we require that
        # these other references are not keeping the page in the document's
        # list.  We check that we are returning a newly loaded page by
        # asserting that our returned `fz_page*` is different from the original
        # `fz_page*` - the original was not freed, so a new `fz_page` cannot
        # reuse the same block of memory.
        #
        
        refs_old = page.this.m_internal.refs
        m_internal_old = page.this.m_internal_value()
        
        page.this = None
        page._erase()  # remove the page
        page = None
        TOOLS.store_shrink(100)
        page = self.load_page(pno)  # reload the page

        # copy annot refs over to the new dictionary
        #page_proxy = weakref.proxy(page)
        for k, v in old_annots.items():
            annot = old_annots[k]
            #annot.parent = page_proxy  # refresh parent to new page
            page._annot_refs[k] = annot
        if refs_old == 1:
            # We know that `page.this = None` will have decremented the ref
            # count to zero so we are guaranteed that the new `fz_page` is a
            # new page even if it happens to have reused the same block of
            # memory.
            pass
        else:
            # Check that the new `fz_page*` is different from the original.
            m_internal_new = page.this.m_internal_value()
            assert m_internal_new != m_internal_old, \
                    f'{refs_old=} {m_internal_old=:#x} {m_internal_new=:#x}'
        return page

    def repair(self):
        '''
        If we are a PDF document, does repair.
        '''
        pdf = _as_pdf_document(self, required=False)
        if pdf.m_internal:
            mupdf.pdf_check_document(pdf)
    
    def resolve_link(self, uri=None, chapters=0):
        """Calculate internal link destination.

        Args:
            uri: (str) some Link.uri
            chapters: (bool) whether to use (chapter, page) format
        Returns:
            (page_id, x, y) where x, y are point coordinates on the page.
            page_id is either page number (if chapters=0), or (chapter, pno).
        """
        if not uri:
            if chapters:
                return (-1, -1), 0, 0
            return -1, 0, 0
        try:
            loc, xp, yp = mupdf.fz_resolve_link(self.this, uri)
        except Exception:
            if g_exceptions_verbose:    exception_info()
            if chapters:
                return (-1, -1), 0, 0
            return -1, 0, 0
        if chapters:
            return (loc.chapter, loc.page), xp, yp
        pno = mupdf.fz_page_number_from_location(self.this, loc)
        return pno, xp, yp

    def rewrite_images(
        self,
        dpi_threshold=None,
        dpi_target=0,
        quality=0,
        lossy=True,
        lossless=True,
        bitonal=True,
        color=True,
        gray=True,
        set_to_gray=False,
        options=None,
    ):
        """Rewrite images in a PDF document.

        The typical use case is to reduce the size of the PDF by recompressing
        images. Default parameters will convert all images to JPEG where
        possible, using the specified resolutions and quality. Exclude
        undesired images by setting parameters to False.
        Args:
            dpi_threshold: look at images with a larger DPI only.
            dpi_target: change eligible images to this DPI.
            quality: Quality of the recompressed images (0-100).
            lossy: process lossy image types (e.g. JPEG).
            lossless: process lossless image types (e.g. PNG).
            bitonal: process black-and-white images (e.g. FAX)
            color: process colored images.
            gray: process gray images.
            set_to_gray: whether to change the PDF to gray at process start.
            options: (PdfImageRewriterOptions) Custom options for image
                    rewriting (optional). Expert use only. If provided, other
                    parameters are ignored, except set_to_gray.
        """
        quality_str = str(quality)
        if not dpi_threshold:
            dpi_threshold = dpi_target = 0
        if dpi_target > 0 and dpi_target >= dpi_threshold:
            raise ValueError("{dpi_target=} must be less than {dpi_threshold=}")
        template_opts = mupdf.PdfImageRewriterOptions()
        dir1 = set(dir(template_opts))  # for checking that only existing options are set
        if not options:
            opts = mupdf.PdfImageRewriterOptions()
            if bitonal:
                opts.bitonal_image_recompress_method = mupdf.FZ_RECOMPRESS_FAX
                opts.bitonal_image_subsample_method = mupdf.FZ_SUBSAMPLE_AVERAGE
                opts.bitonal_image_subsample_to = dpi_target
                opts.bitonal_image_recompress_quality = quality_str
                opts.bitonal_image_subsample_threshold = dpi_threshold
            if color:
                if lossless:
                    opts.color_lossless_image_recompress_method = mupdf.FZ_RECOMPRESS_JPEG
                    opts.color_lossless_image_subsample_method = mupdf.FZ_SUBSAMPLE_AVERAGE
                    opts.color_lossless_image_subsample_to = dpi_target
                    opts.color_lossless_image_subsample_threshold = dpi_threshold
                    opts.color_lossless_image_recompress_quality = quality_str
                if lossy:
                    opts.color_lossy_image_recompress_method = mupdf.FZ_RECOMPRESS_JPEG
                    opts.color_lossy_image_subsample_method = mupdf.FZ_SUBSAMPLE_AVERAGE
                    opts.color_lossy_image_subsample_threshold = dpi_threshold
                    opts.color_lossy_image_subsample_to = dpi_target
                    opts.color_lossy_image_recompress_quality = quality_str
            if gray:
                if lossless:
                    opts.gray_lossless_image_recompress_method = mupdf.FZ_RECOMPRESS_JPEG
                    opts.gray_lossless_image_subsample_method = mupdf.FZ_SUBSAMPLE_AVERAGE
                    opts.gray_lossless_image_subsample_to = dpi_target
                    opts.gray_lossless_image_subsample_threshold = dpi_threshold
                    opts.gray_lossless_image_recompress_quality = quality_str
                if lossy:
                    opts.gray_lossy_image_recompress_method = mupdf.FZ_RECOMPRESS_JPEG
                    opts.gray_lossy_image_subsample_method = mupdf.FZ_SUBSAMPLE_AVERAGE
                    opts.gray_lossy_image_subsample_threshold = dpi_threshold
                    opts.gray_lossy_image_subsample_to = dpi_target
                    opts.gray_lossy_image_recompress_quality = quality_str
        else:
            opts = options

        dir2 = set(dir(opts))  # checking that only possible options were used
        invalid_options = dir2 - dir1
        if invalid_options:
            raise ValueError(f"Invalid options: {invalid_options}")

        if set_to_gray:
            self.recolor(1)
        pdf = _as_pdf_document(self)
        mupdf.pdf_rewrite_images(pdf, opts)

    def recolor(self, components=1):
        """Change the color component count on all pages.

        Args:
            components: (int) desired color component count, one of 1, 3, 4.

        Invokes the same-named method for all pages.
        """
        if not self.is_pdf:
            raise ValueError("is no PDF")
        for i in range(self.page_count):
            self.load_page(i).recolor(components)

    def resolve_names(self):
        """Convert the PDF's destination names into a Python dict.

        The only parameter is the pymupdf.Document.
        All names found in the catalog under keys "/Dests" and "/Names/Dests" are
        being included.

        Returns:
            A dcitionary with the following layout:
            - key: (str) the name
            - value: (dict) with the following layout:
                * "page":  target page number (0-based). If no page number found -1.
                * "to": (x, y) target point on page - currently in PDF coordinates,
                        i.e. point (0,0) is the bottom-left of the page.
                * "zoom": (float) the zoom factor
                * "dest": (str) only occurs if the target location on the page has
                        not been provided as "/XYZ" or if no page number was found.
            Examples:
            {'__bookmark_1': {'page': 0, 'to': (0.0, 541.0), 'zoom': 0.0},
            '__bookmark_2': {'page': 0, 'to': (0.0, 481.45), 'zoom': 0.0}}

            or

            '21154a7c20684ceb91f9c9adc3b677c40': {'page': -1, 'dest': '/XYZ 15.75 1486 0'}, ...
        """
        if hasattr(self, "_resolved_names"):  # do not execute multiple times!
            return self._resolved_names
        # this is a backward listing of page xref to page number
        page_xrefs = {self.page_xref(i): i for i in range(self.page_count)}

        def obj_string(obj):
            """Return string version of a PDF object definition."""
            buffer = mupdf.fz_new_buffer(512)
            output = mupdf.FzOutput(buffer)
            mupdf.pdf_print_obj(output, obj, 1, 0)
            output.fz_close_output()
            return JM_UnicodeFromBuffer(buffer)

        def get_array(val):
            """Generate value of one item of the names dictionary."""
            templ_dict = {"page": -1, "dest": ""}  # value template
            if val.pdf_is_indirect():
                val = mupdf.pdf_resolve_indirect(val)
            if val.pdf_is_array():
                array = obj_string(val)
            elif val.pdf_is_dict():
                array = obj_string(mupdf.pdf_dict_gets(val, "D"))
            else:  # if all fails return the empty template
                return templ_dict

            # replace PDF "null" by zero, omit the square brackets
            array = array.replace("null", "0")[1:-1]

            # find stuff before first "/"
            idx = array.find("/")
            if idx < 1:  # this has no target page spec
                templ_dict["dest"] = array  # return the orig. string
                return templ_dict

            subval = array[:idx].strip()  # stuff before "/"
            array = array[idx:]  # stuff from "/" onwards
            templ_dict["dest"] = array
            # if we start with /XYZ: extract x, y, zoom
            # 1, 2 or 3 of these values may actually be supplied
            if array.startswith("/XYZ"):
                del templ_dict["dest"]  # don't return orig string in this case

                # make a list of the 3 tokens following "/XYZ"
                array_list = array.split()[1:4]  # omit "/XYZ"

                # fill up missing tokens with "0" strings
                while len(array_list) < 3:  # fill up if too short
                    array_list.append("0")  # add missing values

                # make list of 3 floats: x, y and zoom
                t = list(map(float, array_list))  # the resulting x, y, z values
                templ_dict["to"] = (t[0], t[1])
                templ_dict["zoom"] = t[2]

            # extract page number
            if subval.endswith("0 R"):  # page xref given?
                templ_dict["page"] = page_xrefs.get(int(subval.split()[0]),-1)
            else:  # naked page number given
                templ_dict["page"] = int(subval)
            return templ_dict

        def fill_dict(dest_dict, pdf_dict):
            """Generate name resolution items for pdf_dict.

            This may be either "/Names/Dests" or just "/Dests"
            """
            # length of the PDF dictionary
            name_count = mupdf.pdf_dict_len(pdf_dict)

            # extract key-val of each dict item
            for i in range(name_count):
                key = mupdf.pdf_dict_get_key(pdf_dict, i)
                val = mupdf.pdf_dict_get_val(pdf_dict, i)
                if key.pdf_is_name():  # this should always be true!
                    dict_key = key.pdf_to_name()
                else:
                    message(f"key {i} is no /Name")
                    dict_key = None

                if dict_key:
                    dest_dict[dict_key] = get_array(val)  # store key/value in dict

        # access underlying PDF document of fz Document
        pdf = mupdf.pdf_document_from_fz_document(self)

        # access PDF catalog
        catalog = mupdf.pdf_dict_gets(mupdf.pdf_trailer(pdf), "Root")

        dest_dict = {}

        # make PDF_NAME(Dests)
        dests = mupdf.pdf_new_name("Dests")

        # extract destinations old style (PDF 1.1)
        old_dests = mupdf.pdf_dict_get(catalog, dests)
        if old_dests.pdf_is_dict():
            fill_dict(dest_dict, old_dests)

        # extract destinations new style (PDF 1.2+)
        tree = mupdf.pdf_load_name_tree(pdf, dests)
        if tree.pdf_is_dict():
            fill_dict(dest_dict, tree)

        self._resolved_names = dest_dict  # store result or reuse
        return dest_dict

    def save(
            self,
            filename,
            garbage=0,
            clean=0,
            deflate=0,
            deflate_images=0,
            deflate_fonts=0,
            incremental=0,
            ascii=0,
            expand=0,
            linear=0,
            no_new_id=0,
            appearance=0,
            pretty=0,
            encryption=1,
            permissions=4095,
            owner_pw=None,
            user_pw=None,
            preserve_metadata=1,
            use_objstms=0,
            compression_effort=0,
            raise_on_repair=False,
            ):
        # From %pythonprepend save
        #
        is_repaired_pre = self.is_repaired
        """Save PDF to file, pathlib.Path or file pointer."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if type(filename) is str:
            pass
        elif hasattr(filename, "open"):  # assume: pathlib.Path
            filename = str(filename)
        elif hasattr(filename, "name"):  # assume: file object
            filename = filename.name
        elif not hasattr(filename, "seek"):  # assume file object
            raise ValueError("filename must be str, Path or file object")
        if filename == self.name and not incremental:
            raise ValueError("save to original must be incremental")
        if linear and use_objstms:
            raise ValueError("'linear' and 'use_objstms' cannot both be requested")
        if self.page_count < 1:
            raise ValueError("cannot save with zero pages")
        if incremental:
            if self.name != filename or self.stream:
                raise ValueError("incremental needs original file")
        if user_pw and len(user_pw) > 40 or owner_pw and len(owner_pw) > 40:
            raise ValueError("password length must not exceed 40")
        
        pdf = _as_pdf_document(self)
        opts = mupdf.PdfWriteOptions()
        opts.do_incremental = incremental
        opts.do_ascii = ascii
        opts.do_compress = deflate
        opts.do_compress_images = deflate_images
        opts.do_compress_fonts = deflate_fonts
        opts.do_decompress = expand
        opts.do_garbage = garbage
        opts.do_pretty = pretty
        opts.do_linear = linear
        opts.do_clean = clean
        opts.do_sanitize = clean
        opts.dont_regenerate_id = no_new_id
        opts.do_appearance = appearance
        opts.do_encrypt = encryption
        opts.permissions = permissions
        if owner_pw is not None:
            opts.opwd_utf8_set_value(owner_pw)
        elif user_pw is not None:
            opts.opwd_utf8_set_value(user_pw)
        if user_pw is not None:
            opts.upwd_utf8_set_value(user_pw)
        opts.do_preserve_metadata = preserve_metadata
        opts.do_use_objstms = use_objstms
        opts.compression_effort = compression_effort

        out = None
        pdf.m_internal.resynth_required = 0
        JM_embedded_clean(pdf)
        if no_new_id == 0:
            JM_ensure_identity(pdf)
        if isinstance(filename, str):
            #log( 'calling mupdf.pdf_save_document()')
            mupdf.pdf_save_document(pdf, filename, opts)
        else:
            out = JM_new_output_fileptr(filename)
            #log( f'{type(out)=} {type(out.this)=}')
            mupdf.pdf_write_document(pdf, out, opts)
            out.fz_close_output()
        if raise_on_repair:
            if self.is_repaired and not is_repaired_pre:
                raise Exception(f'Document save did a repair')

    def save_snapshot(self, filename):
        """Save a file snapshot suitable for journalling."""
        if self.is_closed:
            raise ValueError("doc is closed")
        if type(filename) is str:
            pass
        elif hasattr(filename, "open"):  # assume: pathlib.Path
            filename = str(filename)
        elif hasattr(filename, "name"):  # assume: file object
            filename = filename.name
        else:
            raise ValueError("filename must be str, Path or file object")
        if filename == self.name:
            raise ValueError("cannot snapshot to original")
        pdf = _as_pdf_document(self)
        mupdf.pdf_save_snapshot(pdf, filename)

    def saveIncr(self):
        """ Save PDF incrementally"""
        return self.save(self.name, incremental=True, encryption=mupdf.PDF_ENCRYPT_KEEP)

    # ------------------------------------------------------------------------------
    # Remove potentially sensitive data from a PDF. Similar to the Adobe
    # Acrobat 'sanitize' function
    # ------------------------------------------------------------------------------
    def scrub(
            doc: 'Document',
            attached_files: bool = True,
            clean_pages: bool = True,
            embedded_files: bool = True,
            hidden_text: bool = True,
            javascript: bool = True,
            metadata: bool = True,
            redactions: bool = True,
            redact_images: int = 0,
            remove_links: bool = True,
            reset_fields: bool = True,
            reset_responses: bool = True,
            thumbnails: bool = True,
            xml_metadata: bool = True,
            ) -> None:
        
        def remove_hidden(cont_lines):
            """Remove hidden text from a PDF page.

            Args:
                cont_lines: list of lines with /Contents content. Should have status
                    from after page.cleanContents().

            Returns:
                List of /Contents lines from which hidden text has been removed.

            Notes:
                The input must have been created after the page's /Contents object(s)
                have been cleaned with page.cleanContents(). This ensures a standard
                formatting: one command per line, single spaces between operators.
                This allows for drastic simplification of this code.
            """
            out_lines = []  # will return this
            in_text = False  # indicate if within BT/ET object
            suppress = False  # indicate text suppression active
            make_return = False
            for line in cont_lines:
                if line == b"BT":  # start of text object
                    in_text = True  # switch on
                    out_lines.append(line)  # output it
                    continue
                if line == b"ET":  # end of text object
                    in_text = False  # switch off
                    out_lines.append(line)  # output it
                    continue
                if line == b"3 Tr":  # text suppression operator
                    suppress = True  # switch on
                    make_return = True
                    continue
                if line[-2:] == b"Tr" and line[0] != b"3":
                    suppress = False  # text rendering changed
                    out_lines.append(line)
                    continue
                if line == b"Q":  # unstack command also switches off
                    suppress = False
                    out_lines.append(line)
                    continue
                if suppress and in_text:  # suppress hidden lines
                    continue
                out_lines.append(line)
            if make_return:
                return out_lines
            else:
                return None

        if not doc.is_pdf:  # only works for PDF
            raise ValueError("is no PDF")
        if doc.is_encrypted or doc.is_closed:
            raise ValueError("closed or encrypted doc")

        if not clean_pages:
            hidden_text = False
            redactions = False

        if metadata:
            doc.set_metadata({})  # remove standard metadata

        for page in doc:
            if reset_fields:
                # reset form fields (widgets)
                for widget in page.widgets():
                    widget.reset()

            if remove_links:
                links = page.get_links()  # list of all links on page
                for link in links:  # remove all links
                    page.delete_link(link)

            found_redacts = False
            for annot in page.annots():
                if annot.type[0] == mupdf.PDF_ANNOT_FILE_ATTACHMENT and attached_files:
                    annot.update_file(buffer_=b" ")  # set file content to empty
                if reset_responses:
                    annot.delete_responses()
                if annot.type[0] == mupdf.PDF_ANNOT_REDACT:  # pylint: disable=no-member
                    found_redacts = True

            if redactions and found_redacts:
                page.apply_redactions(images=redact_images)

            if not (clean_pages or hidden_text):
                continue  # done with the page

            page.clean_contents()
            if not page.get_contents():
                continue
            if hidden_text:
                xrefs = page.get_contents()
                assert len(xrefs) == 1  # only one because of cleaning.
                xref = xrefs[0]
                cont = doc.xref_stream(xref)
                cont_lines = remove_hidden(cont.splitlines())  # remove hidden text
                if cont_lines:  # something was actually removed
                    cont = b"\n".join(cont_lines)
                    doc.update_stream(xref, cont)  # rewrite the page /Contents

            if thumbnails:  # remove page thumbnails?
                if doc.xref_get_key(page.xref, "Thumb")[0] != "null":
                    doc.xref_set_key(page.xref, "Thumb", "null")

        # pages are scrubbed, now perform document-wide scrubbing
        # remove embedded files
        if embedded_files:
            for name in doc.embfile_names():
                doc.embfile_del(name)

        if xml_metadata:
            doc.del_xml_metadata()
        if not (xml_metadata or javascript):
            xref_limit = 0
        else:
            xref_limit = doc.xref_length()
        for xref in range(1, xref_limit):
            if not doc.xref_object(xref):
                msg = "bad xref %i - clean PDF before scrubbing" % xref
                raise ValueError(msg)
            if javascript and doc.xref_get_key(xref, "S")[1] == "/JavaScript":
                # a /JavaScript action object
                obj = "<</S/JavaScript/JS()>>"  # replace with a null JavaScript
                doc.update_object(xref, obj)  # update this object
                continue  # no further handling

            if not xml_metadata:
                continue

            if doc.xref_get_key(xref, "Type")[1] == "/Metadata":
                # delete any metadata object directly
                doc.update_object(xref, "<<>>")
                doc.update_stream(xref, b"deleted", new=True)
                continue

            if doc.xref_get_key(xref, "Metadata")[0] != "null":
                doc.xref_set_key(xref, "Metadata", "null")
    
    def search_page_for(
            doc: 'Document',
            pno: int,
            text: str,
            quads: bool = False,
            clip: rect_like = None,
            flags: int = None,
            textpage: 'TextPage' = None,
            ) -> list:
        """Search for a string on a page.

        Args:
            pno: page number
            text: string to be searched for
            clip: restrict search to this rectangle
            quads: (bool) return quads instead of rectangles
            flags: bit switches, default: join hyphened words
            textpage: reuse a prepared textpage
        Returns:
            a list of rectangles or quads, each containing an occurrence.
        """
        if flags is None:
            flags = (0
                    | TEXT_DEHYPHENATE
                    | TEXT_PRESERVE_LIGATURES
                    | TEXT_PRESERVE_WHITESPACE
                    | TEXT_MEDIABOX_CLIP
                    )
        return doc[pno].search_for(
            text,
            quads=quads,
            clip=clip,
            flags=flags,
            textpage=textpage,
        )
    
    def select(self, pyliste):
        """Build sub-pdf with page numbers in the list."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if not self.is_pdf:
            raise ValueError("is no PDF")
        if not hasattr(pyliste, "__getitem__"):
            raise ValueError("sequence required")

        valid_range = range(len(self))
        if (len(pyliste) == 0
            or min(pyliste) not in valid_range
            or max(pyliste) not in valid_range
        ):
            raise ValueError("bad page number(s)")

        # get underlying pdf document,
        pdf = _as_pdf_document(self)
        # create page sub-pdf via pdf_rearrange_pages2().
        #
        # We use PDF_CLEAN_STRUCTURE_KEEP otherwise we lose structure tree
        # which, for example, breaks test_3705.
        mupdf.pdf_rearrange_pages2(pdf, pyliste, mupdf.PDF_CLEAN_STRUCTURE_KEEP)

        # remove any existing pages with their kids
        self._reset_page_refs()

    def set_language(self, language=None):
        pdf = _as_pdf_document(self)
        if not language:
            lang = mupdf.FZ_LANG_UNSET
        else:
            lang = mupdf.fz_text_language_from_string(language)
        mupdf.pdf_set_document_language(pdf, lang)
        return True

    def set_layer(self, config, basestate=None, on=None, off=None, rbgroups=None, locked=None):
        """Set the PDF keys /ON, /OFF, /RBGroups of an OC layer."""
        if self.is_closed:
            raise ValueError("document closed")
        ocgs = set(self.get_ocgs().keys())
        if ocgs == set():
            raise ValueError("document has no optional content")

        if on:
            if type(on) not in (list, tuple):
                raise ValueError("bad type: 'on'")
            s = set(on).difference(ocgs)
            if s != set():
                raise ValueError("bad OCGs in 'on': %s" % s)

        if off:
            if type(off) not in (list, tuple):
                raise ValueError("bad type: 'off'")
            s = set(off).difference(ocgs)
            if s != set():
                raise ValueError("bad OCGs in 'off': %s" % s)

        if locked:
            if type(locked) not in (list, tuple):
                raise ValueError("bad type: 'locked'")
            s = set(locked).difference(ocgs)
            if s != set():
                raise ValueError("bad OCGs in 'locked': %s" % s)

        if rbgroups:
            if type(rbgroups) not in (list, tuple):
                raise ValueError("bad type: 'rbgroups'")
            for x in rbgroups:
                if not type(x) in (list, tuple):
                    raise ValueError("bad RBGroup '%s'" % x)
                s = set(x).difference(ocgs)
                if s != set():
                    raise ValueError("bad OCGs in RBGroup: %s" % s)

        if basestate:
            basestate = str(basestate).upper()
            if basestate == "UNCHANGED":
                basestate = "Unchanged"
            if basestate not in ("ON", "OFF", "Unchanged"):
                raise ValueError("bad 'basestate'")
        pdf = _as_pdf_document(self)
        ocp = mupdf.pdf_dict_getl(
                mupdf.pdf_trailer( pdf),
                PDF_NAME('Root'),
                PDF_NAME('OCProperties'),
                )
        if not ocp.m_internal:
            return
        if config == -1:
            obj = mupdf.pdf_dict_get( ocp, PDF_NAME('D'))
        else:
            obj = mupdf.pdf_array_get(
                    mupdf.pdf_dict_get( ocp, PDF_NAME('Configs')),
                    config,
                    )
        if not obj.m_internal:
            raise ValueError( MSG_BAD_OC_CONFIG)
        JM_set_ocg_arrays( obj, basestate, on, off, rbgroups, locked)
        mupdf.ll_pdf_read_ocg( pdf.m_internal)

    def set_layer_ui_config(self, number, action=0):
        """Set / unset OC intent configuration."""
        # The user might have given the name instead of sequence number,
        # so select by that name and continue with corresp. number
        if isinstance(number, str):
            select = [ui["number"] for ui in self.layer_ui_configs() if ui["text"] == number]
            if select == []:
                raise ValueError(f"bad OCG '{number}'.")
            number = select[0]  # this is the number for the name
        pdf = _as_pdf_document(self)
        if action == 1:
            mupdf.pdf_toggle_layer_config_ui(pdf, number)
        elif action == 2:
            mupdf.pdf_deselect_layer_config_ui(pdf, number)
        else:
            mupdf.pdf_select_layer_config_ui(pdf, number)

    def set_markinfo(self, markinfo: dict) -> bool:
        """Set the PDF MarkInfo values."""
        xref = self.pdf_catalog()
        if xref == 0:
            raise ValueError("not a PDF")
        if not markinfo or not isinstance(markinfo, dict):
            return False
        valid = {"Marked": False, "UserProperties": False, "Suspects": False}

        if not set(valid.keys()).issuperset(markinfo.keys()):
            badkeys = f"bad MarkInfo key(s): {set(markinfo.keys()).difference(valid.keys())}"
            raise ValueError(badkeys)
        pdfdict = "<<"
        valid.update(markinfo)
        for key, value in valid.items():
            value=str(value).lower()
            if value not in ("true", "false"):
                raise ValueError(f"bad key value '{key}': '{value}'")
            pdfdict += f"/{key} {value}"
        pdfdict += ">>"
        self.xref_set_key(xref, "MarkInfo", pdfdict)
        return True

    def set_metadata(doc: 'Document', m: dict = None) -> None:
        """Update the PDF /Info object.

        Args:
            m: a dictionary like doc.metadata.
        """
        if not doc.is_pdf:
            raise ValueError("is no PDF")
        if doc.is_closed or doc.is_encrypted:
            raise ValueError("document closed or encrypted")
        if m is None:
            m = {}
        elif type(m) is not dict:
            raise ValueError("bad metadata")
        keymap = {
            "author": "Author",
            "producer": "Producer",
            "creator": "Creator",
            "title": "Title",
            "format": None,
            "encryption": None,
            "creationDate": "CreationDate",
            "modDate": "ModDate",
            "subject": "Subject",
            "keywords": "Keywords",
            "trapped": "Trapped",
        }
        valid_keys = set(keymap.keys())
        diff_set = set(m.keys()).difference(valid_keys)
        if diff_set != set():
            msg = "bad dict key(s): %s" % diff_set
            raise ValueError(msg)

        t, temp = doc.xref_get_key(-1, "Info")
        if t != "xref":
            info_xref = 0
        else:
            info_xref = int(temp.replace("0 R", ""))

        if m == {} and info_xref == 0:  # nothing to do
            return

        if info_xref == 0:  # no prev metadata: get new xref
            info_xref = doc.get_new_xref()
            doc.update_object(info_xref, "<<>>")  # fill it with empty object
            doc.xref_set_key(-1, "Info", "%i 0 R" % info_xref)
        elif m == {}:  # remove existing metadata
            doc.xref_set_key(-1, "Info", "null")
            doc.init_doc()
            return

        for key, val in [(k, v) for k, v in m.items() if keymap[k] is not None]:
            pdf_key = keymap[key]
            if not bool(val) or val in ("none", "null"):
                val = "null"
            else:
                val = get_pdf_str(val)
            doc.xref_set_key(info_xref, pdf_key, val)
        doc.init_doc()
        return

    def set_oc(doc: 'Document', xref: int, oc: int) -> None:
        """Attach optional content object to image or form xobject.

        Args:
            xref: (int) xref number of an image or form xobject
            oc: (int) xref number of an OCG or OCMD
        """
        if doc.is_closed or doc.is_encrypted:
            raise ValueError("document close or encrypted")
        t, name = doc.xref_get_key(xref, "Subtype")
        if t != "name" or name not in ("/Image", "/Form"):
            raise ValueError("bad object type at xref %i" % xref)
        if oc > 0:
            t, name = doc.xref_get_key(oc, "Type")
            if t != "name" or name not in ("/OCG", "/OCMD"):
                raise ValueError("bad object type at xref %i" % oc)
        if oc == 0 and "OC" in doc.xref_get_keys(xref):
            doc.xref_set_key(xref, "OC", "null")
            return None
        doc.xref_set_key(xref, "OC", "%i 0 R" % oc)
        return None

    def set_ocmd(
            doc: 'Document',
            xref: int = 0,
            ocgs: typing.Union[list, None] = None,
            policy: OptStr = None,
            ve: typing.Union[list, None] = None,
            ) -> int:
        """Create or update an OCMD object in a PDF document.

        Args:
            xref: (int) 0 for creating a new object, otherwise update existing one.
            ocgs: (list) OCG xref numbers, which shall be subject to 'policy'.
            policy: one of 'AllOn', 'AllOff', 'AnyOn', 'AnyOff' (any casing).
            ve: (list) visibility expression. Use instead of 'ocgs' with 'policy'.

        Returns:
            Xref of the created or updated OCMD.
        """

        all_ocgs = set(doc.get_ocgs().keys())

        def ve_maker(ve):
            if type(ve) not in (list, tuple) or len(ve) < 2:
                raise ValueError("bad 've' format: %s" % ve)
            if ve[0].lower() not in ("and", "or", "not"):
                raise ValueError("bad operand: %s" % ve[0])
            if ve[0].lower() == "not" and len(ve) != 2:
                raise ValueError("bad 've' format: %s" % ve)
            item = "[/%s" % ve[0].title()
            for x in ve[1:]:
                if type(x) is int:
                    if x not in all_ocgs:
                        raise ValueError("bad OCG %i" % x)
                    item += " %i 0 R" % x
                else:
                    item += " %s" % ve_maker(x)
            item += "]"
            return item

        text = "<</Type/OCMD"

        if ocgs and type(ocgs) in (list, tuple):  # some OCGs are provided
            s = set(ocgs).difference(all_ocgs)  # contains illegal xrefs
            if s != set():
                msg = "bad OCGs: %s" % s
                raise ValueError(msg)
            text += "/OCGs[" + " ".join(map(lambda x: "%i 0 R" % x, ocgs)) + "]"

        if policy:
            policy = str(policy).lower()
            pols = {
                "anyon": "AnyOn",
                "allon": "AllOn",
                "anyoff": "AnyOff",
                "alloff": "AllOff",
            }
            if policy not in ("anyon", "allon", "anyoff", "alloff"):
                raise ValueError("bad policy: %s" % policy)
            text += "/P/%s" % pols[policy]

        if ve:
            text += "/VE%s" % ve_maker(ve)

        text += ">>"

        # make new object or replace old OCMD (check type first)
        if xref == 0:
            xref = doc.get_new_xref()
        elif "/Type/OCMD" not in doc.xref_object(xref, compressed=True):
            raise ValueError("bad xref or not an OCMD")
        doc.update_object(xref, text)
        return xref

    def set_pagelayout(self, pagelayout: str):
        """Set the PDF PageLayout value."""
        valid = ("SinglePage", "OneColumn", "TwoColumnLeft", "TwoColumnRight", "TwoPageLeft", "TwoPageRight")
        xref = self.pdf_catalog()
        if xref == 0:
            raise ValueError("not a PDF")
        if not pagelayout:
            raise ValueError("bad PageLayout value")
        if pagelayout[0] == "/":
            pagelayout = pagelayout[1:]
        for v in valid:
            if pagelayout.lower() == v.lower():
                self.xref_set_key(xref, "PageLayout", f"/{v}")
                return True
        raise ValueError("bad PageLayout value")

    def set_pagemode(self, pagemode: str):
        """Set the PDF PageMode value."""
        valid = ("UseNone", "UseOutlines", "UseThumbs", "FullScreen", "UseOC", "UseAttachments")
        xref = self.pdf_catalog()
        if xref == 0:
            raise ValueError("not a PDF")
        if not pagemode:
            raise ValueError("bad PageMode value")
        if pagemode[0] == "/":
            pagemode = pagemode[1:]
        for v in valid:
            if pagemode.lower() == v.lower():
                self.xref_set_key(xref, "PageMode", f"/{v}")
                return True
        raise ValueError("bad PageMode value")

    def set_page_labels(doc, labels):
        """Add / replace page label definitions in PDF document.

        Args:
            doc: PDF document (resp. 'self').
            labels: list of label dictionaries like:
            {'startpage': int, 'prefix': str, 'style': str, 'firstpagenum': int},
            as returned by get_page_labels().
        """
        # William Chapman, 2021-01-06

        def create_label_str(label):
            """Convert Python label dict to corresponding PDF rule string.

            Args:
                label: (dict) build rule for the label.
            Returns:
                PDF label rule string wrapped in "<<", ">>".
            """
            s = "%i<<" % label["startpage"]
            if label.get("prefix", "") != "":
                s += "/P(%s)" % label["prefix"]
            if label.get("style", "") != "":
                s += "/S/%s" % label["style"]
            if label.get("firstpagenum", 1) > 1:
                s += "/St %i" % label["firstpagenum"]
            s += ">>"
            return s

        def create_nums(labels):
            """Return concatenated string of all labels rules.

            Args:
                labels: (list) dictionaries as created by function 'rule_dict'.
            Returns:
                PDF compatible string for page label definitions, ready to be
                enclosed in PDF array 'Nums[...]'.
            """
            labels.sort(key=lambda x: x["startpage"])
            s = "".join([create_label_str(label) for label in labels])
            return s

        doc._set_page_labels(create_nums(labels))

    def set_toc(
            doc: 'Document',
            toc: list,
            collapse: int = 1,
            ) -> int:
        """Create new outline tree (table of contents, TOC).

        Args:
            toc: (list, tuple) each entry must contain level, title, page and
                optionally top margin on the page. None or '()' remove the TOC.
            collapse: (int) collapses entries beyond this level. Zero or None
                shows all entries unfolded.
        Returns:
            the number of inserted items, or the number of removed items respectively.
        """
        if doc.is_closed or doc.is_encrypted:
            raise ValueError("document closed or encrypted")
        if not doc.is_pdf:
            raise ValueError("is no PDF")
        if not toc:  # remove all entries
            return len(doc._delToC())

        # validity checks --------------------------------------------------------
        if type(toc) not in (list, tuple):
            raise ValueError("'toc' must be list or tuple")
        toclen = len(toc)
        page_count = doc.page_count
        t0 = toc[0]
        if type(t0) not in (list, tuple):
            raise ValueError("items must be sequences of 3 or 4 items")
        if t0[0] != 1:
            raise ValueError("hierarchy level of item 0 must be 1")
        for i in list(range(toclen - 1)):
            t1 = toc[i]
            t2 = toc[i + 1]
            if not -1 <= t1[2] <= page_count:
                raise ValueError("row %i: page number out of range" % i)
            if (type(t2) not in (list, tuple)) or len(t2) not in (3, 4):
                raise ValueError("bad row %i" % (i + 1))
            if (type(t2[0]) is not int) or t2[0] < 1:
                raise ValueError("bad hierarchy level in row %i" % (i + 1))
            if t2[0] > t1[0] + 1:
                raise ValueError("bad hierarchy level in row %i" % (i + 1))
        # no formal errors in toc --------------------------------------------------

        # --------------------------------------------------------------------------
        # make a list of xref numbers, which we can use for our TOC entries
        # --------------------------------------------------------------------------
        old_xrefs = doc._delToC()  # del old outlines, get their xref numbers

        # prepare table of xrefs for new bookmarks
        old_xrefs = []
        xref = [0] + old_xrefs
        xref[0] = doc._getOLRootNumber()  # entry zero is outline root xref number
        if toclen > len(old_xrefs):  # too few old xrefs?
            for i in range((toclen - len(old_xrefs))):
                xref.append(doc.get_new_xref())  # acquire new ones

        lvltab = {0: 0}  # to store last entry per hierarchy level

        # ------------------------------------------------------------------------------
        # contains new outline objects as strings - first one is the outline root
        # ------------------------------------------------------------------------------
        olitems = [{"count": 0, "first": -1, "last": -1, "xref": xref[0]}]
        # ------------------------------------------------------------------------------
        # build olitems as a list of PDF-like connected dictionaries
        # ------------------------------------------------------------------------------
        for i in range(toclen):
            o = toc[i]
            lvl = o[0]  # level
            title = get_pdf_str(o[1])  # title
            pno = min(doc.page_count - 1, max(0, o[2] - 1))  # page number
            page_xref = doc.page_xref(pno)
            page_height = doc.page_cropbox(pno).height
            top = Point(72, page_height - 36)
            dest_dict = {"to": top, "kind": LINK_GOTO}  # fall back target
            if o[2] < 0:
                dest_dict["kind"] = LINK_NONE
            if len(o) > 3:  # some target is specified
                if type(o[3]) in (int, float):  # convert a number to a point
                    dest_dict["to"] = Point(72, page_height - o[3])
                else:  # if something else, make sure we have a dict
                    # We make a copy of o[3] to avoid modifying our caller's data.
                    dest_dict = o[3].copy() if type(o[3]) is dict else dest_dict
                    if "to" not in dest_dict:  # target point not in dict?
                        dest_dict["to"] = top  # put default in
                    else:  # transform target to PDF coordinates
                        page = doc[pno]
                        point = Point(dest_dict["to"])
                        point.y = page.cropbox.height - point.y
                        point = point * page.rotation_matrix
                        dest_dict["to"] = (point.x, point.y)
            d = {}
            d["first"] = -1
            d["count"] = 0
            d["last"] = -1
            d["prev"] = -1
            d["next"] = -1
            d["dest"] = utils.getDestStr(page_xref, dest_dict)
            d["top"] = dest_dict["to"]
            d["title"] = title
            d["parent"] = lvltab[lvl - 1]
            d["xref"] = xref[i + 1]
            d["color"] = dest_dict.get("color")
            d["flags"] = dest_dict.get("italic", 0) + 2 * dest_dict.get("bold", 0)
            lvltab[lvl] = i + 1
            parent = olitems[lvltab[lvl - 1]]  # the parent entry

            if (
                dest_dict.get("collapse") or collapse and lvl > collapse
            ):  # suppress expansion
                parent["count"] -= 1  # make /Count negative
            else:
                parent["count"] += 1  # positive /Count

            if parent["first"] == -1:
                parent["first"] = i + 1
                parent["last"] = i + 1
            else:
                d["prev"] = parent["last"]
                prev = olitems[parent["last"]]
                prev["next"] = i + 1
                parent["last"] = i + 1
            olitems.append(d)

        # ------------------------------------------------------------------------------
        # now create each outline item as a string and insert it in the PDF
        # ------------------------------------------------------------------------------
        for i, ol in enumerate(olitems):
            txt = "<<"
            if ol["count"] != 0:
                txt += "/Count %i" % ol["count"]
            try:
                txt += ol["dest"]
            except Exception:
                # Verbose in PyMuPDF/tests.
                if g_exceptions_verbose >= 2:   exception_info()
                pass
            try:
                if ol["first"] > -1:
                    txt += "/First %i 0 R" % xref[ol["first"]]
            except Exception:
                if g_exceptions_verbose >= 2:   exception_info()
                pass
            try:
                if ol["last"] > -1:
                    txt += "/Last %i 0 R" % xref[ol["last"]]
            except Exception:
                if g_exceptions_verbose >= 2:   exception_info()
                pass
            try:
                if ol["next"] > -1:
                    txt += "/Next %i 0 R" % xref[ol["next"]]
            except Exception:
                # Verbose in PyMuPDF/tests.
                if g_exceptions_verbose >= 2:   exception_info()
                pass
            try:
                if ol["parent"] > -1:
                    txt += "/Parent %i 0 R" % xref[ol["parent"]]
            except Exception:
                # Verbose in PyMuPDF/tests.
                if g_exceptions_verbose >= 2:   exception_info()
                pass
            try:
                if ol["prev"] > -1:
                    txt += "/Prev %i 0 R" % xref[ol["prev"]]
            except Exception:
                # Verbose in PyMuPDF/tests.
                if g_exceptions_verbose >= 2:   exception_info()
                pass
            try:
                txt += "/Title" + ol["title"]
            except Exception:
                # Verbose in PyMuPDF/tests.
                if g_exceptions_verbose >= 2:   exception_info()
                pass

            if ol.get("color") and len(ol["color"]) == 3:
                txt += f"/C[ {_format_g(tuple(ol['color']))}]"
            if ol.get("flags", 0) > 0:
                txt += "/F %i" % ol["flags"]

            if i == 0:  # special: this is the outline root
                txt += "/Type/Outlines"  # so add the /Type entry
            txt += ">>"
            doc.update_object(xref[i], txt)  # insert the PDF object

        doc.init_doc()
        return toclen

    def set_toc_item(
            doc: 'Document',
            idx: int,
            dest_dict: OptDict = None,
            kind: OptInt = None,
            pno: OptInt = None,
            uri: OptStr = None,
            title: OptStr = None,
            to: point_like = None,
            filename: OptStr = None,
            zoom: float = 0,
            ) -> None:
        """Update TOC item by index.

        It allows changing the item's title and link destination.

        Args:
            idx:
                (int) desired index of the TOC list, as created by get_toc.
            dest_dict:
                (dict) destination dictionary as created by get_toc(False).
                Outrules all other parameters. If None, the remaining parameters
                are used to make a dest dictionary.
            kind:
                (int) kind of link (pymupdf.LINK_GOTO, etc.). If None, then only
                the title will be updated. If pymupdf.LINK_NONE, the TOC item will
                be deleted.
            pno:
                (int) page number (1-based like in get_toc). Required if
                pymupdf.LINK_GOTO.
            uri:
                (str) the URL, required if pymupdf.LINK_URI.
            title:
                (str) the new title. No change if None.
            to:
                (point-like) destination on the target page. If omitted, (72, 36)
                will be used as target coordinates.
            filename:
                (str) destination filename, required for pymupdf.LINK_GOTOR and
                pymupdf.LINK_LAUNCH.
            name:
                (str) a destination name for pymupdf.LINK_NAMED.
            zoom:
                (float) a zoom factor for the target location (pymupdf.LINK_GOTO).
        """
        xref = doc.get_outline_xrefs()[idx]
        page_xref = 0
        if type(dest_dict) is dict:
            if dest_dict["kind"] == LINK_GOTO:
                pno = dest_dict["page"]
                page_xref = doc.page_xref(pno)
                page_height = doc.page_cropbox(pno).height
                to = dest_dict.get('to', Point(72, 36))
                to.y = page_height - to.y
                dest_dict["to"] = to
            action = utils.getDestStr(page_xref, dest_dict)
            if not action.startswith("/A"):
                raise ValueError("bad bookmark dest")
            color = dest_dict.get("color")
            if color:
                color = list(map(float, color))
                if len(color) != 3 or min(color) < 0 or max(color) > 1:
                    raise ValueError("bad color value")
            bold = dest_dict.get("bold", False)
            italic = dest_dict.get("italic", False)
            flags = italic + 2 * bold
            collapse = dest_dict.get("collapse")
            return doc._update_toc_item(
                xref,
                action=action[2:],
                title=title,
                color=color,
                flags=flags,
                collapse=collapse,
            )

        if kind == LINK_NONE:  # delete bookmark item
            return doc.del_toc_item(idx)
        if kind is None and title is None:  # treat as no-op
            return None
        if kind is None:  # only update title text
            return doc._update_toc_item(xref, action=None, title=title)

        if kind == LINK_GOTO:
            if pno is None or pno not in range(1, doc.page_count + 1):
                raise ValueError("bad page number")
            page_xref = doc.page_xref(pno - 1)
            page_height = doc.page_cropbox(pno - 1).height
            if to is None:
                to = Point(72, page_height - 36)
            else:
                to = Point(to)
                to.y = page_height - to.y

        ddict = {
            "kind": kind,
            "to": to,
            "uri": uri,
            "page": pno,
            "file": filename,
            "zoom": zoom,
        }
        action = utils.getDestStr(page_xref, ddict)
        if action == "" or not action.startswith("/A"):
            raise ValueError("bad bookmark dest")

        return doc._update_toc_item(xref, action=action[2:], title=title)

    def set_xml_metadata(self, metadata):
        """Store XML document level metadata."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        root = mupdf.pdf_dict_get( mupdf.pdf_trailer( pdf), PDF_NAME('Root'))
        if not root.m_internal:
            RAISEPY( MSG_BAD_PDFROOT, JM_Exc_FileDataError)
        res = mupdf.fz_new_buffer_from_copied_data( metadata.encode('utf-8'))
        xml = mupdf.pdf_dict_get( root, PDF_NAME('Metadata'))
        if xml.m_internal:
            JM_update_stream( pdf, xml, res, 0)
        else:
            xml = mupdf.pdf_add_stream( pdf, res, mupdf.PdfObj(), 0)
            mupdf.pdf_dict_put( xml, PDF_NAME('Type'), PDF_NAME('Metadata'))
            mupdf.pdf_dict_put( xml, PDF_NAME('Subtype'), PDF_NAME('XML'))
            mupdf.pdf_dict_put( root, PDF_NAME('Metadata'), xml)

    def subset_fonts(doc: 'Document', verbose: bool = False, fallback: bool = False) -> OptInt:
        """Build font subsets in a PDF.

        Eligible fonts are potentially replaced by smaller versions. Page text is
        NOT rewritten and thus should retain properties like being hidden or
        controlled by optional content.

        This method by default uses MuPDF's own internal feature to create subset
        fonts. As this is a new function, errors may still occur. In this case,
        please fall back to using the previous version by using "fallback=True".
        Fallback mode requires the external package 'fontTools'.

        Args:
            fallback: use the older deprecated implementation.
            verbose: only used by fallback mode.

        Returns:
            The new MuPDF-based code returns None.  The deprecated fallback
            mode returns 0 if there are no fonts to subset.  Otherwise, it
            returns the decrease in fontsize (the difference in fontsize),
            measured in bytes.
        """
        # Font binaries: -  "buffer" -> (names, xrefs, (unicodes, glyphs))
        # An embedded font is uniquely defined by its fontbuffer only. It may have
        # multiple names and xrefs.
        # Once the sets of used unicodes and glyphs are known, we compute a
        # smaller version of the buffer user package fontTools.

        if not fallback:  # by default use MuPDF function
            pdf = mupdf.pdf_document_from_fz_document(doc)
            mupdf.pdf_subset_fonts2(pdf, list(range(doc.page_count)))
            return

        font_buffers = {}

        def get_old_widths(xref):
            """Retrieve old font '/W' and '/DW' values."""
            df = doc.xref_get_key(xref, "DescendantFonts")
            if df[0] != "array":  # only handle xref specifications
                return None, None
            df_xref = int(df[1][1:-1].replace("0 R", ""))
            widths = doc.xref_get_key(df_xref, "W")
            if widths[0] != "array":  # no widths key found
                widths = None
            else:
                widths = widths[1]
            dwidths = doc.xref_get_key(df_xref, "DW")
            if dwidths[0] != "int":
                dwidths = None
            else:
                dwidths = dwidths[1]
            return widths, dwidths

        def set_old_widths(xref, widths, dwidths):
            """Restore the old '/W' and '/DW' in subsetted font.

            If either parameter is None or evaluates to False, the corresponding
            dictionary key will be set to null.
            """
            df = doc.xref_get_key(xref, "DescendantFonts")
            if df[0] != "array":  # only handle xref specs
                return None
            df_xref = int(df[1][1:-1].replace("0 R", ""))
            if (type(widths) is not str or not widths) and doc.xref_get_key(df_xref, "W")[
                0
            ] != "null":
                doc.xref_set_key(df_xref, "W", "null")
            else:
                doc.xref_set_key(df_xref, "W", widths)
            if (type(dwidths) is not str or not dwidths) and doc.xref_get_key(
                df_xref, "DW"
            )[0] != "null":
                doc.xref_set_key(df_xref, "DW", "null")
            else:
                doc.xref_set_key(df_xref, "DW", dwidths)
            return None

        def set_subset_fontname(new_xref):
            """Generate a name prefix to tag a font as subset.

            We use a random generator to select 6 upper case ASCII characters.
            The prefixed name must be put in the font xref as the "/BaseFont" value
            and in the FontDescriptor object as the '/FontName' value.
            """
            # The following generates a prefix like 'ABCDEF+'
            import random
            import string
            prefix = "".join(random.choices(tuple(string.ascii_uppercase), k=6)) + "+"
            font_str = doc.xref_object(new_xref, compressed=True)
            font_str = font_str.replace("/BaseFont/", "/BaseFont/" + prefix)
            df = doc.xref_get_key(new_xref, "DescendantFonts")
            if df[0] == "array":
                df_xref = int(df[1][1:-1].replace("0 R", ""))
                fd = doc.xref_get_key(df_xref, "FontDescriptor")
                if fd[0] == "xref":
                    fd_xref = int(fd[1].replace("0 R", ""))
                    fd_str = doc.xref_object(fd_xref, compressed=True)
                    fd_str = fd_str.replace("/FontName/", "/FontName/" + prefix)
                    doc.update_object(fd_xref, fd_str)
            doc.update_object(new_xref, font_str)

        def build_subset(buffer, unc_set, gid_set):
            """Build font subset using fontTools.

            Args:
                buffer: (bytes) the font given as a binary buffer.
                unc_set: (set) required glyph ids.
            Returns:
                Either None if subsetting is unsuccessful or the subset font buffer.
            """
            try:
                import fontTools.subset as fts
            except ImportError:
                if g_exceptions_verbose:    exception_info()
                message("This method requires fontTools to be installed.")
                raise
            import tempfile
            with tempfile.TemporaryDirectory() as tmp_dir:
                oldfont_path = f"{tmp_dir}/oldfont.ttf"
                newfont_path = f"{tmp_dir}/newfont.ttf"
                uncfile_path = f"{tmp_dir}/uncfile.txt"
                args = [
                    oldfont_path,
                    "--retain-gids",
                    f"--output-file={newfont_path}",
                    "--layout-features=*",
                    "--passthrough-tables",
                    "--ignore-missing-glyphs",
                    "--ignore-missing-unicodes",
                    "--symbol-cmap",
                ]

                # store glyph ids or unicodes as file
                with io.open(f"{tmp_dir}/uncfile.txt", "w", encoding='utf8') as unc_file:
                    if 0xFFFD in unc_set:  # error unicode exists -> use glyphs
                        args.append(f"--gids-file={uncfile_path}")
                        gid_set.add(189)
                        unc_list = list(gid_set)
                        for unc in unc_list:
                            unc_file.write("%i\n" % unc)
                    else:
                        args.append(f"--unicodes-file={uncfile_path}")
                        unc_set.add(255)
                        unc_list = list(unc_set)
                        for unc in unc_list:
                            unc_file.write("%04x\n" % unc)

                # store fontbuffer as a file
                with io.open(oldfont_path, "wb") as fontfile:
                    fontfile.write(buffer)
                try:
                    os.remove(newfont_path)  # remove old file
                except Exception:
                    pass
                try:  # invoke fontTools subsetter
                    fts.main(args)
                    font = Font(fontfile=newfont_path)
                    new_buffer = font.buffer  # subset font binary
                    if font.glyph_count == 0:  # intercept empty font
                        new_buffer = None
                except Exception:
                    exception_info()
                    new_buffer = None
            return new_buffer

        def repl_fontnames(doc):
            """Populate 'font_buffers'.

            For each font candidate, store its xref and the list of names
            by which PDF text may refer to it (there may be multiple).
            """

            def norm_name(name):
                """Recreate font name that contains PDF hex codes.

                E.g. #20 -> space, chr(32)
                """
                while "#" in name:
                    p = name.find("#")
                    c = int(name[p + 1 : p + 3], 16)
                    name = name.replace(name[p : p + 3], chr(c))
                return name

            def get_fontnames(doc, item):
                """Return a list of fontnames for an item of page.get_fonts().

                There may be multiple names e.g. for Type0 fonts.
                """
                fontname = item[3]
                names = [fontname]
                fontname = doc.xref_get_key(item[0], "BaseFont")[1][1:]
                fontname = norm_name(fontname)
                if fontname not in names:
                    names.append(fontname)
                descendents = doc.xref_get_key(item[0], "DescendantFonts")
                if descendents[0] != "array":
                    return names
                descendents = descendents[1][1:-1]
                if descendents.endswith(" 0 R"):
                    xref = int(descendents[:-4])
                    descendents = doc.xref_object(xref, compressed=True)
                p1 = descendents.find("/BaseFont")
                if p1 >= 0:
                    p2 = descendents.find("/", p1 + 1)
                    p1 = min(descendents.find("/", p2 + 1), descendents.find(">>", p2 + 1))
                    fontname = descendents[p2 + 1 : p1]
                    fontname = norm_name(fontname)
                    if fontname not in names:
                        names.append(fontname)
                return names

            for i in range(doc.page_count):
                for f in doc.get_page_fonts(i, full=True):
                    font_xref = f[0]  # font xref
                    font_ext = f[1]  # font file extension
                    basename = f[3]  # font basename

                    if font_ext not in (  # skip if not supported by fontTools
                        "otf",
                        "ttf",
                        "woff",
                        "woff2",
                    ):
                        continue
                    # skip fonts which already are subsets
                    if len(basename) > 6 and basename[6] == "+":
                        continue

                    extr = doc.extract_font(font_xref)
                    fontbuffer = extr[-1]
                    names = get_fontnames(doc, f)
                    name_set, xref_set, subsets = font_buffers.get(
                        fontbuffer, (set(), set(), (set(), set()))
                    )
                    xref_set.add(font_xref)
                    for name in names:
                        name_set.add(name)
                    font = Font(fontbuffer=fontbuffer)
                    name_set.add(font.name)
                    del font
                    font_buffers[fontbuffer] = (name_set, xref_set, subsets)

        def find_buffer_by_name(name):
            for buffer, (name_set, _, _) in font_buffers.items():
                if name in name_set:
                    return buffer
            return None

        # -----------------
        # main function
        # -----------------
        repl_fontnames(doc)  # populate font information
        if not font_buffers:  # nothing found to do
            if verbose:
                message(f'No fonts to subset.')
            return 0

        old_fontsize = 0
        new_fontsize = 0
        for fontbuffer in font_buffers.keys():
            old_fontsize += len(fontbuffer)

        # Scan page text for usage of subsettable fonts
        for page in doc:
            # go through the text and extend set of used glyphs by font
            # we use a modified MuPDF trace device, which delivers us glyph ids.
            for span in page.get_texttrace():
                if type(span) is not dict:  # skip useless information
                    continue
                fontname = span["font"][:33]  # fontname for the span
                buffer = find_buffer_by_name(fontname)
                if buffer is None:
                    continue
                name_set, xref_set, (set_ucs, set_gid) = font_buffers[buffer]
                for c in span["chars"]:
                    set_ucs.add(c[0])  # unicode
                    set_gid.add(c[1])  # glyph id
                font_buffers[buffer] = (name_set, xref_set, (set_ucs, set_gid))

        # build the font subsets
        for old_buffer, (name_set, xref_set, subsets) in font_buffers.items():
            new_buffer = build_subset(old_buffer, subsets[0], subsets[1])
            fontname = list(name_set)[0]
            if new_buffer is None or len(new_buffer) >= len(old_buffer):
                # subset was not created or did not get smaller
                if verbose:
                    message(f'Cannot subset {fontname!r}.')
                continue
            if verbose:
                message(f"Built subset of font {fontname!r}.")
            val = doc._insert_font(fontbuffer=new_buffer)  # store subset font in PDF
            new_xref = val[0]  # get its xref
            set_subset_fontname(new_xref)  # tag fontname as subset font
            font_str = doc.xref_object(  # get its object definition
                new_xref,
                compressed=True,
            )
            # walk through the original font xrefs and replace each by the subset def
            for font_xref in xref_set:
                # we need the original '/W' and '/DW' width values
                width_table, def_width = get_old_widths(font_xref)
                # ... and replace original font definition at xref with it
                doc.update_object(font_xref, font_str)
                # now copy over old '/W' and '/DW' values
                if width_table or def_width:
                    set_old_widths(font_xref, width_table, def_width)
            # 'new_xref' remains unused in the PDF and must be removed
            # by garbage collection.
            new_fontsize += len(new_buffer)

        return old_fontsize - new_fontsize

    def switch_layer(self, config, as_default=0):
        """Activate an OC layer."""
        pdf = _as_pdf_document(self)
        cfgs = mupdf.pdf_dict_getl(
                mupdf.pdf_trailer( pdf),
                PDF_NAME('Root'),
                PDF_NAME('OCProperties'),
                PDF_NAME('Configs')
                )
        if not mupdf.pdf_is_array( cfgs) or not mupdf.pdf_array_len( cfgs):
            if config < 1:
                return
            raise ValueError( MSG_BAD_OC_LAYER)
        if config < 0:
            return
        mupdf.pdf_select_layer_config( pdf, config)
        if as_default:
            mupdf.pdf_set_layer_config_as_default( pdf)
            mupdf.ll_pdf_read_ocg( pdf.m_internal)

    def update_object(self, xref, text, page=None):
        """Replace object definition source."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        xreflen = mupdf.pdf_xref_len(pdf)
        if not _INRANGE(xref, 1, xreflen-1):
            RAISEPY("bad xref", MSG_BAD_XREF)
        ENSURE_OPERATION(pdf)
        # create new object with passed-in string
        new_obj = JM_pdf_obj_from_str(pdf, text)
        mupdf.pdf_update_object(pdf, xref, new_obj)
        if page:
            JM_refresh_links( _as_pdf_page(page))

    def update_stream(self, xref=0, stream=None, new=1, compress=1):
        """Replace xref stream part."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        xreflen = mupdf.pdf_xref_len(pdf)
        if xref < 1 or xref > xreflen:
            raise ValueError( MSG_BAD_XREF)
        # get the object
        obj = mupdf.pdf_new_indirect(pdf, xref, 0)
        if not mupdf.pdf_is_dict(obj):
            raise ValueError( MSG_IS_NO_DICT)
        res = JM_BufferFromBytes(stream)
        if not res.m_internal:
            raise TypeError( MSG_BAD_BUFFER)
        JM_update_stream(pdf, obj, res, compress)
        pdf.dirty = 1

    @property
    def version_count(self):
        '''
        Count versions of PDF document.
        '''
        pdf = _as_pdf_document(self, required=0)
        if pdf.m_internal:
            return mupdf.pdf_count_versions(pdf)
        return 0

    def write(
            self,
            garbage=False,
            clean=False,
            deflate=False,
            deflate_images=False,
            deflate_fonts=False,
            incremental=False,
            ascii=False,
            expand=False,
            linear=False,
            no_new_id=False,
            appearance=False,
            pretty=False,
            encryption=1,
            permissions=4095,
            owner_pw=None,
            user_pw=None,
            preserve_metadata=1,
            use_objstms=0,
            compression_effort=0,
            raise_on_repair=False,
    ):
        from io import BytesIO
        bio = BytesIO()
        self.save(
                bio,
                garbage=garbage,
                clean=clean,
                no_new_id=no_new_id,
                appearance=appearance,
                deflate=deflate,
                deflate_images=deflate_images,
                deflate_fonts=deflate_fonts,
                incremental=incremental,
                ascii=ascii,
                expand=expand,
                linear=linear,
                pretty=pretty,
                encryption=encryption,
                permissions=permissions,
                owner_pw=owner_pw,
                user_pw=user_pw,
                preserve_metadata=preserve_metadata,
                use_objstms=use_objstms,
                compression_effort=compression_effort,
                raise_on_repair=raise_on_repair,
        )
        return bio.getvalue()
    
    def tobytes(self, *args, **kwargs):
        return self.write(*args, **kwargs)

    @property
    def xref(self):
        """PDF xref number of page."""
        CheckParent(self)
        return self.parent.page_xref(self.number)

    def xref_copy(doc: 'Document', source: int, target: int, *, keep: list = None) -> None:
        """Copy a PDF dictionary object to another one given their xref numbers.

        Args:
            doc: PDF document object
            source: source xref number
            target: target xref number, the xref must already exist
            keep: an optional list of 1st level keys in target that should not be
                  removed before copying.
        Notes:
            This works similar to the copy() method of dictionaries in Python. The
            source may be a stream object.
        """
        if doc.xref_is_stream(source):
            # read new xref stream, maintaining compression
            stream = doc.xref_stream_raw(source)
            doc.update_stream(
                target,
                stream,
                compress=False,  # keeps source compression
                new=True,  # in case target is no stream
            )

        # empty the target completely, observe exceptions
        if keep is None:
            keep = []
        for key in doc.xref_get_keys(target):
            if key in keep:
                continue
            doc.xref_set_key(target, key, "null")
        # copy over all source dict items
        for key in doc.xref_get_keys(source):
            item = doc.xref_get_key(source, key)
            doc.xref_set_key(target, key, item[1])
    
    def xref_get_key(self, xref, key):
        """Get PDF dict key value of object at 'xref'."""
        pdf = _as_pdf_document(self)
        xreflen = mupdf.pdf_xref_len(pdf)
        if not _INRANGE(xref, 1, xreflen-1) and xref != -1:
            raise ValueError( MSG_BAD_XREF)
        if xref > 0:
            obj = mupdf.pdf_load_object(pdf, xref)
        else:
            obj = mupdf.pdf_trailer(pdf)
        if not obj.m_internal:
            return ("null", "null")
        subobj = mupdf.pdf_dict_getp(obj, key)
        if not subobj.m_internal:
            return ("null", "null")
        text = None
        if mupdf.pdf_is_indirect(subobj):
            type = "xref"
            text = "%i 0 R" % mupdf.pdf_to_num(subobj)
        elif mupdf.pdf_is_array(subobj):
            type = "array"
        elif mupdf.pdf_is_dict(subobj):
            type = "dict"
        elif mupdf.pdf_is_int(subobj):
            type = "int"
            text = "%i" % mupdf.pdf_to_int(subobj)
        elif mupdf.pdf_is_real(subobj):
            type = "float"
        elif mupdf.pdf_is_null(subobj):
            type = "null"
            text = "null"
        elif mupdf.pdf_is_bool(subobj):
            type = "bool"
            if mupdf.pdf_to_bool(subobj):
                text = "true"
            else:
                text = "false"
        elif mupdf.pdf_is_name(subobj):
            type = "name"
            text = "/%s" % mupdf.pdf_to_name(subobj)
        elif mupdf.pdf_is_string(subobj):
            type = "string"
            text = JM_UnicodeFromStr(mupdf.pdf_to_text_string(subobj))
        else:
            type = "unknown"
        if text is None:
            res = JM_object_to_buffer(subobj, 1, 0)
            text = JM_UnicodeFromBuffer(res)
        return (type, text)

    def xref_get_keys(self, xref):
        """Get the keys of PDF dict object at 'xref'. Use -1 for the PDF trailer."""
        pdf = _as_pdf_document(self)
        xreflen = mupdf.pdf_xref_len( pdf)
        if not _INRANGE(xref, 1, xreflen-1) and xref != -1:
            raise ValueError( MSG_BAD_XREF)
        if xref > 0:
            obj = mupdf.pdf_load_object( pdf, xref)
        else:
            obj = mupdf.pdf_trailer( pdf)
        n = mupdf.pdf_dict_len( obj)
        rc = []
        if n == 0:
            return rc
        for i in range(n):
            key = mupdf.pdf_to_name( mupdf.pdf_dict_get_key( obj, i))
            rc.append(key)
        return rc

    def xref_is_font(self, xref):
        """Check if xref is a font object."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if self.xref_get_key(xref, "Type")[1] == "/Font":
            return True
        return False

    def xref_is_image(self, xref):
        """Check if xref is an image object."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if self.xref_get_key(xref, "Subtype")[1] == "/Image":
            return True
        return False

    def xref_is_stream(self, xref=0):
        """Check if xref is a stream object."""
        pdf = _as_pdf_document(self, required=0)
        if not pdf.m_internal:
            return False    # not a PDF
        return bool(mupdf.pdf_obj_num_is_stream(pdf, xref))

    def xref_is_xobject(self, xref):
        """Check if xref is a form xobject."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        if self.xref_get_key(xref, "Subtype")[1] == "/Form":
            return True
        return False

    def xref_length(self):
        """Get length of xref table."""
        xreflen = 0
        pdf = _as_pdf_document(self, required=0)
        if pdf.m_internal:
            xreflen = mupdf.pdf_xref_len(pdf)
        return xreflen

    def xref_object(self, xref, compressed=0, ascii=0):
        """Get xref object source as a string."""
        if self.is_closed:
            raise ValueError("document closed")
        if g_use_extra:
            ret = extra.xref_object( self.this, xref, compressed, ascii)
            return ret
        pdf = _as_pdf_document(self)
        xreflen = mupdf.pdf_xref_len(pdf)
        if not _INRANGE(xref, 1, xreflen-1) and xref != -1:
            raise ValueError( MSG_BAD_XREF)
        if xref > 0:
            obj = mupdf.pdf_load_object(pdf, xref)
        else:
            obj = mupdf.pdf_trailer(pdf)
        res = JM_object_to_buffer(mupdf.pdf_resolve_indirect(obj), compressed, ascii)
        text = JM_EscapeStrFromBuffer(res)
        return text

    def xref_set_key(self, xref, key, value):
        """Set the value of a PDF dictionary key."""
        if self.is_closed:
            raise ValueError("document closed")

        if not key or not isinstance(key, str) or INVALID_NAME_CHARS.intersection(key) not in (set(), {"/"}):
            raise ValueError("bad 'key'")
        if not isinstance(value, str) or not value or value[0] == "/" and INVALID_NAME_CHARS.intersection(value[1:]) != set():
            raise ValueError("bad 'value'")

        pdf = _as_pdf_document(self)
        xreflen = mupdf.pdf_xref_len(pdf)
        #if not _INRANGE(xref, 1, xreflen-1) and xref != -1:
        #    THROWMSG("bad xref")
        #if len(value) == 0:
        #    THROWMSG("bad 'value'")
        #if len(key) == 0:
        #    THROWMSG("bad 'key'")
        if not _INRANGE(xref, 1, xreflen-1) and xref != -1:
            raise ValueError( MSG_BAD_XREF)
        if xref != -1:
            obj = mupdf.pdf_load_object(pdf, xref)
        else:
            obj = mupdf.pdf_trailer(pdf)
        new_obj = JM_set_object_value(obj, key, value)
        if not new_obj.m_internal:
            return  # did not work: skip update
        if xref != -1:
            mupdf.pdf_update_object(pdf, xref, new_obj)
        else:
            n = mupdf.pdf_dict_len(new_obj)
            for i in range(n):
                mupdf.pdf_dict_put(
                        obj,
                        mupdf.pdf_dict_get_key(new_obj, i),
                        mupdf.pdf_dict_get_val(new_obj, i),
                        )

    def xref_stream(self, xref):
        """Get decompressed xref stream."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        xreflen = mupdf.pdf_xref_len( pdf)
        if not _INRANGE(xref, 1, xreflen-1) and xref != -1:
            raise ValueError( MSG_BAD_XREF)
        if xref >= 0:
            obj = mupdf.pdf_new_indirect( pdf, xref, 0)
        else:
            obj = mupdf.pdf_trailer( pdf)
        r = None
        if mupdf.pdf_is_stream( obj):
            res = mupdf.pdf_load_stream_number( pdf, xref)
            r = JM_BinFromBuffer( res)
        return r

    def xref_stream_raw(self, xref):
        """Get xref stream without decompression."""
        if self.is_closed or self.is_encrypted:
            raise ValueError("document closed or encrypted")
        pdf = _as_pdf_document(self)
        xreflen = mupdf.pdf_xref_len( pdf)
        if not _INRANGE(xref, 1, xreflen-1) and xref != -1:
            raise ValueError( MSG_BAD_XREF)
        if xref >= 0:
            obj = mupdf.pdf_new_indirect( pdf, xref, 0)
        else:
            obj = mupdf.pdf_trailer( pdf)
        r = None
        if mupdf.pdf_is_stream( obj):
            res = mupdf.pdf_load_raw_stream_number( pdf, xref)
            r = JM_BinFromBuffer( res)
        return r

    def xref_xml_metadata(self):
        """Get xref of document XML metadata."""
        pdf = _as_pdf_document(self)
        root = mupdf.pdf_dict_get( mupdf.pdf_trailer( pdf), PDF_NAME('Root'))
        if not root.m_internal:
            RAISEPY( MSG_BAD_PDFROOT, JM_Exc_FileDataError)
        xml = mupdf.pdf_dict_get( root, PDF_NAME('Metadata'))
        xref = 0
        if xml.m_internal:
            xref = mupdf.pdf_to_num( xml)
        return xref
    
    __slots__ = ('this', 'page_count2', 'this_is_pdf', '__dict__')
    
    outline = property(lambda self: self._outline)
    is_stream = xref_is_stream

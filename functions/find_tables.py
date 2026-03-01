"""
Function: fitz.find_tables
Signature: find_tables(page, clip=None, vertical_strategy: str = 'lines', horizontal_strategy: str = 'lines', vertical_lines: list = None, horizontal_lines: list = None, snap_tolerance: float = 3, snap_x_tolerance: float = None, snap_y_tolerance: float = None, join_tolerance: float = 3, join_x_tolerance: float = None, join_y_tolerance: float = None, edge_min_length: float = 3, min_words_vertical: float = 3, min_words_horizontal: float = 1, intersection_tolerance: float = 3, intersection_x_tolerance: float = None, intersection_y_tolerance: float = None, text_tolerance=3, text_x_tolerance=3, text_y_tolerance=3, strategy=None, add_lines=None, add_boxes=None, paths=None)
Description: No docstring available.
"""

import fitz

# Source code of fitz.find_tables:
def find_tables(
    page,
    clip=None,
    vertical_strategy: str = "lines",
    horizontal_strategy: str = "lines",
    vertical_lines: list = None,
    horizontal_lines: list = None,
    snap_tolerance: float = DEFAULT_SNAP_TOLERANCE,
    snap_x_tolerance: float = None,
    snap_y_tolerance: float = None,
    join_tolerance: float = DEFAULT_JOIN_TOLERANCE,
    join_x_tolerance: float = None,
    join_y_tolerance: float = None,
    edge_min_length: float = 3,
    min_words_vertical: float = DEFAULT_MIN_WORDS_VERTICAL,
    min_words_horizontal: float = DEFAULT_MIN_WORDS_HORIZONTAL,
    intersection_tolerance: float = 3,
    intersection_x_tolerance: float = None,
    intersection_y_tolerance: float = None,
    text_tolerance=3,
    text_x_tolerance=3,
    text_y_tolerance=3,
    strategy=None,  # offer abbreviation
    add_lines=None,  # user-specified lines
    add_boxes=None,  # user-specified rectangles
    paths=None,  # accept vector graphics as parameter
):
    pymupdf._warn_layout_once()
    CHARS.clear()
    EDGES.clear()
    TEXTPAGE = None
    old_small = bool(pymupdf.TOOLS.set_small_glyph_heights())  # save old value
    pymupdf.TOOLS.set_small_glyph_heights(True)  # we need minimum bboxes
    if page.rotation != 0:
        page, old_xref, old_rot, old_mediabox = page_rotation_set0(page)
    else:
        old_xref, old_rot, old_mediabox = None, None, None

    if snap_x_tolerance is None:
        snap_x_tolerance = UNSET
    if snap_y_tolerance is None:
        snap_y_tolerance = UNSET
    if join_x_tolerance is None:
        join_x_tolerance = UNSET
    if join_y_tolerance is None:
        join_y_tolerance = UNSET
    if intersection_x_tolerance is None:
        intersection_x_tolerance = UNSET
    if intersection_y_tolerance is None:
        intersection_y_tolerance = UNSET
    if strategy is not None:
        vertical_strategy = strategy
        horizontal_strategy = strategy

    settings = {
        "vertical_strategy": vertical_strategy,
        "horizontal_strategy": horizontal_strategy,
        "explicit_vertical_lines": vertical_lines,
        "explicit_horizontal_lines": horizontal_lines,
        "snap_tolerance": snap_tolerance,
        "snap_x_tolerance": snap_x_tolerance,
        "snap_y_tolerance": snap_y_tolerance,
        "join_tolerance": join_tolerance,
        "join_x_tolerance": join_x_tolerance,
        "join_y_tolerance": join_y_tolerance,
        "edge_min_length": edge_min_length,
        "min_words_vertical": min_words_vertical,
        "min_words_horizontal": min_words_horizontal,
        "intersection_tolerance": intersection_tolerance,
        "intersection_x_tolerance": intersection_x_tolerance,
        "intersection_y_tolerance": intersection_y_tolerance,
        "text_tolerance": text_tolerance,
        "text_x_tolerance": text_x_tolerance,
        "text_y_tolerance": text_y_tolerance,
    }

    old_quad_corrections = pymupdf.TOOLS.unset_quad_corrections()
    try:
        page.get_layout()
        if page.layout_information:
            pymupdf.TOOLS.unset_quad_corrections(True)
            boxes = [
                pymupdf.Rect(b[:4]) for b in page.layout_information if b[-1] == "table"
            ]
        else:
            boxes = []

        if boxes:  # layout did find some tables
            pass
        elif page.layout_information is not None:
            # layout was executed but found no tables
            # make sure we exit quickly with an empty TableFinder
            tbf = TableFinder(page)
            return tbf

        tset = TableSettings.resolve(settings=settings)
        page.table_settings = tset

        TEXTPAGE = make_chars(page, clip=clip)  # create character list of page
        make_edges(
            page,
            clip=clip,
            tset=tset,
            paths=paths,
            add_lines=add_lines,
            add_boxes=add_boxes,
        )  # create lines and curves

        tbf = TableFinder(page, settings=tset)
        tbf.textpage = TEXTPAGE  # store textpage for later use
        if boxes:
            # only keep Finder tables that match a layout box
            tbf.tables = [
                tab
                for tab in tbf.tables
                if any(_iou(tab.bbox, r) >= 0.6 for r in boxes)
            ]
        # build the complementary list of layout table boxes
        my_boxes = [
            r for r in boxes if all(_iou(r, tab.bbox) < 0.6 for tab in tbf.tables)
        ]
        if my_boxes:
            word_rects = [pymupdf.Rect(w[:4]) for w in TEXTPAGE.extractWORDS()]
            tp2 = page.get_textpage(flags=TABLE_DETECTOR_FLAGS)
        for rect in my_boxes:
            cells = make_table_from_bbox(tp2, word_rects, rect)  # pylint: disable=E0606
            tbf.tables.append(Table(page, cells))
    except Exception as e:
        pymupdf.message("find_tables: exception occurred: %s" % str(e))
        return None
    finally:
        pymupdf.TOOLS.set_small_glyph_heights(old_small)
        if old_xref is not None:
            page = page_rotation_reset(page, old_xref, old_rot, old_mediabox)
        pymupdf.TOOLS.unset_quad_corrections(old_quad_corrections)
    for table in tbf.tables:
        table.textpage = TEXTPAGE
    return tbf

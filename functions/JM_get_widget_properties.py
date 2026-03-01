"""
Function: fitz.JM_get_widget_properties
Signature: JM_get_widget_properties(annot, Widget)
Description:
Populate a Python Widget object with the values from a PDF form field.
Called by "Page.first_widget" and "Widget.next".
"""

import fitz

# Source code of fitz.JM_get_widget_properties:
def JM_get_widget_properties(annot, Widget):
    '''
    Populate a Python Widget object with the values from a PDF form field.
    Called by "Page.first_widget" and "Widget.next".
    '''
    #log( '{type(annot)=}')
    annot_obj = mupdf.pdf_annot_obj(annot.this)
    #log( 'Have called mupdf.pdf_annot_obj()')
    page = _pdf_annot_page(annot.this)
    pdf = page.doc()
    tw = annot

    def SETATTR(key, value):
        setattr(Widget, key, value)

    def SETATTR_DROP(mod, key, value):
        # Original C code for this function deletes if PyObject* is NULL. We
        # don't have a representation for that in Python - e.g. None is not
        # represented by NULL.
        setattr(mod, key, value)

    #log( '=== + mupdf.pdf_widget_type(tw)')
    field_type = mupdf.pdf_widget_type(tw.this)
    #log( '=== - mupdf.pdf_widget_type(tw)')
    Widget.field_type = field_type
    if field_type == mupdf.PDF_WIDGET_TYPE_SIGNATURE:
        if mupdf.pdf_signature_is_signed(pdf, annot_obj):
            SETATTR("is_signed", True)
        else:
            SETATTR("is_signed",False)
    else:
        SETATTR("is_signed", None)
    SETATTR_DROP(Widget, "border_style", JM_UnicodeFromStr(mupdf.pdf_field_border_style(annot_obj)))
    SETATTR_DROP(Widget, "field_type_string", JM_UnicodeFromStr(JM_field_type_text(field_type)))

    field_name = mupdf.pdf_load_field_name(annot_obj)
    SETATTR_DROP(Widget, "field_name", field_name)

    def pdf_dict_get_inheritable_nonempty_label(node, key):
        '''
        This is a modified version of MuPDF's pdf_dict_get_inheritable(), with
        some changes:
        * Returns string from pdf_to_text_string() or None if not found.
        * Recurses to parent if current node exists but with empty string
          value.
        '''
        slow = node
        halfbeat = 11   # Don't start moving slow pointer for a while.
        while 1:
            if not node.m_internal:
                return
            val = mupdf.pdf_dict_get(node, key)
            if val.m_internal:
                label = mupdf.pdf_to_text_string(val)
                if label:
                    return label
            node = mupdf.pdf_dict_get(node, PDF_NAME('Parent'))
            if node.m_internal == slow.m_internal:
                raise Exception("cycle in resources")
            halfbeat -= 1
            if halfbeat == 0:
                slow = mupdf.pdf_dict_get(slow, PDF_NAME('Parent'))
                halfbeat = 2
    
    # In order to address #3950, we use our modified pdf_dict_get_inheritable()
    # to ignore empty-string child values.
    label = pdf_dict_get_inheritable_nonempty_label(annot_obj, PDF_NAME('TU'))
    if label is not None:
        SETATTR_DROP(Widget, "field_label", label)

    fvalue = None
    if field_type == mupdf.PDF_WIDGET_TYPE_RADIOBUTTON:
        obj = mupdf.pdf_dict_get( annot_obj, PDF_NAME('Parent'))    # owning RB group
        if obj.m_internal:
            SETATTR_DROP(Widget, "rb_parent", mupdf.pdf_to_num( obj))
        obj = mupdf.pdf_dict_get(annot_obj, PDF_NAME('AS'))
        if obj.m_internal:
            fvalue = mupdf.pdf_to_name(obj)
    if not fvalue:
        fvalue = mupdf.pdf_field_value(annot_obj)
    SETATTR_DROP(Widget, "field_value", JM_UnicodeFromStr(fvalue))

    SETATTR_DROP(Widget, "field_display", mupdf.pdf_field_display(annot_obj))

    border_width = mupdf.pdf_to_real(mupdf.pdf_dict_getl(annot_obj, PDF_NAME('BS'), PDF_NAME('W')))
    if border_width == 0:
        border_width = 1
    SETATTR_DROP(Widget, "border_width", border_width)

    obj = mupdf.pdf_dict_getl(annot_obj, PDF_NAME('BS'), PDF_NAME('D'))
    if mupdf.pdf_is_array(obj):
        n = mupdf.pdf_array_len(obj)
        d = [0] * n
        for i in range(n):
            d[i] = mupdf.pdf_to_int(mupdf.pdf_array_get(obj, i))
        SETATTR_DROP(Widget, "border_dashes", d)

    SETATTR_DROP(Widget, "text_maxlen", mupdf.pdf_text_widget_max_len(tw.this))

    SETATTR_DROP(Widget, "text_format", mupdf.pdf_text_widget_format(tw.this))

    obj = mupdf.pdf_dict_getl(annot_obj, PDF_NAME('MK'), PDF_NAME('BG'))
    if mupdf.pdf_is_array(obj):
        n = mupdf.pdf_array_len(obj)
        col = [0] * n
        for i in range(n):
            col[i] = mupdf.pdf_to_real(mupdf.pdf_array_get(obj, i))
        SETATTR_DROP(Widget, "fill_color", col)

    obj = mupdf.pdf_dict_getl(annot_obj, PDF_NAME('MK'), PDF_NAME('BC'))
    if mupdf.pdf_is_array(obj):
        n = mupdf.pdf_array_len(obj)
        col = [0] * n
        for i in range(n):
            col[i] = mupdf.pdf_to_real(mupdf.pdf_array_get(obj, i))
        SETATTR_DROP(Widget, "border_color", col)

    SETATTR_DROP(Widget, "choice_values", JM_choice_options(annot))

    da = mupdf.pdf_to_text_string(mupdf.pdf_dict_get_inheritable(annot_obj, PDF_NAME('DA')))
    SETATTR_DROP(Widget, "_text_da", JM_UnicodeFromStr(da))

    obj = mupdf.pdf_dict_getl(annot_obj, PDF_NAME('MK'), PDF_NAME('CA'))
    if obj.m_internal:
        SETATTR_DROP(Widget, "button_caption", JM_UnicodeFromStr(mupdf.pdf_to_text_string(obj)))

    SETATTR_DROP(Widget, "field_flags", mupdf.pdf_field_flags(annot_obj))

    # call Py method to reconstruct text color, font name, size
    Widget._parse_da()

    # extract JavaScript action texts
    s = mupdf.pdf_dict_get(annot_obj, PDF_NAME('A'))
    ss = JM_get_script(s)
    SETATTR_DROP(Widget, "script", ss)

    SETATTR_DROP(Widget, "script_stroke",
            JM_get_script(mupdf.pdf_dict_getl(annot_obj, PDF_NAME('AA'), PDF_NAME('K')))
            )

    SETATTR_DROP(Widget, "script_format",
            JM_get_script(mupdf.pdf_dict_getl(annot_obj, PDF_NAME('AA'), PDF_NAME('F')))
            )

    SETATTR_DROP(Widget, "script_change",
            JM_get_script(mupdf.pdf_dict_getl(annot_obj, PDF_NAME('AA'), PDF_NAME('V')))
            )

    SETATTR_DROP(Widget, "script_calc",
            JM_get_script(mupdf.pdf_dict_getl(annot_obj, PDF_NAME('AA'), PDF_NAME('C')))
            )

    SETATTR_DROP(Widget, "script_blur",
            JM_get_script(mupdf.pdf_dict_getl(annot_obj, PDF_NAME('AA'), mupdf.pdf_new_name('Bl')))
            )

    SETATTR_DROP(Widget, "script_focus",
            JM_get_script(mupdf.pdf_dict_getl(annot_obj, PDF_NAME('AA'), mupdf.pdf_new_name('Fo')))
            )

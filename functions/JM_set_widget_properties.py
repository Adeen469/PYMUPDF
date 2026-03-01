"""
Function: fitz.JM_set_widget_properties
Signature: JM_set_widget_properties(annot, Widget)
Description:
Update the PDF form field with the properties from a Python Widget object.
Called by "Page.add_widget" and "Annot.update_widget".
"""

import fitz

# Source code of fitz.JM_set_widget_properties:
def JM_set_widget_properties(annot, Widget):
    '''
    Update the PDF form field with the properties from a Python Widget object.
    Called by "Page.add_widget" and "Annot.update_widget".
    '''
    if isinstance( annot, Annot):
        annot = annot.this
    assert isinstance( annot, mupdf.PdfAnnot), f'{type(annot)=} {type=}'
    page = _pdf_annot_page(annot)
    assert page.m_internal, 'Annot is not bound to a page'
    annot_obj = mupdf.pdf_annot_obj(annot)
    pdf = page.doc()
    def GETATTR(name):
        return getattr(Widget, name, None)

    value = GETATTR("field_type")
    field_type = value

    # rectangle --------------------------------------------------------------
    value = GETATTR("rect")
    rect = JM_rect_from_py(value)
    rot_mat = JM_rotate_page_matrix(page)
    rect = mupdf.fz_transform_rect(rect, rot_mat)
    mupdf.pdf_set_annot_rect(annot, rect)

    # fill color -------------------------------------------------------------
    value = GETATTR("fill_color")
    if value and PySequence_Check(value):
        n = len(value)
        fill_col = mupdf.pdf_new_array(pdf, n)
        col = 0
        for i in range(n):
            col = value[i]
            mupdf.pdf_array_push_real(fill_col, col)
        mupdf.pdf_field_set_fill_color(annot_obj, fill_col)

    # dashes -----------------------------------------------------------------
    value = GETATTR("border_dashes")
    if value and PySequence_Check(value):
        n = len(value)
        dashes = mupdf.pdf_new_array(pdf, n)
        for i in range(n):
            mupdf.pdf_array_push_int(dashes, value[i])
        mupdf.pdf_dict_putl(annot_obj, dashes, PDF_NAME('BS'), PDF_NAME('D'))

    # border color -----------------------------------------------------------
    value = GETATTR("border_color")
    if value and PySequence_Check(value):
        n = len(value)
        border_col = mupdf.pdf_new_array(pdf, n)
        col = 0
        for i in range(n):
            col = value[i]
            mupdf.pdf_array_push_real(border_col, col)
        mupdf.pdf_dict_putl(annot_obj, border_col, PDF_NAME('MK'), PDF_NAME('BC'))

    # entry ignored - may be used later
    #
    #int text_format = (int) PyInt_AsLong(GETATTR("text_format"));
    #

    # field label -----------------------------------------------------------
    value = GETATTR("field_label")
    if value is not None:
        label = JM_StrAsChar(value)
        mupdf.pdf_dict_put_text_string(annot_obj, PDF_NAME('TU'), label)

    # field name -------------------------------------------------------------
    value = GETATTR("field_name")
    if value is not None:
        name = JM_StrAsChar(value)
        old_name = mupdf.pdf_load_field_name(annot_obj)
        if name != old_name:
            mupdf.pdf_dict_put_text_string(annot_obj, PDF_NAME('T'), name)

    # max text len -----------------------------------------------------------
    if field_type == mupdf.PDF_WIDGET_TYPE_TEXT:
        value = GETATTR("text_maxlen")
        text_maxlen = value
        if text_maxlen:
            mupdf.pdf_dict_put_int(annot_obj, PDF_NAME('MaxLen'), text_maxlen)
    value = GETATTR("field_display")
    d = value
    mupdf.pdf_field_set_display(annot_obj, d)

    # choice values ----------------------------------------------------------
    if field_type in (mupdf.PDF_WIDGET_TYPE_LISTBOX, mupdf.PDF_WIDGET_TYPE_COMBOBOX):
        value = GETATTR("choice_values")
        JM_set_choice_options(annot, value)

    # border style -----------------------------------------------------------
    value = GETATTR("border_style")
    val = JM_get_border_style(value)
    mupdf.pdf_dict_putl(annot_obj, val, PDF_NAME('BS'), PDF_NAME('S'))

    # border width -----------------------------------------------------------
    value = GETATTR("border_width")
    border_width = value
    mupdf.pdf_dict_putl(
            annot_obj,
            mupdf.pdf_new_real(border_width),
            PDF_NAME('BS'),
            PDF_NAME('W'),
            )

    # /DA string -------------------------------------------------------------
    value = GETATTR("_text_da")
    da = JM_StrAsChar(value)
    mupdf.pdf_dict_put_text_string(annot_obj, PDF_NAME('DA'), da)
    mupdf.pdf_dict_del(annot_obj, PDF_NAME('DS'))  # not supported by MuPDF
    mupdf.pdf_dict_del(annot_obj, PDF_NAME('RC'))  # not supported by MuPDF

    # field flags ------------------------------------------------------------
    field_flags = GETATTR("field_flags")
    if field_flags is not None:
        if field_type == mupdf.PDF_WIDGET_TYPE_COMBOBOX:
            field_flags |= mupdf.PDF_CH_FIELD_IS_COMBO
        elif field_type == mupdf.PDF_WIDGET_TYPE_RADIOBUTTON:
            field_flags |= mupdf.PDF_BTN_FIELD_IS_RADIO
        elif field_type == mupdf.PDF_WIDGET_TYPE_BUTTON:
            field_flags |= mupdf.PDF_BTN_FIELD_IS_PUSHBUTTON
        mupdf.pdf_dict_put_int( annot_obj, PDF_NAME('Ff'), field_flags)

    # button caption ---------------------------------------------------------
    value = GETATTR("button_caption")
    ca = JM_StrAsChar(value)
    if ca:
        mupdf.pdf_field_set_button_caption(annot_obj, ca)

    # script (/A) -------------------------------------------------------
    value = GETATTR("script")
    JM_put_script(annot_obj, PDF_NAME('A'), mupdf.PdfObj(), value)

    # script (/AA/K) -------------------------------------------------------
    value = GETATTR("script_stroke")
    JM_put_script(annot_obj, PDF_NAME('AA'), PDF_NAME('K'), value)

    # script (/AA/F) -------------------------------------------------------
    value = GETATTR("script_format")
    JM_put_script(annot_obj, PDF_NAME('AA'), PDF_NAME('F'), value)

    # script (/AA/V) -------------------------------------------------------
    value = GETATTR("script_change")
    JM_put_script(annot_obj, PDF_NAME('AA'), PDF_NAME('V'), value)

    # script (/AA/C) -------------------------------------------------------
    value = GETATTR("script_calc")
    JM_put_script(annot_obj, PDF_NAME('AA'), PDF_NAME('C'), value)

    # script (/AA/Bl) -------------------------------------------------------
    value = GETATTR("script_blur")
    JM_put_script(annot_obj, PDF_NAME('AA'), mupdf.pdf_new_name('Bl'), value)

    # script (/AA/Fo) codespell:ignore --------------------------------------
    value = GETATTR("script_focus")
    JM_put_script(annot_obj, PDF_NAME('AA'), mupdf.pdf_new_name('Fo'), value)

    # field value ------------------------------------------------------------
    value = GETATTR("field_value")  # field value
    text = JM_StrAsChar(value)  # convert to text (may fail!)
    if field_type == mupdf.PDF_WIDGET_TYPE_RADIOBUTTON:
        if not value:
            mupdf.pdf_set_field_value(pdf, annot_obj, "Off", 1)
            mupdf.pdf_dict_put_name(annot_obj, PDF_NAME('AS'), "Off")
        else:
            # TODO check if another button in the group is ON and if so set it Off
            onstate = mupdf.pdf_button_field_on_state(annot_obj)
            if onstate.m_internal:
                on = mupdf.pdf_to_name(onstate)
                mupdf.pdf_set_field_value(pdf, annot_obj, on, 1)
                mupdf.pdf_dict_put_name(annot_obj, PDF_NAME('AS'), on)
            elif text:
                mupdf.pdf_dict_put_name(annot_obj, PDF_NAME('AS'), text)
    elif field_type == mupdf.PDF_WIDGET_TYPE_CHECKBOX:
        onstate = mupdf.pdf_button_field_on_state(annot_obj)
        on = onstate.pdf_to_name()
        if value in (True, on) or text == 'Yes':
            mupdf.pdf_set_field_value(pdf, annot_obj, on, 1)
            mupdf.pdf_dict_put_name(annot_obj, PDF_NAME('AS'), on)
            mupdf.pdf_dict_put_name(annot_obj, PDF_NAME('V'), on)
        else:
            mupdf.pdf_dict_put_name( annot_obj, PDF_NAME('AS'), 'Off')
            mupdf.pdf_dict_put_name( annot_obj, PDF_NAME('V'), 'Off')
    else:
        if text:
            mupdf.pdf_set_field_value(pdf, annot_obj, text, 1)
            if field_type in (mupdf.PDF_WIDGET_TYPE_COMBOBOX, mupdf.PDF_WIDGET_TYPE_LISTBOX):
                mupdf.pdf_dict_del(annot_obj, PDF_NAME('I'))
    mupdf.pdf_dirty_annot(annot)
    mupdf.pdf_set_annot_hot(annot, 1)
    mupdf.pdf_set_annot_active(annot, 1)
    mupdf.pdf_update_annot(annot)

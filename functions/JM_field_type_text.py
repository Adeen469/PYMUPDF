"""
Function: fitz.JM_field_type_text
Signature: JM_field_type_text(wtype)
Description:
String from widget type
"""

import fitz

# Source code of fitz.JM_field_type_text:
def JM_field_type_text(wtype):
    '''
    String from widget type
    '''
    if wtype == mupdf.PDF_WIDGET_TYPE_BUTTON:
        return "Button"
    if wtype == mupdf.PDF_WIDGET_TYPE_CHECKBOX:
        return "CheckBox"
    if wtype == mupdf.PDF_WIDGET_TYPE_RADIOBUTTON:
        return "RadioButton"
    if wtype == mupdf.PDF_WIDGET_TYPE_TEXT:
        return "Text"
    if wtype == mupdf.PDF_WIDGET_TYPE_LISTBOX:
        return "ListBox"
    if wtype == mupdf.PDF_WIDGET_TYPE_COMBOBOX:
        return "ComboBox"
    if wtype == mupdf.PDF_WIDGET_TYPE_SIGNATURE:
        return "Signature"
    return "unknown"

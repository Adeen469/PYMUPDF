"""
Function: fitz.JM_put_script
Signature: JM_put_script(annot_obj, key1, key2, value)
Description:
Create a JavaScript PDF action.
Usable for all object types which support PDF actions, even if the
argument name suggests annotations. Up to 2 key values can be specified, so
JavaScript actions can be stored for '/A' and '/AA/?' keys.
"""

import fitz

# Source code of fitz.JM_put_script:
def JM_put_script(annot_obj, key1, key2, value):
    '''
    Create a JavaScript PDF action.
    Usable for all object types which support PDF actions, even if the
    argument name suggests annotations. Up to 2 key values can be specified, so
    JavaScript actions can be stored for '/A' and '/AA/?' keys.
    '''
    key1_obj = mupdf.pdf_dict_get(annot_obj, key1)
    pdf = mupdf.pdf_get_bound_document(annot_obj)  # owning PDF

    # if no new script given, just delete corresponding key
    if not value:
        if key2 is None or not key2.m_internal:
            mupdf.pdf_dict_del(annot_obj, key1)
        elif key1_obj.m_internal:
            mupdf.pdf_dict_del(key1_obj, key2)
        return

    # read any existing script as a PyUnicode string
    if not key2.m_internal or not key1_obj.m_internal:
        script = JM_get_script(key1_obj)
    else:
        script = JM_get_script(mupdf.pdf_dict_get(key1_obj, key2))

    # replace old script, if different from new one
    if value != script:
        newaction = JM_new_javascript(pdf, value)
        if not key2.m_internal:
            mupdf.pdf_dict_put(annot_obj, key1, newaction)
        else:
            mupdf.pdf_dict_putl(annot_obj, newaction, key1, key2)

"""
Function: fitz.JM_set_object_value
Signature: JM_set_object_value(obj, key, value)
Description:
Set a PDF dict key to some value
"""

import fitz

# Source code of fitz.JM_set_object_value:
def JM_set_object_value(obj, key, value):
    '''
    Set a PDF dict key to some value
    '''
    eyecatcher = "fitz: replace me!"
    pdf = mupdf.pdf_get_bound_document(obj)
    # split PDF key at path seps and take last key part
    list_ = key.split('/')
    len_ = len(list_)
    i = len_ - 1
    skey = list_[i]

    del list_[i]    # del the last sub-key
    len_ = len(list_)   # remaining length
    testkey = mupdf.pdf_dict_getp(obj, key)    # check if key already exists
    if not testkey.m_internal:
        #No, it will be created here. But we cannot allow this happening if
        #indirect objects are referenced. So we check all higher level
        #sub-paths for indirect references.
        while len_ > 0:
            t = '/'.join(list_) # next high level
            if mupdf.pdf_is_indirect(mupdf.pdf_dict_getp(obj, JM_StrAsChar(t))):
                raise Exception("path to '%s' has indirects", JM_StrAsChar(skey))
            del list_[len_ - 1]   # del last sub-key
            len_ = len(list_)   # remaining length
    # Insert our eyecatcher. Will create all sub-paths in the chain, or
    # respectively remove old value of key-path.
    mupdf.pdf_dict_putp(obj, key, mupdf.pdf_new_text_string(eyecatcher))
    testkey = mupdf.pdf_dict_getp(obj, key)
    if not mupdf.pdf_is_string(testkey):
        raise Exception("cannot insert value for '%s'", key)
    temp = mupdf.pdf_to_text_string(testkey)
    if temp != eyecatcher:
        raise Exception("cannot insert value for '%s'", key)
    # read the result as a string
    res = JM_object_to_buffer(obj, 1, 0)
    objstr = JM_EscapeStrFromBuffer(res)

    # replace 'eyecatcher' by desired 'value'
    nullval = "/%s(%s)" % ( skey, eyecatcher)
    newval = "/%s %s" % (skey, value)
    newstr = objstr.replace(nullval, newval, 1)

    # make PDF object from resulting string
    new_obj = JM_pdf_obj_from_str(pdf, newstr)
    return new_obj

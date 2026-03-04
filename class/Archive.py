"""
Class: fitz.Archive

Description: No docstring available.

Inheritance (MRO): Archive -> object

"""

import fitz

# ===== Methods and Attributes of fitz.Archive =====

# __eq__(self, value, /)  [wrapper_descriptor]
#     -> Return self==value.

# __gt__(self, value, /)  [wrapper_descriptor]
#     -> Return self>value.

# __hash__(self, /)  [wrapper_descriptor]
#     -> Return hash(self).

# __init__(self, *args)  [function]
#     -> Archive(dirname [, path]) - from folder

# __lt__(self, value, /)  [wrapper_descriptor]
#     -> Return self<value.

# __ne__(self, value, /)  [wrapper_descriptor]
#     -> Return self!=value.

# __repr__(self)  [function]
#     -> Return repr(self).

# __str__(self, /)  [wrapper_descriptor]
#     -> Return str(self).

# add(self, content, path=None)  [function]
#     -> Add a sub-archive.

# entry_list = <property object at 0x000002052DE30F90>  [property]

# has_entry(self, name)  [function]

# read_entry(self, name)  [function]


# ===== Source Code =====
class Archive:
    def __init__( self, *args):
        '''
        Archive(dirname [, path]) - from folder
        Archive(file [, path]) - from file name or object
        Archive(data, name) - from memory item
        Archive() - empty archive
        Archive(archive [, path]) - from archive
        '''
        self._subarchives = list()
        self.this = mupdf.fz_new_multi_archive()
        if args:
            self.add( *args)
    
    def __repr__( self):
        return f'Archive, sub-archives: {len(self._subarchives)}'

    def _add_arch( self, subarch, path=None):
        mupdf.fz_mount_multi_archive( self.this, subarch, path)
    
    def _add_dir( self, folder, path=None):
        sub = mupdf.fz_open_directory( folder)
        mupdf.fz_mount_multi_archive( self.this, sub, path)
    
    def _add_treeitem( self, memory, name, path=None):
        buff = JM_BufferFromBytes( memory)
        sub = mupdf.fz_new_tree_archive( mupdf.FzTree())
        mupdf.fz_tree_archive_add_buffer( sub, name, buff)
        mupdf.fz_mount_multi_archive( self.this, sub, path)
    
    def _add_ziptarfile( self, filepath, type_, path=None):
        if type_ == 1:
            sub = mupdf.fz_open_zip_archive( filepath)
        else:
            sub = mupdf.fz_open_tar_archive( filepath)
        mupdf.fz_mount_multi_archive( self.this, sub, path)
    
    def _add_ziptarmemory( self, memory, type_, path=None):
        buff = JM_BufferFromBytes( memory)
        stream = mupdf.fz_open_buffer( buff)
        if type_==1:
            sub = mupdf.fz_open_zip_archive_with_stream( stream)
        else:
            sub = mupdf.fz_open_tar_archive_with_stream( stream)
        mupdf.fz_mount_multi_archive( self.this, sub, path)
    
    def add( self, content, path=None):
        '''
        Add a sub-archive.

        Args:
            content:
                The content to be added. May be one of:
                    `str` - must be path of directory or file.
                    `bytes`, `bytearray`, `io.BytesIO` - raw data.
                    `zipfile.Zipfile`.
                    `tarfile.TarFile`.
                    `pymupdf.Archive`.
                    A two-item tuple `(data, name)`.
                    List or tuple (but not tuple with length 2) of the above.
            path: (str) a "virtual" path name, under which the elements
                of content can be retrieved. Use it to e.g. cope with
                duplicate element names.
        '''
        def is_binary_data(x):
            return isinstance(x, (bytes, bytearray, io.BytesIO))

        def make_subarch(entries, mount, fmt):
            subarch = dict(fmt=fmt, entries=entries, path=mount)
            if fmt != "tree" or self._subarchives == []:
                self._subarchives.append(subarch)
            else:
                ltree = self._subarchives[-1]
                if ltree["fmt"] != "tree" or ltree["path"] != subarch["path"]:
                    self._subarchives.append(subarch)
                else:
                    ltree["entries"].extend(subarch["entries"])
                    self._subarchives[-1] = ltree

        if isinstance(content, pathlib.Path):
            content = str(content)
        
        if isinstance(content, str):
            if os.path.isdir(content):
                self._add_dir(content, path)
                return make_subarch(os.listdir(content), path, 'dir')
            elif os.path.isfile(content):
                assert isinstance(path, str) and path != '', \
                        f'Need name for binary content, but {path=}.'
                with io.open(content, 'rb') as f:
                    ff = f.read()
                self._add_treeitem(ff, path)
                return make_subarch([path], None, 'tree')
            else:
                raise ValueError(f'Not a file or directory: {content!r}')

        elif is_binary_data(content):
            assert isinstance(path, str) and path != '' \
                    f'Need name for binary content, but {path=}.'
            self._add_treeitem(content, path)
            return make_subarch([path], None, 'tree')

        elif isinstance(content, zipfile.ZipFile):
            filename = getattr(content, "filename", None)
            if filename is None:
                fp = content.fp.getvalue()
                self._add_ziptarmemory(fp, 1, path)
            else:
                self._add_ziptarfile(filename, 1, path)
            return make_subarch(content.namelist(), path, 'zip')

        elif isinstance(content, tarfile.TarFile):
            filename = getattr(content.fileobj, "name", None)
            if filename is None:
                fp = content.fileobj
                if not isinstance(fp, io.BytesIO):
                    fp = fp.fileobj
                self._add_ziptarmemory(fp.getvalue(), 0, path)
            else:
                self._add_ziptarfile(filename, 0, path)
            return make_subarch(content.getnames(), path, 'tar')

        elif isinstance(content, Archive):
            self._add_arch(content, path)
            return make_subarch([], path, 'multi')
        
        if isinstance(content, tuple) and len(content) == 2:
            # covers the tree item plus path
            data, name = content
            assert isinstance(name, str), f'Unexpected {type(name)=}'
            if is_binary_data(data):
                self._add_treeitem(data, name, path=path)
            elif isinstance(data, str):
                if os.path.isfile(data):
                    with io.open(data, 'rb') as f:
                        ff = f.read()
                    self._add_treeitem(ff, name, path=path)
            else:
                assert 0, f'Unexpected {type(data)=}.'
            return make_subarch([name], path, 'tree')
        
        elif hasattr(content, '__getitem__'):
            # Deal with sequence of disparate items.
            for item in content:
                self.add(item, path)
            return
        
        else:
            raise TypeError(f'Unrecognised type {type(content)}.')
        assert 0

    @property
    def entry_list( self):
        '''
        List of sub archives.
        '''
        return self._subarchives
    
    def has_entry( self, name):
        return mupdf.fz_has_archive_entry( self.this, name)
    
    def read_entry( self, name):
        buff = mupdf.fz_read_archive_entry( self.this, name)
        return JM_BinFromBuffer( buff)

import os, mimetypes
mimetypes.init()

fnm = input("Input the Filename: ")
nm, extnsn = os.path.splitext(fnm)
etyp = mimetypes.types_map[extnsn]
print(f"The extension of the file is: '{etyp}'")
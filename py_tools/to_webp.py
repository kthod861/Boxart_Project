from PIL import Image, ImageEnhance
import os

def list_file(img_folder):
    lboxartfiles = os.listdir(img_folder)
    list_files = []
    for box_file in lboxartfiles:
        list_files.append( os.path.join( img_folder, box_file) )
    return list_files



img_fold_src = r"C:\Users\K_thod\Desktop\New folder"

lfile = list_file(img_fold_src)

for f in lfile:
    impath, imname = os.path.split( f )
    image = Image.open(f)

    imgout = imname.split('.', 1)[0]
    out = os.path.join( impath, "{}.webp".format(imgout))

    image.save(out, 'webp', optimize=True, quality=80)

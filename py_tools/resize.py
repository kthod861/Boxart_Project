from PIL import Image, ImageEnhance
import os

def list_file(img_folder):
    lboxartfiles = os.listdir(img_folder)
    list_files = []
    for box_file in lboxartfiles:
        list_files.append( os.path.join( img_folder, box_file) )
    return list_files



img_fold_src = r"F:\RetroBat\emulationstation\.emulationstation\themes\Meringue_Knulli\_inc\systems\controllers"

lfile = list_file(img_fold_src)

for f in lfile:

    impath, imname = os.path.split( f )
    im = Image.open(f)

    image_size = im.size
    maxsize = 600
    if any ( [image_size[0]>maxsize, image_size[1]>maxsize]):
        im.thumbnail((maxsize,maxsize),Image.Resampling.LANCZOS)
        im.save(f, 'png', optimize=True, quality=80)
    #imgout = imname.split('.', 1)[0]
    #out = os.path.join( impath, "{}.webp".format(imgout))


    #image.save(out, 'webp', optimize=True, quality=80)

print("DONE")
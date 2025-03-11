from PIL import Image
import os
import random
import math


def list_file(img_folder):
    lboxartfiles = os.listdir(img_folder)
    list_files = []
    for box_file in lboxartfiles:
        list_files.append( os.path.join( img_folder, box_file) )
    return list_files

def keep_above_size(box_files, min_img_size):
    lout = []

    for box_file in box_files:
        im = Image.open(box_file)
        im_size = im.size
        if all(i >= min_img_size for i in im_size):
            lout.append(box_file)
    return lout




source_folder = r"F:\libretro-thumbnails\Nintendo - Game Boy\Named_Boxarts"
destination_folder = r"F:\Boxart_Project\Batocera_Systems\gb"
min_size = 512


box_files = list_file(source_folder)

above_size = keep_above_size(box_files, min_size)

print( "{}/{} images above {} pixels".format(len(above_size), len(box_files), min_size ))
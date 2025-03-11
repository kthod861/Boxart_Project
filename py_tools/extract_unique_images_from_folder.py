from PIL import Image
import os
import random
import math
import shutil
import subprocess
import json
## find-dups install needed

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
        if all(i >= min_img_size for i in list(im_size)):
            lout.append(box_file)
    return lout

def copyfile(source_filepath, dest_folder):
    fold,filename = os.path.split( source_filepath )
    dst = os.path.join( dest_folder, filename)
    shutil.copyfile(source_filepath, dst)

def get_unique(source_folder):
    jsonout = r"F:\Boxart_Project\res.json"
    src = source_folder.replace('\\','\\\\')

    cmdline = 'find-dups "{}" --algorithm phash --hash-size 4 --parallel --progress --hash-db "{}"'.format(src, jsonout)
    p = subprocess.Popen( cmdline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    for line in p.stdout.readlines():
        print (line)
    retval = p.wait()



    with open(jsonout, 'r') as f:
        D,info = json.load(f)

    luniquehash = []
    lunique = []
    for k,v in D.items():
        if not v in luniquehash:
            luniquehash.append(v)
            lunique.append(k)

    print( len( lunique ))
    os.remove(jsonout)
    return lunique

def filter_names(box_files):
    lout = []
    ltest = []
    for box in box_files:
        ppath,pfile = os.path.split(box)

        spl = pfile.split("(")
        if len(spl)>=2:
            if spl[0] not in ltest:
                ltest.append(spl[0] )
                lout.append( box)

        else:
            lout.append(box)
    return lout


## V1 not really working

source_folder = r"F:\libretro-thumbnails\Nintendo - Wii U\Named_Boxarts"
destination_folder = r"F:\Boxart_Project\Batocera_Systems\wiiu"
min_size = 400

## simple file listing
box_files = list_file(source_folder)

##List above size and copy them
above_size = keep_above_size(box_files, min_size)


### filternames
namefiltered = filter_names(above_size)


## copy filtered for ffurther checking
filtered_res_fold = os.path.join( source_folder, "filtered_res")
if not os.path.exists(filtered_res_fold):
    os.mkdir(filtered_res_fold)

for f in namefiltered:
    copyfile(f, filtered_res_fold)

##keep unique
lunique = get_unique(filtered_res_fold)

for unique_file in lunique:
    if os.path.exists(unique_file):
        fpath,ffile = os.path.split(unique_file)
        newfile = os.path.join( destination_folder, ffile )
        shutil.copy(unique_file, newfile)

#rem filterd fold
shutil.rmtree(filtered_res_fold)


print( "\n\ninitial boxarts : {}\nabovesize : {}\nnamefiltered : {}\nunique : {}".format(len(box_files), len(above_size), len(namefiltered), len(lunique) ))





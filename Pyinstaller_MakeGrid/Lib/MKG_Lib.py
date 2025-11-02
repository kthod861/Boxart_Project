#from PySide2 import QtUiTools, QtWidgets
from PySide6 import QtUiTools,QtCore,QtGui,QtWidgets
from PySide6.QtWidgets import (QApplication,QDockWidget,QPushButton,QHBoxLayout,QListWidgetItem,QFileDialog)
from PIL import Image, ImageEnhance
import os
import random
import math

def popup(s):
    dlg = QtWidgets.QMessageBox(None)
    dlg.setWindowTitle("POPUP")
    dlg.setText(str(s))
    button = dlg.exec_()

    if button == QtWidgets.QMessageBox.Ok:
        return True

def get_resolution(img_folder):
    lfiles = os.listdir(img_folder)

    lresolutions =[]
    lamount = []
    limage = []

    for img in lfiles:
        imgpath = os.path.join( img_folder, img)
        try:
            im = Image.open(imgpath)
            if im.size not in lresolutions:
                lresolutions.append(im.size)
                lamount.append(1)
                limage.append([imgpath])
            else:
                idx = lresolutions.index(im.size)
                lamount[idx]+=1
                limage[idx].append(imgpath)
        except:
            continue
    if lamount:
        maxamount = max(lamount)
        idxres = lamount.index(maxamount)
        print( "-- Main resolution : {} ({} files / {})".format(lresolutions[idxres],maxamount, len(lfiles)  ) )
        return lresolutions[idxres],limage[idxres]
    else:
        return None,None
        print(lresolutions)
        print(lamount)

def calc_aspectratio(imsize):
    w,h = float(imsize[0]), float(imsize[1])
    return w/h

def get_resolution_onlyrescompatible(img_folder):
    lfiles = os.listdir(img_folder)

    lresolutions =[]
    lapspectratio = []
    lamount = []
    limage = []

    for img in lfiles:
        imgpath = os.path.join( img_folder, img)
        try:
            im = Image.open(imgpath)
            ratio = calc_aspectratio(im.size)
            if ratio not in lapspectratio:
                lresolutions.append(im.size)
                lapspectratio.append(ratio)
                lamount.append(1)
                limage.append([imgpath])
            else:
                idx = lapspectratio.index(ratio)
                lamount[idx]+=1
                limage[idx].append(imgpath)

        except:
            continue

    if lamount:
        maxamount = max(lamount)
        idxres = lamount.index(maxamount)
        log = "-- Main resolution : {} ({}) ({} files / {})".format(lresolutions[idxres],lapspectratio[idxres], maxamount, len(lfiles)  )
        return lresolutions[idxres],limage[idxres], log
    else:
        return None,None,None
        print(lresolutions)
        print(lamount)

def get_resolution_allimages(img_folder):
    lfiles = os.listdir(img_folder)

    lresolutions =[]
    lapspectratio = []
    lamount = []
    limage = []
    lallimage = []
    for img in lfiles:
        imgpath = os.path.join( img_folder, img)
        try:
            im = Image.open(imgpath)
            ratio = calc_aspectratio(im.size)
            if ratio not in lapspectratio:
                lresolutions.append(im.size)
                lapspectratio.append(ratio)
                lamount.append(1)
                limage.append([imgpath])
            else:
                idx = lapspectratio.index(ratio)
                lamount[idx]+=1
                limage[idx].append(imgpath)
            lallimage.append(imgpath)
        except:
            continue

    if lamount:
        maxamount = max(lamount)
        idxres = lamount.index(maxamount)
        log = "-- Main resolution : {} ({}) ({} files / {})".format(lresolutions[idxres],lapspectratio[idxres], maxamount, len(lfiles) )
        return lresolutions[idxres],lallimage, log
    else:
        return None,None, None
        print(lresolutions)
        print(lamount)

def makegrid_fixed_outputres(thumb_res, output_res, output_path, list_images, perline_target, padding, color_scale = 1.0):
    log = ""
    out_w,out_h = output_res[0],output_res[1]
    thumb_w,thumb_h = thumb_res[0],thumb_res[1]

    result = Image.new('RGB', (out_w,out_h))

    target_thumb_w = int( out_w/perline_target )
    p = target_thumb_w/thumb_w
    target_thumb_h = int( thumb_h*p)

    nrow = math.ceil( out_w/target_thumb_w )
    nline = math.ceil( out_h/target_thumb_h )

    log += "-- Grid: {}/{}\n".format(nrow,nline)
    log += "-- New resolution: {}/{}\n".format(target_thumb_w, target_thumb_h)

    amountofimages = nrow*nline
    if len(list_images) >= amountofimages:
        log += "-- No duplicata"
        res = random.sample( range(0, len(list_images)), amountofimages)
    else:
        log += "-- Duplicata"
        res = []
        for i in range(len(list_images)):
            res.append(i)

        li = list(range(0,len(list_images)))
        for i in range( amountofimages ):
            if len(res) <= amountofimages:
                res.append( random.choice(li) )
        

    i=0
    for X in range( nrow ):
        for Y in range( nline ):
            choice = list_images[ res[i] ]

            im = Image.open(choice )
            try:
                im2 = ImageEnhance.Color(im)
                new_image = im2.enhance(color_scale)

                im1 = new_image.resize( (target_thumb_w-padding, target_thumb_h-padding) )
                result.paste(im1, ( X*target_thumb_w, Y*target_thumb_h ) )
            except:
                im1 = im.resize( (target_thumb_w-padding, target_thumb_h-padding) )
                result.paste(im1, ( X*target_thumb_w, Y*target_thumb_h ) )
            i+=1


    
    result.save(output_path)
    return log

def cleanup_unidentified(imgfolder):
    limage = os.listdir(imgfolder)

    for image in limage:
        image_path = os.path.join( imgfolder,image )
        try:
            im = Image.open(image_path )
        except:
            os.rename(image_path, image_path+".NO")
    
def main_grid_creator(boxart_fold, output_resolution, ntiles, padding, ouputimg, only_compat_aspectratio = False, cleanup = False, color_scale = 1.0):
    llog = []
    if only_compat_aspectratio:
        resolution, limages, log  = get_resolution_onlyrescompatible(boxart_fold)
    else:
        resolution, limages, log  = get_resolution_allimages(boxart_fold)
    llog.append( log )
    if resolution:
        if cleanup:
            cleanup_unidentified(boxart_fold)

        reslog = makegrid_fixed_outputres(resolution, output_resolution, ouputimg, limages, ntiles, padding, color_scale = color_scale)
        llog.append( reslog )
        return True, llog

    llog.append("Unable to define a resolution, source folder must be empty")
    return False, llog


def list_file(folders, ext = ".png"):
    list_files = []
    for folderprocess in folders:
        for dirpath, dirnames, filenames in os.walk(folderprocess):
            for filename in [f for f in filenames if f.endswith(ext)]:
                list_files.append( os.path.join(dirpath, filename) )
    return list_files

def compress_boxart( boxart_fold, img_quality = 80 , base_height = 300):
    msg = ""
    limages = list_file( [boxart_fold] )
    for image_file in limages:
        try:
            img = Image.open(image_file)
            
            if base_height < int(img.size[1]):
                hpercent = (base_height / float(img.size[1]))
                wsize = int((float(img.size[0]) * float(hpercent)))
                img = img.resize((wsize, base_height), Image.Resampling.LANCZOS)
            img.save(image_file, 'PNG', optimize=True, quality=img_quality)
        except IOError:
                    msg += "\ ncannot create thumbnail for '%s'" % image_file 
        
    return ( "Processed {} files\n\nLogs:\n{}".format( len(limages ), msg))
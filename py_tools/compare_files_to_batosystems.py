from PIL import Image, ImageEnhance
import os, shutil

def list_file(img_folder):
    lboxartfiles = os.listdir(img_folder)
    list_files = []
    for box_file in lboxartfiles:
        list_files.append( os.path.join( img_folder, box_file) )
    return list_files





def move_notbato_files(img_fold_src,bato_folders ):
    lfile = list_file(img_fold_src)
    ldir = list_file(bato_folders)
    lsystem = []
    for fold in ldir:
        mpath,systemname = os.path.split( fold )
        lsystem.append( systemname )

    for imgpath in lfile:
        if not "TMP" in imgpath:
            mpath,imgfile = os.path.split( imgpath )

            imgname = imgfile.split(".")[0]
            if imgname not in lsystem:
                dst = os.path.join(img_fold_src, "TMP", imgfile  )
                shutil.move(imgpath, dst)

def check_missing_system(img_fold_src,bato_folders):
    lfile = list_file(img_fold_src)
    ldir = list_file(bato_folders)

    limages = []
    for imgpath in lfile:
        if not "TMP" in imgpath:
            mpath,imgfile = os.path.split( imgpath )
            imgname = imgfile.split(".")[0] 
            limages.append(imgname)

    for fold in ldir:
        mpath,systemname = os.path.split( fold )
        if systemname not in limages:
            print("Missing {}".format(systemname))

def compare_folders(a, b):
    lfileA = list_file(a)
    limagesA = []
    for imgpath in lfileA:
        if not "TMP" in imgpath:
            mpath,imgfile = os.path.split( imgpath )
            imgname = imgfile.split(".")[0] 
            limagesA.append(imgname)

    lfileB = list_file(b)
    limagesB = []
    for imgpath in lfileB:
        if not "TMP" in imgpath:
            mpath,imgfile = os.path.split( imgpath )
            imgname = imgfile.split(".")[0] 
            limagesB.append(imgname)    

    for imgA in limagesA:
        if not imgA in limagesB:
            print( imgA)

    for imgB in limagesB:
        if not imgB in limagesA:
            print( imgB)

#img_fold_src = r"F:\RetroBat\emulationstation\.emulationstation\themes\MeringuePersonnal_ES_DE_Knulli\_inc\systems\controllers"
#img_fold_src = r"F:\RetroBat\emulationstation\.emulationstation\themes\MeringuePersonnal_ES_DE_Knulli\_inc\systems\background_16_9"
img_fold_src = r"F:\RetroBat\emulationstation\.emulationstation\themes\MeringuePersonnal_ES_DE_Knulli\_inc\systems\background_4_3"
bato_folders = r"F:\Boxart_Project\Batocera_Systems"


#move_notbato_files(img_fold_src,bato_folders )
#check_missing_system(img_fold_src,bato_folders)


a = r"F:\RetroBat\emulationstation\.emulationstation\themes\MeringuePersonnal_ES_DE_Knulli\_inc\systems\background_16_9"
#b = r"F:\RetroBat\emulationstation\.emulationstation\themes\MeringuePersonnal_ES_DE_Knulli\_inc\systems\background_4_3"
b = r"F:\RetroBat\emulationstation\.emulationstation\themes\MeringuePersonnal_ES_DE_Knulli\_inc\systems\controllers"
compare_folders(a, b)
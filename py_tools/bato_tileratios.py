import os
import math
import xmltodict

def list_file(img_folder):
    lboxartfiles = os.listdir(img_folder)
    list_files = []
    for box_file in lboxartfiles:
        list_files.append( os.path.join( img_folder, box_file) )
    return list_files

def calc_ratio(tileratio, screenratio , factor):
    x = factor

    ratio = tileratio[1]/tileratio[0]
    #print(ratio)
    gridXsize = screenratio[0] / factor
    gridYsize = gridXsize * ratio


    y =  math.floor( screenratio[1]/ gridYsize )

    #y = math.ceil(factor / (fmax/fmin) )

    return x,y

def get_coversize_from_xml(xml_path):
    with open(xml_path, encoding='utf-8', errors='ignore') as f:
        D = xmltodict.parse( f.read() )
        for k,v in D["theme"]["variables"].items():
            if k == "systemCoverSize":
                x,y = v.split("-")
                return int(x),int(y)

## GET sysstem list from backgoeunds
bato_rom_systems_folder = r"F:\RetroBat\emulationstation\.emulationstation\themes\Meringue_Knulli\_inc\systems\background"

tmp = list_file(bato_rom_systems_folder)
batosystems = []
for o in tmp:
    ppath,pfile = os.path.split( o )
    sysname = pfile.split(".webp")[0]
    batosystems.append( sysname )

## get ES-DE xml files
es_de_globals_folder = r"C:\Users\K_thod\ES-DE\themes\Meringue_ES_DE_rg406\_inc\systems\metadata-global"
metadata_globals = list_file(es_de_globals_folder)



#Build relationship between bato system and es-de metadata
D = {}
for system_name in batosystems:
    D[system_name] = {}
    meta_data_system = None
    for glb in metadata_globals:
        ppath,pfile = os.path.split( glb )
        if system_name in pfile:
            meta_data_system = glb
            D[system_name]["meta_data_file"] = meta_data_system
            tile_coversize = get_coversize_from_xml(meta_data_system)
            D[system_name]["tile_coversize"] = tile_coversize

            break
    if not meta_data_system:
        #print("unable to find : {}".format( system_name))
        D[system_name]["meta_data_file"] = None
        D[system_name]["tile_coversize"] = None



## Make to output xmls
ouput_xml_folder = r"F:\RetroBat\emulationstation\.emulationstation\themes\Meringue_Knulli\_inc\coversize_grid_wide"
screenratio = [1,0.85]
smallfactor = 7
medfactor = 5
largefactor = 3

for system_name, sysD in D.items():
    if sysD["tile_coversize"]:
        small = calc_ratio(sysD["tile_coversize"], screenratio ,smallfactor) 
        mid = calc_ratio(sysD["tile_coversize"], screenratio ,medfactor) 
        large = calc_ratio(sysD["tile_coversize"], screenratio ,largefactor) 
        #print( small)


        resultfile = os.path.join(ouput_xml_folder, "{}.xml".format(system_name))

        Dout = {}
        Dout["theme"] = {}
        Dout["theme"]["variables"] = {}
        Dout["theme"]["variables"]["GridLayout_small"] = "{} {}".format(small[0],small[1]-1)
        Dout["theme"]["variables"]["GridLayout_medium"] = "{} {}".format(mid[0],mid[1]-1)
        Dout["theme"]["variables"]["GridLayout_large"] = "{} {}".format(large[0],large[1])

        with open(resultfile, 'w') as result_file:
            result_file.write(xmltodict.unparse(Dout, pretty=True))


'''
tileratio = [1,1]

screenratio = [1,0.85]

smallfactor = 7
medfactor = 5
largefactor = 3


res = calc_ratio(tileratio, screenratio ,smallfactor)
print(res)
res = calc_ratio(tileratio, screenratio ,medfactor)
print(res)
res = calc_ratio(tileratio, screenratio ,largefactor)
print(res)
'''


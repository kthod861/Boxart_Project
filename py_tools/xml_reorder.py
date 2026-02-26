import xmltodict, json, os


def list_file(img_folder):
    lboxartfiles = os.listdir(img_folder)
    list_files = []
    for box_file in lboxartfiles:
        list_files.append( os.path.join( img_folder, box_file) )
    return list_files



xmlfold = r"C:\Users\K_thod\ES-DE\themes\Meringue_ES_DE_rg406\_inc\coversize-basic-grid-variables"
lxml = list_file(xmlfold)


usefull_keys = ["grid-base-item-w", "grid-base-item-h", "grid-item-spacing"]

for xmlfile in lxml:
    jsonD = {
            "theme": {
                "variant": [
                    {
                        "@name": "gamelist-grid-small",
                        "aspectRatio": [{"@name": "1:1", "variables":{}},{"@name": "4:3", "variables":{}},{"@name": "16:9", "variables":{}}]
                    },
                    {
                        "@name": "gamelist-grid-medium",
                        "aspectRatio": [{"@name": "1:1", "variables":{}},{"@name": "4:3", "variables":{}},{"@name": "16:9", "variables":{}}]
                    },
                    {
                        "@name": "gamelist-grid-large",
                        "aspectRatio": [{"@name": "1:1", "variables":{}},{"@name": "4:3", "variables":{}},{"@name": "16:9", "variables":{}}]
                    },
                    {
                        "@name": "gamelist-grid-x-large",
                        "aspectRatio": [{"@name": "1:1", "variables":{}},{"@name": "4:3", "variables":{}},{"@name": "16:9", "variables":{}}]
                    }
                ]
            }
        }

    with open(xmlfile) as f:
        D = xmltodict.parse( f.read() )
        lratio = D["theme"]["aspectRatio"]
        for ratio in lratio:
            ratioName = ratio["@name"]
            print( ratioName )
            lfontsize = ratio["fontSize"]
            for fontsize in lfontsize:
                fontsizeName = fontsize["@name"]
                print( fontsizeName)

                ## VARIANTS
                variantreplace = "gamelist-grid-{}".format(fontsizeName)
                print( variantreplace)
                for dstvariantD in jsonD["theme"]["variant"]:
                    if dstvariantD["@name"] == variantreplace:
                        for dstratioD in  dstvariantD["aspectRatio"]:
                            if dstratioD["@name"] == ratioName:
                                for k,v in fontsize["variables"].items():
                                    if k in usefull_keys:
                                        dstratioD["variables"][k] = v





    #print( json.dumps( jsonD,indent=4))



    #print(xmltodict.unparse(jsonD, pretty=True))
    with open(xmlfile, 'w') as result_file:
        result_file.write(xmltodict.unparse(jsonD, pretty=True))
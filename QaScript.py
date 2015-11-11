# ------------------------------------------------------------------------------
# Testing Examples
# coding: utf-8
# Copyright (c) 2010 The Foundry Visionmongers Ltd.  All Rights Reserved.
# ------------------------------------------------------------------------------

import mari, os, platform, getpass

myPlatform = platform.system()
currentLoadedGeo = ""
testDir = ""
ref = ""


if myPlatform.startswith("Windows"):
    testDir =  os.path.join(r"\\netqa\\netqa\Testing\Mari\models\QaScriptModels")
    #Z:\Testing\TestHarness\Mari\referenceImages\16bitHDR1k
    ref = os.path.join(r"\\netqa\\netqa\Testing\TestHarness\Mari\referenceImages\16bitHDR1k")
else:
    testDir = os.path.join(r"/mnt/netqa/Testing/Mari/models/QaScriptModels")
    #//netqa/netqa/Testing/Mari/models
    ref = os.path.join(r"/","mnt","netqa","Testing","TestHarness","Mari","referenceImages","16bitHDR1k")

if os.path.exists(testDir) and os.path.exists(ref):
    print ("Found Testing Directory", testDir)
    print ("Found Image Reference Path", ref)

def createProject(name,obj):

    try:

        mari.projects.create(name, obj, [], [])

    except RuntimeError:
        print "Closing Project - Opening new project"
        mari.projects.close(False)
        mari.projects.create(name, obj, [], [])

    currentLoadedGeo == obj


# ------------------------------------------------------------------------------

def makeSimpleCube():
    ''' Create a simple cube project with 6 patches '''

    cube = os.path.join(testDir, "Cube6x6.obj")
    createProject("Simple Cube Project", cube)

# ------------------------------------------------------------------------------

def makeSimpleSphere():
    ''' Create a simple cube project with 6 patches '''

    sphere = os.path.join(testDir, "Sphere.obj")
    createProject("Simple Sphere Project", sphere)

# ------------------------------------------------------------------------------

def makePiggy():
    '''  '''

    piggy = os.path.join(testDir, "Piggy.obj")
    createProject("Simple Sphere Project", piggy)

# ------------------------------------------------------------------------------

def makeTerminatorHead():

    TerminatorHead = os.path.join(testDir,"TerminatorHead.obj")
    createProject("Terminator Head Project",TerminatorHead)

def makeSubD():
    ''' Create a project and generates subdivion using default settings '''

    subDCube = os.path.join(testDir, "Cube6x6.obj")
    createProject("Simple SubD Project", subDCube)

    geo = mari.geo.current()
    geo.generateSubdivision({"Level": 3,"Method":"Catmull Clark","Boundary Interpolation":"Edge And Corner"})

def createFBXProject():
    ''' '''

def createABCProject():
    ''' '''

def createPTexProject():
    ''' '''

def createHDRProject():
    ''' Loads a simple cube with 6x6 patches and HDR images on the base layer. Gpu preferecnes and paint will also be set up for HDR painting '''

    mari.prefs.set("GPU/Virtual Texture/atlasFormat", "Half")
    cube = os.path.join(testDir, "cube6x6.obj")
    createProject("HDR Cube Project", cube)

    channel = mari.geo.current().currentChannel()
    channel.setDepth(16,1)

    currentLayer = channel.currentLayer()
    currentLayer.importImages(os.path.join(ref,"16bitHDR1k.$UDIM.hdr"))

    paint_buffer = mari.canvases.paintBuffer()
    paint_buffer.setDepth(16)
    paint_buffer.setClampColors(False)

def createTexTransferProject():
    ''' Loads a simple Texture trasfer project '''

def getGPUinfo():
    print("\n")
    print("Graphic Card Information ")
    print("-"*40)
    graphicInfo = mari.gl_render.platformInformation()
    for x in graphicInfo.keys():
        print graphicInfo[x]
    print("\n")

def getVersionInfo():
    print("\n")
    print("Mari Version Information ")
    print("-"*40)
    version = mari.app.version()
    print version.info()
    print("\n")

def objInfo():
    ''' Prints information on loaded geometry '''
    print(currentLoadedGeo)

def listProdecurals():
    ''' grabs and lists procedural names '''

    for index, x in enumerate(mari.LayerStack.proceduralLayerTypeList()):
        print index +1, ":" , x

def listAdjustments():
    ''' grabs and lists adjusment names '''

    for index, x in enumerate(mari.LayerStack.adjustmentLayerTypeList()):
       print index +1, ":" , x

def listBlendModes():
    ''' grabs and lists adjusment names '''

def listTools():

    for x in mari.tools.toolsList():
        print x

def groupedLayers():
    ''' List all grouped layers '''

def createLayers():
    ''' '''

def getMeshPath():

    meshPath = mari.geo.current().currentVersion().meshPaths()[0]
    print ("\n")
    print "Current Mesh Path " + str(meshPath)

getGPUinfo()
getVersionInfo()
executable = mari.utils.sys.executable

print("\n")
print "Paths"
print("-"*40)
print "Mari Location "    + str(executable)
print "OCIO Config File " + str(mari.utils.ocio.CONFIG_PATH_DEFAULT)
print "PySide Version "   + str(mari.utils.ocio.PySide.sys.version)
print("\n")


# Register a new action with the action manager, and add it to QA menu
#File      -------------------------------------------------------------------------------------------------------------
#mari.menus.addAction(mari.actions.create('Get File', 'getFiles()'), "MainWindow/&QA/&Example Projects")
# Projects -------------------------------------------------------------------------------------------------------------
mari.menus.addAction(mari.actions.create('Simple Cube', 'makeSimpleCube()'), "MainWindow/&QA/&Example Projects")
mari.menus.addAction(mari.actions.create('Simple Sphere', 'makeSimpleSphere()'), "MainWindow/&QA/&Example Projects")
mari.menus.addAction(mari.actions.create('Piggy Project', 'makePiggy()'), "MainWindow/&QA/&Example Projects")
mari.menus.addAction(mari.actions.create('Terminator Head', 'makeTerminatorHead()'), "MainWindow/&QA/&Example Projects")
mari.menus.addAction(mari.actions.create('HDR Cube Paint', 'createHDRProject()'), "MainWindow/&QA/&Example Projects")
mari.menus.addAction(mari.actions.create('SubD Cube Project', 'makeSubD()'), "MainWindow/&QA/&Example Projects")

# System Details -------------------------------------------------------------------------------------------------------
mari.menus.addAction(mari.actions.create("Graphics Card Info", "getGPUinfo()"), "MainWindow/&QA/&Platform Info")
mari.menus.addAction(mari.actions.create("Mari Version","getVersionInfo()"), "MainWindow/&QA/&Platform Info")

# Licence --------------------------------------------------------------------------------------------------------------
#mari.menus.addAction(mari.actions.create("Graphics Card Info", "getGPUinfo()"), "MainWindow/&QA/&Platform Info")
#mari.menus.addAction(mari.actions.create("Mari Version","getVersionInfo()"), "MainWindow/&QA/&Platform Info")

# GeoInfo
mari.menus.addAction(mari.actions.create("Mesh Path","getMeshPath()"), "MainWindow/&QA/&Geo Info")

# Lists ----------------------------------------------------------------------------------------------------------------
mari.menus.addAction(mari.actions.create("List Adjustments","listAdjustments()"), "MainWindow/&QA/&Layers")
mari.menus.addAction(mari.actions.create("List Prodecurals","listProdecurals()"), "MainWindow/&QA/&Layers")
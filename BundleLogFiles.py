'''
Created on 22 Apr 2014

@author: john.crowe
'''
import os, zipfile

def checkExists(myDirs):

    import sys

    print("Checking if Files Exist\n")
    for files in myDirs:
        if os.path.exists(os.path.join(files)):
            print("".join("Path exist: " + files))

        else:
            print("".join(files + " Does not exist! Exiting"))
            sys.exit(1)

    copyFiles(myDirs)

def getDMP(dmpdir):

    latest = sorted([f for f in os.listdir(dmpdir) if f.endswith(".dmp")])
    print("Most recent file = %s" % (latest[-1]))
    return latest

def copyFiles(files):

    import shutil

    copyDir = files[0]

    for x in files[1:]:
        shutil.copy(x, copyDir)
        print("Copying " + x + " to " + copyDir)

def zipArchive(path):

    zipf = zipfile.ZipFile(os.path.join(path, "BugLogs.zip"), "w",zipfile.ZIP_DEFLATED)
    zipDir = path,zipf

    for x in os.listdir(path):
        if x != "BugLogs.zip":
            zipf.write(os.path.join(path,x))
    zipf.close()

def errorsWarnings(path,log):

    writeFile = open(path + "Errors.txt","w")

    for x in open(log):
        if x.startswith("Error") or x.startswith("Warning"):
            writeFile.write(os.path.join(x))
    writeFile.close()


def getFiles():

    import getpass

    USER = getpass.getuser()
    ARCHIVEDIR = os.path.join("C:\Users\john.crowe\Documents\BUGARCHIVE\\")
    DMP    = os.path.join('C:\Users\\' + USER  +'\Documents\Mari\Logs\\')
    LOG    = os.path.join('C:\Users\\' + USER  +'\Documents\Mari\Logs\MariLog.txt')
    CONFIG = os.path.join('C:\Users\\'+ USER + '\.mari\TheFoundry\Mari.ini')

    findLatest = getDMP(DMP)
    latestDMP = os.path.join(DMP + findLatest[-1])

    PROJECTFILES = [ARCHIVEDIR,CONFIG,LOG,latestDMP]
    checkExists(PROJECTFILES)
    errorsWarnings(ARCHIVEDIR,LOG)
    zipArchive(ARCHIVEDIR)

getFiles()

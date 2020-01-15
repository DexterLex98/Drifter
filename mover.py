# Author: Suraj Das
# Developed: 13-01-2020
# Version: 1.0
# Stage: Alpha

import sys
import os
import logging as LG
import errno as error

print("\033[1;32;40m Drifter \n")
# Getting User inputs

Folderpath = input("Give Folder Path:")
MovePath = input("Where you want to move:")
extensionType = input("Extension Type:")

dirArg = Folderpath
movArg = MovePath
extenArg = extensionType

print("Extension selected: {}\n".format(extenArg))

print(dirArg)
DriveSplit = dirArg.split(os.sep)
LG.info("Drive Splitted : {}".format(DriveSplit))


# print("Files:\n") // DEBUG-MODE
dirList = os.listdir(dirArg)

def File_recognizer(directory, exten):
    os.chdir(Folderpath)
    count = 0
    psdfiles = []
    try:
        for i, dirfiles in enumerate(directory):
            psdFiles = os.path.splitext(dirfiles)
            if psdFiles[1] == exten:
                psd_dirs = os.path.realpath(dirfiles)
                psdfiles.insert(i,psd_dirs)
            # elif psdFiles[1] != exten:
            #     print("Not {} file".format(exten))

    except FileNotFoundError:
        pass

    return psdfiles

# Storing files

psdData = File_recognizer(dirList,extenArg)

def moveFiles(MV_files,User_directory):
    try:
        fd = Folderpath
        ChangedDir = os.chdir(fd)
        print(os.getcwd())
        # print(MV_files, "\n")
        for files in MV_files:
            cmd = 'move "{}" "{}" '.format(files,User_directory)
            os.system(cmd)
        # LG.warning(cmd) // DEBUG-LOGGING

        print("\nFiles Moved !")
        print("\n========")

    except FileNotFoundError:
        print("Directory not found !\n")
        sys.exit(error.ENOENT)




# Moving the files to specified directory
moveFiles(psdData,movArg)

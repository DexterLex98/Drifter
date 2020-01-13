
import sys
import os
import logging as LG
import errno as error

print("\033[1;32;40m Mover \n")
#This parses the file path
Folderpath = input("Give Folder Path:")
MovePath = input("Where you want to move:")
dirArg = Folderpath
movArg = MovePath

print(dirArg)
DriveSplit = dirArg.split(os.sep)
LG.info("Drive Splitted : {}".format(DriveSplit))


# print("Files:\n")
dirList = os.listdir(dirArg)

def File_recognizer(directory):
    os.chdir(Folderpath)
    count = 0
    psdfiles = []
    try:
        for i, dirfiles in enumerate(directory):
            psdFiles = os.path.splitext(dirfiles)
            if psdFiles[1] == '.psd':
                psd_dirs = os.path.realpath(dirfiles)
                psdfiles.insert(i,psd_dirs)
            # elif psdFiles[1] != '.psd':
            #     print("Not PSD.")
    except FileNotFoundError:
        pass

    return psdfiles

# Storing the data files
psdData = File_recognizer(dirList)

def moveFiles(MV_files,User_directory):
    try:
        fd = Folderpath
        ChangedDir = os.chdir(fd)
        print(os.getcwd())
        # print(MV_files, "\n")
        for files in MV_files:
            cmd = 'move "{}" "{}" '.format(files,User_directory)
            os.system(cmd)
        # LG.warning(cmd)

        print("\nFiles Moved !")
        print("\n========")

    except FileNotFoundError:
        print("Directory not found !\n")
        sys.exit(error.ENOENT)




# Moving the files to specified directory
moveFiles(psdData,movArg)

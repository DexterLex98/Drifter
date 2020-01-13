
import sys
import os 

print("\033[1;32;40m Mover\n")
#This parses the file path 
Folderpath = input("Give Folder Path:")
MovePath = input("Where you want to move:")
dirArg = Folderpath
movArg = MovePath

print(dirArg)
DriveSplit = dirArg.split(os.sep)
print("Drive Splitted : {}".format(DriveSplit))


# print("Files:\n")
dirList = os.listdir(dirArg)

def File_recognizer(directory):
    count = 0
    psdfiles = []
    # print(type(psdfiles))
    
    try:
        for i, dirfiles in enumerate(directory):
            psdFiles = os.path.splitext(dirfiles)
            
            if psdFiles[1] == '.psd' :
                psdfiles.insert(i,psdFiles)

            elif psdFiles[1] != '.psd':
                # print("Not Photoshop Files")
        # print(psdfiles)
    # This will move the files to the directory specified


    except FileNotFoundError:
        print("NO .psd files found")
    return psdfiles

# Storing the data files 
psdData = File_recognizer(dirList)

def moveFiles(MV_files, User_directory):
    try:
        os.chdir('')
    except expression as identifier:
        pass
    


# Moving the files to specified directory
moveFiles(psdData,movArg)



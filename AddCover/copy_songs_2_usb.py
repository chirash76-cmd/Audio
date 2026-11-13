import os,shutil
from pathlib import Path

#copied
def numberSort(songList):
    return sorted(songList, key=lambda s: (s[0].isdigit() if s else False, s.lower()))
#--

def findFolders(sourceFolder):
    itemsList = os.listdir(sourceFolder)
    folderList = []
    for item in itemsList:
        if (sourceFolder/item).is_dir():
            folderList.append(item)
    return folderList

def copyFolder(foldername,destination, folder_progress,total_folders):
    items = numberSort(os.listdir(foldername))
    os.mkdir(destination/foldername)
    total = len(items)
    count = 1
    for item in items:
        if (Path(foldername)/item).is_dir():
            copyFolder(Path(foldername)/item,destination,"","")
        else:
            print(f"Copying Folder {foldername} ( {folder_progress} / {total_folders} ): ( {count} / {total} ) : {item.rstrip(".mp3")}")
            shutil.copy(Path(foldername)/item,destination/foldername/item)
            count+=1

def clearUSB(destinationUSB):
    items = os.listdir(destinationUSB)
    for item in items:
        itemPath = Path(destinationUSB)/item
        if (itemPath).is_dir():
            shutil.rmtree(itemPath)
        else:
            os.remove(itemPath)
    print("Cleaned USB...\n")
# see all folders

# enter each folder in given order and copy folder songs in alphabetical order.
#Numbered songs at end

MusicFolder = Path("/home/bluepick/Music/")
usb = Path("/home/bluepick/USb/")
# usb = Path(input("Enter USB Path:\n"))
DestinationUSB = usb/"Audio/"
WipeUSB = True

os.chdir(MusicFolder)
folders = ["New","Animated","Music","Hindi","Phonk","OldClassic","Rap","Remix","Football"]
for item in os.listdir(MusicFolder):
    if item not in folders and os.path.isdir(MusicFolder/item):
        folders.append(item)
folders.remove("AddCover")
folders.remove("UNP")

#Main
if "Audio" not in os.listdir(usb):
    print("Creating New Folder")
    os.mkdir(DestinationUSB)
    Clearence = True
elif WipeUSB:
    print("Deleting and Creating New folder")
    shutil.rmtree(DestinationUSB)
    os.mkdir(DestinationUSB)
    Clearence = True
else:
    Clearence = False


if Clearence:
    totalFolders = len(folders)
    folder_progress=1
    for folder in folders:
        copyFolder(folder,DestinationUSB,folder_progress,totalFolders)
        print(f"Done copying folder {folder} : ( {folder_progress} / {totalFolders} )\n")
        folder_progress+=1

    print("Copying songs to USB completed")
else:
    print("Clearence not Obtained. "+"Try cleaning the usb or set WipeUSB = True")

import os,shutil

#Change These accordingly
musicFolderPath = "/home/bluepick/Music/"
usbFolderPath = "/run/media/bluepick/Rishaan/"
usbFolderPath = "/home/bluepick/Documents/usb/"
musicFolderName = "Audio"

# musicFolderPath = os.path.join(musicFolderPath,"Sequence")

def copy_folder(folderpath,folderdestination):
    destinationFolder = folderpath.split("/")[-1]
    destinationFolderPath = os.path.join(folderdestination,destinationFolder)

    #create folder if it doesnt exist
    if not os.path.exists(destinationFolderPath):
        os.mkdir(destinationFolderPath)

    #create sorted list
    items = ListSorter(folderpath)

    #copy items
    count = 0
    for item in items:
        itemPath = os.path.join(folderpath,item)
        destinationItems = os.listdir(destinationFolderPath)
        if os.path.isfile(itemPath):
            if item.endswith(".mp3") and item not in destinationItems:
                shutil.copy(itemPath,destinationFolderPath)
                count+=1
                print(f"{destinationFolder}: {count}/{len(items)} : {item}")

def ListSorter(folderpath):
    items = os.listdir(folderpath)
    sortedList = []
    for item in items:
        if item.endswith(".mp3"):
            sortedList.append((item,item.lower().strip()))
            sortedList.sort(key= lambda x: "zzzzzz"+x[1] if x[1][0].isdigit() else x[1])
    finalList = []
    for item in sortedList:
        finalList.append(item[0])
    return finalList

# copy_folder(musicFolderPath,usbFolderPath)
# "/home/bluepick/Documents/testing/Audio/Folder Name" , "/home/bluepick/Documents/testing/usb/Audio"



#Main

#Filter Folders
ordered_folders = ["Favourites","Animated","Music","Hindi"]
folders = os.listdir(musicFolderPath)

new_folders = [folder for folder in folders if folder.startswith("New")]
new_folders.sort(reverse=True)

for item in folders:
    itemPath = os.path.join(musicFolderPath,item)
    if os.path.isfile(itemPath):
        folders.remove(item)
folders.remove("AddCover")
folders.remove("UNP")

for folder in folders:
    if folder not in ordered_folders and not folder.startswith("New"):
        ordered_folders.append(folder)

for folder in new_folders:
    ordered_folders.insert(0,folder)


#Copy ordered_folders
# musicFolderName = musicFolderPath.split("/")[-2]
destinationMainFolderPath = os.path.join(usbFolderPath,musicFolderName)

if not (os.path.exists(musicFolderPath) and os.path.exists(usbFolderPath)):
    print("Invalid Input Paths")
elif os.path.exists(destinationMainFolderPath):
    print("Folder already exists")
    print("Exiting")
else:
    os.mkdir(destinationMainFolderPath)
    for folder in ordered_folders:
        folderPath = os.path.join(musicFolderPath,folder)
        copy_folder(folderPath,destinationMainFolderPath)
    print("Performing Manual copy")
    copy_folder("/home/bluepick/Music/Animated/Miku/",os.path.join(destinationMainFolderPath,"Animated/Miku"))
    copy_folder("/home/bluepick/Music/Animated/Neuro-sama/",os.path.join(destinationMainFolderPath,"Animated/Neuro-sama"))
    print("\nProcess Completed!")


from pathlib import Path
import shutil
import os

source_dir = "" #this should be the usb path
file_dir = Path("data_files/incoming")
file_dest = Path("data_files/approved")
file_dup = Path("data_files/duplicated")
file_rej = Path("data_files/rejected")



if file_dir.is_dir():
    print("Files in incoming folder:")
    for item in file_dir.iterdir():
        print(item.name)
else:
    print("No files in incoming folder")

def file_jump():
    """ using shutil since it can move files directly from the usb to project folders"""
    for files in os.listdir(file_dir):
        source_path = os.path.join(file_dir, files) #change file_dir to source_dir which is the usb path
        dest_path = os.path.join(file_dest, files)

        #to-do: add validation for file. can be sent to approved, duplicated, or rejected

        if os.path.isfile(source_path):
            shutil.move(source_path, dest_path)
            print("files have been moved")

#file_jump()

def file_reverse(): #this is just for testing purposes for now
    for files in os.listdir(file_dest):
        source_path = os.path.join(file_dir, files)  # change file_dir to source_dir which is the usb path
        dest_path = os.path.join(file_dest, files)

        if os.path.isfile(dest_path):
            shutil.move(dest_path,source_path)
            print("files have been moved")

#file_reverse()

# for item in file_dir.iterdir(): #this removes files from base source to avoid future duplicates
#     item.unlink()
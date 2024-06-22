import os
import shutil
from pathlib import Path

LOCATION = input("Enter dir location to organize files from: ")
NEW_DIR = input("Enter new directory name: ")

def move_dir_initself(src_dir, new_dir):
    source_path = Path(src_dir)
    new_dir_path = source_path / new_dir

    # Create a new directory inside the specified location
    new_dir_path.mkdir(exist_ok=True)

    # Get the listing of the files in the source directory
    new_files = os.listdir(source_path)

    extensions = []  # Initialize a placeholder for the extensions
    
    # Loop to iterate over the listing and extract the extensions
    for file in new_files:
        if (source_path / file).is_file():  # Ensure it's a file
            root, ext = os.path.splitext(file)
            extensions.append(ext)
    
    files_set = set(extensions)
    print(files_set)
    
    # Create folders with extension names
    for item in files_set:
        if item:  # Ensure the item is not an empty string
            ext_dir = source_path / item[1:]  # Remove the dot from the extension
            ext_dir.mkdir(exist_ok=True)
    
    # Move files into the corresponding directories
    for file in new_files:
        if (source_path / file).is_file():  # Ensure it's a file
            root, ext = os.path.splitext(file)
            if ext:  # Ensure the file has an extension
                src_file = source_path / file
                dest_dir = source_path / ext[1:]
                dest_file = dest_dir / file
                shutil.move(src_file, dest_file)

move_dir_initself(LOCATION, NEW_DIR)

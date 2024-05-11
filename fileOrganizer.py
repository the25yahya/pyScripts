#task : File Organizer: Write a script that organizes files in a directory based on their extensions. It should create folders for each unique extension and move corresponding files into these folders.
import os
import shutil

DIR_NAME = input("Enter directory path you want to organize: ")

# Get a list of files in the directory
DIR_LIST = os.listdir(DIR_NAME)

# Extract extensions from filenames
EXTENSIONS = [os.path.splitext(element) for element in DIR_LIST]

for file_tuple in EXTENSIONS:
    file_name, file_extension = file_tuple
    
    # Remove the dot from the file extension
    file_extension = file_extension.lstrip('.')
    
    # Construct the folder path
    folder_path = os.path.join(DIR_NAME, file_extension)
    
    # Create the folder for each file extension if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    # Construct the source file path
    source_file = os.path.join(DIR_NAME, file_name + '.' + file_extension)
    
    # Construct the destination folder path
    destination_folder = os.path.join(folder_path, file_name + '.' + file_extension)
    
    # Move the file to its corresponding folder
    shutil.move(source_file, destination_folder)

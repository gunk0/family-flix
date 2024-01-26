import os
import shutil

# Set the path to the directory containing the folders
directory_path = "/Volumes/Seagate Backup Plus Drive/Flix/content/mov"

# Set the name of the file to be copied
file_path = "/Users/adam/Desktop/movieContent.html"

# Loop through each folder in the directory
for folder_name in os.listdir(directory_path):
    folder_path = os.path.join(directory_path, folder_name)
    if os.path.isdir(folder_path):
        shutil.copy(file_path, folder_path)

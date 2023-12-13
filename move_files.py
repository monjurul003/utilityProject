import os
import shutil

def move_files_to_parent_directory():
    for root, dirs, files in os.walk('.'):
        for file in files:
            # Cut the file from the subdirectory and move it to the parent directory
            shutil.move(os.path.join(root, file), os.path.join(os.getcwd(), file))

move_files_to_parent_directory()
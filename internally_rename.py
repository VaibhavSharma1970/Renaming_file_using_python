# import os
# from datetime import datetime

import os

# Define the root directory containing the subfolders with files
root_directory = '/path/to/root/directory'

# Define a function to rename files in a directory
def rename_files_in_directory(directory_path, new_names):
    file_list = os.listdir(directory_path)
    if len(file_list) != len(new_names):
        print(f"Number of files in {directory_path} and new names don't match.")
        return
    for i, file_name in enumerate(file_list):
        old_path = os.path.join(directory_path, file_name)
        new_path = os.path.join(directory_path, new_names[i])
        try:
            os.rename(old_path, new_path)
            print(f'Renamed: {file_name} to {new_names[i]}')
        except Exception as e:
            print(f'Error renaming {file_name}: {e}')

# Define a dictionary where keys are folder paths and values are lists of new names
folder_rename_mapping = {
    '/path/to/folder1': ['new_name1.txt', 'new_name2.jpg', 'new_name3.png'],
    '/path/to/folder2': ['file1.txt', 'file2.jpg', 'file3.png'],
    # Add more folder paths and corresponding new names as needed
}

# Iterate through the dictionary and rename files in each folder
for folder_path, new_names in folder_rename_mapping.items():
    rename_files_in_directory(folder_path, new_names)
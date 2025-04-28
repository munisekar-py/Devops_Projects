#This program am using minimal OS/sys Modules to build file operations. 
#There are other modules shutil and pathlib can be easy which not Used here.
# Am trying to increase execution more efficient using minimal modules.


import sys
import os
from datetime import datetime

#Defining copy_file() Function

def copy_file(source_path, dest_path):

    try:
        with open(source_path, 'rb') as src_file:
            content = src_file.read()

    #Open the destination file in binary write mode (wb)
        with open(dest_path, 'wb') as dst_file:
            dst_file.write(content)

        print(f"Copied: {os.path.basename(dest_path)}")
    except Exception as e:
        print(f"Failed to copy {source_path}: {e}")

# Check if the file already exists at destination.
def get_unique_filename(destination_dir, filename):
    """Manually checks for duplicate and appends timestamp"""
    dest_file = os.path.join(destination_dir, filename)
    if not os.path.exists(dest_file):
        return filename
    name, ext = os.path.splitext(filename)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{name}_{timestamp}{ext}"

def backup_files_manual(source_dir, destination_dir):
    # Check if source directory exists
    if not os.path.isdir(source_dir):
        print(f"Source directory '{source_dir}' does not exist or is not a directory.")
        return

    # Check if destination exists; if not, manually create it
    if not os.path.isdir(destination_dir):
        try:
            os.mkdir(destination_dir)
            print(f"Destination directory not found, Created...'{destination_dir}'")
        except Exception as e:
            print(f"Cannot create destination directory: {e}")
            return

    # List all items and copy files
    try:
        file_list = os.listdir(source_dir)
        for file_name in file_list:
            src_file_path = os.path.join(source_dir, file_name)

            # Only process regular files (not directories)
            if not os.path.isfile(src_file_path):
                continue

            unique_name = get_unique_filename(destination_dir, file_name)
            dest_file_path = os.path.join(destination_dir, unique_name)
            copy_file(src_file_path, dest_file_path)
    except Exception as e:
        print(f"Error during backup: {e}")

if __name__ == "__main__":
    # Avoid argparse; use sys.argv manually
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]
    backup_files_manual(source_dir, destination_dir)

# -*- coding: utf-8 -*-
"""
Created on Fri May 31 21:53:29 2024

@author: tjlim10
"""
import os

def find_folders_missing_file(directory, target_file):
    # List to store the folders missing the target file
    missing_folders = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        # Check if the target file is in the current folder
        if target_file not in files:
            # If the target file is missing, add the folder to the list
            missing_folders.append(root)
    
    return missing_folders

def write_missing_folders_to_file(missing_folders, output_file):
    with open(output_file, 'w') as f:
        for folder in missing_folders:
            f.write(folder + '\n')

def main():
    directory = "S:\Source_variability\SourceTracker\Exports"  # Replace with the path to your directory
    target_file = 'mixing_proportions.txt'
    output_file = 'missing_files.txt'
    
    missing_folders = find_folders_missing_file(directory, target_file)
    write_missing_folders_to_file(missing_folders, output_file)
    print(f'List of folders missing {target_file} has been written to {output_file}')

if __name__ == "__main__":
    main()

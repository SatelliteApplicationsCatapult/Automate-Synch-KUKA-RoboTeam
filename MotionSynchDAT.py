# This code is to use on a DAT file renamed as a txt file to make the program for the KUKA Robots to work in Synch
# This is useful when you have more than 10 points in the KUKA program for the robots to do in Synch 

# IMPORTANT INFORMATION  #########################################################################
# The POINTS NEED TO BE DEFINED AS SLIN for the program to work and for Synch to work!!!!!!!!
# Points should be named ONLY BY NUMBERS IN ASCENDING ORDER!!!!!!! E.g: 1, 2, 3, ... 800
# This program will go through each point declared
# You will need to process the SRC file as well with the other program MotionSynchSRC.py
# You need to do this for BOTH Robot program that will work in synch

# Make a copy of the DAT file to change and change its type to .txt
# Enter the correct path file and path output with a new name (L31-32). Make sure the name of the generated file is the same as the associated src file program.
# Run the program
# Rename the generated file to be of type .dat
###################################################################################################

import re

# Needed for Synch, change type
to_change_type_L = r"L(\d{1,3})"
sub_type_L = r"LCPDAT\1"

# "replacements" contains the replacement to do defined above. Required for Synch to work
replacements = [
    (to_change_type_L, sub_type_L)
]

# Enter text file Path
# Input: file path for file to change. Model to follow: r"C:\Users\...\File_Name.src"
# Output: file path for file to generate. Model to follow: r"C:\Users\...\File_Name.src"input_file_path = r"C:\Users\Name.Name\Documents\Input_File_name.txt"
input_file_path = r"C:\Users\Name.Name\Document\Input_File_Name.src"
output_file_path = r"C:\Users\Name.Name\Documents\Output_File_name.txt"

# Code will create a new file with the changes wanted
with open(output_file_path, "w+") as new, open(input_file_path, "r") as original:
    for line in original:
        new_line = line
        for pattern, replacement in replacements:
            new_line = re.sub(pattern, replacement, new_line)
        new.write(new_line)
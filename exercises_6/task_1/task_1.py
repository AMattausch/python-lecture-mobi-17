# Task 1: validate FASTA file

import sys
import re # Only required for regex approach
import os.path as op

fasta_paths = sys.argv[1:] # This script will be able to take multiple fasta files as arguments

def validate_fasta(fasta_path):
    valid_characters = "ACGTN"
    with open(fasta_path, mode='r') as fasta_file:
        # The hard way: iterate through all lines & characters, check if they are valid
        for line in fasta_file:
            if line[0] == '>':
                # Handle comment lines
                continue
            else:
                for character in line.rstrip('\n').upper():
                    if not(character in valid_characters):
                        # If an invalid char is found, return false. This also immedeately exits the function, preventing further checking.
                        return False
        else:
            # If the file was checked without occurence of invalid chars, return True
            return True
    
        # Quicker way: regex to the rescue!
        """
        for line in fasta_file:
            if re.search('[^ACGTN]', line.rstrip('\n').upper()) and not line[0] == '>':
                return False
        else:
            return True
        """

for file in fasta_paths:
    if validate_fasta(file):
        print(f"File {op.basename(file)} is a valid file.")
    else:
        print(f"File {op.basename(file)} is not a valid file.")

# Task 2a: create a dictionary with RNA triplets as keys and the corresponding amino acid as values.
# To run these scripts, get the required data from the python lecture website and put them into exercises_5/data/
import os.path as op # Just importing this to get the location of the required files

with open(op.join(op.dirname(__file__), "../data/triplet_code.txt")) as triplet_code: 
    # I'm using a relative path to make this work independent on where the project folder is saved
    # Ignore the op.join() etc. stuff, use absolute paths in yout own scripts.
    triplet_dict = {line.split('\t')[0]: line.rstrip('\n').split('\t')[1] for line in triplet_code.readlines()}

print(triplet_dict)
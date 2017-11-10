# Task 2b: print sorted RNA triplet dict.
import os.path as op

with open(op.join(op.dirname(__file__), "../data/triplet_code.txt")) as triplet_code: 
    triplet_dict = {line.split('\t')[0]: line.rstrip('\n').split('\t')[1] for line in triplet_code.readlines()}

sorted_dict_keys = sorted(triplet_dict.keys())

for key in sorted_dict_keys:
    print(key, triplet_dict[key])
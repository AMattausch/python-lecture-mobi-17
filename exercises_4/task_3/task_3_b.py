# Task 3b: calculate mean of specified column in tab-separated file
import sys
import numpy as np

tsv_path = sys.argv[1]
# Column number shall be 1-based in command line 
col_num = int(sys.argv[2]) - 1 # Make sure to cast as int 

with open(tsv_path) as tsv_file:
    # For each of the input file's row, get the specified column 
    col = [float(line.rstrip('\n').split('\t')[col_num]) for line in tsv_file.readlines()]
    # Calculate and print mean
    mean = np.mean(col)
    print(f"The mean of column {col_num+1} is: {mean}")
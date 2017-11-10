# Task 2b: split CpG content file into lower and upper quartile

import sys
import numpy as np

cpg_content_file_path = sys.argv[1]
lower_quartile_file = sys.argv[2]
upper_quartile_file = sys.argv[3]

# Read the promotor-wise CpG content file
with open(cpg_content_file_path, mode='r') as cpg_file:
    cpg_data = list(cpg_file.readlines())
    cpg_content = [float(line.split('\t')[3]) for line in cpg_data if not line[0] == '#']

# Use numpy's percentile function to get the respectiver percentiles
percentile_25 = np.percentile(cpg_content, 25)
percentile_75 = np.percentile(cpg_content, 75)

# Create list for upper and lower quartile by picking each promotor whose CpG is above/below the percentiles
cpg_lower_quartile =  [line for line in cpg_data if float(line.split('\t')[3]) < percentile_25]
cpg_upper_quartile =  [line for line in cpg_data if float(line.split('\t')[3]) > percentile_75]

# Create new output files for upper and lower quartile
with open(lower_quartile_file, mode='w') as fobj:
    for line in cpg_lower_quartile:
        print(line, file=fobj, end='')

with open(upper_quartile_file, mode='w') as fobj:
    for line in cpg_upper_quartile:
        print(line, file=fobj, end='')
# Task 3a: calculate mean methylation for regions of interest
import sys
import numpy as np

# This script is currently non-functional due to missing input files.
# Its main purpose is to show an example solution to task 3a.

meth_input_file_path = sys.argv[1]
roi_input_file_path = sys.argv[2]
roi_meth_output_path = sys.argv[3]

with open(meth_input_file_path, mode='r') as meth_file:
    cpg_positions = [{'chrom':line.split('\t')[0],
                      'start':int(line.split('\t')[1]),
                      'beta_value':float(line.split('\t')[2])} for line in meth_file.readlines()]

with open(roi_input_file_path, mode='r') as roi_file:
    roi_positions = [{'chrom':line.split('\t')[0],
                      'start':int(line.split('\t')[1]), 
                      'stop':int(line.split('\t')[2]),
                      'beta_list':[]} for line in roi_file.readlines()]

curr_roi = 0
curr_cpg = 0

# Check overlaps, overlapping CpG's beta values will be added to the regions beta_list to later calculate the mean beta value 
while curr_roi < len(roi_positions) and curr_cpg < len(cpg_positions):
    if cpg_positions[curr_cpg]['start']+1 < roi_positions[curr_roi]['start']:
        curr_cpg += 1
    elif cpg_positions[curr_cpg]['start'] >= roi_positions[curr_roi]['stop']: 
        curr_roi += 1
    else:
        roi_positions[curr_roi]['beta_list'].append(cpg_positions[curr_cpg]['beta_value'])
        curr_cpg += 1
        
# Write new BED file with mean beta values
with open(roi_meth_output_path, mode='w') as fobj:
    for roi in roi_positions:
        roi['beta_value'] =  np.mean(roi['beta_list'])
        print(f"{roi['chrom']}\t{roi['start']}\t{roi['stop']}\t{roi['beta_value']}", file=fobj)

# Task 2a: calculate CpG content of regions of interest

import sys

# Get the arguments
cpg_input_file_path = sys.argv[1]
roi_input_file_path = sys.argv[2]
cpg_content_output_path = sys.argv[3]

# Get the data for the CpGs out of the file generated in Task 1
with open(cpg_input_file_path, mode='r') as cpg_file:
    # We are going to create a list of the starting positions.
    # Since we are not going to need any other info on the cpgs than the start position, a simple list of intergers will get the job done.
    # If additional info was needed, one could also create a list of dictionaries with entries for start, stop etc., see the promotor file handling for this.
    cpg_positions = []
    for line in cpg_file.readlines():
        if line[0] == '#':
            continue # If the read line is the header (if there is one) and start with '#', go to next line
        line_data = line.split('\t') # Split the line by its tab delimiters
        cpg_positions.append(int(line_data[1])) # Append cpg start position to our cpg index list, make sure to cast str to int

    # Additional possible solution: use a list comprehension:
    # cpg_positions = [line.split('\t')[1] for line in cpg_file.readlines() if not (line[0] == '#')]

# in a similar way, create a list of dictionaries for the promotor regions

with open(roi_input_file_path, mode='r') as roi_file:
    roi_positions = []
    for line in roi_file.readlines():
        if line[0] == '#':
            continue
        line_data = line.split('\t')
        # Create a dictionary containing the promotor's information
        # Also create a dict entry for the cpg_content
        line_data_dict = {'chrom':line_data[0], 'start':int(line_data[1]), 'stop':int(line_data[2]), 'cpg_count':0} 
        roi_positions.append(line_data_dict) # Append promotor dictionary

    # again, it's also possible to use a list comprehension:
    # roi_positions = [{'chrom':line.split('\t')[0],
    #                   'start':line.split('\t')[1], 
    #                   'stop':line.split('\t')[2],
    #                   'cpg_count':0} for line in roi_file.readlines() if not line[0] == '#']

# Next step: for each promotor region, get the amount of CpGs that lie inside.
# One possible solution would be to check the relative position of each CpG for each promotor region.
# However, since both the promotor regions and the CpGs do not overlap and are in order already, we can simplyfy the process and perform a kind of twin-iteration.
# For both promotor and cpg list, we will have a variable that defines the currently examined CpG/promotor.
# If the current CpG is before the current promotor, go to the next CpG
# If the current CpG is inside the current promotor, increase the promotors CpG counter by one and go to the next CpG
# If the current CpG is behind the current promotor, go to the next promotor and check for the relative position again.

curr_roi = 0
curr_cpg = 0

while curr_roi < len(roi_positions) and curr_cpg < len(cpg_positions):
    # Case 1: end of CpG before current promotor
    if cpg_positions[curr_cpg]+1 < roi_positions[curr_roi]['start']:
        curr_cpg += 1
    # Case 2: start of CpG behind current promotor (note: stop positions are non-inclusive)
    elif cpg_positions[curr_cpg] >= roi_positions[curr_roi]['stop']: 
        curr_roi += 1
    # Case 3: inside current promotor
    else:
        roi_positions[curr_roi]['cpg_count'] += 1
        curr_cpg += 1
        
# Write new BED file with cpg contents
with open(cpg_content_output_path, mode='w') as fobj:
    for roi in roi_positions:
        roi['cpg_content'] = roi['cpg_count'] * 2 / (roi['stop'] - roi['start'])
        print(f"{roi['chrom']}\t{roi['start']}\t{roi['stop']}\t{roi['cpg_content']}", file=fobj)

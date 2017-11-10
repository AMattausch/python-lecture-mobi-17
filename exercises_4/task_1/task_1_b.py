# Task 1b: create index file for specified dinucleotide
# To get the data required for this script, download it from http://hgdownload.soe.ucsc.edu/goldenPath/hg19/chromosomes/chr21.fa.gz
# Decompress the file (e.g. using 7-zip) and store it in the 'data' subdir of 'exercises_4'.

# Step 1: Save the script parameter for the input fasta filename in the variable "input_filename". Save
# the script parameter for the output file name in the variable "output_filename". These parameters
# serve as placeholders for the arguments passed when calling the script.
import sys # Import sys module
input_filename = sys.argv[1] # First parsed argument is input
output_filename = sys.argv[2] # Second parsed argument is output

# Step 2: Read the dinucleotide fom stdin and store it in the variable "dinucleotide".
dinucleotide = input("Enter the DNA dinucleotide to be indexed: ").upper() # Capitalize so we won't have to deal with the case bullshit

# Step 3: Check if "dinucleotide" is a valid DNA base dinucleotide.
permitted_bases = "AGCT"
if not (len(dinucleotide) == 2 and dinucleotide[0] in permitted_bases and dinucleotide[1] in permitted_bases):
    print("Invalid dinucleotide.")
    quit()

# Step 4: Read all lines from the fasta file and store them in a list.
with open(input_filename, mode='r') as input_file:
    data = input_file.readlines()

# Step 5: Get the sequence name of the fasta sequence (hint: the first line of a fasta file always starts
# with a ">" followed by the sequence name).
seq_name = data.pop(0).lstrip('>').rstrip('\n') # .pop(0) also removes the first line from the list
    
# Step 6: Concatenate all lines and store them in a new variable "fasta_sequence".
# Step 7: Replace all newline characters ("\n") with "".
fasta_sequence = ''.join(data).upper().replace('\n', '') # Also capitalize whole sequence

# Step 8: Open the output file for writing.
with open(output_filename, mode='w') as output_file:

    # Step 9: Iterate over the whole fasta sequence stored in "fasta_sequence" and determine for every
    # position if it contains the given dinucleotide. If so, write the sequence name and the position into
    # the output file (separated by a tab ("\t")). Hint: Fasta files consist of lower- and uppercase
    # characters! -> Already took care of that by completely capitalizing it
    pos = 0
    while pos+1 < len(fasta_sequence): # This may take a while...
        if fasta_sequence[pos:pos+2] == dinucleotide:
            # Make a proper BED file, with columns for name, start, stop 
            # (with the stop position NOT included in the dinucleotide)
            print(seq_name, pos, pos+2, sep='\t', file=output_file) 
        pos += 1

# Step 10: Close the fileobjects
# Already took care of that by using 'with open() as file_obj'!

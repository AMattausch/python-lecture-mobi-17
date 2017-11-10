# Task 2c: translate RNA seq to aminoacid seq
import os.path as op

with open(op.join(op.dirname(__file__), "../data/triplet_code.txt")) as triplet_code: 
    triplet_dict = {line.split('\t')[0]: line.rstrip('\n').split('\t')[1] for line in triplet_code.readlines()}

# Load the RNA sequence, strip comment lines (starting with '>')
with open(op.join(op.dirname(__file__), "../data/RNA.fasta")) as rna_file: 
    rna_seq = ''.join([line.rstrip('\n') for line in rna_file.readlines() if not line[0] == '>'])

# Split RNA sequence into a list of three-character-strings
rna_seq_triplets = [rna_seq[i:i+3] for i in range(0, len(rna_seq), 3)]

aa_seq = ''
for triplet in rna_seq_triplets:
    # Look up the triplets corresponding AA in the triplet dict, append it to the AA sequence string
    aa_seq += triplet_dict[triplet]

print(aa_seq)
# Task 1c: check wheter sequence is DNA/RNA/invalid

dna_seq = "gattaca"
rna_seq = "GAUUacA"
invalid_seq_1 = "XYZ" # Contains invalid character
invalid_seq_2 = "AAAUT" # Contains both DNA nd RNA characters
indet_seq = "AAAAA" # No U/T, indeterminable whether RNA or DNA

permitted_letters = "ATCGU" # Now also with U

seq_list = [dna_seq, rna_seq, invalid_seq_1, invalid_seq_2, indet_seq] # Put all sequences into a list, so we can iterate over them
for seq in seq_list: # Perform the validation for each sequence by iterating over the list of sequences
    print("Validating sequence:", seq)
    # First check for invalid letters
    seq = seq.upper()
    for letter in seq: 
        if not letter in permitted_letters:
            print("Sequence invalid, contains invalid letters!")
            break
    else: # Once the sequence as made it through the first check, determine whether it's DNA or RNA
        if not ('U' in seq and 'T' in seq): # Make sure sequence does not contain both U and T
            if 'U' in seq:  # Triggers if seq is RNA
                print("Sequence is RNA")
            elif 'T' in seq: # Triggers if seq is DNA
                print("Sequence is DNA")
            else: # Triggers in any other case
                print("Impossible to determine whether sequence is RNA or DNA!")
        else:
            print("Sequence invalid, contains both U and T!")


# An additonal approach for RNA/DNA checking (assuming it has already been checked for invalid characters)
seq = "ATCUG"
if (('U' in seq) ^ ('T' in seq)): # '^' marks and exclusive or, that will only trigger if exactly one of the conditions is true
    if 'U' in seq:  # Triggers if seq is RNA
        print("Sequence is RNA")
    elif 'T' in seq: # Triggers if seq is DNA
        print("Sequence is DNA")
elif ('U' in seq and 'T' in seq):
    print("Sequence invalid, contains both U and T!")
else:    
    print("Impossible to determine whether sequence is RNA or DNA!")



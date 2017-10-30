# Task 2a: calculate RevComp strands for each sequence

seq_list = ["ACGT",
            "GATTACA",
            "TTAACCGG"] # List / dict definition also works over multiple lines!


for seq in seq_list:
    # Approach one: use replace statements
    print(seq.replace('A', 't') # replace all bases and make them lower-case, so they are not replaced by the other replace statements
             .replace('T', 'a')
             .replace('G', 'c')
             .replace('C', 'g')
             .upper() # Capitalize the sequence again
             [::-1]) # Use and index to revert the sequence as we want it in 5'-3' order

    # Approach two: use a dictionary to translate the sequence
    comp_dict = {'A':'T',
                 'T':'A',
                 'G':'C',
                 'C':'G'}
    
    comp_seq = '' # Start with an empty sequence
    for base in seq:
        comp_seq += comp_dict[base] # Append the complementary base
    print(comp_seq[::-1]) # Print the reverted complementary sequence
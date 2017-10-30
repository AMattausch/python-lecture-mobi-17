# Task 1d: get counts statistics for the sequence

dna_seq = "GATTACA"
rna_seq = "GAUUACA"

permitted_letters = "ATCGU"

seq_list = [dna_seq, rna_seq]
for seq in seq_list:
    print("Validating sequence:", seq)
    seq = seq.upper()
    for letter in seq: 
        if not letter in permitted_letters:
            print("Sequence invalid, contains invalid letters!")
            break
    else:
        if not ('U' in seq and 'T' in seq):
            if 'U' in seq:
                print("Sequence is RNA")
            elif 'T' in seq:
                print("Sequence is DNA")
            else:
                print("Impossible to determine whether sequence is RNA or DNA!")
                continue 
                # This will stop further execution of the current iteration and jump to the next iteration of the containing loop 
                # (i.e. go to next sequence)
        else:
            print("Sequence invalid, contains both U and T!")
            continue # same as above
        # After passing the above checks, create statistics for each base
        stats_dict = {} # Create an empty dictionary for the statistics

        # As we want to treat both DNA and RNA, we better create this dictionary dynamically to fit the possible bases
        for letter in seq: # Most simple approach (however it's quite redundant)
            stats_dict[letter] = 0
        # Additional approach that will only set the entries for each unique letter:
        for letter in set(seq):
            stats_dict[letter] = 0
        # Third approach, using a comprehension, making the whole thing a one-liner 
        # for comprehensions, check LP part IV, chapter 20, super useful stuff - while not of relevance for the exam I suppose
        stats_dict = {letter:0 for letter in set(seq)}

        for letter in seq:
            stats_dict[letter] += 1
        
        sequence_length = len(seq) # The length of a string (or any other iterable, such as lists) can easily be determined using len()

        print("Counts for each base:", stats_dict)      
        print("Total length of the sequence:", sequence_length)

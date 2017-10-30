# Task 1f: is this possible without using lists?
# Answer: Yes! Apart from the seq_list, I haven't used a single list in this script. 
# Instead, it relies on the fact that python string are iterable and indexable, just like python lists are.
# This also allows for faster coding, since "ABC" is faster to type than ['A', 'B', 'C'].

dna_seq = "GATTACA"
rna_seq = "GAUUACA"

permitted_letters = "ATCGU"

seq_list = [dna_seq, rna_seq]
i = 0
while i < len(seq_list):
    seq = seq_list[i].upper()
    i += 1
    print("Validating sequence:", seq)
    j = 0
    while j < len(seq):
        letter = seq[j]
        j += 1 
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
        else:
            print("Sequence invalid, contains both U and T!")
            continue
        stats_dict = {letter:0 for letter in set(seq)}

        k = 0
        while k < len(seq):
            letter = seq[k]
            k += 1
            stats_dict[letter] += 1
        
        sequence_length = len(seq)

        print("Counts for each base:", stats_dict)      
        print("Total length of the sequence:", sequence_length)

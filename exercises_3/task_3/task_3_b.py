# Task 3b: calculate amount of possible ORFs
# I consider an ORF to be at least six base pairs long (one start codon and one stop codon).
# One could calculate the number of possible ORFs mathematically, 
# however since the script is intended to be extended to further examine the sequence, we are going to use loops

seq_list = ["AAAAAA", # Exactly 1 ORF
            "AAAAAAA", # 2 ORFs
            "AAAAAAAAA", # 5 ORFs: 4 for 2-Codon ORFs, 1 for 3-Codon-ORFs
            "GCAGTCGTATCG",
            "GTCTAGGCTCTTATACTA",
            "CAGCT"] # Too short to contain an ORF

for seq in seq_list:
    possible_orfs = 0
    # I will actually use while loops for this!
    orf_length = 6
    while orf_length <= len(seq):
        frame_shift = 0
        while orf_length + frame_shift <= len(seq):
            possible_orfs += 1
            frame_shift += 1
        orf_length += 3
    print(f"Sequence {seq} has {possible_orfs} possible ORFs.")
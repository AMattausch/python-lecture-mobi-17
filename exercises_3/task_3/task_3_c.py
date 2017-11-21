# Task 3c: check for hypothetical proteins

seq_list = ["AUGUGA", # 1 Hypotherical protein
            "TTTAUGTTTUAG",
            "TTTAUGTUGA", # Start and stop codon with different frame shifts -> not hyp. protein
            "AUGTAUGTTUGATUAG", # Two overlapping proteins with different frame shifts
            "TTTTAUGTT", # Start codon, but no stop codon 
            "TTTTUAATT", # No start codon
            "TTTTTTTTT"] # No start or stop codon

stop_codons = ["UGA", "UAA", "UAG"]

for seq in seq_list:
    possible_orfs = 0
    orf_length = 6
    while orf_length <= len(seq):
        frame_shift = 0
        while orf_length + frame_shift <= len(seq):
            possible_orfs += 1
            frame_shift += 1
        orf_length += 3
    print(f"Sequence {seq} has {possible_orfs} possible ORF(s).")

    hypo_proteins = 0
    frame_shift = 0
    while frame_shift+3 < len(seq):
        if seq[frame_shift:frame_shift+3] == 'AUG': # Check wheter the current codon is a start codon
            codon_offset = 3 # Next codon is 3 bases away
            while frame_shift+3+codon_offset < len(seq): # Iterate in 3-base-steps over the rest of the sequence
                if seq[frame_shift+codon_offset:frame_shift+codon_offset+3] in stop_codons: # Check whether the current codon in the list of stop codons
                    hypo_proteins += 1
                    break # Stop checking for further stop codons
                else:
                    codon_offset += 3
        frame_shift += 1
    
    print(f"Sequence contains {hypo_proteins} hypothetical protein(s)")
# Task 3d: substrings for hypothetical proteins

seq_list = ["TTTAUGTTTUAG",
            "TTTAUGTUGA",
            "AUGTAUGTTUGATUAG"]
            
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
    while frame_shift+2 <= len(seq):
        if seq[frame_shift:frame_shift+3] == 'AUG':
            codon_offset = 3
            while frame_shift+codon_offset <= len(seq):
                if seq[frame_shift+codon_offset:frame_shift+codon_offset+3] in stop_codons:
                    hypo_proteins += 1
                    hypo_prot_seq = seq[frame_shift:frame_shift+codon_offset+3] # Just some indexing to get the substring
                    print(f"Hypothetical protein {hypo_proteins}:",hypo_prot_seq)
                    break
                else:
                    codon_offset += 3
        frame_shift += 1
    
    print(f"Sequence contains {hypo_proteins} hypothetical protein(s)")
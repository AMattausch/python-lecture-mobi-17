# Task 3a: calculate GC content

seq_list = ["ACGT",
            "TTCCGG",
            "CCCCCCC",
            "AAAAAAA"]

for seq in seq_list:
    # Most simple approach in my opinion (without list comprehensions or lists at all):
    gc_content = (seq.count('G') + seq.count('C'))/len(seq)
    print(f"GC content of sequence {seq}: {gc_content}") 

# Use a list comprehension instead of a for loop:
# Make way more sense if you want to store the result instead of directly printing it
[print(f"GC content of sequence {seq}:", (seq.count('G') + seq.count('C'))/len(seq)) for seq in seq_list] # Creates a list with the GC content for each sequence

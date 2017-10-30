# Task 1b: check if the sequence only contains permitted letters (i.e. A, T, C, G)

seq = "GATTACA"

permitted_letters = "ATCG" # One could also use ['A', 'T', 'C', 'G'], or list("ATCG")

seq = seq.upper() # Capitalize the whole sequence, easy way to make the validation case-insensitive
for letter in seq: # This loop will iterate letter-by-letter over seq 
    if not letter in permitted_letters:  # This conditional will trigger if the current letter is NOT in the permitted letters
        print("Sequence contains invalid letters!")
        break # This will stop the loop at once, preventing further iterations
else: 
    # Similar to if-conditionals, for-loops can have en else-statements that will trigger on successful completion of the loop 
    # (i.e. it was not interrupted by a break statement)
    print("Sequence contains only valid characters")


# Different approach with a negative control:
invalid_seq = list("AAAXYZAAA") # Sequence now as a list
# Due to the break statement, we should only receive a single warning for this sequence

for letter in invalid_seq:
    if not letter in permitted_letters:
        print("Sequence contains invalid letters!")
        break
else:
    print("Sequence contains only valid characters")
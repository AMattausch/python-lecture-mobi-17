# Task 1a: convert a string-type sequence to a list of individual characters

seq = "GATTACA"

seq_list = list(seq)    # Since strings are iterables, you can easily convert them to a list using the list() method
# For more about lists, see LP Part II Chapter 8: 'Lists and dictionaries'

print("Sequence as string:", seq) # GATTACA
print("Sequence as list:", seq_list) # ['G', 'A', 'T', 'T', 'A', 'C', 'A']

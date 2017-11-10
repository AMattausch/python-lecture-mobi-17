# Task 1 s: sort list by sum of sublists

l = [[4, 3], [2, 7], [1, 8], [9, 1], [5, 6]]
# Sorted by using a lambda function as key
sorted_l = sorted(l, key=lambda x: sum(x))
print(sorted_l)
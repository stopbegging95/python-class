numbers = (1, 2, 3, 3, 4, 5, 6, 6, 6, 6, 7, 8, 9, 10, 10, 10, 5, 5, 8, 8, 8, 8)

# get the total number of 6, 5, and 8 in the tuple
print(numbers.count(6))
print(numbers.count(5))
print(numbers.count(8))

# get total number in the tuple
print(len(numbers))

# get the max number in the tuple
print(max(numbers))

# get the min number in the tuple
print(min(numbers))

# sort the tuple in ascending order
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# sort the tuple in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)


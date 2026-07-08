first = (1, 2, 3, 4, 5)
second = (6, 7, 8, 9, 10)

# nesting tuples in a list
print([first, second])

third = [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)]
print(third)

fourth = ("a", "b", "c", "d", "e")
third.append(fourth)
print(third)

third.remove(fourth)
print(third)
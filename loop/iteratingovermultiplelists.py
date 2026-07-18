# combining lists with zip()
# names = ["alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# cities = ["NYC", "LA", "Chicago"]

# for name, age, city in zip(names, ages, cities):
#     print(f"{name} is {age} years old and lives in {city}")

# zip with different lengths - stops at shortest
# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c', 'd']

# for num, letter in zip(list1, list2):
#     print(f"{num}: {letter}")

# using zip_longest to handle different lengths
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
from itertools import zip_longest
for num,letter in zip_longest(list1, list2, fillvalue="N/A"):
    print(f"{num}: {letter}")
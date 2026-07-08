# using the unpacking functionality
myname = ("ibrahim")
print(tuple(myname))

number = (1, 2, 3, 4, 5)
a, b, c, d, e = number
print(a, b, c, d, e)

a, *b, c = number
print(a, b, c)

nums = ("1", "2", "3", "4", "5", "6", "7")
print(nums)

del nums
print(nums)
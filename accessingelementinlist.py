# mixture = [1, 4, "Simplelearn", "Get", "Certified"]
# print(mixture[3])
# print(mixture[-2])
# print(mixture[:3])
# print(mixture[3:])
# print(mixture[-2:])
# print(mixture[2:4])

# get 1, "Simplelearn", and "Certified"
# mixture2 = [1, 4, "Simplelearn", "Get", "Certified", "Medical", "Doctor"]

# printingout = "Getting 1, Simplelearn, and Certified ="
# print(printingout, mixture2[::1])
# print(printingout, mixture2[0:])
# print(printingout, mixture2[::2])
# print(printingout, mixture2[::3])

# Operation in list
# zero = [0] * 100
# print(zero)

# concantination
letters = ['a', 'b', 'c', 'd']
words = ["get", "Certified", "Get", "ahead"]
conc = letters + words
print(conc)

# Printing other numbers
num = [1,2,3,4]
one, *other = num
print(one)
print(other)

# method in lists
num3 = [1,2,3,4,5,6,7]
num3.append(8)
print(num3)
num3.insert(7, 10) 
# insert check for index and replace the number in that index with the second value in the insert function, while
#  the first number check for the index position of the number in the list
print(num3)

# removing the added value added to the list with insert function
num3.remove(10)
print(num3)

# sorting of alphabets
var1 = ['c', 'e', 'a', 'b', 'd']
var1.sort()
print(var1)
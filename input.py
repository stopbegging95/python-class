age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")


# addition of two numbers
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

sum = number1 + number2

print("Sum of the first and second number is equal to ", sum)

# Using float() for decimal number
price = float(input("Enter the price: "))
print("The price of the item paid for is ", price)

# Input with string concatenation
first_name = input("First name: ")
last_name = input("Last name: ")

full_name = first_name + " " + last_name
print("Your full name is ", full_name)

name = "Umar001"
age = 25
print(f"My name {name} and I am {age} years")
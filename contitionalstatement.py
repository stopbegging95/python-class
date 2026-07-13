# python if statement
age = 20
if age >= 18:
    print("You are an adult")

score = 80
if score >= 30:
    print("You Passed")

# the if... else statement
newage = 16

if newage >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")

# even and odd numbers
numbers = 5

if numbers % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# The if...elif...else Statement

# if condition1:
#     # code
# elif condition2:
#     # code
# else:
#     # code

score = 75

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Fail")

# Nested if statement

manage = 70
has_id = True 

if manage >= 68:
    if has_id:
        print("You can enter")

# testing with username and password
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong Username or Password Try Again!")


# Using Logical Operators in Conditions

# using the AND logical operator 
votingage = 25
citizen = True
if votingage >= 18 and citizen:
    print("You are eligible to vote.")

# or condition
dayoftheweek = "Tuesday"

if dayoftheweek == "Wednesday" or dayoftheweek == "Tuesday":
    print("This is week day")
else:
    print("It weekend")

# using the not conditional statement 
logged_in = True

if not logged_in:
    print("Please log in")
else:
    print("You are logged in")
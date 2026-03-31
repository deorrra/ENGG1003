# Question 1
print("Question 1\n")
print("a/")
a = 3.5
b = 10.5
c = 3
x = 2
y = a * x ** 2 + b * x // (2 * a) + c       # ax^2 + bx/2a +c
print(y)

print("\nb/")
d = (- b - ((b ** 2) - (4 * a * c)) ** (1 / 2)) / (2 * a)
print(d)

# Question 2
print("\nQuestion 2\n")
print("a/")

import math                 # Imports a list of variables specific for math functions
pi = math.pi                # Sets the variable pi as equal to the float value of pi from the math library
print(f"{pi:.8f}")          # Prints the variable pi to 8 decimal places

print("\nb/")

num2b = 4 ** 6              # Sets the variable num2b as equal to 4 to the 6th power.
print(f"{num2b:10d}")       # Prints the integer in a field with a width of 10 characters, the characters preceding the integer are ' ' or blank space.

# Question 3
print("\nQuestion 3\n")

total = -30                  # total cost of items in dollars
is_member = True            # True if the customer is a member, otherwise False

# Side line comments will explain the statement in plain text

if total < 0:                               # If the total is less than zero dollars
    print("Invalid total")                  # Invalid total will be printed
elif total >= 30 and is_member == True:     # However if the total is greater than or equal to thirty dollars and the customer is a member
    print("Shipping: $0")                   # Then the shipping cost is zero dollars
elif is_member == False and total >= 50:    # If the customer is not a member but the total is greater than or equal to fifty dollars
    print("Shipping: $0")                   # Then the shipping cost will also be zero dollars
else:                                       # In any other case of the total cost
    print("Shipping: $5")                   # The shipping cost will be five dollars
def function():             # defines the function + function name
    print("Hello World")    # The code within the scope of the function that will run when called

function()                  # The function call


def first_function():
    print("We did it!")

first_function()


# Arguments
def num_squared(num):       # The num is the argument of this function. It is something that can be specified in a function call
    print(num ** 2)         # The operation squaring the number argument

num_squared(5)

def num_powered(num, power):    # Both of these arguments must be called later otherwise there will be a type error as only calling one argument is incompatible with a function that requires two args!
    print(num ** power)

num_powered(5, 3)

def number_args(*number):           # The star preceding the argument name is a wildcard. This states that you don't know the exact amount of arguments that would pass through the function.
    print(number[0] * number[1])

number_args(5, 6, 1, 2, 8)  #tuple!

# Since you dont need to pass a tuple or other data collection type in the function call we can just call a pre existing collection

x = (8, 2, 1, 6, 5)
number_args(*x)     # The star is required for this argument as it defines the range of the tuple. Without the star it will call the nth element of the tuple, which is not defined. The star basically confirms that the range is the amount of elements in the tuple (whatever we add in).


def number_kwarg(**number):     # The double star indicates that the number argument will be satisfied by a later defined number of keywords when calling the function
    print(f"My number is: {number['integer']}. My other number is: {number['integer2']}")   # integer 1+2 are the keywords here that have been defined in the function call. they are written as strings as the function requires them to match the data type of their variable.

number_kwarg(integer = '2309', integer2 = '23')     # integer and integer2 are the random keywords. they could be named anything (i believe they have to be strings though


# Return statements

def add(x, y):
    return x + y

print(add(3, 5))

def add2(x, y):
    print(x + y)

add2(3, 5)

def add3(x, y):
    print(x + y)

result = add3(3, 5)         # Ass the error states. The function doesn't return anything. It will still print the sum as the arguments are defined. but the value of the function is still left as empty.  Thus, also printing None.
print(result)                     # Because we set the value of the satisfied function to a variable. The function will never be fully defined. Removing the variable component fixes this error, as shown above.
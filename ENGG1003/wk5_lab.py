# Question 1
print("Question 1")

def f():
    return 42

def g(x):
    return x ** 2

def h(x, y):
    return x * y

x = f()
print(x)

print(g(x))

y = 2
print(h(x, y))



# Question 2
print("\nQuestion 2")

x = [8, 2, 3, -1, 7.5]

def mult(arr):
    result = 1

    for val in x:
        result *= val
    return result

print(mult(x))


# Question 3
print("\nQuestion 3")

import math
def areapoly(n, s):
    A = (1/4) * n * (s**2) * math.atan(math.pi/ n)
    return A

n = 5
print(areapoly(n, s=1))
print(areapoly(n, s=2))

# Question 4
print("\nQuestion 4")

x = [0, 5, 1, -6, 4, 7, -3, -27, 6, -2, 8]

def myminmax(arr):
    smallest = arr[0]
    largest = arr[0]
    for val in arr:
        if val < smallest:
            smallest = val
        if val > largest:
            largest = val

    return smallest, largest

print(x)
low, high = myminmax(x)
print(f"lowest = {low}")
print(f"array minimum = {min(x)}")
print(f"lowest = {high}")
print(f"array maximum = {max(x)}")

# Question 5
print("\nQuestion 5")

x = [1.624, -0.611, -1.072, 0.865, -2.301, 1.744, -0.761, 0.319, -0.249]

def minpos(x):
    mp = math.inf
    idx = 0

    for i in range(len(x)):
        if 0 < x[i] < mp:
            mp = x[i]
            idx = i


    return mp, idx
mp, idx = minpos(x)
print(f"smallest = {mp}")
print(f"index of smallest = {idx}")


# Question 6
print("\nQuestion 6")

# 1. Create factorial function
# 2. loop over the number terms we want to compute
# 3. Compute the coefficient
# 4. Compute the odd exponents of the x value
# 5. Flip sign every term
# 6. Multiply by 2 / sqrt(pi)

def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def erf(x, num_terms):
    result = 0

    for n in range(num_terms):
        # 3
        coefficient = 1 / factorial(n) * (2*n + 1)

        # 4
        odd_exponent = 2*n + 1

        result += ((-1) ** n) * coefficient * x * odd_exponent

        # 5
        #(-1) ** n
    return result
print(factorial(3))
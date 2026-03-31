# Part a

# The slope-intercept form of a straight line is denoted: y = mx + c

def straight_line(c1, c2, x):       # Naming the function 'straight_line' and defining the arguments to be used in the straight line formula.
    y = (c1 * x) + c2               # Adjusting the arguments to the slope-intercept form above: y = c1x + c2
    return y                        # When the function is called and the arguments are passed. The value of y will be returned.

# Part b

# A parabolic line is a polynomial with a degree of 2: y = ax^2 + bx + c, where a =/= 0.

def parabolic_line(c1, c2, c3, x):
    y = (c1 * x**2) + (c2 * x) + c3
    return y

# Part c

# A cubic line is a polynomial with a degree of 3: y = ax^3 + bx^2 + cx + d, where a =/= 0.

def cubic_line(c1, c2, c3, c4, x):
    y = (c1 * x**3) + (c2 * x**2) + (c3 * x) + c4
    return y

# Part d

# A polynomial with degree n: y = c_1x^n + c_2x^n-1 + c_3x^n-2 + ... + c_n

# coeffs is a list with length n
# x as before

coeffs = [1, 2, 3]
#   the value n which will be equal to the last element of coeffs
# the value used must count from 0
# [0] = c1, [1] = c2, [2] = c3
# => c_n = coeffs[n] + 1

def general_polynomial(coeffs, x):
    y = (coeffs[n] + i) ** (n - i)

    return y


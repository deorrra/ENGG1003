# Part a

import integration as integ

#T = integ.trapezoidal(f, a, b)
#S = integ.simpson(f, a, b)
# f(x) = \int_{0}^{1} (7+14x^6) dx


# def trapezoidal_vs_polynomial
# Evaluate the integral using trapezoidal rule - approximating the region under the graph of the function from a,b with trapezoidal
# Area of a rectangle + triangle => integrate between a,b
# 1/2(b - a)(f(a) + f(b))


# algebraic integration => multiply by the reciprocal of the increased power.
# return exact value


def f(x):
    f = 7 + 14 * x ** 6
    return f

T = integ.trapezoidal(f, 0, 1)
print(T)



# def simpson_vs_polynomial


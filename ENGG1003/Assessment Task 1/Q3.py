# Part a

def add(a, b):
    return a + b

# Part b

def sub(a, b):
    return a - b

# Part c

def mult(a, b):
    return a * b

# Part d

def div(a, b):
    return a / b

# Part e

def simple_calc(eq):
    eq = eq.split(" ")
    a = int(eq[0])
    op = eq[1]
    b = int(eq[2])

    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mult(a, b)
    elif op == "/":
        return div(a, b)
    else:
        return "Inoperable equation"
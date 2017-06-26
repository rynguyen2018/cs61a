# Names
x = 1
y = x + x
x, y = x + y, x


# Environment Diagrams
x = 1
y = x
x = 2
x, y = x + y, x


# Let's see it in action
f = min
f = max
g, h = min, max
max = g
max(f(2, g(h(1, 5), 3)), 4)


# User-defined Functions
def square(x):
    return x * x
y = square(-2)


# Multiple Environments
y = square(square(3))


# None
def does_not_return_square(x):
    x * x
does_not_return_square(4)
sixteen = does_not_return_square(4)
# sixteen + 4 # Error!


# Nested Print Expressions
print(print(1), print(2))


# More Functions
def describe(f, x):
    """
    >>> four = describe(square, -2)
    Calling function with argument -2
    Result was 4
    >>> four
    4
    >>> sixteen = describe(square, four)
    Calling function with argument 4
    Result was 16
    >>> sixteen
    16
    """
    print('Calling function with argument', x)
    result = f(x)
    print('Result was', result)
    return result
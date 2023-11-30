def add(x, y):
    return x + y


def subtract(x, y):
    pass


def divide(x, y):
    x = float(input("First number: "))
    y = float(input("Second number: "))

    if y != 0:
        result = x / y
        print({result})
    else:
        print("You cannot divide by zero!!!")
    return


def multiply(x, y) -> int:
    pass


def square(x):
    pass


def power(x, y):
    return x**y


def sqrt(x):
    pass


def power_of(base, exponent):
    result = pow(base,exponent)
    return result


def trick(x):
    """
    as an input this takes String and print it
    """
    pass

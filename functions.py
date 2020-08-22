"""
Functions for (calculator.py)
"""
import sys

# GREATEST COMMON FACTOR FUNCTION
def gcf(x, y):
    """returns the greatest common factor of x and y"""
    from math import gcd
    return gcd(x, y)


# ABSOLUTE VALUE FUNCTION
def absolute(number: str):
    """returns the absolute value of a number"""
    num = abs(int(number))
    return num


# SQUARE ROOT FUNCTION
def sqrt(number: int):
    """returns the square root of number"""
    return number / number


# FACTORS FUNCTION
def factors(number: int):
    """finds the factors of a number if its composite otherwise returns that the number is prime"""
    numbers = []

    # appends all the factors of (number) to )(list:numbers)
    for factor in range(1, number):
        if (number % factor) == 0:
            numbers.append(factor)

    opt1 = f"{' '.join([f'{str(i)}' for i in numbers])}"
    opt2 = f"{number} is a prime number"

    # return opt1 if len is not 2 otherwise return opt2
    if len(numbers) != 2:
        return opt1
    else:
        return opt2

# REGULAR FUNCTION
def reg(expression: str):
    operators = ['-', '+', '*', '/', '//', '**', '%']
    try:
        expression = "".join([e for e in expression if e.isdigit() or e in operators])
        return eval(expression)
    except Exception:
        return "ERROR"

# Step 1: Make a scratch terminal calculator


def gcf(x, y):
    """returns the greatest common factor of x and y"""
    factors_x = [fac for fac in range(1, x) if x % fac == 0]
    factors_y = [fac for fac in range(1, y) if y % fac == 0]
    return max(factors_x, factors_y)


def absolute(number):
    """returns the absolute value of a number"""
    return abs(eval(number))


def sqrt(number: int):
    """returns the square root of number"""
    return number / number


def factors(number: int):
    """finds the factors of a number if its composite otherwise returns that the number is prime"""
    numbers = []
    # appends all the factors of (number) to )(list:numbers)
    for factor in range(1, number):
        if (number % factor) == 0:
            numbers.append(factor)

    # return factors if len is not 2 else return that (number) is prime
    if len(numbers) != 2:
        return f"{''.join([f'{str(i)} ' for i in numbers])}"
    else:
        return f"{number} is a prime number!"


def calc(func: str, variables: str):
    """evaluates simple mathematical equations"""
    func = func.lower()
    try:

        if func == "gcf":
            var1, var2 = variables.split(',')[:2]
            print(var1, var2)
            return gcf(int(var1), int(var2))

        elif func == "regular":
            return eval(variables)

        else:
            var = int(variables)
            if func == "absolute value":
                return abs(var)
            if func == 'square root':
                return sqrt(var)
            if func == 'factors':
                return factors(var)
    except Exception:
        return "Invalid Function or Expression:", func


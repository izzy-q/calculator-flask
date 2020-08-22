"""
Calculator Module
"""

import functions as f


def calc(func: str, variables: str):
    """evaluates simple mathematical equations"""
    func = func.lower()
    try:
        if func == "gcf":
            var1, var2 = variables.split(',')[:2]
            return f.gcf(int(var1), int(var2))

        elif func == "regular":
            return f.reg(variables)

        else:
            var = int(variables)
            if func == "abs":
                return f.absolute(var)
            if func == 'sqrt':
                return f.sqrt(var)
            if func == 'factors':
                return f.factors(var)

    except Exception:
        return "Invalid Function or Expression:", func

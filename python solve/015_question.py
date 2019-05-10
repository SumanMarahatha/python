import math


def sqt(x):
    if isinstance(x, (int, float)):
        return math.sqrt(x)
    else:
        return "Type Error!"


print(sqt(4))

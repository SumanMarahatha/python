def isSum(n1, n2, n3):
    if n1 == (n2 + n3):
        return True

    return False


def isDifference(n1, n2, n3):
    if n1 == (n2 - n3):
        return True

    return False


def isProduct(n1, n2, n3):
    if n1 == (n2 * n3):
        return True

    return False


# Get three numbers a, b  and c
a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))

if isSum(a, b, c)



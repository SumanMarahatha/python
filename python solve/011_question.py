class Iterator:
    def __init__(self, n):
        for i in range(n):
            print(i,)


def factors(n):
    facts = []

    for i in range(1, n // 2):
        if n % i == 0:
            facts.append(i)

    facts.append(n)

    return facts


a = Iterator(10)
print(factors(48))

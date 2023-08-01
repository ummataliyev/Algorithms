def date(n):
    print(n)
    if n <= 1:
        return
    else:
        date(n-1)


date(10)


def fact(x):
    """Calculator for factorail"""
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


print(fact(5))

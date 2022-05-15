from ast import Num


def digitize(n):
    n = [int(i) for i in str(n)[::-1]]
    return n

"n = list(map(int, str(num)))"

print(digitize(35718))
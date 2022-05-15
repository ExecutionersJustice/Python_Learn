def sumOfNumbers(a, b):
    sum = 0
    if (a == b):
        return a
    else:
        while (a < b):
            sum += a
            a += 1
        while (a > b):
            sum += a
            a -= 1
        return sum + b

print(sumOfNumbers(-2, 6))

def sumOfNumbers2(a, b):
    sum = 0
    if (a == b):
        return a or b
    elif (a <= b):
        while (a <= b):
            sum += a
            a += 1
    else:
        while (a >= b):
            sum += a
            a -= 1
    return sum

print(sumOfNumbers2(2, 6))

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
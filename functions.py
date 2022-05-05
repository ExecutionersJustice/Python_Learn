def stringFormat (s):
    if " " in s:
        s = s.upper()
    else:
        s = s.lower()
    return s

print(stringFormat("Gavno Zhopa"))


def getSum(a, b, c=0, d=1):
    return a + b + c + d

print(getSum(5, 8))


def getSum2(z, x, h=0, f=1): 
    return z + x + h + f
    # h/f - имен. аргументы, z/x - позиц. аргументы. Позиц. аргументы должны стоять перед имен.аргументами

print(getSum2(25, 40))
print(getSum2(25, 40, f=17))

# def function(*arguments, **keywordArguments): # * - позиционные аргументы, преобразует в кортеж
# ** - именованные аргументы, преобразует в словарь
    
def sumCal(*arguments):
    return arguments

print(sumCal(1, 5, 10))

def sumCal2(*arguments):
    return sum(arguments)

print(sumCal2(1, 5, 10))

def func(**keywordArguments):
    print(keywordArguments)

func(a=1, b=5, c=20)

def funcc(a, x, *arguments, **keywordArguments):
    print(a)
    print(x)
    print(arguments)
    print(keywordArguments)

funcc(55, 77, 86, 96, b="Test", c="Hi")

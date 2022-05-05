def findSum(n):
    sum = 0
     for element in range(n + 1):
         if element % 3 == 0 or element % 5 == 0:
             sum += element 
     return sum

def findSum2(n):
     return sum(i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0)

            

findSum(5) # return 8 (3 + 5) 
findSum(10) # return 33 (3 + 5 + 6 + 9 + 10)

print(findSum2(10))


def gavno():
    return sum(i for i in range(1, 11))


print(gavno())



names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]

def get_names(names):
    for element in names:
        if len(element) != 4:
            names.remove(element)
    return names

print(get_names(names))
        
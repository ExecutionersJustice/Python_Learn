myList = [1, 2, 3, "hello", "world", True]
print(myList)

myList2 = list("Hello")
myList3 = list((1, 2, 3))

print(myList2, myList3)

myList4 = [i for i in "Hello"] # same as myList2 = list("Hello")
myList5 = [i for i in "Hello World" if i not in ["a", "e", "i", "o", "u", " "]]

print(myList5)



print(list(range(1, 11))) #если печатать range() то отдаст (1, 11) тк это генератор (не отдает последовательноть одну за другой)


for i in range(1,4):
    print(f"Внешний цикл {i}")
    for j in range(1, 4):
        print(f"Внутренний цикл {j}")
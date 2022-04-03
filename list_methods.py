myList = [1, 2, 3, "hello", ["test", 10], "world", True]

print(len(myList))
print(myList[4][0]) # достает элемент списка ["test', 10] в списке myList
print(myList[0:3]) # получить элменты от 0 до 3 (3 не входит в последовательность)


people = ["Ivan", "Slava", "Ilya"]
print(people[0])

people[1] = "Nika"
print(people)

people[:2] = ["Valera", "Denchik"]
print(people)

people.append("Putin") # Добавляет новый элемент списка
print(people)

ukraine_president = ["Zelenskiy"]
people.extend(ukraine_president) # Добавляет в список people элементы списка ukraine_president 
print(people)

people.insert(3, "Baiden") # (Добавляет элемент в список на позицию)
print(people)

people.remove("Putin") # Удаляет элемент списка (только первый попавшийся)
print(people)

peopleWithoutBaiden = people.pop(3) # Удаляет n-ый элемент и возвращает его в переменную. Если индекс не указан, возвращает последний элемент списка
print(people, peopleWithoutBaiden)

print(people.index("Denchik")) # Возвращает положение первого элемента со значением X

numbers = [7, 5, 6, 1, 9, 4, 3, 2]
print(numbers.index(6))
print(numbers.count(5)) # Возвращает количество элементов со значением X
numbers.reverse()
print(numbers)

numbers = sorted(numbers) # Функция sorted() сортирует список
print(numbers)

# numbers.reverse() - Разворачивает список
# numbers.copy() - Возвращает копию списка
# numbers.clear() - Очищает список, список становиться пустым []

digits = numbers.copy()
print(digits)

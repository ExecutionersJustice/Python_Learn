def multiplicationTable (a, b):
    for i in range(1, a):
        print(f"Умножаем {i}")
        for j in range(1, b):
            print(f"{i} * {j} = {i * j} ")

multiplicationTable(5, 8)
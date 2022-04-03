from xml.dom.minidom import Element


# numbers = [1, 2, 4]
# new_numbers = [element * 2 for element in numbers]
# print(new_numbers)

# numbers2 = [1, 2, 3]
# new_numbers2 = [(element * element) for element in numbers2]
# print(new_numbers2[0] + new_numbers2[1] + new_numbers2[2])

# time = [3, 6.7, 11.8]
# litres = [int(time[0] * 0.5), int(time[1] * 0.5), int(time[2] * 0.5)]
# print(litres)

s = "Helloworld"
if s.find(" ") == -1:
    print(s.lower())
else:
    print(s.upper())

if " " in s:
    s = s.upper()
else:
    s = s.lower()
print(s)


l1 = [1, 2, 3]
res = 0
for num in l1:
    res += num ** 2
print(res)


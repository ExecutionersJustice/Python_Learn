x = 0
if x:
    print("X returned TRUE")
else:
    print("X returned FALSE")

light = "red"

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Stop")
else:
    print("Go")


age = int(input("How old are you? "))

if age >= 18:
    print("Welcome")
else:
    print(f"You must be {18 - age} years older in order to access the website")

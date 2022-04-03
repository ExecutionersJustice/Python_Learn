name = "John"
age = 30

print("My name is " + name + ". I'm " + str(age))

print("My name is %(name)s. I'm %(age)d" %{"name": name, "age": age})

print("My name is %s. I'm %d" %(name, age))

print("Title: %s, Price: %f" %("Sony", 40))


#format
print("My name is {}. I'm {} years old.".format(name, age))
# {} - 0 / 1 by default
print("My name is {x}. I'm {y} years old.".format(x = name, y = age))

#f-strings
print(f"My name is {name}. I'm {age}.")
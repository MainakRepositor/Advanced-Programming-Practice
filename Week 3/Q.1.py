'''1.Develop an Python code to display the following output using class and object (only one
class and two objects)'''
class Birdie:

    species = "bird"

  
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Birdie("Blu", 10)
woo = Birdie("Woo", 15)

print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

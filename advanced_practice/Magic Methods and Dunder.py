### 1. Magic Methods and Dunder ###
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __del__(self):
        print("Object is being deconstructed!")

p = Person("Mike", 25)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

        # def __str__(self):
        #     return f"Vector({self.x}, {self.y})"
        def __repr__(self):
            return f"X: {self.x}, Y:{self.y}"
        

v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2
# print(v3.x)
# print(v3.y)
print(v3)

### 2. Decorators ###
def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("I am decorating your function")
        return_value = function(*args, **kwargs)
        return return_value

    return wrapper

@mydecorator
def hello_world():
    print("Hello World")
# mydecorator(hello_world)()

@mydecorator
def hello(person):
    print(f"Hello {person}")
    return f"Hello {person}!"

print(hello("Mike")) 
# I am decorating your function
# Hello Mike
# Hello Mike!

def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("I am decorating your function")
        return_value = function(*args, **kwargs)
        return return_value

    return wrapper

@mydecorator
def hello_world():
    print("Hello World")
# = mydecorator(hello_world)()

@mydecorator
def hello(person):
    print(f"Hello {person}")
    return f"Hello {person}!"

print(hello("Mike")) 
# I am decorating your function
# Hello Mike
# Hello Mike!


# Example 1 - logging #
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper

@logged
def add(x, y):
    return x+y
print(add(10, 20))
# add returned value 30
# 30


# Example 2 - Timing #
import time
def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after - before} seconds to execute")
        return value
    return wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(1,x):
        result *= i
    return result

myfunction(10000)
# myfunction took 0.022345314025878906 seconds to execute


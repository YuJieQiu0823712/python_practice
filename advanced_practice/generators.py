### 3. Generators ###
import sys

def mygenerator(n):
    for x in range(n):
        yield x ** 3

values = mygenerator(1000000)
print(sys.getsizeof(values))
# 112 bytes
# not matter how big the generator is, it will always take the same space in memory
# 1. Generators don’t store all values in memory.
#   Instead, it creates a generator object, which can produce values one at a time.
# 2. Memory size is mostly constant.
#   measures the size of the generator object itself, not the values it will produce.
# 3. The size doesn’t depend on n because the generator doesn’t hold the sequence in memory, unlike a list.

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

value = infinite_sequence()

print(next(value)) # 1
print(next(value)) # 5
print(next(value)) # 25
print(next(value)) # 125
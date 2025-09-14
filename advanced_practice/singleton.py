from abc import ABCMeta
class IPerson(metaclass=ABCMeta):
    @staticmethod
    def print_data():
        """implement in child class"""

class PersonSingleton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None: 
            PersonSingleton("Defult Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age):
        if PersonSingleton.__instance != None: # check if instance already exists
            raise Exception("Singleton cannot be instantiated more than once")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")

p = PersonSingleton("Mike", 25)
print(p)
p.print_data()

# p2 = PersonSingleton("Bob", 25) # error because singleton already exists
p2 = PersonSingleton.get_instance() # get the existing instance
print(p2) # same memory address as p
p2.print_data()

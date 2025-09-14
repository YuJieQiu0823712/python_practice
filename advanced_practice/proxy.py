from abc import ABCMeta

class IPerson(metaclass=ABCMeta):
    @staticmethod
    def person_method():
        """Interface Method"""
    
class Person(IPerson):
    def person_method(self):
        print("I am a person")

class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()
        # Provide a surrogate or placeholder for another object to control access to it.
        # It doesn’t typically add new behaviors but instead adds control 
        # (e.g., caching, access rights, lazy initialization, remote access).

    def person_method(self):
        print("I am the proxy functionality")
        self.person.person_method()

p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()
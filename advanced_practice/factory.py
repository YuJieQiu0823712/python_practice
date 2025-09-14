from abc import ABCMeta
# abc => abstract class

class IPerson(metaclass=ABCMeta):
    @staticmethod
    def person_method():
        """Interface method"""

class Student(IPerson):
    def __init__(self):
        self.name = "Basic student name"

    def person_method(self):
        print("I am a student")

class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic teacher name"

    def person_methos(self):
        print("I am a teacher")

# s1 = Student()
# s1.person_method()
# t1 = Teacher()
# t1.person_method()

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "student":
            return Student()
        if person_type == "teacher":
            return Teacher()
        print("Invalid Type")
        return -1



if __name__ == "__main__":
    choice = input("What type of person do you wnt to create?")
    person = PersonFactory.build_person(choice)
    person.person_method()
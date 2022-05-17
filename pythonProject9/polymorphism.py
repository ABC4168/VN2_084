# # class Pycharm:
# #     def execute(self):
# #         print("Running")
# #         print("Compiling")
# #
# # class MyEditior:
# #     def execute(self):
# #         print("Spell check")
# #         print("Convention check")
# #         print("Running")
# #         print("Compiling")
# #
# # class Laptop:
# #     def code(self,ide):
# #         ide.execute()
# #
# # ide = MyEditior()
# #
# # lap1 = Laptop()
# # lap1.code(ide)
#
#
#
# class CSStudent:
#     stream = 'cse'   #class variable
#     def __init__(self,name,roll):
#         self.name = name    #Instance variable
#         self.roll = roll    #Instance variable
#
# a = CSStudent("Mudassir",1)
# b = CSStudent("Khan",2)
#
#
# print(a.stream)
# print(b.stream)
# print(a.name)
# print(b.name)
# print(a.roll)
# print(b.roll)
#
# # class variable can be access using class
#
# print(CSStudent.stream)
#
# a.stream = 'EEE'
# print('......................')
# print(a.stream)
# print(b.stream)
#
#
# CSStudent.stream = 'mech'
# print(a.stream)
# print(b.stream)

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person("Mohammed Mudassir", 25)
person2 = Person.fromBirthYear('Mohammed Mudassir', 1997)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(25))






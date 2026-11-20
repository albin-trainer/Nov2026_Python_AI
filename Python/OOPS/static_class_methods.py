class Person:
    msg="I m Person"

    @classmethod
    def print1(cls):
        print(cls.msg)
        print(cls.work)
    @staticmethod
    def print2():
        print(Person.msg)

    def print3(self):
        print("instance method")

class Emp(Person) :
    msg="I m Employee"
    work="Capgemini"

e= Emp()
e.print1()#I m Employee
e.print2()#I m Person
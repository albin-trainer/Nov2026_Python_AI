class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        name = self.name.upper() 
        return name

e1 = Employee("john")
e2 = Employee("alex")

print(e1.display()) #JOHN
print(e1.name) ##in lower case bcoz strings are immutable
print(e2.name)
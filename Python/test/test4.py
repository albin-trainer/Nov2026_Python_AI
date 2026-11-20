class Employee:
    company = "ABC"

e1 = Employee()
e2 = Employee()

print(e1.company) #ABC
print(Employee.company)  #ABC

e1.company = "XYZ" # its creating a new attribute  for e1
print(e2.company) #ABC

Employee.company = "PQR"

print(e1.company) #"xYZ"
print(e2.company)#PQR
print(Employee.company) #PQR
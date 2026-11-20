
def addNames(name,name_list=[]):
     name_list.append(name)
     print(name_list)

addNames("Mohammed")
addNames("Mehul")
addNames("Hyma")
addNames("Taruni")
##Functions are objects in python
# print(addNames.__defaults__)
print(addNames.__defaults__)
print(type(addNames.__defaults__))




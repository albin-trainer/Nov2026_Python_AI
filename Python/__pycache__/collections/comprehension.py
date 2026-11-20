# i want to create  a list from 1 10 10

list=[]
#Tradional Old Approach
for i in range(1,11):
    list.append(i)
print(list)

#List comprehension
list= [n for n in range(1,11)]
print(list)
##Create a list using comprehension squares of nums from 1 to 10

list= [n*n for n in range(1,11)]
print(list)

##Create a list using comprehension  of nums from 1 to 100 even nums

list= [n for n in range(1,101) if n%2==0]
print(list)

names=["Sanjay", "Arun", "Kavya","Sahithiya","Geetha","amrutha","Taruni","Hyma"]

#list=[n for n in names if n.startswith(("A","E","I","O","U"))]

list=[n for n in names if n[0].upper() in "AEIOU"]
print(list)


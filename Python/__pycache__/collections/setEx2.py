myList=["Bangalore","Mysore","Delhi","Mumbai","Delhi","Pune"]
print(myList)

##Convert to Set
mySet=set(myList)
print(mySet)
##In a single stmt i want to change all the  set data to capital case
city="Bangalore"
print(city.upper())

mySet={ c.upper() for c in mySet }
print(mySet)



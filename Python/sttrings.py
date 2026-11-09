city="Bangalore"
print(city.lower())
print(city.upper())
print(city.capitalize())
print(city[0]) #in other languages used to access element by index
#Indexing and Slicing
#In python it can be used for slicing as well
s=city[1:] #start Index : End Index : forward or reverse
print(s)
s=city[1:3:] #Start index 1 and End Index 3 (Exclusive)
print(s)
s=city[8:3:-1] 
print(s)

wish="Good Morning Have a nice Day"
print(wish[0])#1st index
print(wish[-1])# last index
print(wish[-2])
#reverse a string
print(wish[::-1]) #reverse a string
print(wish[11::-1])
print(wish[::2])#Go onn aeanc a (STEP 2)
print(wish[::-2])#Reverse by 2 steps

fruits="     Apple,Orange,Mango,Banana,Grapes,Staw Berry, Kiwi,Cherry        "
print(len(fruits))
fruits=fruits.strip() #Removes the space front and back and creates a new string 
print(len(fruits))
print(fruits)
fruitList=  fruits.split(",") #returns a list (dynamic Array)
print(type(fruitList))
print(fruitList[0]) # Apple
for f in fruitList:
    print(f)


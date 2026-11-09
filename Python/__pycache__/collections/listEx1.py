fruitsList=["Apple","Mango","Grapes","Water Melon"]
print(fruitsList)

fruitsList.append("Lichie") #add at the end
print("----------------")
for f in fruitsList:
    print(f)

#add element between Apple and Mango
fruitsList.insert(1,"Papaya")
print(fruitsList)

nums=[12,32,12,34,4,12,34,11,44,67,56]
# find the max, min and perform sorting ascending and descending
print(max(nums))
print(min(nums))
nums.sort() #modify the original list reverse  arg default value is false
print(nums)
nums.sort(reverse=True)
print(nums)
newlist=sorted(nums) #wont modify the orignal list
print(nums)
print(newlist)



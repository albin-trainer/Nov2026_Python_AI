foodItems={"Briyani","Pizza","Fried Rice","Dosa","Spaghetti","Sushi","Dosa","Momos"}

print(foodItems)
foodItems.add("Idly Sambhar")
print(foodItems)
foodItems.discard("Momos")
#foodItems.remove("Momos") ##since Momos is not a memner it raise a error 

foodItems2={"Pizza","Fried Rice","Dosa"}
print(foodItems.difference(foodItems2))
#try union, intersection functions

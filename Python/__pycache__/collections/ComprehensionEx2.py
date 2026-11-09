studentRecord="101-Sanjay-89-78-99-67-99"
list=studentRecord.split("-") #converted str to list
print(type(list))
print(len(list))
print(list)
scores=list[2:] #slicing from the 2nd index
print(scores)
#### without comprehension
s=0
for score in scores:
    s=int(score)+s
print(s)

scoeList=[  int (score)  for score in scores ]

print(sum(scoeList))
print(sum([  int (score)  for score in scores ]))
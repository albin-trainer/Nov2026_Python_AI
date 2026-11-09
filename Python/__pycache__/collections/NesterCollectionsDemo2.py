student=[
    {"id":1,"studName":"Aishwarya","marks":95},
    {"id":2,"studName":"Rajesh","marks":78},
    {"id":3,"studName":"Sanjay","marks":89},
    {"id":4,"studName":"Pranesh","marks":95},
    {"id":5,"studName":"Rishi","marks":91},
]

### using List Comprehension create a list of only student name 
# who scored more than or eq to 90 

stds=[ s.get("studName")    for s in student if s.get("marks") >=90   ]
print(stds)

# Map comprehension. create a map from existing list
print("------------------------")

studRecord= {    s["studName"] : s["marks"]  for s in student   }
print(studRecord)

#use Dict comprehension create a dictionary  of only
#  student name is key and marks the value
# who scored more than or eq to 90 
print("------------------------")
studRecord= {    s["studName"] : s["marks"]  for s in student  if s["marks"]>=90 }
print(studRecord)

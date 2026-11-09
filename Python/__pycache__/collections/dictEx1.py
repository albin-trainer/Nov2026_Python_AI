employee={
    "id":101,
    "ename":"Aishwarya",
    "address":"Bangalore",
    "salary":50000
}
print(employee)
print(employee.get("ename"))
print(employee.get("email")) # None
print(employee.get("email","NA")) #If email not available it just return NA
print(employee.get("address","NA"))

print("************interating a key ******************")
for  k in employee.keys() :
    print(k)

print("*********iterating values**************")
for v in employee.values():
    print(v)
print("---------------------------")
for k,v in employee.items():
    print(f"{k} : {v}")

employee.update({"address":"Erode"})
print(employee)

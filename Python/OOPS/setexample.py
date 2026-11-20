class Employee:
    def __init__(self,eid,ename,address):
        self.eid=eid
        self.ename=ename
        self.address=address

    def __hash__(self):
        print("**hash called ****")
        return self.eid
    
    def __eq__(self, other):
        print("***eq called ****")
        return self.eid==other.eid and self.ename==other.ename and self.address==other.address
    
e1=Employee(1,"Charukesh","BLR")
e2=Employee(2,"Charukesh","BLR") #If both hash codes are same it calles __eq__ to verify the contents
e3=Employee(2,"Pranesh","BLR")
e4=Employee(3,"Surendra","BLR")
e5=Employee(4,"Rishi","BLR")
emp_set={e1,e2,e3,e4,e5} 
print(len(emp_set))

for e in emp_set:
    print(e.eid, e.ename, e.address)
    print("-------")

myFavFruits={"Apple","Apple","Banana"}
print(myFavFruits) #Apple , Banana

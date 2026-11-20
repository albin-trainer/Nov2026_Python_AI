class Customer:
   def  __init__(self,cid,cname,address):
        self.cid=cid
        self.cname=cname
        self.address=address

   def printCustomerData(self):
        print("printing customer data")
        print(f"cust id is {self.cid} and cust name is {self.cname} and address is {self.address}")

c1= Customer(101,"Mohammed","Bangalore")
c1.printCustomerData()

c2=Customer(102,"Triveni","Bangalore")
c2.printCustomerData()

#Create 5 customer objects
#create a list and store all customer objects
#iterate using a loop

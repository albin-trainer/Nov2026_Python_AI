
def setEmpDetails(id,name,address="BLR"): #Non-default arg cannot follow default arg
    print(f"Emp id is {id} and ename is {name} and address is {address}")


setEmpDetails(1,"Pranesh","Bangalore")
#setEmpDetails(2,"Bangalore","Sravanthi") #not ERROR BUT LOGICAL MISTAKE
setEmpDetails(2,address="Bangalore",name="Sravanthi") #keyword arg

#setEmpDetails(id=99,"Rithwika","Bangalore") #Incorrect positional arg cannot appear after keyword arg
setEmpDetails(id=99,name="Rithwika",address="Bangalore") 
setEmpDetails(100,"Janavi")

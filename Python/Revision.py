data =99
def hello():
    x=data+10 ##Reading the Global variable 
    print(x)

hello()

def changeData():
    ##there is a posibility that accidently some one ccan change the global data 
    data=data+10##Reading and updating the global variables
    print(data)

#changeData()

def changeData2():
    data=199 # Local variable
    print(data) #199

changeData2()
print(data)
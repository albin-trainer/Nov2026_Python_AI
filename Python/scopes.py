
data=100 #Global scope

def myFunction1():
   # data=99
    global data #To Access Global scope data
    data=data+10
    print("data in function1 ",data)

myFunction1()
print(data) #110

def myFunction2():
    data=1 #Local scope
    print("data in function2 ",data)
    print("Accessing global variable in a function",  globals()["data"])
    globals()["data"]=9999

myFunction2()
print(data) #9999

def Outer():
    x=100
    y=123
    def Inner():
        x=99 ##Scope is Local to the Inner Function
        print(x) #99
        nonlocal y #Enclosing Scope
        y=1234
    Inner()#invoking Inner
    print(x)#100
    print(y)
Outer()

#Global scopes
# built in functions such as  print (), len(), globals() etc ...


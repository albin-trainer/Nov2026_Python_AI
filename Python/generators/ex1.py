def getData():
    print("get data 1")
    yield 1 #returns 1 and here it is paused
    print("get data 2")
    yield 2 #returns 2and paused here
    print("get data 3")
    yield 3
    print("get data 4")
    yield 4
    print("get data 5")
    yield 5

# will not invoke getData func, instead it returns a generatpr
x=getData() 

print(next(x)) #1 here it invokes getData() Func
print("-----")
print(next(x))

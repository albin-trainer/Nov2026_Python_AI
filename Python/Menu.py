import Calculator as c
print("1. Add")
print("2. Diff")
print("3. Product")
print("4. Division")
print("5. Exit")
ch=int(input("Enter a choice"))
a=int( input("Enter num1"))
b=int( input("Enter num2"))
match (ch):
    case 1:
        print(c.add(a,b))
    case 2:
        print(c.diff(a,b))
    case 3:
        print(c.product(a,b))
    case 4 :
        print(c.div(a,b))
    case 5:
        print("Bye")
    case _:
        print("invalid choice")

def add(a,b):
    print("hello1")

add(1,1)

def add(a,b,c):
    print("hello2")
#add(1,1)
add(1,1,1)

    
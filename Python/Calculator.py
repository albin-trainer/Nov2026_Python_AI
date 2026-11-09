def add(a,b):
    return a+b

#return typeis optional
def diff(a,b)->int:
    return a-b

#return type is a hint
#it wont force that it must return
#str
def product(a:int,b:int)->str:
    return a*b

def div(a,b):
    return a/b
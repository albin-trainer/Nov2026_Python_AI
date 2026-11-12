def calculator(eval,x,y):
    return eval(x,y)

def findSum(a,b):
    return a+b

result=calculator(findSum,99,1)
print(result)

#findSum,findDiff,findProduct,
#  findDiv thru Lambda expression

r=calculator(lambda a,b: a+b,10,10 )
print(r)

r=calculator(lambda x,y:x*y,10,10)
print(r)
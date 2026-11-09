#import Calculator
import Calculator as c
a:int =10 #optional to give the type
b=50
#sum=Calculator.add(a,b)
sum=c.add(a,b)

print(f"Sum of {a} and {b} is {sum}")
#data:int is just a type hint not strict type declaration
data:int="Hello"
print(type(data))

result=c.product(9,9)
print(F"The result is {result}")

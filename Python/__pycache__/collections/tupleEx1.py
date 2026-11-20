mydata=(1,2,3,4,5,6)  ##Immutable (cannot modify)
print(mydata)
print(mydata[0])
print(mydata[2:])
print(mydata[-2:])
print(mydata[-2::-1])

#In python a function can return any no of values through tuples
def getData():
    return 10,20,30,40,50,60,70
values=getData()
print(values)
print(type(values))

#values[0]=99 ##ERROR 
###unpacking 
a,b,c,d,e,f,h=getData()

print(a)
print(b)

i,j, *k,r =getData() #unpacking *k==> remaining values goes to k
print(i,j)
print(k)
print(r)

def getData():
    for i in range(1,10):
        print("fetching ",i)
        yield i


x =getData()

for i in range(1,10):
   result= next(x)
   print("Received ",result)
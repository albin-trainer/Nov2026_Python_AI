class Product:
    def __init__(self,pid,pname,price,ratings):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.ratings=ratings

    def print(self):
        print(f"Id : {self.pid} Prod Name : {self.pname} Price : {self.price} Ratings :{self.ratings}")

productList=[
    Product(101,"Laptop",50000,4.5),
    Product(102,"Watch",2000,4.7),
    Product(103,"Shoes",3000,4.1),
    Product(104,"T Shirt",1000,4.9),
    Product(105,"Jeans",2000,4.2),
    Product(106,"Mobile",20000,4.8)
] 
for p in productList :
    p.print()
def selectPrice(e):
    return e.price

productList.sort(key=selectPrice)
print("-------sorted by price-------------------")
for p in productList :
    p.print()




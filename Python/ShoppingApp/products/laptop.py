from .product import Product
class Laptop(Product) :

    def __init__(self, prod_id, pname, price,os,memory):
        super().__init__(prod_id, pname, price)
        self.os=os
        self.memory=memory

    def display(self):
        super().display()
        print(f" OS {self.os}")
        print(f"Memory {self.memory}")

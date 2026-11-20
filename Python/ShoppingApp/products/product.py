class Product :
    def __init__(self,prod_id,pname,price):
        self.prod_id=prod_id
        self.pname=pname
        self.price=price

    def display(self):
        print(f"prodid id is {self.prod_id}")
        print(f"prodname  is {self.pname}")
        print(f"price  is {self.price}")

   
from .product import Product
class Book(Product):
    def __init__(self, prod_id, pname, price,authour,genre):
        super().__init__(prod_id, pname, price)
        self.authour=authour
        self.genre=genre
    
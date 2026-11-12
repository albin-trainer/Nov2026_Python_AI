class Parent1:
    def __init__(self):
        print("Parent1 constructor")
        super().__init__()

class Parent2 :
    def __init__(self):
        print("Parent2 constructor")
        super().__init__()
#Method Resolution Order
#is the exact sequence Python follows to search 
class Child(Parent1,Parent2):
    def __init__(self):
        super().__init__()
        print("Child constructor")


c =Child()

class Parent :
    def __init__(self):
        self.x=10


class Child(Parent) :
    def __init__(self):
       self.y=99
      # super().__init__()

c =Child()
print(c.x) #AttributeError @ runtime .....
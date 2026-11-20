class Demo:
    def __init__(self):
        self.values = []

    def add(self, x):
        self.values.append(x)

d1 = Demo()
d2 = Demo()

d1.add(10)
d2.add(20)
d1.add(30)
d2.add(20)
print(d1.values)
print(d2.values)
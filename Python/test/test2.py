class Test:
    def __init__(self):
        self.x = 10

    def change(self, x):
        x = 50

t = Test()
t.change(t.x)
print(t.x)
def test():
    yield 1
    yield 2
    yield 3

g = test()

for x in g: #internally next() invoked
    print(x)

print(next(g)) #StopIteration Error
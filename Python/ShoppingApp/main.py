from products.laptop import Laptop
from products.book import Book
laptop1=Laptop(1001,"HP",50000,"Windows","16GB")
#laptop1.display()
print("-----------------------------------")
book=Book(1002,"Harry Porter", 500,"JK Rowlin","Fantacy")
#book.display()
# add laptop and book in a list and iterate
#call display() inside the loop
products=[]#list
products.append(laptop1)
products.append(book)

for p in products:
    p.display()
    print("------------------------")

print("-------Duck typing Demo ----------")
 #Duck typing, never chks type, it just access the method
def displayAll(anything):
    anything.display()

displayAll(laptop1)
print("*********")
displayAll(book)

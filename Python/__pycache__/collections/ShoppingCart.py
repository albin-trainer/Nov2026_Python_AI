products={} #Empty Dictionary

def addProductIntoCart(pname,quantity=1):
    print("Shoud add product in the dictionary")
    #Key is the prodname and value is the quantity in
    #if the product already exists in the dictionary , increase the quantity
 #   print(pname in products)
  #  print(products.get(pname))
   # if(pname in products):
    if products.get(pname)!=None:
        q=products.get(pname)
        q=q+quantity
        products.update({pname:q})
    else:
     products.update({pname:quantity})


addProductIntoCart("Apple")
addProductIntoCart("Orange")
addProductIntoCart("Apple")
addProductIntoCart("Grapes",5)
addProductIntoCart("Banana")
addProductIntoCart("Orange",2)

print(products) #{Apple:2, Orange:3, Grapes:5,Banana:1}

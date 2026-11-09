#Calculate the electricity bill
# for 1st 100 units - amt to 0 (only for users consumed less than 500 units)
#for 101 to 200- every unit cost 7 Rs
# for 201 to 300 every unit cost 12 rs
#more than  300 every unit cost 20 rs
#more than 500, 25 rs per unit and  no free units for 1st 100 units 4 per per unit 
# if units cconsumed is 301, the amt to pay is 0 +700 + 1200 + 20

a=10
b=20
c=30
if a>b and a >c:
    print("a is bigger")
elif b> c and b>a:
    print("B is Bigger")
else:
    print("C is bigger")


    
#Common falsy values include False, None, 0, 0.0, "", [], {}, and set().

# nums=[1,2,3,4,5]
# print(nums[4])
# print(nums[5]) #program stop here .....
# print("End of the application")



try:
    nums=[1,2,3,4,5]
    print(nums[4])#5
    print(nums[1])#2
    x=10
    print(x/5)
    print("End of the application")
    msg="Hello"
   # msg.f1(); #Attribute Error
   # print(y) #NameError

    #val=input ("Emter any Number") #returns string
    #val=int(val) #ValueError, if unable to change to int
    #print(val)

    empData={"id":101,"name":"Aiswarya"}
    print(empData['address']) #KeyError

except IndexError :
    print("index is out of bounds, try again ....")
except ZeroDivisionError as e:
    print("divide by zero ",e)
except AttributeError as e:
    print("Attribute not found ",e)
except NameError as e:
    print("Name Errpr ",e)
except ValueError as e:
    print(e)
except KeyError as e:
    print(e)
else :
    print("Other exceptions")

print("----Application executed successfully -------")
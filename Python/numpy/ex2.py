import numpy as np

bang_temp=np.array([25,24,30,29.5]) # in celcious
print(bang_temp)
print(bang_temp.dtype)

# i want to add +1 to in every elements
print(bang_temp+1) #Vectorization

# i want to convert these temperature into kelvin
tk =  bang_temp * 9 / 5 + 32   #Vectorization
print(tk)
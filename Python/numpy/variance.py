import numpy as np
##Variance measures how far a set of numbers are spread out from their average (mean).

arr1=np.array([499,500,501,500,498])
arr2=np.array([400,500,600,450,550])
print(np.var(arr1))
print(np.var(arr2))
print(np.std(arr2)) #square root of variance . std dev (actual deviation)


nums=[1,2,3,4,5,6,7,18,90,10,-11,12,183,14,15]

def selectEvenNums(n):
    return n%2==0
##filter is a built-in function , used to filter the elements
## filter(function, list or set or tuple (iterable))
#filteredObj=filter(selectEvenNums,nums)
filteredObj=filter( lambda n:n%2==0 ,nums)
##Print even nums
print(list(filteredObj))
r=sum(nums)
print(r)
print(max(nums))
print(min(nums))

def findSquare(n):
    return n**2
print(list (map(findSquare,nums))) #find the square of each number

print(list(map(lambda n :n**2,nums)))




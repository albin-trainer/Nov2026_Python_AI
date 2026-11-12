class Student :
    score=99 #class variable not instance variable

s1=Student()
s2=Student()

print(s1.score) #reads
print(s2.score)#reads
s1.score=100 ### Here python creates instance variable s1 
print(s1.score)
print(s2.score)

print(Student.score)#class variables can accessed by class name

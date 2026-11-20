import numpy as np

marks=np.array([
    [80,60,90],
    [90,89,87],
    [67,90,89],
    [89,78,95],
    [88,87,97]
])
names=np.array(["Hyma","Charu","Aishwarya","Jahnvi","Roopesh"])
print(marks.dtype)
print(marks)
print(marks.ndim)
print(marks.shape)
#give some grace marks to java=1, python=10, sql=2
grace_mark=np.array([1,10,2])
updated_score=marks+grace_mark #Vectorization
print(updated_score)
#find the total score per student
score_per_student=  np.sum(updated_score, axis=1)
print(score_per_student)
#find the avg score per student
avg_score_student=np.mean(updated_score,axis=1)
print(avg_score_student)

#find the avg score by subject wise, 
# means Java , python and  sql
avg_score_subject=np.mean(updated_score,axis=0)
print(avg_score_subject)

#find the toppers who scored more than 90
toppers=avg_score_student >=90
print(toppers)
print(names[toppers])
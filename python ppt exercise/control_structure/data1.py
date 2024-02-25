
student =['ram','shyam','hari']
#student.insert(1,'rita')
#student.append('sita')
#student[1] ='shyam babu raut'
i=0
for s in student:
    if  s== 'shyam':
        print(i)
        student[i]='hey shyam'
    i+=1
print(student)

#print(len(student))
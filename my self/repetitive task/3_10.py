'''entry = input("please make your blog entrry for today:")
found = False
for word in entry.split():
    if word in ['orderly','shooping','repeat','again','gamble','bid']:
        found = True
if found:
    print("you really need to talk to somebody else!!")
else:
    print("thanks for you entry")
    '''
    

s= input("enter enter a list of integer:")
lst = s.split()
count =0
coun = 0
for e in lst:
    if int (e) % 2 ==0:
        count= count+1
print("there were",count,"even integer in the list>")
for o in lst:
    if int(o) % 2 != 0:
        coun =coun+1
print("there were",coun,"odd integer in the list>")

#WAP to display even numbers between 10 and 20

even = 0
for num in range (1 , 11):
    if num %2 == 0:
        print (num)
        even +=num
print("sum of even number:", even )



odd = 0
for num in range (1,50):
    if num %2 != 0:
        print(num)
        odd +=num
print("the sum of even number is :", odd)
        

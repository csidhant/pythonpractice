'''n= float(input("enter the  number:"))
def even_check (n):
    lst = s.split()
    count =0
    
    for i in range (1,n+1):
        if i%2 == 0:
            count +=1
    print("there were",count,"even integer in the list>")
even_check(n)
    
'''
'''s= input("enter enter a list of integer:")
def  even_odd_number ():
        
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
   # even_odd_number(100)
'''
'''s = input("Enter a list of integers separated by spaces: ")

lst = [int(e) for e in s.split()]

count_even = 0
count_odd = 0

even_numbers = []
odd_numbers = []

for num in lst:
    if num % 2 == 0:
        count_even += 1
        even_numbers.append(num)
    else:
        count_odd += 1
        odd_numbers.append(num)

print("There were", count_even, "even integers in the list.")
print("Even numbers:", even_numbers)

print("There were", count_odd, "odd integers in the list.")
print("Odd numbers:", odd_numbers)
'''

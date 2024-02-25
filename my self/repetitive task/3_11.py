'''n = int(input("enter a non- negative integer:"))
factorial = 1
for i in range (1,n+1):
    factorial = factorial*i
    print ("str (n)+! = " ,factorial)'''

filename = input ("enter a name odf the file:")
catfile = open (filename,'r')
for line in catfile:
    print(line.rstrip())
catfile.close()
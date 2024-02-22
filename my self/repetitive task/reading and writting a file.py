''' a commonly used command in linux os is called cat which stand for
catalog but actually print he content of the file to the screen. we can write
a similar program in python . here is the code for this to work, you must enter a name
of a file in the same directory of folder as the program that are running
'''
filename = input("enter a name of the file:")
catfile = open (filename,"r")
for line in catfile:
    print(line)
catfile.close()

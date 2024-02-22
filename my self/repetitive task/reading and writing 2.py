''' the program below write the file name by the user the file is opened opened and is closed .closing is important when writting a a file uou know
when the file as been completely written otherwise, in some situation the data may be still in the memory closing the output file insure that the data has
actually made it to the file
'''
filename = input("enter the name of the file:")
yourname = input("what is your name:")
age = int(input("how old are you:"))
outfile = open (filename,"w")
outfile.write ("hello" + yourname+"how are you?\n")
outfile.write ("next year will be ", +str(age+1)+  "year old \n")
outfile.close()

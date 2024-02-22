# the program that count the number of entities in your phonebook
phonebook = open ("addressbook.txt","r")
numEntries = 0
lastName = phonebook.readlines().rstrip()
while lastName != " ":
    firstName = phonebook.readline().rstrip()
    street= phonebook.readline().rstrip()
    citystatezip = phonebook.readline().rstrip()
    homepage = phonebook.readline().rstrip()
    mobilephone=phonebook.readline().rsplit()
    numEntries = numEntries +1
    lastName = phonebook.readline().rsplit()
print("you have ", numEntries,"entries in your address book.")

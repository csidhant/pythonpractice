top = int (input("enter a numerator:"))
bottom = int(input ("enetr a denomenator:"))
if bottom != 0 and top % bottom == 0:
    print("the numerator is evenly divided by denomenator")
else:
    print("fraction is not whole number")

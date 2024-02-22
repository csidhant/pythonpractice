# find out he triangle is perfect or not
sideone = int(input("enetr the sortest side of triangle:"))
sidetwo = int(input("enetr the middle side of triangle:"))
sidethree = int(input("enetr the longest side of triangle:"))
msg= "it is perfect triangle!!"
if sideone % 3!=0:
    msg="it is not a perfect triangle"
if sidetwo %4 !=0:
    msg ="not a perfect triangle"
if sidethree %5 != 0:
    msg ="it is not a perfect triangle"
if sideone**2 + sidetwo**2 != sidethree**2:
    msg ="not perfect triangle"
print(msg)
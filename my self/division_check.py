top = float (input("enter a numenator:"))
bottom =float (input("enter a denomenator:"))
guess = float (input("enter your guess:"))
result= top/bottom
biggest= abs(result)
if abs (guess) > biggest :
     biggest = abs(guess)
if abs ((guess - result)/biggest) < .001:
     print ("your guess is right")
else:
     print("sorry, thats wrong. the correct value was ", result)
                

import random
import math
lower=int(input("Enter lower bound:-"))
upper=int(input("Enter upper bound:-"))
n=random.randint(lower,upper)



count =5
while count>0:
    x=int(input("Enter a number:-"))
    count-=1
    if x==n:
        print("win!")
        break
    elif x>n:
        print("you guessed too high!")
    elif x<n:
        print("you guessed too low!")
    else:
        print("Wrong!")
    

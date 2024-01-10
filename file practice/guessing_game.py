import random
# بازی حدس عدد
rm = random.randint(1,100)

while 1:
    g = int(input("your guess: "))
    
    if g > rm:
        print("To Long")
    elif g < rm:
        print("To Short")
    else:
        print("Your Win!nnnnn. ")
        break
import random
x = random.randint(0, 100)

print("Let's Play! Guess any number less than 100:")

for count in range(1, 11):  # to give only 10 guess using for loop
    num = int(input("Enter your guess: ")) #user input
    
    if num < x:
        print("Your number is less than what we have. Try again! Only have " + str(10-count) +" tries" )
    elif num > x:
        print("Your number is greater than what we have. Try again!Only have " + str (10-count) +" tries")
    else:
        print("Whohoo! You guessed it right in " + str(count) +" tries!!")
        exit
else:
    print("Game Over! You used all 10 tries. The number is: " +str(x) )
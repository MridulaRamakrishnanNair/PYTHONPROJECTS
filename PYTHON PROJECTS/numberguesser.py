import random
import time
print("Hi! Welcome to the number guesser! I am going to pick a number between 1 and 10")
time.sleep(2)
print("Picking a number.........!!!!")
time.sleep(5)
guess = int(input("Hey There! what is your guess?"))
correct_number = random.randint(1,10)
guesscount = 0

while guess != correct_number:
    guesscount +=1
    if guess < correct_number:
        guess = int(input("You need to guess a higher number!! what's your guess this time?"))
    else:
        guess = int(input("You need to guess a lower number!! what's your guess this time?"))

print("Congratulations! You got the right answer!! :)")

if guesscount > 5:
    print(f"you made {guesscount} guesses before getting to the right answer!!Try making fewer guesses next time!")
    
else:
    print(f"you just made {guesscount} guesses before getting to the right answer!!")
    
import random


def guess(x) :
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number :
        guess = int(input(f"Guess a nummber from 1 to {x} : "))

        if guess < random_number :
            print("Guess again. Too low.")
        elif guess > random_number :
            print("Guess again. Too high.")
        else :
            print("Congrats. You have guessed the number.")

def computer_guess(x) :
    low = 1
    high = x+1
    feedback = ""

    while feedback != 'C' :
        guess = random.randint(low, high) 
        feedback = input(f"Is {guess} Too High (H) or Too Low (L) or Correct (C) ?? ").upper()
        if feedback == 'H' :
            high = guess - 1
        elif feedback == 'L' :
            low = guess + 1
        elif feedback == 'C' :
            print(f"The computer has guessed the number ({guess}) correctly !")
        else : 
            print("Invalid input")

computer_guess(20)
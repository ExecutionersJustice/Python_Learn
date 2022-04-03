from random import randint

def guessNumberGame ():
    count = 0
    guess = 0
    number = randint(1, 100)
    while guess != number:
        guess = int(input("Enter your number "))
        count += 1
        if guess > number:
            print("The number is lower")
        elif guess < number:
            print("The number is higher")
    else: 
        print(f"BOOM JACKPOT MF, IT TOOK YOU {count} TIMES TO HIT")
    
guessNumberGame()


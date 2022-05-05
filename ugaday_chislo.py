from random import randint

def guessNumberGame ():
    count = 0
    number = randint(1, 100)
    while True:
        guess = int(input("Enter your number "))
        count += 1
        if guess > number:
            print("The number is lower")
        elif guess < number:
            print("The number is higher")
        else: 
            print(f"BOOM JACKPOT MF, IT TOOK YOU {count} TIMES TO HIT.")
            nextTry = input("WOULD YOU LIKE TO PLAY AGAIN? Y/N =  ")
            if nextTry == "Y":
                count = 0
                number = randint(1, 100)
            else:
                print("Goodbye Lucky")
                break
    
guessNumberGame()


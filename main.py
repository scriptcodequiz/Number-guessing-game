import random
nomber = random.randint(1, 20)

def welcome ():
    print ("Hello, welcome to the number guessing game.")

guess = None

count = 0
continue_playgin = True
while continue_playgin:
    guess = int(input("What is the number?"))

    if guess > nomber:
        print("The number is smaller")
    elif guess < nomber:
        print ("The number is larger")
    else:
        print("You won that game")
        print(f"The number the computer chose was {nomber}")

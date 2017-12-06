import random
def goguess():
    tries = 1
    print("I have a number between 1 and 20 inclusive.")
    guess = int(raw_input("Guess: "))
    for x in range(1):
        x = random.randint(1,20)
    while guess != x:
        if guess > x:
            print("Your guess is too high. Try again.")
            guess = int(raw_input("Guess: "))
            tries += 1
        elif guess < x:
            print("Your guess is too low. Try again.")
            guess = int(raw_input("Guess: "))
            tries += 1
    if guess == x:
        print("You guessed right!")
        print tries
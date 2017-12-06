import random
def lottery(a):
    guesses = set(a)
    lista=[]
    matches = 0
    for x in range(5):
        x = random.randint(1,50)
        lista+=[x]
        answer = set(lista)
    for number in guesses:
        if number in answer:
            matches += 1
    if len(guesses) != 5:
        print("Error: invalid ticket")
    elif len(answer) != 5:
        print("Error: invalid winning sequence")
    else:
        print guesses
        print answer
        print matches
def grade():
    num=int(raw_input('Insert a grade score: '))
    if num >= 90:
        print('A')
    elif num >= 80:
        print('B')
    elif num >= 70:
        print('C')
    elif num >= 60:
        print('D')
    else:
        print('F')
        
import random
def randomLetter():
    name=(raw_input('Insert your name: '))
    print(random.choice(name))
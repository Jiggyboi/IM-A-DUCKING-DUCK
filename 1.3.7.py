import matplotlib.pyplot as plt
import random
def dice(n):
    list=[]
    for x in range(n):
        x=random.randint(1,6)
        list+=[x]
    print sum(list)
    
def roll_hundred_pair():
    list = []
    for num in range(100):
        x = random.randint(1,6)
        y = random.randint(1,6)
        list+=[x+y]
    plt.hist(list)
    plt.show()
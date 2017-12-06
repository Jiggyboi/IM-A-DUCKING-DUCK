import random
list = []
def randNum():
    global list
    for x in range(1):
        x = random.randint(1,6)
    for y in range(1):
        y = random.randint(1,6)
    for z in range(1):
        z = random.randint(1,6)
    a=(x,y,z)
    if x == y or x == z or y == z:
        print x,y,z
        print('HAHA NERRRRRRRRRD YOU LOST')
    else:
        print x,y,z
        print('Oh hey... you won... hooray')
    list+=[a]
    return list
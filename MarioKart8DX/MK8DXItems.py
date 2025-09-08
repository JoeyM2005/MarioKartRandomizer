import random
import time

random.seed(time.time())

randomItems = True

def itemList():
    return ['Banana Peel', 'Triple Banana Peels', 'Green Shell', 'Triple Green Shells',
        'Red Shell', 'Triple Red Shells','Blue Shell', 'Bomb-omb', 'Mushroom', 'Triple Mushroom',
        'Golden/Queen Mushroom', 'Bullet Bill', 'Blooper', 'Lightning', 'Star','Fireflower', 'Boomerang',
        'Piranha Plant', 'Boom Box', '8', 'Coin', 'Boo']

def itemListLength():
     itemlist = itemList()
     return len(itemlist)

def randomItem(value=True):
    randomItems = value
    return randomItems

def calcuitem(random_set_b=False, max_items=-1):
    itemlisttemp = itemList()
    itemlistlengthtemp = itemListLength()
    if random_set_b:
        max_items = random.randint(1, max_items)

    print('\nITEMS')
    for i in range(max_items):
        item = itemlisttemp[random.randint(0, itemlistlengthtemp - 1)]
        itemlisttemp.remove(item)
        itemlistlengthtemp-=1
                
        print(f'\tITEM {i+1}: {item}')

def items(random_set_b, max_items):
        
        if(max_items != 0):
            #input for random vs set number
            if(randomItem()):
                calcuitem(random_set_b, max_items)
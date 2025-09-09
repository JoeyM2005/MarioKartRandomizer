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

def calcuitem(random_set_b=False, max_items=-1):
    if random_set_b:
        max_items = random.randint(1, max_items)

    print('\nITEMS')
    randomItems = random.sample(itemList(), max_items)
    
    for i in range(len(randomItems)):
        print(f'\tITEM {i+1}: {randomItems[i]}')

def items(random_set_b, max_items):
        
        if(max_items != 0):
            #input for random vs set number
            calcuitem(random_set_b, max_items)
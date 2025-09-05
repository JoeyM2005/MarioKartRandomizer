import random
import time

random.seed(time.time())

def calcuitem(random_set_b=False, max_items=-1, itemList = []):
    if random_set_b:
        max_items = random.randint(1, max_items)

    print('\nITEMS')
    for i in range(max_items):
        item = itemList[random.randint(0, len(itemList) - 1)]
        itemList.remove(item)
                
        print(f'\tITEM {i+1}: {item}')

def items():
        
        itemList = ['Banana Peel', 'Triple Banana Peels', 'Green Shell', 'Triple Green Shells',
        'Red Shell', 'Triple Red Shells','Blue Shell', 'Bomb-omb', 'Mushroom', 'Triple Mushroom',
        'Golden/Queen Mushroom', 'Bullet Bill', 'Blooper', 'Lightning', 'Star','Fireflower', 'Boomerang',
        'Piranha Plant', 'Boom Box', '8', 'Coin', 'Boo']
        numItemsList = len(itemList)

        #input for random vs set number
        random_set_i = input("\nDo you want a random number of items (random), set a number of items (set), or no random items (none)? \n")
        randomItems = True
        while True:
            match random_set_i.lower():
                case "random":
                    max_items = int(input(f"What is the max number of items you wish to randomize? (MAX of {numItemsList})\n"))
                    random_set_b = True
                case "set":
                    max_items = int(input(f"How many items do you want? (MAX of {numItemsList})\n"))
                    random_set_b = False
                case "none":
                    randomItems = False
                    max_items = 1
                case _:
                    random_set_i = input("\nDo you want a random number of items (random) or a set a number of items (set) \n")
            if ((max_items > 0) and (max_items <= numItemsList)):
                break

        if(randomItems):
            calcuitem(random_set_b, max_items, itemList)
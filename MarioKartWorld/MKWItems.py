import random
import time

random.seed(time.time())

'''
def items():
    itemSetList = ['Normal', 'Frantic', 'Mushroom Only'] 
    probabilities = [0.56, 0.39, 0.05]
    #print(probabilities)
    #results = [random.choices(itemList, weights=probabilities, k=1)[0] for _ in range(20)]
    results = random.choices(itemSetList, weights=probabilities, k=1)[0] #singular result
     
    print('\nITEMS:')
    print(f'\t{results}')
    
    #print(f'Normal: {results.count('Normal')}')
    #print(f'Mushroom Only: {results.count('Mushroom Only')}')
    #print(f'Frantic: {results.count('Frantic')}')
'''


randomItems = True

def itemList():
    return ['Coin', 'Green Shell', 'Triple Green Shells', 'Red Shell', 'Triple Red Shells', 'Blue Shell',
            'Banana Peel', 'Triple Banana Peels', 'Mushroom', 'Triple Mushrooms', 'Golden Mushroom',
            'Mega Mushroom', 'Feather', 'Fire Flower', 'Ice Flower', 'Boomerang Flower', 'Star',
            'Super Horn', 'Lightning', 'Hammer', 'Blooper', 'Bob-omb', 'Bullet Bill', 'Boo', 'Coin Shell',
            '? Block', 'Kamek', 'Dash Food']

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
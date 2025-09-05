import random
import time
random.seed(time.time())

def items():
    itemList = ['Normal', 'Frantic', 'Mushroom Only'] 
    probabilities = [0.56, 0.39, 0.05]
    #print(probabilities)
    #results = [random.choices(itemList, weights=probabilities, k=1)[0] for _ in range(20)]
    results = random.choices(itemList, weights=probabilities, k=1)[0] #singular result
     
    print('\nITEMS:')
    print(f'\t{results}')
    
    #print(f'Normal: {results.count('Normal')}')
    #print(f'Mushroom Only: {results.count('Mushroom Only')}')
    #print(f'Frantic: {results.count('Frantic')}')
       

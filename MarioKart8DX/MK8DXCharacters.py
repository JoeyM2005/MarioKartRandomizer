import random
import time

random.seed(time.time())

def characters(players):
    characters = ['Mario', 'Luigi', 'Peach', 'Daisy', 'Rosalina', 'Tanooki Mario', 'Cat Peach', birdo(),
            yoshi(), 'Toad', 'Koopa Troopa', shyGuy(), 'Lakitu', 'Toadette', 'King Boo', 'Petey Piranha',
            'Baby Mario', 'Baby Luigi', 'Baby Peach', 'Baby Daisy', 'Baby Rosalina', metalMario(), 'Pink Gold Peach', 'Wiggly',
            'Wario', 'Waluigi', 'Donkey Kong', 'Bowser', 'Dry Bones', 'Bowser Jr.', 'Dry Bowser', 'Kamek',
            'Lemmy', 'Lary', 'Wendy', 'Ludwig', 'Iggy', 'Roy', 'Morton', 'Peachette',
            inkling(), villager(), 'Isabelle', link(), 'Diddy Kong', 'Funky Kong', 'Pauline']

    # Character Print
    print('\nCHARACTER')
    for i in range(players):
        character = random.randint(1, len(characters) - 1)
        print(f'\tPlayer {i+1}: {characters[character]}')

def randomCharVar(charList):
    m_num = random.randint(0, len(charList) - 1)
    return charList[m_num]

def birdo():
    birdos = ['Birdo (Pink)', 'Birdo (Light Blue)', 'Birdo (Black)', 'Birdo (Red)',
    'Birdo (Yellow)', 'Birdo (White)', 'Birdo (Blue)', 'Birdo (Green)', 'Birdo (Orange)']
    return randomCharVar(birdos)

def yoshi():
    yoshis = ['Green Yoshi', 'Light-blue Yoshi', 'Black Yoshi', 'Red Yoshi',
    'Yellow Yoshi', 'Black Yoshi', 'Blue Yoshi', 'Pink Yoshi', 'Orange Yoshi']
    return randomCharVar(yoshis)

def inkling():
    inklings = ['Inkling Girl (Orange)', 'Inkling Girl (Green)', 'Inkling Girl (Pink)',
    'Inkling Boy (Blue)', 'Inkling Boy (Purple)', 'Inkling Boy (Light-blue)']
    return randomCharVar(inklings)

def villager():
    villagers = ['Villager (Boy)', 'Villager (Girl)']
    return randomCharVar(villagers)
    
def link():
    links = ['Link (Champion Tunic)', 'Link (Classic)']
    return randomCharVar(links)
    
def metalMario():
    metalMarios = ['Gold Mario', 'Metal Mario']
    return randomCharVar(metalMarios)

def shyGuy():
    shyGuys = ['Red Shy Guy', 'Light-Blue Shy Guy', 'Black Shy Guy', 'Green Shy Guy',
    'Yellow Shy Guy', 'White Shy Guy', 'Blue Shy Guy', 'Pink Shy Guy', 'Orange Shy Guy']
    return randomCharVar(shyGuys)

"""
if __name__ == "__main__":

    players = 4
    for i in range(50):
        characters(players)
"""
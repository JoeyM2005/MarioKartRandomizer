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



def birdo():
    birdos = ['Birdo (Pink)', 'Birdo (Light Blue)', 'Birdo (Black)', 'Birdo (Red)',
    'Birdo (Yellow)', 'Birdo (White)', 'Birdo (Blue)', 'Birdo (Green)', 'Birdo (Orange)']
    b_num = random.randint(0, len(birdos) - 1)
    return birdos[b_num]

def yoshi():
    yoshis = ['Green Yoshi', 'Light-blue Yoshi', 'Black Yoshi', 'Red Yoshi',
    'Yellow Yoshi', 'Black Yoshi', 'Blue Yoshi', 'Pink Yoshi', 'Orange Yoshi']
    y_num = random.randint(0, len(yoshis) - 1)
    return yoshis[y_num]

def inkling():
    inklings = ['Inkling Girl (Orange)', 'Inkling Girl (Green)', 'Inkling Girl (Pink)',
    'Inkling Boy (Blue)', 'Inkling Boy (Purple)', 'Inkling Boy (Light-blue)']
    i_num = random.randint(0, len(inklings) - 1)
    return inklings[i_num]

def villager():
    villagers = ['Villager (Boy)', 'Villager (Girl)']
    v_num = random.randint(0, len(villagers) - 1)
    return villagers[v_num]
    
def link():
    links = ['Link (Champion Tunic)', 'Link (Classic)']
    l_num = random.randint(0, len(links) - 1)
    return links[l_num]
    
def metalMario():
    metalMarios = ['Gold Mario', 'Metal Mario']
    m_num = random.randint(0, len(metalMarios) - 1)
    return metalMarios[m_num]

def shyGuy():
    shyGuys = ['Red Shy Guy', 'Light-Blue Shy Guy', 'Black Shy Guy', 'Green Shy Guy',
    'Yellow Shy Guy', 'White Shy Guy', 'Blue Shy Guy', 'Pink Shy Guy', 'Orange Shy Guy']
    s_num = random.randint(0, len(shyGuys) - 1)
    return shyGuys[s_num]




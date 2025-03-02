import random
import time

random.seed(time.time())

# Global Constants
KART = 40
WHEEL = 21
GLIDE = 15

MAX_ITEMS = 7

ITEM_ROW = 4
ITEM_COL = 6

# More Advanced Player Randomization
def birdo():
    b_row, b_col = random.randint(1, 3), random.randint(1, 3)
    if (b_row == 1):
        if (b_col == 1): return 'Birdo'
        if (b_col == 2): return 'Birdo (Light Blue)'
        if (b_col == 3): return 'Birdo (Black)'
    if (b_row == 2):
        if (b_col == 1): return 'Birdo (Red)'
        if (b_col == 2): return 'Birdo (Yellow)'
        if (b_col == 3): return 'Birdo (White)'
    if (b_row == 3):
        if (b_col == 1): return 'Birdo (Blue)'
        if (b_col == 2): return 'Birdo (Green)'
        if (b_col == 3): return 'Birdo (Orange)'

def yoshi():
    y_row, y_col = random.randint(1, 3), random.randint(1, 3)
    if (y_row == 1):
        if (y_col == 1): return 'Green Yoshi'
        if (y_col == 2): return 'Light-blue Yoshi'
        if (y_col == 3): return 'Black Yoshi'
    if (y_row == 2):
        if (y_col == 1): return 'Red Yoshi'
        if (y_col == 2): return 'Yellow Yoshi'
        if (y_col == 3): return 'Black Yoshi'
    if (y_row == 3):
        if (y_col == 1): return 'Blue Yoshi'
        if (y_col == 2): return 'Pink Yoshi'
        if (y_col == 3): return 'Orange Yoshi'

def inkling():
    i_row, i_col = random.randint(1, 2), random.randint(1, 2)
    if (i_row == 1):
        if (i_col == 1): return 'Inkling Girl (Orange)'
        if (i_col == 2): return 'Inkling Girl (Green)'
        if (i_col == 3): return 'Inkling Girl (Pink)'
    if (i_row == 2):
        if (i_col == 1): return 'Inkling Boy (Blue)'
        if (i_col == 2): return 'Inkling Boy (Purple)'
        if (i_col == 3): return 'Inkling Boy (Light-blue)'

def villager():
    v_row = random.randint(1, 2)
    if (v_row == 1): return 'Villager (Boy)'
    if (v_row == 2): return 'Villager (Girl)'
    
def link():
    l_row = random.randint(1, 2)
    if (l_row == 1): return 'Link (Champion Tunic)'
    if (l_row == 2): return 'Link (Classic)'
    
'''def metalMario():
    m_row = random.randint(1, 2)
    if (m_row == 1): 'Gold Mario'
    if (m_row == 2): 'Metal Mario'''

def shyGuy():
    s_num = random.randint(1, 9)
    if (s_num == 1): 'Red Shy Guy'
    if (s_num == 2): 'Light-Blue Shy Guy'
    if (s_num == 3): 'Black Shy Guy'
    if (s_num == 4): 'Green Shy Guy'
    if (s_num == 5): 'Yellow Shy Guy'
    if (s_num == 6): 'White Shy Guy'
    if (s_num == 7): 'Blue Shy Guy'
    if (s_num == 8): 'Pink Shy Guy'
    if (s_num == 9): 'Orange Shy Guy'

def items(row, col):
    if (row == 1):
        if (col == 1): return 'Banana Peel'
        if (col == 2): return 'Triple Banana Peels'
        if (col == 3): return 'Green Shell'
        if (col == 4): return 'Triple Green Shells'
        if (col == 5): return 'Red Shell'
        if (col == 6): return 'Triple Red Shells'
    if (row == 2):
        if (col == 1): return 'Blue Shell'
        if (col == 2): return 'Bomb-omb'
        if (col == 3): return 'Mushroom'
        if (col == 4): return 'Triple Mushroom'
        if (col == 5): return 'Golden/Queen Mushroom'
        if (col == 6): return 'Bullet Bill'
    if (row == 3):
        if (col == 1): return 'Blooper'
        if (col == 2): return 'Lightning'
        if (col == 3): return 'Star'
        if (col == 4): return 'Fireflower'
        if (col == 5): return 'Boomerang'
        if (col == 6): return 'Piranha Plant'
    if (row == 4):
        if (col == 1): return 'Boom Box'
        if (col == 2): return '8'
        if (col == 3): return 'Coin'
        if (col == 4): return 'Boo'

if __name__ == "__main__":
    
    characters = ['Mario', 'Luigi', 'Peach', 'Daisy', 'Rosalina', 'Tanooki Mario', 'Cat Peach', birdo(),
            yoshi(), 'Toad', 'Koopa Troopa', shyGuy(), 'Lakitu', 'Toadette', 'King Boo', 'Petey Piranha',
            'Baby Mario', 'Baby Luigi', 'Baby Peach', 'Baby Daisy', 'Baby Rosalina', 'Metal Mario', 'Pink Gold Peach', 'Wiggly',
            'Wario', 'Waluigi', 'Donkey Kong', 'Bowser', 'Dry Bones', 'Bowser Jr.', 'Dry Bowser', 'Kamek',
            'Lemmy', 'Lary', 'Wendy', 'Ludwig', 'Iggy', 'Roy', 'Morton', 'Peachette',
            inkling(), villager(), 'Isabelle', link(), 'Diddy Kong', 'Funky Kong', 'Pauline']
    
    playChoice = "yes"
    while(playChoice.lower() == "yes"):
        rand_items = random.randint(1,7)
    
        players = int(input("\nHow many players? (MAX of 4)\n"))
        while players not in {1, 2, 3, 4}:
            players = int(input("How many players? (MAX of 4)\n"))
        
        COURSES = int(input("\nHow many Courses? (MAX of 48)\n"))
        while COURSES not in {1, 4, 6, 8, 12, 16, 24, 32, 48}:
            COURSES = int(input("How many Courses? (MAX of 48)\n"))
                
        COURSE_ROW = 4
        COURSE_COL = 6
        
        print('\nCHARACTER')
        for i in range(players):
            character = random.randint(1, len(characters))
            print(f'\tPlayer {i+1}: {characters[character]}')
        
        print('\nKART')
        for i in range(players):
            print(f'\tPlayer {i+1}: {random.randint(1, KART)}')
        
        print('\nWHEEL')
        for i in range(players):
            print(f'\tPlayer {i+1}: {random.randint(1, WHEEL)}')
        
        print('\nGLIDE')
        for i in range(players):
            print(f'\tPlayer {i+1}: {random.randint(1, GLIDE)}')
        
        print('\nITEMS')
        for i in range(rand_items):
            loopRow = random.randint(1, ITEM_ROW)
            if loopRow == 4:
                loopCol = random.randint(1, ITEM_COL - 2)
            else:
                loopCol = random.randint(1, ITEM_COL)
                
            print(f'\tITEM {i+1}: {items(loopRow, loopCol)}')
            
        print('\nCOURSE')
        course = random.randint(1,4)
        course_row = random.randint(1, COURSE_ROW)
        course_col = random.randint(1, COURSE_COL)
        
        courseList = {1:{1:[1, 2, 3, 4],2:[1, 2, 3, 4],3:[1, 2, 3, 4],4:[1, 2, 3, 4],5:[1, 2, 3, 4],6:[1, 2, 3, 4]},
        2:{1:[1, 2, 3, 4],2:[1, 2, 3, 4],3:[1, 2, 3, 4],4:[1, 2, 3, 4],5:[1, 2, 3, 4],6:[1, 2, 3, 4]},
        3:{1:[1, 2, 3, 4],2:[1, 2, 3, 4],3:[1, 2, 3, 4],4:[1, 2, 3, 4],5:[1, 2, 3, 4],6:[1, 2, 3, 4]},
        4:{1:[1, 2, 3, 4],2:[1, 2, 3, 4],3:[1, 2, 3, 4],4:[1, 2, 3, 4],5:[1, 2, 3, 4],6:[1, 2, 3, 4]}}
        
        courseNamesList = { 1: {'Mushroom Cup':['Mario Kart Stadium', 'Water Park', 'Sweet Sweet Canyon', 'Thwomp Ruins'],
                                'Flower Cup':['Mario Circuit', 'Toad Harbor', 'Twisted Mansion', 'Shy Guy Falls'],
                                'Star Cup':['Sunshine Airport', 'Dolphin Shoals', 'Electrodome', 'Mount Wario'],
                                'Speccial Cup':['Cloudtop Cruise', 'Bone-Dry Dunes', "Bowser's Castle", 'Rainbow Road'],
                                'Egg Cup':['Yoshi Circuit', 'Excitebike Arena', 'Dragon Driftway', 'Mute City'],
                                'Crossing Cup':['Baby Park', 'Cheese Land', 'Wild Woods', 'Animal Crossing'] },
                            2: {'Shell Cup':['Moo Moo Meaows', 'Mario Circuit', 'Cheep Cheep Beach', "Toad's Turnpike"],
                                'Banana Cup':['Dry Dry Desert', 'Donut Plain 3', 'Royal Raceway', 'DK Jungle'],
                                'Leaf Cup':['Wario Stadium', 'Sherbet Land', 'Music Park', 'Yoshi Valley'],
                                'Lightning Cup':['Tick-Tock Clock', 'Piranha Plant Slide', 'Grumble Volcano', 'Rainbow Road'],
                                'Triforce Cup':["Wario's Gold Mine", 'Rainbow Road', 'Ice Ice Outpost', 'Hyrule Circuit'],
                                'Bell Cup':['Neo Bowser City', 'Ribbon Road', 'Super Bell Subway', 'Big Blue']},
                            3: {'Golden Dash Cup':['Paris Promenade', 'Toad Circuit', 'Chco Mountain', 'Coconut Mall'],
                                'Lucky Cat Cup':['Tokyo Blur', 'Shroom Ridge', 'Sky Garden', 'Ninja Hideway'],
                                'Turnip Cup':['New York Minute', 'Mario Circuit 3', 'Kalimari Desert', 'Waluigi Pinball'],
                                'Propeller Cup':['Sydney Sprint', 'Snow Land', 'Mushroom Gorge', 'Sky-High Sundae'],
                                'Rock Cup':['London Loop', 'Boo Lake', 'Rock Rock Mountain', 'Maple Treeway'],
                                'Moon Cup':['Berlin Byways', 'Peach Gardens', 'Merry Mountain', 'Rainbow Road']},
                            4: {'Fruit Cup':['Amsterdan Drift', 'Riverside Park', 'DK Summit', "Yoshi's Island"],
                                'Boomerang Cup':['Bangkok Rush', 'Mario Circuit', 'Waluigi Stadium', 'Singapore Speedway'],
                                'Feathers Cup':['Athens Dash', 'Daisy Cruiser', 'Moonview Highway', 'Squeaky Clean Spirit'],
                                'Cherry Cup':['Los Angeles Laps', 'Sunset Wilds', 'Koopa Cape', 'Vancouver Velocity'],
                                'Acorn Cup':['Rome Avanti', 'DK Mountain', 'Daisy Circuit', 'Pirnha Plant Cove'],
                                'Spiny Cup':['Madrid Drive', "Rosalina's Ice World", 'Bowser Castle 3', 'Rainbow Road']} }
            
        for i in range(COURSES):
            while(course not in courseList[course_row][course_col]):
                course_row = random.randint(1, COURSE_ROW)
                course_col = random.randint(1, COURSE_COL)
                course = random.randint(1,4)
            courseList[course_row][course_col].remove(course)
            cupList = list(courseNamesList[course_row].keys())
            cup = (cupList[course_col - 1])
            track = courseNamesList[course_row][cup][course - 1]
            
            print(f'\tCOURSE {i+1}: {cup}: {track}')
        
        playChoice = input("\nWould you like to play? (YES/NO)\n")
    print("Kill yourself ong")

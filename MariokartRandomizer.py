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
    return metalMarios[m_row]

def shyGuy():
    shyGuys = ['Red Shy Guy', 'Light-Blue Shy Guy', 'Black Shy Guy', 'Green Shy Guy',
    'Yellow Shy Guy', 'White Shy Guy', 'Blue Shy Guy', 'Pink Shy Guy', 'Orange Shy Guy']
    s_num = random.randint(0, len(shyGuys) - 1)
    return shyGuys[s_num]



if __name__ == "__main__":
    
    characters = ['Mario', 'Luigi', 'Peach', 'Daisy', 'Rosalina', 'Tanooki Mario', 'Cat Peach', birdo(),
            yoshi(), 'Toad', 'Koopa Troopa', shyGuy(), 'Lakitu', 'Toadette', 'King Boo', 'Petey Piranha',
            'Baby Mario', 'Baby Luigi', 'Baby Peach', 'Baby Daisy', 'Baby Rosalina', 'Metal Mario', 'Pink Gold Peach', 'Wiggly',
            'Wario', 'Waluigi', 'Donkey Kong', 'Bowser', 'Dry Bones', 'Bowser Jr.', 'Dry Bowser', 'Kamek',
            'Lemmy', 'Lary', 'Wendy', 'Ludwig', 'Iggy', 'Roy', 'Morton', 'Peachette',
            inkling(), villager(), 'Isabelle', link(), 'Diddy Kong', 'Funky Kong', 'Pauline']
    
    # Player input for playing the game, how many players, and how many courses
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
        

        # Character Print
        print('\nCHARACTER')
        for i in range(players):
            character = random.randint(1, len(characters) - 1)
            print(f'\tPlayer {i+1}: {characters[character]}')
        
        # Kart Print
        print('\nKART')
        for i in range(players):
            print(f'\tPlayer {i+1}: {random.randint(1, KART)}')
        
        # Wheel Print
        print('\nWHEEL')
        for i in range(players):
            print(f'\tPlayer {i+1}: {random.randint(1, WHEEL)}')
        
        # Glider Print
        print('\nGLIDER')
        for i in range(players):
            print(f'\tPlayer {i+1}: {random.randint(1, GLIDE)}')
        

        # Items logic
        print('\nITEMS')
        itemList = ['Banana Peel', 'Triple Banana Peels', 'Green Shell', 'Triple Green Shells',
        'Red Shell', 'Triple Red Shells','Blue Shell', 'Bomb-omb', 'Mushroom', 'Triple Mushroom',
        'Golden/Queen Mushroom', 'Bullet Bill', 'Blooper', 'Lightning', 'Star','Fireflower', 'Boomerang',
        'Piranha Plant', 'Boom Box', '8', 'Coin', 'Boo']

        for i in range(rand_items):
            item = itemList[random.randint(0, len(itemList) - 1)]
            itemList.remove(item)
                
            print(f'\tITEM {i+1}: {item}')


        # Course logic   
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
        
        # Translates from numbers to the course cup and track for printing
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

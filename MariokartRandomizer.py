import random
import time

random.seed(time.time())

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
    return metalMarios[m_num]

def shyGuy():
    shyGuys = ['Red Shy Guy', 'Light-Blue Shy Guy', 'Black Shy Guy', 'Green Shy Guy',
    'Yellow Shy Guy', 'White Shy Guy', 'Blue Shy Guy', 'Pink Shy Guy', 'Orange Shy Guy']
    s_num = random.randint(0, len(shyGuys) - 1)
    return shyGuys[s_num]

def items(random_set_b, max_items):
    if random_set_b:
        max_items = random.randint(1, max_items)

    print('\nITEMS')
    for i in range(max_items):
        item = itemList[random.randint(0, len(itemList) - 1)]
        itemList.remove(item)
                
        print(f'\tITEM {i+1}: {item}')

def characters():
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

def karts():
    # Kart List
    kartList = ["Standard Kart", "Pipe Frame", "Mach 8", "Steel Driver", "Cat Cruiser", "Circuit Special", "Tri-Speeder", "Badwagon",
                    "Prancer", "Biddybuggy", "Landship", "Sneeker", "Sportes Coupe", "Gold Standard", "GLA", "W 25 Silver Arrow",
                    "300 SL Roadster", "Blue Falcon", "Tanooki Kart", "B Dasher", "Streetle", "P-Wing", "Koopa Clown", "Standard Bike",
                    "Comet", "Sport Bike", "The Duke", "Flame Rider", "Varmint", "Mr. Scooty", "Jet Bike", "Yoshi Bike", "Master Cycle",
                    "Master Cycke Zero", "City Tripper", "Standard ATV", "WIld Wiggler", "Teddy Buggy", "Bone Rattler", "Splat Buggy", 
                    "Inkstriker"]
    
    # Kart Print
    print('\nKART')
    for i in range(players):
        rand_value = random.randint(0, len(kartList) - 1)
        print(f'\tPlayer {i+1}: {rand_value + 1} \t{kartList[rand_value]}')

def wheels():
    # Wheel List
    wheelList = ["Standard", "Monster", "Roller", "Slim", "Slick", "Metal", "Button", "Off-Road", "Sponge", "Wood", "Cushion",
                    "Blue Standard", "Hot Monster", "Azure Rider", "Crimson Slim", "Cyber Slick", "Retro Off-Road", "Gold Tires", 
                    "GLA Tires", "Triforce Tires", "Ancient Tires", "Leaf Tires"]
    
    # Wheel Print
    print('\nWHEEL')
    for i in range(players):
        rand_value = random.randint(0, len(wheelList) - 1)
        print(f'\tPlayer {i+1}: {rand_value + 1} \t{wheelList[rand_value]}')

def gliders():
    # Glide List
    gildeList = ["Super Glider", "Cloud Glider", "Wario Wing", "Waddle Wing", "Peach Parasol", "Parachute", "Parefoil", 
                 "Flower Glider", "Bowser Kite", "Plane Glider", "MKTV Parafoil", "Gold Glider", "Hylian Kite", 
                 "Paraglider", "Paper Glider"]

    # Glider Print
    print('\nGLIDER')
    for i in range(players):
        rand_value = random.randint(0, len(gildeList) - 1)
        print(f'\tPlayer {i+1}: {rand_value + 1} \t{gildeList[rand_value]}')



def courses():
    COURSE_ROW = 4
    COURSE_COL = 6

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
                            'Feather Cup':['Athens Dash', 'Daisy Cruiser', 'Moonview Highway', 'Squeaky Clean Spirit'],
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


if __name__ == "__main__":

    # Player input for playing the game, how many players, and how many courses
    playChoice = "yes"
    while(playChoice.lower() == "yes"):
        max_items = -1
    
        players = int(input("\nHow many players? (MAX of 4)\n"))
        while players not in {1, 2, 3, 4}:
            players = int(input("How many players? (MAX of 4)\n"))
        
        COURSES = int(input("\nHow many Courses? (MAX of 48)\n"))
        while COURSES not in {1, 4, 6, 8, 12, 16, 24, 32, 48}:
            COURSES = int(input("How many Courses? (MAX of 48)\n"))

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
                case _:
                    random_set_i = input("\nDo you want a random number of items (random) or a set a number of items (set) \n")
            if ((max_items > 0) and (max_items <= numItemsList)):
                break

        #character roll
        characters()
        
        #kart roll
        karts()
        
        #wheel roll
        wheels()
        
        #glider roll
        gliders()

        # Items logic
        if(randomItems):
            items(random_set_b, max_items)

        # Course logic   
        courses()
        
        playChoice = input("\nWould you like to play? (YES/NO)\n")
    print("Kill yourself ong")
import random
import time
from MKWcharacter import Mario, Luigi, Peach, Daisy, Yoshi, Toad, KoopaTroopa, Bowser
from MKWcharacter import Wario, Waluigi, Rosalina, Pauline, BabyMario, BabyLuigi
from MKWcharacter import BabyPeach, BabyDaisy, Lakitu, Toadette, Bowserjr 
from MKWcharacter import BabyRosalina, Birdo, KingBoo, ShyGuy, DonkeyKong 

random.seed(time.time())


def characters():
    characters = [Mario(), Luigi(), Peach(), Daisy(), Yoshi(), Toad(), KoopaTroopa(), Bowser(),
                  Wario(), Waluigi(), Rosalina(), Pauline(), BabyMario(), BabyLuigi(),
                  BabyPeach(), BabyDaisy(), Lakitu(), Toadette(), Bowserjr(), 
                  BabyRosalina(), Birdo(), KingBoo(), ShyGuy(), DonkeyKong(), 'Nabbit', 
                  'Piranha Plant', 'Hammer Bro', 'Monty Mole', 'Goomba', 'Spike', 'Side Stepper', 
                  'Cheep Cheep', 'DryBones', 'Wiggler', 'Cataquack', 'Pianta', 'Rocky Wrench',
                  'Pokey', 'Peepa', 'Stingby', 'Cow', 'Snowman', 'Penguin', 'Para-Biddybud',
                  "Chargin' Chuck"]
    
    
    # Character Print
    print('\nCHARACTER')
    for i in range(players):
        character = random.randint(1, len(characters) - 1)
        print(f'\tPlayer {i+1}: {characters[character]}')

def karts():
    # Kart List
    kartList = ['Standard Kart', 'PlushBuggy', 'Zoom Buggy', 'Rally Kart', 'Baby Blooper',
                "Chargin' Truck", 'Standard Bike', 'Cute Scoot', 'Hyper Pipe', 
                'Rally Bike', 'Mach Rocket', 'Funky Dorrie', 'Hot Rod', 'Roadster Royale',
                'Biddybuggy', 'Ribbit Revster', 'B Dasher', 'Tiny Titan', 'Tune Thumper', 
                'W-Twon Chopper', 'Dread Sled', 'Junkyard Hog', 'Lobster Roller',
                'Stellar Sled', 'Reel Racer', 'Carpet Flyer', 'Big Horn', 'Bumble V', 'Cloud 9',
                "Li'l Dumpy", 'Fin Twin', 'Dolphin Dasher', 'Loco Moto', 'R.O.B. H.O.G.',
                'Blastronaut III', 'Mecha Trike', 'Pipe Frame', 'Blldozer', 'Rallygator',
                'Bowser Bruiser' ]
    
    # Kart Print
    print('\nKART')
    for i in range(players):
        rand_value = random.randint(0, len(kartList) - 1)
        print(f'\tPlayer {i+1}: {rand_value + 1} \t{kartList[rand_value]}')

def items():
    itemList = ['Normal', 'Franctic', 'Normal', 'Mushroom Only', 'Normal', 'Franctic', 'Normal', 'Mushroom Only'] 
    itemodds = len(itemList)
    itemoutput = random.randint(1, itemodds)

    print('\nITEMS')
    print(itemList[itemoutput])

def courses():  
    COURSE_ROW = 1
    COURSE_COL = 8

    #CUPS = 8
    #cups = random.randint(1, CUPS)

    print('\nCourses')
    course = random.randint(1,4)
    course_row = random.randint(1, COURSE_ROW)
    course_col = random.randint(1, COURSE_COL)
        

        
    courseList = {1:{1:[1, 2, 3, 4],2:[1, 2, 3, 4],3:[1, 2, 3, 4],4:[1, 2, 3, 4],5:[1, 2, 3, 4],
                           6:[1, 2, 3, 4], 7:[1, 2, 3, 4],8:[1, 2, 3, 4]}}
    
        
    courseNamesList = {1: {'Mushroom Cup':['Mario Bros. Circuit', 'Crown City', 'Whistle Summit', 'DK Spaceport'], 
                       'Flower Cup':['Desert Hills', 'Shy Guy Bazaar', 'Wario Stadium', 'Airship Fortress'],
                       'Star Cup':['DK Pass', 'Starview Peak', 'Sky-High Sunddae', 'Wario Shipyard'],
                       'Shell Cup':['Koopa Troopia Beach', 'Faraway Oasis', 'Crown City', 'Peach Stadium'],
                       'Banana Cup':['Peach Beach', 'Salty Salty Speedway', 'Dino Dino Jungle', 'Great ? Block Ruins'],
                       'Leaf Cup':['Cheep Cheep Falls', 'Dandelion Deaths', 'Boo Cinema', 'Dry Bones Burnout'],
                       'Lightning Cup':['Moo Moo Meadows', 'Choco Mountain', "Toad's Factory", "Bowser's Castle"],
                       'Special Cup':['Acorn Heights', 'Mario Circuit', 'Peach Stadium', 'Rainbow Road']}}
        
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

'''   for i in range(COURSES):
        while(course not in courseList[cups]):
            cups = random.randint(1, CUPS)
            course = random.randint(1,4)
        courseList[cups].remove(course)

        print(cups)
        cup = courseNamesList[cups]
        track = courseNamesList[cups][course - 1]
        print(f'\tCOURSE {i+1}: {cup}: {track}')
'''

if __name__ == "__main__":

    # Player input for playing the game, how many players, and how many courses
    playChoice = "yes"
    while(playChoice.lower() == "yes"):
    
        players = int(input("\nHow many players? (MAX of 4)\n"))
        while players not in {1, 2, 3, 4}:
            players = int(input("How many players? (MAX of 4)\n"))
        
        COURSES = int(input("\nHow many Courses? (MAX of 32)\n"))
        while COURSES not in {1, 3, 4, 5, 6, 8, 12, 16, 32}: 
            COURSES = int(input("How many Courses? (MAX of 32)\n"))


        #character roll
        characters()
        
        #kart roll
        karts()

        # Items logic
        items()


        # Course logic   
        courses() 
        
        playChoice = input("\nWould you like to play? (YES/NO)\n")
    print("Kill yourself ong")
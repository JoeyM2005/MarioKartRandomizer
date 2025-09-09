import random
import time
random.seed(time.time())


def courses(COURSES):  
    
    courseNamesList = ['Mario Bros. Circuit', 'Crown City', 'Whistle Summit', 'DK Spaceport',
                       'Desert Hills', 'Shy Guy Bazaar', 'Wario Stadium', 'Airship Fortress',
                       'DK Pass', 'Starview Peak', 'Sky-High Sunddae', 'Wario Shipyard',
                       'Koopa Troopia Beach', 'Faraway Oasis', 'Crown City', 'Peach Stadium',
                       'Peach Beach', 'Salty Salty Speedway', 'Dino Dino Jungle', 'Great ? Block Ruins',
                       'Cheep Cheep Falls', 'Dandelion Deaths', 'Boo Cinema', 'Dry Bones Burnout',
                       'Moo Moo Meadows', 'Choco Mountain', "Toad's Factory", "Bowser's Castle",
                       'Acorn Heights', 'Mario Circuit', 'Peach Stadium', 'Rainbow Road']
    
    print('\nCOURSES:')
    courseList = random.sample(courseNamesList, COURSES)
    for i in range(len(courseList)):
        print(f'\tCOURSE {i+1}: {courseList[i]}')
        

if __name__ == "__main__":
    COURSES = int(input("\nHow many Courses? (MAX of 32)\n"))
    while COURSES not in {1, 3, 4, 5, 6, 8, 12, 16, 32}: 
        COURSES = int(input("How many Courses? (MAX of 32)\n"))

    #val, valname = base(COURSES)
    courses(COURSES)
import random
import time
random.seed(time.time())

def courses(COURSES):  
    COURSE_ROW = 1
    COURSE_COL = 8

    #CUPS = 8
    #cups = random.randint(1, CUPS)

    print('\nCOURSES:')
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
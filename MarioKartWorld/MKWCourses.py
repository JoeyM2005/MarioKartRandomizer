import random
import time
random.seed(time.time())


def courses(COURSES):  
    CUPS = 8

    print('\nCOURSES:')
    cups = random.randint(1,CUPS)
    course =  random.randint(1,4)
        
    courseList = {1:[1, 2, 3, 4],2:[1, 2, 3, 4],3:[1, 2, 3, 4],4:[1, 2, 3, 4],5:[1, 2, 3, 4],
                           6:[1, 2, 3, 4], 7:[1, 2, 3, 4],8:[1, 2, 3, 4]}
    
        
    courseNamesList = {'Mushroom Cup':['Mario Bros. Circuit', 'Crown City', 'Whistle Summit', 'DK Spaceport'], 
                       'Flower Cup':['Desert Hills', 'Shy Guy Bazaar', 'Wario Stadium', 'Airship Fortress'],
                       'Star Cup':['DK Pass', 'Starview Peak', 'Sky-High Sunddae', 'Wario Shipyard'],
                       'Shell Cup':['Koopa Troopia Beach', 'Faraway Oasis', 'Crown City', 'Peach Stadium'],
                       'Banana Cup':['Peach Beach', 'Salty Salty Speedway', 'Dino Dino Jungle', 'Great ? Block Ruins'],
                       'Leaf Cup':['Cheep Cheep Falls', 'Dandelion Deaths', 'Boo Cinema', 'Dry Bones Burnout'],
                       'Lightning Cup':['Moo Moo Meadows', 'Choco Mountain', "Toad's Factory", "Bowser's Castle"],
                       'Special Cup':['Acorn Heights', 'Mario Circuit', 'Peach Stadium', 'Rainbow Road']}

    #list no cup
    # print(random.sample(mylist, k=4))
    #courseNamesList = ['Mario Bros. Circuit', 'Crown City', 'Whistle Summit', 'DK Spaceport',
     #                  'Desert Hills', 'Shy Guy Bazaar', 'Wario Stadium', 'Airship Fortress',
      #                 'DK Pass', 'Starview Peak', 'Sky-High Sunddae', 'Wario Shipyard',
       #                'Koopa Troopia Beach', 'Faraway Oasis', 'Crown City', 'Peach Stadium',
        #               'Peach Beach', 'Salty Salty Speedway', 'Dino Dino Jungle', 'Great ? Block Ruins',
         #              'Cheep Cheep Falls', 'Dandelion Deaths', 'Boo Cinema', 'Dry Bones Burnout',
          #             'Moo Moo Meadows', 'Choco Mountain', "Toad's Factory", "Bowser's Castle",
           #            'Acorn Heights', 'Mario Circuit', 'Peach Stadium', 'Rainbow Road']
    
    CupsNames = ['Mushroom Cup', 'Flower Cup', 'Star Cup', 'Shell Cup', 'Banana Cup', 'Leaf Cup', 'Lightning Cup', 'Special Cup']
        
    # Translates from numbers to the course cup and track for printing
    for i in range(COURSES):
        while(course not in courseList[cups]):
            cups = random.randint(1, CUPS)
            course = random.randint(1,4)
        
        courseList[cups].remove(course)
        track = courseNamesList[CupsNames[cups - 1]][course - 1]

        print(f'\tCOURSE {i+1}: {CupsNames[cups - 1]}: {track}')


def base(COURSES):
    COURSE_ROW = 1
    COURSE_COL = 8
    val = [0]*COURSES
    valname = ['None']*COURSES

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
        val[i] = {course_col: course}
        courseList[course_row][course_col].remove(course)
        cupList = list(courseNamesList[course_row].keys())

        cup = (cupList[course_col - 1])
        track = courseNamesList[course_row][cup][course - 1]
        valname[i] = {cup: courseNamesList[course_row][cup][course - 1]}
        print(f'\tCOURSE {i+1}: {cup}: {track}')
    print(val, '\n', valname)
        

    return val, valname

if __name__ == "__main__":
    COURSES = int(input("\nHow many Courses? (MAX of 32)\n"))
    while COURSES not in {1, 3, 4, 5, 6, 8, 12, 16, 32}: 
        COURSES = int(input("How many Courses? (MAX of 32)\n"))

    #val, valname = base(COURSES)
    courses(COURSES)
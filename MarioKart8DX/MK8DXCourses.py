import random
import time

random.seed(time.time())

def courses(COURSES):
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


import random

KART = 40
WHEEL = 21
GLIDE = 15

CHAR_ROW = 6
CHAR_COL = 8

MAX_ITEMS = 7
ITEM_ROW = 4
ITEM_COL = 6

players = int(input("How many players? (MAX of 48) "))

COURSES = int(input("How many Courses? (MAX of 96) "))
COURSE_ROW = 4
COURSE_COL = 6

print('\nCHARACTER')
for i in range(players):
    row = random.randint(1, CHAR_ROW)
    if row == 6:
        col = random.randint(1, CHAR_COL - 1)
    else:
        col = random.randint(1, CHAR_COL)
    print(f'Player {i+1}:\n\tROW: {row}\n\tCOL: {col}')

print('\nKART')
for i in range(players):
    print(f'Player {i+1}: {random.randint(1, KART)}')

print('\nWHEEL')
for i in range(players):
    print(f'Player {i+1}: {random.randint(1, WHEEL)}')

print('\nGLIDE')
for i in range(players):
    print(f'Player {i+1}: {random.randint(1, GLIDE)}')

print('\nITEMS')
for i in range(MAX_ITEMS):
    loopRow = random.randint(1, ITEM_ROW)
    if loopRow == 6:
        loopCol = random.randint(1, ITEM_COL - 2)
    else:
        loopCol = random.randint(1, ITEM_COL)
        
    print(f'\tITEM {i+1} ROW: {loopRow}\n\tITEM {i+1} COL: {loopCol}')
    
print('\nCOURSE')
course = random.randint(1,4)
course_row = random.randint(1, COURSE_ROW)
course_col = random.randint(1, COURSE_COL)

courseList = {1:{1:[1, 2, 3, 4],2:[1, 2, 3, 4],3:[1, 2, 3, 4],4:[1, 2, 3, 4],5:[1, 2, 3, 4],6:[1, 2, 3, 4]},
2:{1:[1, 2, 3, 4],2:[1, 2, 3, 4],3:[1, 2, 3, 4],4:[1, 2, 3, 4],5:[1, 2, 3, 4],6:[1, 2, 3, 4]},
3:{1:[1, 2, 3, 4],2:[1, 2, 3, 4],3:[1, 2, 3, 4],4:[1, 2, 3, 4],5:[1, 2, 3, 4],6:[1, 2, 3, 4]},
4:{1:[1, 2, 3, 4],2:[1, 2, 3, 4],3:[1, 2, 3, 4],4:[1, 2, 3, 4],5:[1, 2, 3, 4],6:[1, 2, 3, 4]}}
    
for i in range(COURSES):
    while(course not in courseList[course_row][course_col]):
        course_row = random.randint(1, COURSE_ROW)
        course_col = random.randint(1, COURSE_COL)
        course = random.randint(1,4)
    courseList[course_row][course_col].remove(course)
    print(f'\tCOURSE {i+1} ROW, COLUMN: {random.randint(1, COURSE_ROW)}, {random.randint(1, COURSE_COL)}')
    

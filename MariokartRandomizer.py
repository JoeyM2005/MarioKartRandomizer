import random
import time

random.seed(time.time())

KART = 40
WHEEL = 21
GLIDE = 15
PLAYERS = []

CHAR_ROW = 6
CHAR_COL = 8

MAX_ITEMS = 7
rand_items = random.randint(1,7)
ITEM_ROW = 4
ITEM_COL = 6

def assignCharacter(row, col):
    if(row == 1):
        if(col == 1): return 'Mario'
        if(col == 2): return 'Luigi'
        if(col == 3): return 'Peach'
        if(col == 4): return 'Daisy'
        if(col == 5): return 'Rosalina'
        if(col == 6): return 'Tanooki Mario'
        if(col == 7): return 'Cat Peach'
        if(col == 8): return 'Birdo'
    if(row == 2):
        if(col == 1): return 'Yoshi'
        if(col == 2): return 'Toad'
        if(col == 3): return 'Koopa Troopa'
        if(col == 4): return 'Shy Guy'
        if(col == 5): return 'Lakitu'
        if(col == 6): return 'Toadette'
        if(col == 7): return 'King Boo'
        if(col == 8): return 'Petey Piranha'
    if(row == 3):
        if(col == 1): return 'Baby Mario'
        if(col == 2): return 'Baby Luigi'
        if(col == 3): return 'Baby Peach'
        if(col == 4): return 'Baby Daisy'
        if(col == 5): return 'Baby Rosalina'
        if(col == 6): return 'Metal/Gold Mario'
        if(col == 7): return 'Pink Gold Peach'
        if(col == 8): return 'Wiggler'
    if(row == 4):
        if(col == 1): return 'Wario'
        if(col == 2): return 'Waluigi'
        if(col == 3): return 'Donkey Kong'
        if(col == 4): return 'Bowser'
        if(col == 5): return 'Dry Bones'
        if(col == 6): return 'Bowser Jr.'
        if(col == 7): return 'Dry Bowser'
        if(col == 8): return 'Kamek'
    if(row == 5):
        if(col == 1): return 'Lemmy'
        if(col == 2): return 'Lary'
        if(col == 3): return 'Wendy'
        if(col == 4): return 'Ludwig'
        if(col == 5): return 'Iggy'
        if(col == 6): return 'Roy'
        if(col == 7): return 'Morton'
        if(col == 8): return 'Peachette'
    if(row == 6):
        if(col == 1): return 'Inkling Girl'
        if(col == 2): return 'Villager'
        if(col == 3): return 'Isabelle'
        if(col == 4): return 'Link'
        if(col == 5): return 'Diddy Kong'
        if(col == 6): return 'Funky Kong'
        if(col == 7): return 'Pauline'

if __name__ == "__main__":
    playChoice = input("Would you like to play? (YES/NO) ")
    while(playChoice.lower() == "yes"):
    
        players = int(input("How many players? (MAX of 4) "))
        
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
            character = assignCharacter(row, col)
            print(f'Player {i+1}:\n\tROW, COL: {row}, {col}, {character}')
        
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
        for i in range(rand_items):
            loopRow = random.randint(1, ITEM_ROW)
            if loopRow == 6:
                loopRow = random.randint(1, ITEM_COL - 2)
            else:
                loopCol = random.randint(1, ITEM_COL)
                
            print(f'\tITEM {i+1} ROW, COL: {loopRow}, {loopCol}')
            
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
            print(f'\tCOURSE {i+1} ROW, COLUMN, TRACK: {random.randint(1, COURSE_ROW)}, {random.randint(1, COURSE_COL)}, {course}')
        
        playChoice = input("Would you like to play? (YES/NO)")
    print("Kill yourself ong")

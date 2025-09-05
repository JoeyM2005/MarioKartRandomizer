import random
import time
from MK8DXCharacters import characters
from MK8DXCombos import karts, gliders, wheels
from MK8DXItems import items
from MK8DXCourses import courses

random.seed(time.time())

# More Advanced Player Randomization


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

        
        #character roll
        characters(players)
        
        #kart roll
        karts(players)
        
        #wheel roll
        wheels(players)
        
        #glider roll
        gliders(players)

        # Items logic
        items()

        # Course logic   
        courses(COURSES) 
        
        playChoice = input("\nWould you like to play? (YES/NO)\n")
    print("Kill yourself ong")
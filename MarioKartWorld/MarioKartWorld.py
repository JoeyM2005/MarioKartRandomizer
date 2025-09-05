import random
import time

#imports
from MKWCharacters import characters
from MKWItems import items
from MKWCourses import courses
from MKWKarts import karts

random.seed(time.time())

if __name__ == "__main__":
    # Player input for playing the game, how many players, and how many courses
    playChoice = "yes"
    while(playChoice.lower() == "yes" or playChoice.lower() == "y"):
    
        players = int(input("\nHow many players? (MAX of 4)\n"))
        while players not in {1, 2, 3, 4}:
            players = int(input("How many players? (MAX of 4)\n"))
        
        COURSES = int(input("\nHow many Courses? (MAX of 32)\n"))
        while COURSES not in {1, 3, 4, 5, 6, 8, 12, 16, 32}: 
            COURSES = int(input("How many Courses? (MAX of 32)\n"))


        #character roll
        characters(players) #imported
        
        #kart roll
        karts(players) #imported

        # Items logic
        items() #imported

        # Course logic   
        courses(COURSES) #imported
        
        playChoice = input("\nWould you like to play? (YES/NO)\n")
    print("Kill yourself ong")
import random
import time

#imports
from MKWCharacters import characters
from MKWItems import items, itemListLength
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

        # Items logic
        itemList = ['Coin', 'Green Shell', 'Triple Green Shells', 'Red Shell', 'Triple Red Shells', 'Blue Shell',
            'Banana Peel', 'Triple Banana Peels', 'Mushroom', 'Triple Mushrooms', 'Golden Mushroom',
            'Mega Mushroom', 'Feather', 'Fire Flower', 'Ice Flower', 'Boomerang Flower', 'Star',
            'Super Horn', 'Lightning', 'Hammer', 'Blooper', 'Bob-omb', 'Bullet Bill', 'Boo', 'Coin Shell',
            '? Block', 'Kamek', 'Dash Food']

        #input for random vs set number
        random_set_i = input("\nDo you want a random number of items (random), set a number of items (set), or no random items (none)? \n")

        while True:
            match random_set_i.lower():
                case "random":
                    max_items = int(input(f"What is the max number of items you wish to randomize? (MAX of {itemListLength()})\n"))
                    random_set_b = True
                case "set":
                    max_items = int(input(f"How many items do you want? (MAX of {itemListLength()})\n"))
                    random_set_b = False
                case "none":
                    random_set_b = False
                    max_items = 0
                case _:
                    random_set_i = input("\nDo you want a random number of items (random), set a number of items (set), or no random items (none)? \n")
            if (((max_items > 0) and (max_items <= itemListLength())) or random_set_i.lower() == 'none'):
                break

        #character roll
        characters(players) #imported
        
        #kart roll
        karts(players) #imported

        # Items logic
        items(random_set_b, max_items) #imported

        # Course logic   
        courses(COURSES) #imported
        
        playChoice = input("\nWould you like to play? (YES/NO)\n")
    print("Thank you for using the randomizer")
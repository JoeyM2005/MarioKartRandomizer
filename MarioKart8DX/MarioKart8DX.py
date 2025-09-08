import random
import time
from MK8DXCharacters import characters
from MK8DXCombos import karts, gliders, wheels
from MK8DXItems import items, itemListLength, randomItem
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

        itemList = ['Banana Peel', 'Triple Banana Peels', 'Green Shell', 'Triple Green Shells',
        'Red Shell', 'Triple Red Shells','Blue Shell', 'Bomb-omb', 'Mushroom', 'Triple Mushroom',
        'Golden/Queen Mushroom', 'Bullet Bill', 'Blooper', 'Lightning', 'Star','Fireflower', 'Boomerang',
        'Piranha Plant', 'Boom Box', '8', 'Coin', 'Boo']

        #input for random vs set number
        random_set_i = input("\nDo you want a random number of items (random), set a number of items (set), or no random items (none)? \n")
        randomItem(True)
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
                    max_items = 1
                case _:
                    random_set_i = input("\nDo you want a random number of items (random) or a set a number of items (set) \n")
            if ((max_items > 0) and (max_items <= itemListLength())):
                break


        
        #character roll
        characters(players)
        
        #kart roll
        karts(players)
        
        #wheel roll
        wheels(players)
        
        #glider roll
        gliders(players)

        # Items logic
        items(random_set_b, max_items)

        # Course logic   
        courses(COURSES) 
        
        playChoice = input("\nWould you like to play? (YES/NO)\n")
    print("Kill yourself ong")
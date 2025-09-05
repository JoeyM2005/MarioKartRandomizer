import random
import time

random.seed(time.time())

def karts(players):
    # Kart List
    kartList = ["Standard Kart", "Pipe Frame", "Mach 8", "Steel Driver", "Cat Cruiser", "Circuit Special", "Tri-Speeder", "Badwagon",
                    "Prancer", "Biddybuggy", "Landship", "Sneeker", "Sportes Coupe", "Gold Standard", "GLA", "W 25 Silver Arrow",
                    "300 SL Roadster", "Blue Falcon", "Tanooki Kart", "B Dasher", "Streetle", "P-Wing", "Koopa Clown", "Standard Bike",
                    "Comet", "Sport Bike", "The Duke", "Flame Rider", "Varmint", "Mr. Scooty", "Jet Bike", "Yoshi Bike", "Master Cycle",
                    "Master Cycke Zero", "City Tripper", "Standard ATV", "WIld Wiggler", "Teddy Buggy", "Bone Rattler", "Splat Buggy", 
                    "Inkstriker"]
    
    # Kart Print
    print('\nKART')
    for i in range(players):
        rand_value = random.randint(0, len(kartList) - 1)
        print(f'\tPlayer {i+1}: {rand_value + 1} \t{kartList[rand_value]}')

def wheels(players):
    # Wheel List
    wheelList = ["Standard", "Monster", "Roller", "Slim", "Slick", "Metal", "Button", "Off-Road", "Sponge", "Wood", "Cushion",
                    "Blue Standard", "Hot Monster", "Azure Rider", "Crimson Slim", "Cyber Slick", "Retro Off-Road", "Gold Tires", 
                    "GLA Tires", "Triforce Tires", "Ancient Tires", "Leaf Tires"]
    
    # Wheel Print
    print('\nWHEEL')
    for i in range(players):
        rand_value = random.randint(0, len(wheelList) - 1)
        print(f'\tPlayer {i+1}: {rand_value + 1} \t{wheelList[rand_value]}')

def gliders(players):
    # Glide List
    gildeList = ["Super Glider", "Cloud Glider", "Wario Wing", "Waddle Wing", "Peach Parasol", "Parachute", "Parefoil", 
                 "Flower Glider", "Bowser Kite", "Plane Glider", "MKTV Parafoil", "Gold Glider", "Hylian Kite", 
                 "Paraglider", "Paper Glider"]

    # Glider Print
    print('\nGLIDER')
    for i in range(players):
        rand_value = random.randint(0, len(gildeList) - 1)
        print(f'\tPlayer {i+1}: {rand_value + 1} \t{gildeList[rand_value]}')


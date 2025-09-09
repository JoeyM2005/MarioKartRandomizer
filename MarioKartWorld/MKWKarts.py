import random
import time
random.seed(time.time())

def karts(players):
    # Kart List
    kartList = ['Standard Kart', 'Plushbuggy', 'Zoom Buggy', 'Rally Kart', 'Baby Blooper',
                "Chargin' Truck", 'Standard Bike', 'Cute Scoot', 'Hyper Pipe', 
                'Rally Bike', 'Mach Rocket', 'Funky Dorrie', 'Hot Rod', 'Roadster Royale',
                'Biddybuggy', 'Ribbit Revster', 'B Dasher', 'Tiny Titan', 'Tune Thumper', 
                'W-Twon Chopper', 'Dread Sled', 'Junkyard Hog', 'Lobster Roller',
                'Stellar Sled', 'Reel Racer', 'Carpet Flyer', 'Big Horn', 'Bumble V', 'Cloud 9',
                "Li'l Dumpy", 'Fin Twin', 'Dolphin Dasher', 'Loco Moto', 'R.O.B. H.O.G.',
                'Blastronaut III', 'Mecha Trike', 'Pipe Frame', 'Blldozer', 'Rallygator',
                'Bowser Bruiser' ]
    
    # Kart Print
    print('\nKART:')
    for i in range(players):
        rand_value = random.randint(0, len(kartList) - 1)
        print(f'\tPlayer {i+1}: {rand_value + 1} \t{kartList[rand_value]}')
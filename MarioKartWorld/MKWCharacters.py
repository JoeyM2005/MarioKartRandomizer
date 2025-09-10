import random
import time
random.seed(time.time())


def characters(players):
    characters = [Mario(), Luigi(), Peach(), Daisy(), Yoshi(), Toad(), KoopaTroopa(), Bowser(),
                  Wario(), Waluigi(), Rosalina(), Pauline(), BabyMario(), BabyLuigi(),
                  BabyPeach(), BabyDaisy(), Lakitu(), Toadette(), Bowserjr(), 
                  BabyRosalina(), Birdo(), KingBoo(), ShyGuy(), DonkeyKong(), 'Nabbit', 
                  'Piranha Plant', 'Hammer Bro', 'Monty Mole', 'Goomba', 'Spike', 'Side Stepper', 
                  'Cheep Cheep', 'Dry Bones', 'Wiggler', 'Cataquack', 'Pianta', 'Rocky Wrench',
                  'Pokey', 'Peepa', 'Coin Coffer', 'Stingby', 'Cow', 'Snowman', 'Penguin', 'Para-Biddybud',
                  "Chargin' Chuck", 'Swoop', 'Conkdor', 'Dolphin', 'Fish Bones']
    
    
    # Character Print
    print('\nCHARACTER:')
    for i in range(players):
        character = random.randint(1, len(characters) - 1)
        print(f'\tPlayer {i+1}: {characters[character]}')

def randomCharVar(charList):
    m_num = random.randint(0, len(charList) - 1)
    return charList[m_num]

def Mario():
    Marios = ['Mario', 'Mechanic Mario', 'Sightseeing Mario', 'All-Terrain Mario',
              'Touring Mario', 'Dune Rider Mario', 'Aviator Mario', 'Pro Racer Mario'
              'Cowboy Mario', 'Happi Mario']
    return randomCharVar(Marios)
    
def Luigi():
    Luigis = ['Luigi', 'Touring Luigi', 'Pro Racer Luigi', 'Farmer Luigi',
              'Gondolier Luigi', 'Mechanic Luigi', 'Happi Luigi', 
              'Oasis Luigi', 'All-Terrain Luigi']
    return randomCharVar(Luigis)

def Peach():
    Peaches = ['Pro Racer Peach', 'Peach', 'Farmer Peach', 'Touring Peach', 
              'Sightseeing Peach', 'Aviator Peach', 'Vacation Peach', 
              'Yukato Peach', 'Aero Peach']
    return randomCharVar(Peaches)

def Daisy():
    Daisies = ['Pro Racer Daisy', 'Aero Daisy', 'Daisy', 'Oasis Daisy', 
               'Vacation Daisy', 'Touring Daisy', 'Swimwear Daisy']
    return randomCharVar(Daisies)

def Yoshi():
    Yoshis = ['Yoshi', 'Touring Yoshi', 'Soft Server Yoshi', 'Matsuri Yoshi',
               'Pro Racer Yoshi', 'Biker Yoshi', 'Food Slinger Yoshi', 
               'Aristocrat Yoshi', 'Swimwear Yoshi']
    return randomCharVar(Yoshis)

def DonkeyKong():
    DonkeyKongs = ['All-Terrain Donkey Kong', 'Donkey Kong`']
    return randomCharVar(DonkeyKongs)

def Bowser():
    Bowsers = ['Bowser', 'Pro Racer Bowser', 'Supercharged Bowser', 'Biker Bowser',
               'All-Terrain Bowser']
    return randomCharVar(Bowsers)

def Bowserjr():
    Bowserjrs = ['Bowser Jr.', 'Explorer Bowser Jr.', 'Pro Racer Bowser Jr.',
                  'Biker Jr Bowser Jr']
    return randomCharVar(Bowserjrs)

def KoopaTroopa():
    KoopaTroopas = ['Pro Racer Koopa Troopa', 'Koopa Troopa', 'Sailor Koopa Troopa'
                    'Runner Koopa Troopa', 'All-Terrain Koopa Troopa', 'Work Crew Koopa Troopa']
    return randomCharVar(KoopaTroopas)

def Toad():
    Toads = ['Engineer Toad', 'Toad', 'Burger Bud Toad', 'Pro Racer Toad', 'Explorer Toad']
    return randomCharVar(Toads)

def Toadette():
    Toadettes = ['Toadette', 'Soft Server Toadette', 'Pro Racer Toadette', 'Explorer Toadette',
                 'Conductor Toadette']
    return randomCharVar(Toadettes)

def Lakitu():
    Lakitus = ['Lakitu', 'Pit Crew Lakitu', 'Fisherman Lakitu']
    return randomCharVar(Lakitus)

def KingBoo():
    KingBoos = ['Pro Racer King Boo', 'Aristocrat King Boo', 'King Boo', 'Pirate King Boo']
    return randomCharVar(KingBoos)

def ShyGuy():
    ShyGuys = ['Shy Guy', 'Pit Crew Shy Guy', 'Slope Styler Shy Guy']
    return randomCharVar(ShyGuys)

def Wario():
    Warios = ['Wario', 'Pro Racer Wario', 'Oasis Wario', 'Wicked Wasp Wario', 
              'Road Ruffian Wario', 'Biker Wario', 'Work Crew Wario', 
              'Pirate Wario']
    return randomCharVar(Warios)

def Waluigi():
    Waluigis = ['Pro Racer Waluigi', 'Biker Waluigi', 'Wampire Waluigi', 
                'Road Ruffian Waluigi', 'Waluigi', 'Mariachi Waluigi']
    return randomCharVar(Waluigis)

def Birdo():
    Birdos = ['Birdo', 'Pro Racer Birdo', 'Vacation Birdo']
    return randomCharVar(Birdos)

def Pauline():
    Paulines = ['Aero Pauline', 'Pauline']
    return randomCharVar(Paulines)

def Rosalina():
    Rosalinas = ['Pro Racer Rosalina', 'Rosalina', 'Aurora Rosalina', 
                 'Touring Rosalina', 'Aero Rosalina']
    return randomCharVar(Rosalinas)

def BabyMario():
    BabyMarios = ['Baby Mario', 'Pro Racer Baby Mario', 'Swimwear Baby Mario',
                  'Work Crew Baby Mario']
    return randomCharVar(BabyMarios)

def BabyLuigi():
    BabyLuigis = ['Work Crew Baby Luigi', 'Baby Luigi', 'Pro Racer Baby Luigi']
    return randomCharVar(BabyLuigis)

def BabyPeach():
    BabyPeaches = ['Pro Racer Baby Peach', 'Baby Peach', 'Sailor Baby Peach',
                   'Touring Baby Peach', 'Explorer Baby Peach']
    return randomCharVar(BabyPeaches)

def BabyDaisy():
    BabyDaisies = ['Baby Daisy', 'Touring Baby Daisy', 'Pro Racer Baby Daisy',
                    'Sailor Baby Daisy', 'Explorer Baby Daisy']
    return randomCharVar(BabyDaisies)

def BabyRosalina():
    BabyRosalinas = ['Touring Baby Rosalina', 'Explorer Baby Rosalina', 
                     'Pro Racer Baby Rosalina', 'Baby Rosalina', 'Sailor Baby Rosalina']
    return randomCharVar(BabyRosalinas)


"""
if __name__ == "__main__":

    players = 4
    for i in range(50):
        characters(players)
"""

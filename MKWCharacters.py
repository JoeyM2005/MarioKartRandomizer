import random
import time
random.seed(time.time())

def characters(players):
    characters = [Mario(), Luigi(), Peach(), Daisy(), Yoshi(), Toad(), KoopaTroopa(), Bowser(),
                  Wario(), Waluigi(), Rosalina(), Pauline(), BabyMario(), BabyLuigi(),
                  BabyPeach(), BabyDaisy(), Lakitu(), Toadette(), Bowserjr(), 
                  BabyRosalina(), Birdo(), KingBoo(), ShyGuy(), DonkeyKong(), 'Nabbit', 
                  'Piranha Plant', 'Hammer Bro', 'Monty Mole', 'Goomba', 'Spike', 'Side Stepper', 
                  'Cheep Cheep', 'DryBones', 'Wiggler', 'Cataquack', 'Pianta', 'Rocky Wrench',
                  'Pokey', 'Peepa', 'Stingby', 'Cow', 'Snowman', 'Penguin', 'Para-Biddybud',
                  "Chargin' Chuck"]
    
    
    # Character Print
    print('\nCHARACTER:')
    for i in range(players):
        character = random.randint(1, len(characters) - 1)
        print(f'\tPlayer {i+1}: {characters[character]}')

def Mario():
    Marios = ['Mario', 'Mechanic Mario', 'Sightseeing Mario', 'All-Terrain Mario',
              'Touring Mario', 'Dune Rider Mario', 'Aviator Mario', 'Pro Racer Mario'
              'Cowboy Mario', 'Happi Mario']
    m_num = random.randint(0, len(Marios) - 1)
    return Marios[m_num]
    
def Luigi():
    Luigis = ['Luigi', 'Touring Luigi', 'Pro Racer Luigi', 'Farmer Luigi',
              'Gondolier Luigi', 'Mechanic Luigi', 'Happi Luigi', 
              'Oasis Luigi', 'All-Terrain Luigi']
    m_num = random.randint(0, len(Luigis) - 1)
    return Luigis[m_num]

def Peach():
    Peaches = ['Pro Racer Peach', 'Peach', 'Farmer Peach', 'Touring Peach', 
              'Sightseeing Peach', 'Aviator Peach', 'Vacation Peach', 
              'Yukato Peach', 'Aero Peach']
    m_num = random.randint(0, len(Peaches) - 1)
    return Peaches[m_num]

def Daisy():
    Daisies = ['Pro Racer Daisy', 'Aero Daisy', 'Daisy', 'Oasis Daisy', 
               'Vacation Daisy', 'Touring Daisy', 'Swimwear Daisy']
    m_num = random.randint(0, len(Daisies) - 1)
    return Daisies[m_num]

def Yoshi():
    Yoshies = ['Yoshi', 'Touring Yoshi', 'Soft Server Yoshi', 'Matsuri Yoshi',
               'Pro Racer Yoshi', 'Biker Yoshi', 'Food Slinger Yoshi', 
               'Aristocrat Yoshi', 'Swimwear Yoshi']
    m_num = random.randint(0, len(Yoshies) - 1)
    return Yoshies[m_num]

def DonkeyKong():
    DonkeyKongs = ['All-Terrain Donkey Kong', 'Donkey Kong`']
    m_num = random.randint(0, len(DonkeyKongs) - 1)
    return DonkeyKongs[m_num]

def Bowser():
    Bowsers = ['Bowser', 'Pro Racer Bowser', 'Supercharged Bowser', 'Biker Bowser',
               'All-Terrain Bowser']
    m_num = random.randint(0, len(Bowsers) - 1)
    return Bowsers[m_num]

def Bowserjr():
    Bowserjrs = ['Bowser Jr.', 'Explorer Bowser Jr.', 'Pro Racer Bowser Jr.',
                  'Biker Jr Bowser Jr']
    m_num = random.randint(0, len(Bowserjrs) - 1)
    return Bowserjrs[m_num]

def KoopaTroopa():
    KoopaTroopas = ['Pro Racer Koopa Troopa', 'Koopa Troopa', 'Sailor Koopa Troopa'
                    'Runner Koopa Troopa', 'All-Terrain Koopa Troopa' 'Work Crew Koopa Troopa']
    m_num = random.randint(0, len(KoopaTroopas) - 1)
    return KoopaTroopas[m_num]

def Toad():
    Toads = ['Engineer Toad', 'Toad', 'Burger Bud Toad', 'Pro Racer Toad', 'Explorer Toad']
    m_num = random.randint(0, len(Toads) - 1)
    return Toads[m_num]

def Toadette():
    Toadettes = ['Toadette', 'Soft Server Toadette', 'Pro Racer Toadette', 'Explorer Toadette',
                 'Conductor Toadette']
    m_num = random.randint(0, len(Toadettes) - 1)
    return Toadettes[m_num]

def Lakitu():
    Lakitus = ['Lakitu', 'Pit Crew Lakitu', 'Fisherman Lakitu']
    m_num = random.randint(0, len(Lakitus) - 1)
    return Lakitus[m_num]

def KingBoo():
    KingBoos = ['Pro Racer King Boo', 'Aristocrat King Boo', 'King Boo', 'Pirate King Boo']
    m_num = random.randint(0, len(KingBoos) - 1)
    return KingBoos[m_num]

def ShyGuy():
    ShyGuys = ['Shy Guy', 'Pit Crew Shy Guy', 'Slope Styler Shy Guy']
    m_num = random.randint(0, len(ShyGuys) - 1)
    return ShyGuys[m_num]

def Wario():
    Warios = ['Wario', 'Pro Racer Wario', 'Oasis Wario', 'Wicked Wasp Wario', 
              'Road Ruffian Wario', 'Biker Wario', 'Work Crew Wario', 
              'Pirate Wario']
    m_num = random.randint(0, len(Warios) - 1)
    return Warios[m_num]

def Waluigi():
    Waluigis = ['Pro Racer Waluigi', 'Biker Waluigi', 'Wampire Waluigi', 
                'Road Ruffian Waluigi', 'Waluigi', 'Mariachi Waluigi']
    m_num = random.randint(0, len(Waluigis) - 1)
    return Waluigis[m_num]

def Birdo():
    Birdos = ['Birdo', 'Pro Racer Birdo', 'Vacation Birdo']
    m_num = random.randint(0, len(Birdos) - 1)
    return Birdos[m_num]

def Pauline():
    Paulines = ['Aero Pauline', 'Pauline']
    m_num = random.randint(0, len(Paulines) - 1)
    return Paulines[m_num]

def Rosalina():
    Rosalinas = ['Pro Racer Rosalina', 'Rosalina', 'Aurora Rosalina', 
                 'Touring Rosalina', 'Aero Rosalina']
    m_num = random.randint(0, len(Rosalinas) - 1)
    return Rosalinas[m_num]

def BabyMario():
    BabyMarios = ['Baby Mario', 'Pro Racer Baby Mario', 'Swimwear Baby Mario',
                  'Work Crew Baby Mario']
    m_num = random.randint(0, len(BabyMarios) - 1)
    return BabyMarios[m_num]

def BabyLuigi():
    BabyLuigis = ['Work Crew Baby Luigi', 'Baby Luigi', 'Pro Racer Baby Luigi']
    m_num = random.randint(0, len(BabyLuigis) - 1)
    return BabyLuigis[m_num]

def BabyPeach():
    BabyPeaches = ['Pro Racer Baby Peach', 'Baby Peach', 'Sailor Baby Peach',
                   'Touring Baby Peach', 'Explorer Baby Peach']
    m_num = random.randint(0, len(BabyPeaches) - 1)
    return BabyPeaches[m_num]

def BabyDaisy():
    BabyDaisies = ['Baby Daisy', 'Touring Baby Daisy', 'Pro Racer Baby Daisy',
                    'Sailor Baby Daisy', 'Explorer Baby Daisy']
    m_num = random.randint(0, len(BabyDaisies) - 1)
    return BabyDaisies[m_num]

def BabyRosalina():
    BabyRosalinas = ['Touring Baby Rosalina', 'Explorer Baby Rosalina', 
                     'Pro Racer Baby Rosalina', 'Baby Rosalina', 'Sailor Baby Rosalina']
    m_num = random.randint(0, len(BabyRosalinas) - 1)
    return BabyRosalinas[m_num]


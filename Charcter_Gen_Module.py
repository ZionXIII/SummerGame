# Random Character Character Creator

import random


Class_dict = {'Pit Fighter':(290, , 50, 30, 5, 'Trident', 'Crowd Pleasing', 'Net', 'Rough Play'),
              'Warrior':(300, , 55, 28, 0, 'Slash and Burn', 'Whirlwind', 'Battle Cry', 'Berserk'),
              'Druid':(280, , 45, 24, 7, 'Wrath of Nature', 'Natural Cure', 'Savagry', ''),
              'Executioner':(270, , 60, 20, 2, 'Execution', 'Execution', 'Murderous Intent', 'Stench of Death'), # Garantees to get Execute.
              'Geomancer':(260, , 40, 23, 4, 'Crystal Burst', 'Earthquake', 'Sandstorm', 'Stone Skin'),
              'Assassin':(250, , 80, 13, 9, 'Critical Strike', 'Hunt', 'Lethal Strike', 'Poison'),
              'Scout':(240, , 45, 16, 8, 'Track', 'Long Strike', 'Steady Shot', ''),
              'Shaman':(230, 38, , 17, 3, 'Life Steal', ' Effigy Stab', 'Healing Salve',''),
              'Alchemist':(220, , 36, 19, 1, 'Property Shift: Power for Life', 'Property Shift: Life for Power', 'Poison Bomb', 'Gold Conversion'),
              'Orator':(210, , 33, 10, 6, 'A Call to Arms!', 'We the Powerful!', 'Condemning Shouts!', 'Hearts and Minds!')}
            # 'Class Name': Health, Magic Points, Damage, Defense, Speed, Ability1, Ability2, Ability3, Ability4

Historys_dict = {'Tundra':1,
                 'Mountains':2,
                 'Outlander':1,
                 'Swamps':2,
                 'Rural':1,
                 'Plains':2,
                 'Woodsdwellers':1,
                 'Seafarer':2,
                 'RiverDweller':1,
                 'Desert Nomad':2,}

Group_dict = {'Noble': 3,
              'Orpan': 4,
              'Merchants': 4,
              'Populist': 3,
              'Gangsters': 3,
              'Academics': 4,
              'Fanatic': 3,
              'Military': 4,
              'Farmer': 3,
              'Bohemian': 4}

Ability_dict = {'':(), # (Description, Damage, Secondary Effects)
                
                '':()}

Aspirations_Dict = {'Swords to Plowshares':('health', 'attack'),
                    'Absolute Power':('attack', 'speed'),
                    'Knowledge':('intelligence', 'health'),
                    'Accolades':('', ''),
                    'To Protect the Weak':('', ''),
                    'Thrill of the Hunt':(),
                    'Outsmarting':(),
                    'Riches':(),
                    'The Kill':(),
                    '':()}
                    # 'Trait Name': Stat up, Stat Down
                    
Faults_dict = {'Weak of Heart':('speed','health'),
               'Merciless':(),
               'Uncomprimising':('Defense'),
               'Hotheaded':(),
               'Thrill Seeking':(),
               'Depressed':(),
               'Incompetent':(),
               'Mad':(), # mad mad mad world
               'Hateful':(),
               'Unintelligent':()}
               # 'Trait Name': Stat up, Stat Down

def seed_gen():
    seed = ''
    for i in range(6):
        rand_num = str(random.randrange(0,10))
        seed += rand_num
    return seed

def ability_Draft():
    return False

def history_gen():
    return False


def main(Class_dict, History_dict, Group_dict, Ability_dict, Aspirations_dict, Faults_dict):
    char_seed = 
    return False




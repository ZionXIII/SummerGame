# This is the Classes that will be used for the Tactics game.
#
#
#

class Game_Character:
    def __init__ (self, Class_title, name, health, magic_points, damage, speed, ability1, ability2, effect_pocket=None, char_art, history, group, aspirations, faults):
        self.name = name
        self.health = health
        self.magic_points = magic_points
        self.damage = damage
        self.speed = speed
        self.ability1 = ability1
        self.ability2 = ability2
        self.effect_pocket = effect_pocket
        self.char_art = char_art
        self.history = history
        self.group = group
        self.aspirations = aspirations
        self.faults = faults

    def healthChange(self, health, change):
        self.health += change

    def magicChange(self, magic_points, change):
        self.magic_points += change

    def ability1(self, ability1):
        self.ability_name = ability1[0]
        self.ability_effect = ability1[1]

    def ability2(self, ability2):
        self.ability_name = ability2[0]
        self.ability_effect = ability2[1]

    def effect_pocket(self, effect, turns):
        self.effect = effect
        self.turns = turns

    

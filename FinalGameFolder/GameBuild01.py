# Final fantasy tactics styled clone with RNG character creation.
# By Bryce Emery 2014
# Some code is utilized from Al Sweigart's book on making games with
# pygame. http://inventwithpython.com/pygame
# Image "Plain_Block.png' is also used from the resources used in the book.
# This image will be removed as art is developed by me.
#

import random, sys, copy, os, pygame, Character_Gen_Module.py
from pygame.locals import *

FPS = 30 # frames per second to update
WINWIDTH = 900
WINHEIGHT = 700
HALF_WINWIDTH = int(WINWIDTH/ 2)
HALF_WINHEIGHT = int(WINHEIGHT/ 2)

# The total width and hight for each tile in pixels
TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 45
MAXBOARDTILES = 196 # 14 x 14 tile board

CAM_MOVE_SPEED = 5 # how many pixels per frame the camera moves.

# COLORS      R    G    B
WHITE      = (255, 255, 255)
BLACK      = (0  ,   0,   0)
BURLYWOOD = (222, 184, 135)
GREY       = (128, 128, 128)
LIGHTGREY =  (190, 190, 190)

BGCOLOR = LIGHTGREY

UP = 'up'
DOWN =  'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, PLAYERIMAGES

    # Pygame initialization and basic set up of the global variables.
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

    mousex = 0
    mousey = 0

    mouseSelection = None

    pygame.display.set_caption('Frantic! Frantic! Tactics')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    DISPLAYSURF.fill(BGCOLOR)


    # A global dict value that will contain all the Pygame
    # Surface objects returned by pygame.image.load().
    IMAGESDICT = {'inside floor': pygame.image.load('Plain_Block.png'),
                  'pit fighter': pygame.image.load('Pit_Fighter.png'),
                  'warrior': pygame.image.load('Warrior.png'),
                  'druid': pygame.image.load('Druid.png'),
                  'executioner': pygame.image.load('Executioner.png'),
                  'geomancer': pygame.image.load('Geomancer.png'),
                  'assassin': pygame.image.load('Assassin.png'),
                  'scout': pygame.image.load('Scout.png'),
                  'shaman': pygame.image.load('Shaman.png'),
                  'alchemist': pygame.image.load('Alchemist.png'),
                  'orator': pygame.image.load('Orator.png')}


    # PLAYERIMAGES is a list of all possible characters tha player can be.
    # currentImage is the index of the player's current image.
    currentImages = 0
    PLAYERIMAGES = {IMAGESDICT['pit fighter'],
                    IMAGESDICT['warrior'],
                    IMAGESDICT['druid'],
                    IMAGESDICT['executioner'],
                    IMAGESDICT['geomancer'],
                    IMAGESDICT['assassin'],
                    IMAGESDICT['scout'],
                    IMAGESDICT['shaman'],
                    IMAGESDICT['alchemist'],
                    IMAGESDICT['orator']}

    startScreen() # show the title screen until the user takes action.

    player_one_team = team_creator()
    player_two_team = team_creator()
    
    while True: # main game loop
        mouse_clicked = False

        DISPLAYSURF.fill(BGCOLOR) # Drawing the window
        drawboard()

        for event in pygame.event.get(): # Event handlng loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        

            
def startScreen(): # Shows intructions for two players, ends when player clicks.
    return False

def team_create():
    team_list = []
    for i in range(5):
        char = createCharacter # from Character_Gen_Module, returns class or dict?
        team_list.append(char)
    return team_list # Will return team as tuple of dictionaries.

def menus(mouse_selection):
    
    return menu_selection

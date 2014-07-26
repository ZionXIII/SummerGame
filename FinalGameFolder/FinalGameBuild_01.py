# Final fantasy tactics styled clone with RNG character creation.
# By Bryce Emery 2014
#
#
#
#
#

import random, sys, copy, os, pygame
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

CAM_MOVE_SPEED = 5 # how many pixels per frame the camera moves.

NON_GRASS_TILES_PERCENTAGE = 20 # percentage of map that is not simple grass.


# COLORS      R    G    B
WHITE      = (255, 255, 255)
BLACK      = (0  ,   0,   0)
BURLY WOOD = (222, 184, 135)
GRAY       = (128, 128, 128)

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

    pygame.display.set_caption('Frantic! Frantic! Tactics')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    # A global dict value that will contain all the Pygame
    # Surface objects returned by pygame.image.load().
    IMAGESDICT = {''




                  ''}

    # These dict values are global, and map the character that appears
    # in the level file to the Surface object it represents.
    TILEMAPPING = {''



                   ''}
    OUTSIDEDECOMAPPING = {''



                          ''}

    # PLAYERIMAGES is a list of all possible characters tha player can be.
    # currentImage is the index of the player's current image.
    currentImages = 0
    PLAYERIMAGES = {''


                    ''}

    startScreen() # show the title screen until the user takes action.

    

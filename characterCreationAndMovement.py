# Bryce Emery
# 08/16/14
# 
# Note: a "###" denotes an inprogress comment. 


import pygame, sys
from pygame.locals import *
from math import sqrt

FPS = 30 # frames per second
WINWIDTH = 900
WINHEIGHT = 525
HALF_WINWIDTH = int(WINWIDTH/ 2)
HALF_WINHEIGHT = int(WINHEIGHT/ 2)

# The total width and hight for each tile in pixels
TILESIZE = 45 # height and width are the same
TILEFLOORHEIGHT = 45
MAXBOARDTILES = 100 # 14 x 14 tile board
BOARDLENGTH = sqrt(MAXBOARDTILES)
BOARDLEFT = 200
BOARDTOP = 10
BOARDSIDE = 505
TILELEFT = 200
TILETOP = 10
TILEMARGINS = 5
MENUHEIGHT = 505
MENUWIDTH = 180
BUTTONHEIGHT = 65
BUTTONWIDTH = 170
BUTTONCENTERX = int((MENUWIDTH + 5)/2)


# COLORS           R    G    B    Alpha
WHITE          = (255, 255, 255)
BLACK          = (0  ,   0,   0)
BURLYWOOD      = (222, 184, 135)
GREY           = (128, 128, 128)
LIGHTGREY      = (190, 190, 190)
RED            = (255,   0,   0)
BLUE           = (  0,   0, 255)
GREEN          = (  0, 255,   0)
OLIVEGREEN     = (100, 165, 100)
CRIMSON        = (165, 100, 100)
HIGHLIGHTRED   = (155,   0,   0, 100)
HIGHLIGHTBLUE  = (  0,   0, 155, 100)
HIGHLIGHTGREEN = (  0, 155,   0, 100)
HIGHLIGHTWHITE = (255, 255, 255, 100)

BGCOLOR         = LIGHTGREY
HIGHLIGHTCOLOR  = BLUE
BOARDCOLOR      = OLIVEGREEN
TILECOLOR       = BURLYWOOD
CHARCOLOR       = BLUE

def main():
    global FPSCLOCK, DISPLAYSURF, HALF_WINHEIGHT, HALF_WINWIDTH
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode(( WINWIDTH, WINHEIGHT))
    mousex = 0
    mousey = 0
    mouseSelection = None

    pygame.display.set_caption('Window Practice')
    menu = pygame.Rect( 10, 10, MENUWIDTH, MENUHEIGHT)
    board = pygame.Rect( BOARDLEFT, BOARDTOP, BOARDSIDE, BOARDSIDE)
    menuTitleObj = drawWords('Menu')
    textRectObj = menuTitleObj.get_rect()
    textRectObj.center = (95 , 25)
    tile_list = tileMapping()

    TESTCHARSIZE = int(TILESIZE / 2)
    TESTCHAR = charCreation()

    ### Just kepp going through the list of 6.3, relax and enjoy it. Try to go through it all, since it is short and
    # understanding your own thought process is paramount.
    
    CHAR_CENTER = tile_list[TESTCHAR.location].center
    

    while True: # main game loop
        mouse_clicked = False

        DISPLAYSURF.fill(BGCOLOR)
        pygame.draw.rect(DISPLAYSURF, CRIMSON, menu)
        pygame.draw.rect(DISPLAYSURF, BOARDCOLOR, board)

        DISPLAYSURF.blit(menuTitleObj, textRectObj)

        tileDrawing(tile_list)
        TESTSRITE = pygmae.draw.circle(DISPLAYSURF, BLUE, (CHAR_CENTER), TESTCHARSIZE, 0)
        tileUpdate(tile_list, 32, True, 'TESTCHAR')

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            elif event.type == KEYDOWN:
                key_pressed = True

                if event.key == K_ESCAPE:
                    exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouse_clicked = True
                while mouse_clicked == True:
                    
                    if menu.collidepoint(mousex, mousey) == True:
                        player_action = tileClickGet('menu', mousex, mousey, '') # create menu tile_list
                        menu
                        mouse_clicked = False
                    elif board.collidepoint(mousex, mousey) == True:
                        player_action = tileClickGet('board', mousex, mousey, tile_list)
                        mouse_clicked = False
                    else:
                        mouse_clicked = False
                if tile_list[player_action].

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        

def tileMapping(): # creates the values the tiles for the game board
    next_box_left = TILEMARGINS
    next_box_top = TILEMARGINS
    tile_list = []
    for i in range(int(sqrt(MAXBOARDTILES))): # creates the first square in a row, then moves down a column space.
        tile = pygame.Rect((TILELEFT + next_box_left), (TILETOP + next_box_top), TILESIZE, TILESIZE, occupied = False, occupant = None )# added paramaters for use character movement.
        tile_list.append(tile)
        for j in range(int(sqrt(MAXBOARDTILES) - 1)): # creates the next 9 squares in a row.
            next_box_left += (TILESIZE + TILEMARGINS)
            tile= pygame.Rect((TILELEFT + next_box_left), (TILETOP + next_box_top), TILESIZE, TILESIZE, occupied = False, occupant = None )
            tile_list.append(tile)
        next_box_top += (TILESIZE + TILEMARGINS)
        next_box_left = TILEMARGINS
    return tile_list

def tileDrawing(tile_list): # Draws the game boards tiles.
    for i in range(len(tile_list)):
        pygame.draw.rect(DISPLAYSURF, TILECOLOR,tile_list[i]) # occupied = False, occupant = None

def tileClickGet(location, mousex, mousey, tile_list): 
    mouse_clicked = False
    mouse_click = pygame.Rect( mousex ,mousey, 0, 0)
    if location == 'board':
        for i in range(len(tile_list)):
            tile_clicked = mouse_click.collidelist(tile_list)
            if tile_clicked > -1:
                print('Tile number:', tile_clicked)
                break
    elif location == 'menu':
        for i in range(len(tile_list)):
            tile_clicked = mouse_click.collidelist(title_list[i])
            if tile_clicked >-1:
                print('menu run something here')
                break
    return mouse_clicked

def tileUpdate(tile_list, tile_num, toggle, Occupant=None):
    if toggle == True:
        tile_list[tile_num].occupied = not tile_list[tile_num].occupied
    if parameter != None
        tile_list[tile_num].occupant = Occupant # feed a string name to call a character class.#

def menuButtons(button_clicked='main', character=None):
    if button_clicked == 'main':
        if character == None:
            button_list = ['', 'Move', 'Attack', 'Stats', 'Quit']  
        else:
        button_list = [char.name, 'Move','Attack', 'Stats', 'Quit']
    elif button_clicked == 'Move'
    return button_list

def buttonDrawing(button_list):
    
    for i in range(len(button_list)):
        pygame.draw.rect(DISPLAYSURF, RED, (MENULEFT + 5), (MENUTOP + 5 + (BUTTONHEIGHT * i)), BUTTONWIDTH, BUTTONHEIGHT)
        pygame.###How do I render text esialy!!!##
    return
    
def charCreation():
    TEAMNUMBER = 1
    team_list = []
    for i in range(TEAMNUMBER):
        NAME = 'char_' + str(i)
        CLASS = 'Nothing Yet'
        ATTACKDAMAGE = 10
        ABILITY1 = 'Nothing Yet'
        ABILITY2 = 'Nothing Yetx2'
        MOVESPEED = 5
        SPRITE = 'Needs to be replaced with the pygame.blit function' # Read the string.#
        PLAYERSIDE = 0
        LOCATION = 32
        TESTCHAR = GameCharacter(NAME, CLASS, ATTACKDAMAGE, ABILITY1, ABILITY2, MOVESPEED, SPRITE, PLAYERSIDE, LOCATION, TESTCHAR)
    return TESTCHAR # normally return character team_list.

def creatSprites(char_list):
    sprite_dict = {}
    for i in range(10):
        sprite_dict.append(char_list[i].name)
        sprite_dict[i] = 
            

def listPuller(): # It pulls from lists for the charCreation function.
    return None


class GameCharacter:
    def __init__(self, NAME, CLASS, ATTACKDAMAGE, ABILITY1, ABILITY2, MOVESPEED, SPRITE, PLAYERSIDE, LOCATION=None, EFFECTPOCKET=None):
        self.name = NAME
        self.charclass = CLASS
        self.attackdamage = ATTACKDAMAGE
        self.ability1 = ABILITY1
        self.ability2 = ABILITY2
        self.movespeed = MOVESPEED
        self.sprite = SPRITE
        self.playerside = PLAYERSIDE
        self.location = LOCATION # An index number from the tile_list
        self.effectpockets = EFFECTPOCKET

    def playerMovement(self, location, new_location):
        if new_location > 100 or new_location < 0:
            pass
        


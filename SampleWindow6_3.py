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

    CHAR_CENTER = tile_list[32].center
    
    TESTSPRITE = pygame.draw.circle(DISPLAYSURF, BLUE, CHAR_CENTER, int((TILESIZE/2)) , 0)
    test_char = GameCharacter('test character','test class', 0, 'test ability1', 'test ability2', 6, TESTSPRITE, (CHARX, CHARY), 0)
    
    while True:
        mouse_clicked = False

        DISPLAYSURF.fill(BGCOLOR)
        pygame.draw.rect(DISPLAYSURF, CRIMSON, menu)
        pygame.draw.rect(DISPLAYSURF, BOARDCOLOR, board)
        
        DISPLAYSURF.blit(menuTitleObj, textRectObj)
        
#        menu_title = screenWords('Menu')       

        tileDrawing(tile_list)
        TESTSPRITE = pygame.draw.circle(DISPLAYSURF, BLUE, ( tile_list[32].centerx, tile_list[32].centery), int((TILESIZE/2)) , 0)

        charMoving(tile_list[32], tile_list, test_char, 6)
        
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
        

  #      boxx, boxy = getBoxAtPixel(mousex, mousey)
   #     if boxx != None and boxy != None:
            # The mouse is currently over a box.
    #        drawHighlightBox(boxx, boxy)
            
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
def drawWords(text):
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    return_Text = BASICFONT.render(text, True, GREEN)
    return return_Text

def tileMapping(): # Draws the boxes for the characters
    next_box_left = TILEMARGINS
    next_box_top = TILEMARGINS
    tile_list = []
    for i in range(int(sqrt(MAXBOARDTILES))): # creates the first square in a row, then moves down a column space.
        tile = pygame.Rect((TILELEFT + next_box_left), (TILETOP + next_box_top), TILESIZE, TILESIZE )
        tile_list.append(tile)
        for j in range(int(sqrt(MAXBOARDTILES) - 1)): # creates the next 9 squares in a row.
            next_box_left += (TILESIZE + TILEMARGINS)
            tile= pygame.Rect((TILELEFT + next_box_left), (TILETOP + next_box_top), TILESIZE, TILESIZE )
            tile_list.append(tile)
        next_box_top += (TILESIZE + TILEMARGINS)
        next_box_left = TILEMARGINS
    return tile_list

def updateMenu(click_info, menu_list):
    #menu_dict = {'BASICATTACK', BASEDAMAGE ,'MENU1': ABILITY1, 'MENU2': ABILITY2, 'MENU3': ('Move', MOVESPEED, None)  'MENU4': ('Options', 'Quit', 'Cancel')}
     ### Should be only a few sets of menu configuration, like say four "screens"
    return False

def getMenuClick(mousex, mousey, menu_list):
    
    for i in len(range(menu_list)):
        pass ###
    return False

def tileDrawing(tile_list):
    for i in range(len(tile_list)):
        pygame.draw.rect(DISPLAYSURF, TILECOLOR,tile_list[i])

def drawHighlights(locations): # feed in rectangles to highlight, one or more
    another_Surface = DISPLAYSURF.convert_alpha()
    for i in len(locations): # draw a translucent box over them.
        pygame.rect.draw(another_Surface, HIGHLIGHTWHITE, (locations[i])) ### Current!!!### ### ###
    return another_surface

def tileClickGet(location, mousex, mousey, tile_list):
    mouse_clicked = False
    mouse_click = pygame.Rect( mousex ,mousey, 0, 0)
    if location == 'board':
        for i in range(len(tile_list)):
            tile_clicked = mouse_click.collidelist(tile_list)
            if tile_clicked > -1:
                print('Tile numeber:', tile_clicked)
                break
    elif location == 'menu':
        for i in range(len(tile_list)):
            tile_clicked = mouse_click.collidelist(title_list[i])
            if tile_clicked >-1:
                print('menu run something here')
                break
            
    return None

def movableTiles(current_tile, MOVESPEED): # Using floor divisions, determine the current row 
    MOVING = True                          # (drawn in ascending top left to bottom right), and repeat
    tiles_in_range_list = []               # with diminishing values outward for subsequent rows.
    horizontal_gate = (current_tile // 10) ####### TypeError: unsupported operand type(s) for //: 'pygame.Rect' and 'int' ###### figure out how to save the inex number
   # vertical_gate = (tile      ### Needs implementation to prevent vertical scren wrap or moving out of boundaries.
    for horizontal_tile in range(MOVESPEED):
        in_range_tile = tiles_list[(tile+1)]         # Tiles to the right:
        if (in_range_tile // 10) != horizontal_gate: # Prevents screen wrapping by gating
            pass                                     # out tiles in different rows.
        elif (in_range_tile // 10) == horizontal_gate:
            tiles_in_range_list.append(in_range_tile)
        
        in_range_tile = tile_list[(tile-1)] # Repeat for Tiles to the left
        if (in_range_tile // 10) != horizontal_gate:
            pass
        elif (in_range_tile // 10) == horizontal_gate:
            tiles_in_range_list.append(in_range_tile)
            
        for vertical_tile in range(MOVESPEED - horizontal_tile): # For above and below rows
            up_row_gate = (horizontal_gate + (10 * vertical_tile) + 10)
            down_row_gate = (horizontal_gate - (10 * vertical_tile) - 10)
            in_range_tile = tile_list[(tile+(10*vertical_tile)+horizontal_tile)]
            if (in_range_tile // 10) != up_row_gate:
                pass
            elif (in_range_tile // 10) == up_row_gate:
                tile_in_range_list.append(in_range_tile)
                
            in_range_tile = tile_list[(tile-(10*vertical_tile)-horizontal_tile)]
            if (in_range_tile // 10) != down_row_gate:
                pass
            elif (in_range_tile // 10) == up_row_gate:
                tile_in_range_list.append(down_range_tile)

    return tiles_in_range_list

def charMoving(current_tile, tile_list, current_char, MOVESPEED,):
    MOVING = True
    character_tile = current_char.location
    movable_tiles_list = movableTiles(current_tile, MOVESPEED)
    while MOVING == True:
     ###   draw_menu()
     ###   drawHighlights(tiles_in_range) # Draws highlights to denote movability
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
                    if board.collidepoint(mousex, mousey) == True:
                        player_action = tileClickGet('board', mousex, mousey, tile_list)
                        players_choice  = pygame.player_action(movable_tiles_list) 
                        if players_choice == True: # Is it in range? gate.
                            current_charater.location = players_action
                        mouse_clicked = False
                    else:
                        mouse_clicked = False
    
class GameCharacter:
    def __init__(self, NAME, CLASS, ATTACKDAMAGE, ABILITY1, ABILITY2, MOVESPEED, SPRITE, PLAYERSIDE, LOCATION=(None, None), EFFECTPOCKET=None):
        self.name = NAME
        self.charclass = CLASS
        self.attackdamage = ATTACKDAMAGE
        self.ability1 = ABILITY1
        self.ability2 = ABILITY2
        self.movespeed = MOVESPEED
        self.sprite = SPRITE
        self.playerside = PLAYERSIDE
        self.location = LOCATION
        self.effectpockets = EFFECTPOCKET


   # def attack(self, ATTACKDAMAGE):
    #    self

    def takeDamage():
        return False
   # def ABILITY1(self, ABLITY1):
        
def drawCharacters(character_list): ### Should work for blit images.
    return False
    ### for i in range(len(character_list): 
    ###   pygame.render.blit()

main()
print('uh oh')

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

# COLORS      R    G    B
WHITE      = (255, 255, 255)
BLACK      = (0  ,   0,   0)
BURLYWOOD  = (222, 184, 135)
GREY       = (128, 128, 128)
LIGHTGREY  = (190, 190, 190)
BLUE       = (  0,   0, 255)
GREEN      = (  0, 255,   0)
OLIVEGREEN = (100, 165, 100)
CRIMSON    = (165, 100, 100)

BGCOLOR = LIGHTGREY
HIGHLIGHTCOLOR = BLUE
BOARDCOLOR = OLIVEGREEN
TILECOLOR = BURLYWOOD

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
 
    while True:
        mouse_clicked = False

        DISPLAYSURF.fill(BGCOLOR)
        pygame.draw.rect(DISPLAYSURF, CRIMSON, menu)
        pygame.draw.rect(DISPLAYSURF, BOARDCOLOR, board)
        

        tile_list = tileMapping()
        
        DISPLAYSURF.blit(menuTitleObj, textRectObj) 
        

#        menu_title = screenWords('Menu')       

        tileDrawing(tile_list)
        
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
        tile = pygame.Rect((TILELEFT + next_box_left), (TILETOP + next_box_top), TILESIZE, TILESIZE, occupied = False, occupant = None)
        tile_list.append(tile)
        for j in range(int(sqrt(MAXBOARDTILES) - 1)): # creates the next 9 squares in a row.
            next_box_left += (TILESIZE + TILEMARGINS)
            tile= pygame.Rect((TILELEFT + next_box_left), (TILETOP + next_box_top), TILESIZE, TILESIZE, occupied = False, occupant = None )
            tile_list.append(tile)
        next_box_top += (TILESIZE + TILEMARGINS)
        next_box_left = TILEMARGINS
    return tile_list

def menuListings():
    return False

def tileDrawing(tile_list):
    for i in range(len(tile_list)):
        pygame.draw.rect(DISPLAYSURF, TILECOLOR,tile_list[i])

def tileClickGet(location, mousex, mousey, tile_list):
    mouse_clicked = False
    mouse_click = pygame.Rect( mousex ,mousey, 0, 0)
    if location == 'board':
        for i in range(len(tile_list)):
            tile_clicked = mouse_click.collidelist(tile_list)
            if tile_clicked > -1:
                print('run something here!!!', tile_clicked)
                break
    elif location == 'menu':
        for i in range(len(tile_list)):
            tile_clicked = mouse_click.collidelist(title_list[i])
            if tile_clicked >-1:
                print('menu run something here')
                break
            
    return None
    

main()
print('uh oh')

import pygame, sys
from pygame.locals import *
from math import sqrt

FPS = 30 # frames per second
WINWIDTH = 900
WINHEIGHT = 525
HALF_WINWIDTH = int(WINWIDTH/ 2)
HALF_WINHEIGHT = int(WINHEIGHT/ 2)

# The total width and hight for each tile in pixels
TILESIDE = 45 # height and width are the same
TILEFLOORHEIGHT = 45
MAXBOARDTILES = 100 # 14 x 14 tile board
BOARDLENGTH = sqrt(MAXBOARDTILES)
FIELDLEFT = 200
FIELDTOP = 10
FIELDHEIGHT = 505
FIELDWIDTH = 505
TILELEFT = 205
TILETOP = 15
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

def main():
    global FPSCLOCK, DISPLAYSURF, HALF_WINHEIGHT, HALF_WINWIDTH

    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode(( WINWIDTH, WINHEIGHT))

    mousex = 0
    mousey = 0

    mouseSelection = None

    pygame.display.set_caption('Window Practice')
    

    #IMAGESDICT = {'inside floor': pygame.image.load('Plain_Block.png')}

    menuTitleObj = drawWords('Menu')
    textRectObj = menuTitleObj.get_rect()
    textRectObj.center = (95 , 25)
 
    while True:
        mouse_clicked = False

        DISPLAYSURF.fill(BGCOLOR)
        pygame.draw.rect(DISPLAYSURF, CRIMSON,( 10, 10, MENUWIDTH, MENUHEIGHT))
        pygame.draw.rect(DISPLAYSURF, BURLYWOOD, ( FIELDLEFT, FIELDTOP, FIELDWIDTH, FIELDHEIGHT ))

        tileMapping()
        
        DISPLAYSURF.blit(menuTitleObj, textRectObj) 
        

       # menu_title = screenWords('Menu')       
        
        pygame.draw.line(DISPLAYSURF, BLACK, ((HALF_WINHEIGHT+1), (HALF_WINWIDTH+1)), (HALF_WINHEIGHT, HALF_WINWIDTH))
    
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

            
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        



def drawWords(text):
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    return_Text = BASICFONT.render(text, True, GREEN)
    return return_Text

def tileMapping(): # Draws the boxes for the characters
    next_box_left = 0
    next_box_top = 0
    for i in range(int(sqrt(MAXBOARDTILES))):
        pygame.draw.rect(DISPLAYSURF, OLIVEGREEN, ((TILELEFT), (TILETOP + next_box_top), TILESIDE, TILESIDE ))
        for i in range(int(sqrt(MAXBOARDTILES))):
            pygame.draw.rect(DISPLAYSURF, OLIVEGREEN, ((TILELEFT + next_box_left), (TILETOP + next_box_top), TILESIDE, TILESIDE ))
            next_box_left += (TILESIDE + TILEMARGINS)
        next_box_top += (TILESIDE + TILEMARGINS)
        next_box_left = 0
        


main()

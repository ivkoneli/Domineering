import pygame
import Domineering
import Tabla
import os
import sys
from Button import Button
from DropDown import DropDown
from pygame import mixer
pygame.init()


#defining variables  

# colors 
BG_COLOR = (229,229,229)
SQUARECOLOR = ()
DARK_SQUARE = Tabla.DARK_SQUARE
LIGHT_SQUARE = Tabla.LIGHT_SQUARE
ORANGE = (255,128,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 200, 0)

# field dimension 75x75
SQUARE_DIM = 75

# screen settings
WIDTH, HEIGHT = 900,800
FPS = 60

# starting Player (TRUE = X | FALSE = O)
PLAYER = True

# window canvas setting 

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Domineering")

# loading and transforming sprites 
CHESE_THEME = pygame.image.load("Sprites/ChessTheme.png")
CHESE_THEME_IMAGE = pygame.transform.scale(CHESE_THEME , (100,100))
CRIMSON_THEME = pygame.image.load("Sprites/CrimsonTheme.png")
CRIMSON_THEME_IMAGE = pygame.transform.scale(CRIMSON_THEME , (100,100))
CYBERPUNK_THEME = pygame.image.load("Sprites/CyberPunkTheme.png")
CYBERPUNK_THEME_IMAGE = pygame.transform.scale(CYBERPUNK_THEME , (100,100))
DEFAULT_THEME = pygame.image.load("Sprites/DefaultTheme.png")
DEFAULT_THEME_IMAGE = pygame.transform.scale(DEFAULT_THEME , (100,100))

playerXimg = pygame.image.load("Sprites/playerXsprite.png")
XIMAGE = pygame.transform.scale(playerXimg , (60 , 140)) 
playerOimg = pygame.image.load("Sprites/playerOsprite.png")
OIMAGE = pygame.transform.scale(playerOimg , (145 , 60))
VolumeONimg = pygame.image.load("Sprites/VolumeON.png")
VOLUME_ON = pygame.transform.scale(VolumeONimg , (60,60))
VolumeOFFimg = pygame.image.load("Sprites/VolumeOFF.png")
VOLUME_OFF = pygame.transform.scale(VolumeOFFimg , (60,60))

# Loading sounds 

mixer.music.load("Sounds/BackGroundMusic.mp3")
mixer.music.play(-1)


#Playabilty tests 

#tabla = Domineering.table
#tabla = Domineering.CreateTable(8,8)
#Domineering.PrintTable(tabla)
#Domineering.PlayMove("O",(3 ,"A"),tabla)
#Domineering.PlayMove("O",(5 ,"B"),tabla)
#Domineering.PlayMove("O",(7 ,"C"),tabla)
#Domineering.PlayMove("O",(8 ,"F"),tabla)
#Domineering.PlayMove("X",(2 ,"C"),tabla)
#Domineering.PlayMove("X",(5 ,"D"),tabla)
#Domineering.PlayMove("X",(3 ,"G"),tabla)

# input field for MOVES 



#FONT INIT
MOVE_FONT = pygame.font.Font('freesansbold.ttf', 18)
GAMEOVER_FONT = pygame.font.Font('freesansbold.ttf',50)
TITLE_FONT = pygame.font.Font('freesansbold.ttf',75)
THEME_TEXT_FONT = pygame.font.Font('freesansbold.ttf',25)

Tabla.TABLA = Domineering.CreateTable("Medium")


def drawLargeBoard(Tamni, Svetli):

        for x in range(len(Tabla.TABLA)):
            c = 65 # A
            n = 56 # 8


            WIN.blit(MOVE_FONT.render(chr(c+x), True,BLACK, BG_COLOR),pygame.Rect(175+(x*SQUARE_DIM), 75, SQUARE_DIM,SQUARE_DIM))   #drawing CHAR  border
            WIN.blit(MOVE_FONT.render(chr(c+x), True,BLACK, BG_COLOR),pygame.Rect(175+(x*SQUARE_DIM),725, SQUARE_DIM,SQUARE_DIM))
            WIN.blit(MOVE_FONT.render(chr(n-x) , True,BLACK, BG_COLOR),pygame.Rect(125, 125+(x*SQUARE_DIM), SQUARE_DIM,SQUARE_DIM)) #drawing INT border
            WIN.blit(MOVE_FONT.render(chr(n-x) , True,BLACK, BG_COLOR),pygame.Rect(775, 125+(x*SQUARE_DIM), SQUARE_DIM,SQUARE_DIM))       


            for y in range(len(Tabla.TABLA)):

                SQUARECOLOR = (0,0,0)

                fullRect =  pygame.draw.rect(WIN ,SQUARECOLOR ,
                pygame.Rect(150+(y*SQUARE_DIM),100+(x*SQUARE_DIM) , SQUARE_DIM,SQUARE_DIM), 2)

                midfill =  pygame.draw.rect(WIN ,SQUARECOLOR ,
                pygame.Rect(150+(y*SQUARE_DIM)+2.5,100+(x*SQUARE_DIM)+2.5 , SQUARE_DIM-2.5,SQUARE_DIM-2.5), 5)

                if ( (x + y) % 2 == 0) :
                    WIN.fill(Tamni, midfill)
            
                else :
                    WIN.fill(Svetli, midfill)

def drawMediumBoard(Tamni , Svetli): 

        for x in range(len(Tabla.TABLA)):
            c = 65 # A
            n = 54 # 6


            WIN.blit(MOVE_FONT.render(chr(c+x), True,BLACK, BG_COLOR),pygame.Rect(250+(x*SQUARE_DIM), 125, SQUARE_DIM,SQUARE_DIM))   #drawing CHAR  border
            WIN.blit(MOVE_FONT.render(chr(c+x), True,BLACK, BG_COLOR),pygame.Rect(250+(x*SQUARE_DIM),625, SQUARE_DIM,SQUARE_DIM))
            WIN.blit(MOVE_FONT.render(chr(n-x) , True,BLACK, BG_COLOR),pygame.Rect(175, 175+(x*SQUARE_DIM), SQUARE_DIM,SQUARE_DIM)) #drawing INT border
            WIN.blit(MOVE_FONT.render(chr(n-x) , True,BLACK, BG_COLOR),pygame.Rect(700, 175+(x*SQUARE_DIM), SQUARE_DIM,SQUARE_DIM))       

            for y in range(len(Tabla.TABLA)):

                SQUARECOLOR = (0,0,0)

                fullRect =  pygame.draw.rect(WIN ,SQUARECOLOR ,
                pygame.Rect(225+(y*SQUARE_DIM),150+(x*SQUARE_DIM) , SQUARE_DIM,SQUARE_DIM), 2)

                midfill =  pygame.draw.rect(WIN ,SQUARECOLOR ,
                pygame.Rect(225+(y*SQUARE_DIM)+2.5,150+(x*SQUARE_DIM)+2.5 , SQUARE_DIM-2.5,SQUARE_DIM-2.5), 5)

                if ( (x + y) % 2 == 0) :
                    WIN.fill(Tamni, midfill)
            
                else :
                    WIN.fill(Svetli, midfill)

def drawSmallBoard(Tamni , Svetli):


        for x in range(len(Tabla.TABLA)):
            c = 65 # A
            n = 52 # 4


            WIN.blit(MOVE_FONT.render(chr(c+x), True,BLACK, BG_COLOR),pygame.Rect(310+(x*SQUARE_DIM), 175, SQUARE_DIM,SQUARE_DIM))   #drawing CHAR  border
            WIN.blit(MOVE_FONT.render(chr(c+x), True,BLACK, BG_COLOR),pygame.Rect(310+(x*SQUARE_DIM),540, SQUARE_DIM,SQUARE_DIM))
            WIN.blit(MOVE_FONT.render(chr(n-x) , True,BLACK, BG_COLOR),pygame.Rect(240, 235+(x*SQUARE_DIM), SQUARE_DIM,SQUARE_DIM)) #drawing INT border
            WIN.blit(MOVE_FONT.render(chr(n-x) , True,BLACK, BG_COLOR),pygame.Rect(625, 235+(x*SQUARE_DIM), SQUARE_DIM,SQUARE_DIM))       

            for y in range(len(Tabla.TABLA)):

                SQUARECOLOR = (0,0,0)

                fullRect =  pygame.draw.rect(WIN ,SQUARECOLOR ,
                pygame.Rect(285+(y*SQUARE_DIM),210+(x*SQUARE_DIM) , SQUARE_DIM,SQUARE_DIM), 2)

                midfill =  pygame.draw.rect(WIN ,SQUARECOLOR ,
                pygame.Rect(285+(y*SQUARE_DIM)+2.5,210+(x*SQUARE_DIM)+2.5 , SQUARE_DIM-2.5,SQUARE_DIM-2.5), 5)

                if ( (x + y) % 2 == 0) :
                    WIN.fill(Tamni, midfill)
            
                else :
                    WIN.fill(Svetli, midfill)



# main drawing func 

def draw_window(text , rect):

    #print("Field je" , field)

    WIN.fill(BG_COLOR)
    # drawing of the n*n board + TEXT & CHAR borders        exmple => (8->1 ) (A -> H)


    WIN.blit(text, rect)



    if   len(Tabla.TABLA) == 8 :   # large board
        drawLargeBoard(Tabla.DARK_SQUARE , Tabla.LIGHT_SQUARE)
        xDIM = 105
        yDIM = 157.5
    elif len(Tabla.TABLA) == 6 :   # medium board
        drawMediumBoard(Tabla.DARK_SQUARE , Tabla.LIGHT_SQUARE)
        xDIM = 157.5
        yDIM = 232.5
    elif len(Tabla.TABLA) == 4 :   # small board
        drawSmallBoard(Tabla.DARK_SQUARE , Tabla.LIGHT_SQUARE)
        xDIM = 217.5
        yDIM = 292.5

    # drawing player O moves 

    for x in range(len(Tabla.TABLA)):
        for y in range(len(Tabla.TABLA)-1):
            if y == 1 :
                if Tabla.TABLA[x][y] == "O" and Tabla.TABLA[x][y+1] == "O" and Tabla.TABLA[x][y-1] != "O":
                    WIN.blit(OIMAGE, (yDIM-5 +(y*SQUARE_DIM),xDIM+(x*SQUARE_DIM)))
            else :
                if Tabla.TABLA[x][y] == "O" and Tabla.TABLA[x][y+1] == "O" :
                    WIN.blit(OIMAGE, (yDIM+(y*SQUARE_DIM),xDIM+(x*SQUARE_DIM)))

    # drawing player X moves 

    for x in range((len(Tabla.TABLA)-1)):
        for y in range(len(Tabla.TABLA)):
            if x == 1 :
                if Tabla.TABLA[x][y] == "X" and Tabla.TABLA[x+1][y] == "X" and Tabla.TABLA[x-1][y] != "X":
                    WIN.blit(XIMAGE, (yDIM+(y*SQUARE_DIM),xDIM+(x*SQUARE_DIM)))
            else :
                if Tabla.TABLA[x][y] == "X" and Tabla.TABLA[x+1][y] == "X" :
                    WIN.blit(XIMAGE, (yDIM+(y*SQUARE_DIM),xDIM+(x*SQUARE_DIM)))

    pygame.display.flip()




# playMove 


def igrajPotez(moveText,player):
  
    validanPotez =  Domineering.PlayMove(playerValue(player),(int(moveText[0]),moveText[1]),Tabla.TABLA) # true/false , novuTablu
    Tabla.TABLA = validanPotez[1] 

    if not validanPotez[0]:
        return False
    else :    
        print(moveText[0],moveText[1])
        return True


#helper translate (TRUE,FALSE) => ("X","O")

def playerValue(player):

    if player :
        return 'X'
    return 'O'    


#drwaing END GAME text and RESET after delay

def drawEnd(player):
    pygame.time.delay(500)
    if player == "X":
        text_surface = GAMEOVER_FONT.render("BLACK WINS!",True, GREEN)
        WIN.blit(text_surface,(320 , 350))
    else:
        text_surface = GAMEOVER_FONT.render("ORANGE WINS!",True, GREEN)
        WIN.blit(text_surface,(320 , 350))
    pygame.display.flip()
    pygame.time.delay(4000)
    Reset()

#set table values to their default ("-")

def Reset():
    for i in range(len(Tabla.TABLA)):
        for j in range(len(Tabla.TABLA)):
            Tabla.TABLA[i][j] = "-"

#Translate cursor position into a table field 

def calculateField(position):

    if len(Tabla.TABLA) == 8 :
        j = int((position[0]-150) / 75 )  
        i = int((position[1]-100) / 75 )
    elif len(Tabla.TABLA) == 6 :
        j = int((position[0]-225) / 75 )  
        i = int((position[1]-150) / 75 )
    elif len(Tabla.TABLA) == 4 :
        j = int((position[0]-285) / 75 )  
        i = int((position[1]-210) / 75 )
    print(i ,j)
    return(i , j)


def calculateMove(field):
    moveY = abs(field[0]-len(Tabla.TABLA))
    moveX = chr(65 + field[1])
    print(moveY , moveX)
    return (moveY , moveX)


#Event handling and calling other funcs

def play():
   

    clock = pygame.time.Clock()
    Valid_Sound = mixer.Sound('Sounds/ValidSound.mp3')
    Invalid_Sound = mixer.Sound('Sounds/InvalidSound.mp3')
    Victory_Sound = mixer.Sound('Sounds/VictorySound.mp3')
    run = True 
    active = False
    player = True
    pc = False

    NEXT_MOVE_TEXT = GAMEOVER_FONT.render("CURENTLY PLAYING : X",True, "#FF8C00")
    NEXT_MOVE_RECT = NEXT_MOVE_TEXT.get_rect(center=(450,50))

    

    while(run):



        clock.tick(FPS) 
        for event in pygame.event.get():  
            if player :
                NEXT_MOVE_TEXT = GAMEOVER_FONT.render("CURENTLY PLAYING : X",True, "#FF8C00")
            else :
                NEXT_MOVE_TEXT = GAMEOVER_FONT.render("CURENTLY PLAYING : O",True, "#FF8C00")

            draw_window(NEXT_MOVE_TEXT,NEXT_MOVE_RECT)
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit
                exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:                   
                    run = False
                    mainScreen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 150 and pos[0] <= 750 and pos[1] >=100 and pos[1] <=700 :
                    print(pos)
                    field = calculateField(pos)
                    move  = calculateMove(field)
                    valid = igrajPotez(move,player)
                    nizPoteza = Domineering.possibleMoves(Tabla.TABLA,playerValue(not player))
                    print(nizPoteza)
                    if pc :
                        igrajPotez(nizPoteza[0],False)
                    else:
                        draw_window(NEXT_MOVE_TEXT,NEXT_MOVE_RECT)
                        if valid :
                            Valid_Sound.play()
                            kraj = Domineering.GameOver(playerValue(player), Tabla.TABLA)
                            player =  not player
                            moveText = ""
                            print("Da li je kraj",kraj[0])
                            if kraj[0] :
                                Victory_Sound.play()
                                if not player : 
                                    drawEnd(playerValue(player))
                                    player = True
                                else :  
                                    drawEnd(playerValue(player))
                                    
                            draw_window(NEXT_MOVE_TEXT,NEXT_MOVE_RECT)
                        else :
                            Invalid_Sound.play()
                            print("Nije validan LICHE")
                            player = player                         
        
    # pygame.quit()            
def optionsScreen():

    clock = pygame.time.Clock()
    run = True 

    while(run):
        clock.tick(FPS)

        WIN.fill(BG_COLOR)

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        #TITLE TEXT
        MENU_TEXT = TITLE_FONT.render("Theme Selection",True, "#FF8C00")
        MENU_RECT = MENU_TEXT.get_rect(center=(450,160))

        #CHESS THEME
        CHESS_TEXT = THEME_TEXT_FONT.render("CHESS",True, "DarkGreen")
        CHESS_RECT = CHESS_TEXT.get_rect(center=(WIDTH/2-200,HEIGHT/2-65))
        CHESS_THEME = Button(image = CHESE_THEME_IMAGE , pos=(WIDTH/2-200,HEIGHT/2),
                            text_input = "" , font = GAMEOVER_FONT, base_color ="DarkGreen", hovering_color ="White")
        #CYBERPUNK THEME
        CYBERPUNK_TEXT = THEME_TEXT_FONT.render("CYBERPUNK",True, "#FF33FF")
        CYBERPUNK_RECT = CYBERPUNK_TEXT.get_rect(center=(WIDTH/2+200,HEIGHT/2-65))
        CYBERPUNK_THEME = Button(image = CYBERPUNK_THEME_IMAGE , pos=(WIDTH/2+200,HEIGHT/2),      
                            text_input = "" , font = GAMEOVER_FONT, base_color ="#FF33FF", hovering_color ="White")
        #CRIMSON THEME
        CRIMSON_TEXT = THEME_TEXT_FONT.render("CRIMSON",True, "Crimson")
        CRIMSON_RECT = CRIMSON_TEXT.get_rect(center=(WIDTH/2+200,HEIGHT/2+150-65))                            
        CRIMSON_THEME = Button(image = CRIMSON_THEME_IMAGE , pos=(WIDTH/2+200,HEIGHT/2+150),
                            text_input = "" , font = GAMEOVER_FONT, base_color ="Crimson", hovering_color ="White")
        #DEFAULT THEME
        DEFAULT_TEXT = THEME_TEXT_FONT.render("DEFAULT",True, "Black")
        DEFAULT_RECT = DEFAULT_TEXT.get_rect(center=(WIDTH/2-200,HEIGHT/2+150-65))                           
        DEFAULT_THEME = Button(image = DEFAULT_THEME_IMAGE , pos=(WIDTH/2-200,HEIGHT/2+150),
                            text_input = "" , font = GAMEOVER_FONT, base_color ="Black", hovering_color ="White")


        # DRAW ON SCREEN
        WIN.blit(CHESS_TEXT,CHESS_RECT)
        WIN.blit(CYBERPUNK_TEXT,CYBERPUNK_RECT)
        WIN.blit(CRIMSON_TEXT,CRIMSON_RECT)
        WIN.blit(DEFAULT_TEXT,DEFAULT_RECT)
        WIN.blit(MENU_TEXT,MENU_RECT)

        # UPDATE COLOR ON HOVER
        for button in [CHESS_THEME,CYBERPUNK_THEME,CRIMSON_THEME,DEFAULT_THEME] :
            button.changeColor(MENU_MOUSE_POS)  
            button.update(WIN)

        # MAIN LOOP
        pygame.display.flip()         
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:                   
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHESS_THEME.checkForInput(MENU_MOUSE_POS):
                    Tabla.DARK_SQUARE = (51,102,0)
                    Tabla.LIGHT_SQUARE = (255,255,204)
                if CYBERPUNK_THEME.checkForInput(MENU_MOUSE_POS):
                    Tabla.DARK_SQUARE = (51,255,255)
                    Tabla.LIGHT_SQUARE = (255,51,255)
                if CRIMSON_THEME.checkForInput(MENU_MOUSE_POS):
                    Tabla.DARK_SQUARE = (0,0,0)
                    Tabla.LIGHT_SQUARE = (153,0,0)
                if DEFAULT_THEME.checkForInput(MENU_MOUSE_POS):
                    Tabla.DARK_SQUARE = (0,0,0)
                    Tabla.LIGHT_SQUARE = (179,172,172)
    pygame.display.flip()
                      
def setup():

    
    clock = pygame.time.Clock()
    run = True 

    COLOR_INACTIVE = (179, 172, 172)
    COLOR_ACTIVE = (255, 255, 255)
    COLOR_LIST_INACTIVE = (224, 224, 224)
    COLOR_LIST_ACTIVE = (255, 128, 0)
    
    sizeSelect = DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    350, 150, 200, 50, 
    THEME_TEXT_FONT, 
    "Large", ["Small", "Medium","Large"])

    SIZE_TEXT = THEME_TEXT_FONT.render("Select size",True, "#FF8C00")
    SIZE_RECT = SIZE_TEXT.get_rect(center=(450,130))
    WIN.blit(SIZE_TEXT,SIZE_RECT)

    while(run):

        WIN.fill(BG_COLOR)
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        clock.tick(FPS)


        SUBMIT_BUTTON = Button(image = None , pos=(WIDTH/2,HEIGHT/2+200),
                text_input = "SUBMIT" , font = GAMEOVER_FONT, base_color ="Black", hovering_color ="Orange")
        WIN.blit(SIZE_TEXT,SIZE_RECT)

        for button in [SUBMIT_BUTTON] :
            button.changeColor(MENU_MOUSE_POS)  
            button.update(WIN)


        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
                quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:                   
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SUBMIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Tabla.TABLA = Domineering.CreateTable(sizeSelect.main)
                    print(sizeSelect.main)
                    play()                    
        selected_option = sizeSelect.update(event_list)
        if selected_option >= 0:
            sizeSelect.main = sizeSelect.options[selected_option]
            #print(sizeSelect.main)


        sizeSelect.draw(WIN)
        pygame.display.flip()


def mainScreen():


    WIDTH , HEIGHT = pygame.display.get_window_size()
    clock = pygame.time.Clock()
    runConst = True
    sound = True 




    while runConst :

        WIN.fill(BG_COLOR)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = TITLE_FONT.render("DOMINEERING",True, "#FF8C00")
        MENU_RECT = MENU_TEXT.get_rect(center=(450,160))

        PLAY_BUTTON = Button(image = None , pos=(WIDTH/2,HEIGHT/2),
                            text_input = "PLAY" , font = GAMEOVER_FONT, base_color ="Black", hovering_color ="White")
        OPTIONS_BUTTON = Button(image = None , pos=(WIDTH/2,HEIGHT/2+70),
                            text_input = "OPTIONS" , font = GAMEOVER_FONT, base_color ="Black", hovering_color ="White")
        QUIT_BUTTON = Button(image = None , pos=(WIDTH/2,HEIGHT/2+140),
                            text_input = "QUIT" , font = GAMEOVER_FONT, base_color ="Black", hovering_color ="White")
        MUTE_BUTTON = Button(image = VOLUME_ON , pos=(770,50) ,
                            text_input = "" , font = GAMEOVER_FONT, base_color ="Black", hovering_color ="White")
        WIN.blit(MENU_TEXT,MENU_RECT)


        for button in [PLAY_BUTTON ,OPTIONS_BUTTON,QUIT_BUTTON, MUTE_BUTTON] :
            button.changeColor(MENU_MOUSE_POS)  
            button.update(WIN)
            if mixer.music.get_volume() == 0 :
                MUTE_BUTTON.image = VOLUME_OFF
            else :
                MUTE_BUTTON.image = VOLUME_ON


        for event in pygame.event.get():         
            if event.type == pygame.QUIT:
                runConst = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    runConst = False
                    quit()
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    setup()
                if MUTE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if sound == True :
                        mixer.music.set_volume(0)
                        sound = not sound
                    else :
                        mixer.music.set_volume(1)
                        sound = not sound
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    optionsScreen()
        pygame.display.flip()

  
    # pygame.quit() 



if __name__ == "__main__":
    mainScreen()

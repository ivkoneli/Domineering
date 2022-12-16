import pygame
import Domineering
import Tabla
pygame.init()


#defining variables  

BG_COLOR = (229,229,229)
SQUARECOLOR = ()
ORANGE = (255,128,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 200, 0)
SQUARE_DIM = 75
WIDTH, HEIGHT = 900,800
FPS = 60
PLAYER = True

# window canvas setting 

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Domineering")

# loading and transforming sprites 

playerXimg = pygame.image.load("Sprites/playerXsprite.png")
XIMAGE = pygame.transform.scale(playerXimg , (60 , 140)) 
playerOimg = pygame.image.load("Sprites/playerOsprite.png")
OIMAGE = pygame.transform.scale(playerOimg , (145 , 60))



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

active = False
column_input_rect = pygame.Rect(460,25,50,35)
column_moveText =""
MOVE_FONT = pygame.font.Font('freesansbold.ttf', 18)
GAMEOVER_FONT = pygame.font.Font('freesansbold.ttf',50)
MOVE_TEXT = MOVE_FONT.render(column_moveText, True,BLACK, BG_COLOR)




# main drawing func 

def draw_window(field):

    #print("Field je" , field)

    WIN.fill(BG_COLOR)
    
    # drawing of the n*n board + TEXT & CHAR borders        exmple => (8->1 ) (A -> H)

    for x in range(len(Tabla.TABLA)):
        c = 65 # A
        n = 56 # 8


        WIN.blit(MOVE_FONT.render(chr(c+x), True,BLACK, BG_COLOR),pygame.Rect(175+(x*SQUARE_DIM), 75, SQUARE_DIM,SQUARE_DIM))   #drawing CHAR  border
        WIN.blit(MOVE_FONT.render(chr(c+x), True,BLACK, BG_COLOR),pygame.Rect(175+(x*SQUARE_DIM),725, SQUARE_DIM,SQUARE_DIM))
        WIN.blit(MOVE_FONT.render(chr(n-x) , True,BLACK, BG_COLOR),pygame.Rect(125, 125+(x*SQUARE_DIM), SQUARE_DIM,SQUARE_DIM)) #drawing INT border
        WIN.blit(MOVE_FONT.render(chr(n-x) , True,BLACK, BG_COLOR),pygame.Rect(775, 125+(x*SQUARE_DIM), SQUARE_DIM,SQUARE_DIM))       

        #input field  drawing 
        #pygame.draw.rect(WIN,WHITE,column_input_rect,2)
        #text_surface = MOVE_FONT.render(moveText,True,(0,0,0))
        #WIN.blit(text_surface,(column_input_rect.x + 20 , column_input_rect.y + 10))

        #column_input_rect.w = max(50,text_surface.get_width() + 5)    # dynamic field scaling 
        for y in range(len(Tabla.TABLA)):

            SQUARECOLOR = (0,0,0)

            fullRect =  pygame.draw.rect(WIN ,SQUARECOLOR ,
            pygame.Rect(150+(y*SQUARE_DIM),100+(x*SQUARE_DIM) , SQUARE_DIM,SQUARE_DIM), 2)

            midfill =  pygame.draw.rect(WIN ,SQUARECOLOR ,
            pygame.Rect(150+(y*SQUARE_DIM)+2.5,100+(x*SQUARE_DIM)+2.5 , SQUARE_DIM-2.5,SQUARE_DIM-2.5), 5)

            if ( (x + y) % 2 == 0) :
                WIN.fill((0,0,0), midfill)
            
            else :
                WIN.fill((179,172,172), midfill)
            


    # drawing player O moves 

    for x in range(len(Tabla.TABLA)):
        for y in range(len(Tabla.TABLA)-1):
            if y == 1 :
                if Tabla.TABLA[x][y] == "O" and Tabla.TABLA[x][y+1] == "O" and Tabla.TABLA[x][y-1] != "O":
                    WIN.blit(OIMAGE, (152.5+(y*SQUARE_DIM),105+(x*SQUARE_DIM)))
            else :
                if Tabla.TABLA[x][y] == "O" and Tabla.TABLA[x][y+1] == "O" :
                    WIN.blit(OIMAGE, (157.5+(y*SQUARE_DIM),105+(x*SQUARE_DIM)))

    # drawing player X moves 

    for x in range((len(Tabla.TABLA)-1)):
        for y in range(len(Tabla.TABLA)):
            if x == 1 :
                if Tabla.TABLA[x][y] == "X" and Tabla.TABLA[x+1][y] == "X" and Tabla.TABLA[x-1][y] != "X":
                    WIN.blit(XIMAGE, (157.5+(y*SQUARE_DIM),105+(x*SQUARE_DIM)))
            else :
                if Tabla.TABLA[x][y] == "X" and Tabla.TABLA[x+1][y] == "X" :
                    WIN.blit(XIMAGE, (157.5+(y*SQUARE_DIM),105+(x*SQUARE_DIM)))

    pygame.display.update()




# playMove 

Tabla.TABLA = Domineering.CreateTable(8,8)

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
        text_surface = GAMEOVER_FONT.render("ORANGE WINS!",True, GREEN)
        WIN.blit(text_surface,(350 , 350))
    else:
        text_surface = GAMEOVER_FONT.render("BLACK WINS!",True, GREEN)
        WIN.blit(text_surface,(350 , 350))
    pygame.display.update()
    pygame.time.delay(4000)
    Reset()

#set table values to their default ("-")

def Reset():
    for i in range(len(Tabla.TABLA)):
        for j in range(len(Tabla.TABLA)):
            Tabla.TABLA[i][j] = "-"

#Translate cursor position into a table field 

def calculateField(position):

    j = int((position[0]-150) / 75 )  
    i = int((position[1]-100) / 75 )
    print(i ,j)
    return(i , j)


def calculateMove(field):
    moveY = abs(field[0]-len(Tabla.TABLA))
    moveX = chr(65 + field[1])
    print(moveY , moveX)
    return (moveY , moveX)


#Event handling and calling other funcs

def main():
    clock = pygame.time.Clock()
    run = True 
    active = False
    player = True

    while(run):
        for event in pygame.event.get():
            draw_window((0,0))
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 150 and pos[0] <= 750 and pos[1] >=100 and pos[1] <=700 :
                    print(pos)
                    field = calculateField(pos)
                    move  = calculateMove(field)
                    valid = igrajPotez(move,player)
                    draw_window(field)
                    if valid :
                        kraj = Domineering.GameOver(playerValue(player), Tabla.TABLA)
                        player =  not player
                        moveText = ""
                        print("Da li je kraj",kraj[0])
                        if kraj[0] :
                            if not player : 
                                drawEnd(player)
                            else :  
                                drawEnd(player)
                                draw_window((0,0))
                    else :
                            player = player
                          
                if column_input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

    clock.tick(FPS) 
    pygame.quit()            


if __name__ == "__main__":
    main()

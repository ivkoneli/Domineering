import pygame
import Domineering
pygame.init()

BG_COLOR = (229,229,229)
SQUARECOLOR = ()
ORANGE = (255,128,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 200, 0)
SQUARE_DIM = 75

WIDTH, HEIGHT = 900,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Domineering")

FPS = 60
PLAYER = True

tabla = Domineering.table
tabla= Domineering.CreateTable(8,8)
Domineering.PrintTable(tabla)

column_input_rect = pygame.Rect(460,25,50,35)
MOVE_FONT = pygame.font.Font('freesansbold.ttf', 18)
GAMEOVER_FONT = pygame.font.Font('freesansbold.ttf',50)
column_moveText =""
MOVE_TEXT = MOVE_FONT.render(column_moveText, True,BLACK, BG_COLOR)
active = False

def draw_window(moveText):
    WIN.fill(BG_COLOR)
    for x in range(len(tabla)):
        c = 65
        n = 56
        WIN.blit(MOVE_FONT.render(chr(c+x), True,BLACK, BG_COLOR),pygame.Rect(175+(x*SQUARE_DIM), 75, SQUARE_DIM,SQUARE_DIM))
        WIN.blit(MOVE_FONT.render(chr(c+x), True,BLACK, BG_COLOR),pygame.Rect(175+(x*SQUARE_DIM),725, SQUARE_DIM,SQUARE_DIM))
        WIN.blit(MOVE_FONT.render(chr(n-x) , True,BLACK, BG_COLOR),pygame.Rect(125, 125+(x*SQUARE_DIM), SQUARE_DIM,SQUARE_DIM))
        WIN.blit(MOVE_FONT.render(chr(n-x) , True,BLACK, BG_COLOR),pygame.Rect(775, 125+(x*SQUARE_DIM), SQUARE_DIM,SQUARE_DIM))

        pygame.draw.rect(WIN,WHITE,column_input_rect,2)
        text_surface = MOVE_FONT.render(moveText,True,(0,0,0))
        WIN.blit(text_surface,(column_input_rect.x + 20 , column_input_rect.y + 10))

        column_input_rect.w = max(50,text_surface.get_width() + 5)
        for y in range(len(tabla)):
            SQUARECOLOR = (255,255,255)
            pygame.draw.rect(WIN ,SQUARECOLOR ,
            pygame.Rect(150+(y*SQUARE_DIM),100+(x*SQUARE_DIM) , SQUARE_DIM,SQUARE_DIM), 2)

    for x in range(len(tabla)):
        for y in range(len(tabla)-1):
            if tabla[x][y] == "O" and tabla[x][y+1] == "O":
                    SQUARECOLOR = BLACK
                    pygame.draw.rect(WIN ,SQUARECOLOR ,
                    pygame.Rect(150+(y*SQUARE_DIM)+12.5,100+(x*SQUARE_DIM)+7.5 , 2*SQUARE_DIM-25,SQUARE_DIM-15))

    for x in range(len(tabla)-1):
        for y in range(len(tabla)):
            if tabla[x][y] == "X" and tabla[x+1][y] == "X":
                    SQUARECOLOR = ORANGE
                    pygame.draw.rect(WIN ,SQUARECOLOR ,
                    pygame.Rect(150+(y*SQUARE_DIM)+7.5,100+(x*SQUARE_DIM)+12.5 , SQUARE_DIM-15 ,2*SQUARE_DIM-25))
    pygame.display.update()

def igrajPotez(moveText,player):

    validanPotez =  Domineering.PlayMove(playerValue(player),(int(moveText[0]),moveText[1]),tabla)
    if not validanPotez:
        return False
    else :    
        print(moveText[0],moveText[1])
        return True


def playerValue(player):

    if player :
        return 'X'
    return 'O'    


def drawEnd(player):
    pygame.time.delay(500)
    if player == "X":
        text_surface = GAMEOVER_FONT.render("X WINS!",True, GREEN)
        WIN.blit(text_surface,(370 , 350))
    else:
        text_surface = GAMEOVER_FONT.render("O WINS!",True, GREEN)
        WIN.blit(text_surface,(370 , 350))
    pygame.display.update()
    pygame.time.delay(4000)
    Reset()


def Reset():
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            tabla[i][j] = "-"


def main():
    clock = pygame.time.Clock()
    run = True 
    moveText =""
    active = False
    player = True

    while(run):
        for event in pygame.event.get():
            #draw_window(moveText)
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if column_input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        moveText = moveText[:-1]
                    elif event.key == pygame.K_RETURN:
                        valid = igrajPotez(moveText,player)
                        draw_window(moveText)
                        if valid :
                            kraj = Domineering.GameOver(playerValue(player), tabla)
                            player =  not player
                            moveText = ""
                            print("Da li je kraj",kraj[0])
                            if kraj[0] :
                                if not player : 
                                    drawEnd(player)
                                else :
                                    drawEnd(player)
                                draw_window(moveText)
                        else :
                            player = player

                    else:
                        moveText+=event.unicode
     
            draw_window(moveText)

    clock.tick(FPS) 
    pygame.quit()            


if __name__ == "__main__":
    main()

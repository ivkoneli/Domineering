import pygame
import Domineering

backgroundColor = (229,229,229)
squareColor = ()
ORANGE = (255,128,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
squareDim = 75
tabla = Domineering.table
FPS = 60
WIDTH, HEIGHT = 900,800

PLAYER = True

pygame.init()

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Domineering")
tabla= Domineering.CreateTable(8,8)
#Domineering.PrintTable(tabla)
Domineering.PlayMove("X",(2, "A"),tabla)
#Domineering.PlayMove("X",(3, "G"),tabla)
#Domineering.PlayMove("X",(5, "G"),tabla)
#Domineering.PlayMove("X",(7, "G"),tabla)
#Domineering.PlayMove("X",(1, "H"),tabla)
#Domineering.PlayMove("X",(3, "H"),tabla)
#Domineering.PlayMove("X",(5, "H"),tabla)
#Domineering.PlayMove("X",(7, "H"),tabla)
#Domineering.PlayMove("X",(1, "F"),tabla)
#Domineering.PlayMove("X",(3, "F"),tabla)
#Domineering.PlayMove("X",(5, "F"),tabla)
#Domineering.PlayMove("X",(7, "F"),tabla)
#Domineering.PlayMove("X",(6, "G"),tabla)
#Domineering.PlayMove("X",(7, "G"),tabla)
#Domineering.PlayMove("X",(8, "G"),tabla)
Domineering.PlayMove("O",(4, "B"),tabla)
#Domineering.PlayMove("O",(5, "B"),tabla)
#Domineering.PlayMove("O",(6, "B"),tabla)
#Domineering.PlayMove("O",(7, "B"),tabla)
#Domineering.PlayMove("O",(8, "B"),tabla)
#Domineering.PlayMove("O",(1, "B"),tabla)
#Domineering.PlayMove("O",(2, "B"),tabla)
#Domineering.PlayMove("O",(3, "B"),tabla)
#Domineering.PlayMove("O",(4, "D"),tabla)
#Domineering.PlayMove("O",(5, "D"),tabla)
#Domineering.PlayMove("O",(6, "D"),tabla)
#Domineering.PlayMove("O",(7, "D"),tabla)
#Domineering.PlayMove("O",(8, "D"),tabla)
#Domineering.PlayMove("O",(1, "D"),tabla)
#Domineering.PlayMove("O",(2, "D"),tabla)
#Domineering.PlayMove("O",(3, "D"),tabla)

column_input_rect = pygame.Rect(460,25,50,35)
row_input_rect = pygame.Rect(385,25,50,35)
font = pygame.font.Font('freesansbold.ttf', 18)
GAMEOVER_FONT = pygame.font.Font('freesansbold.ttf',20)
column_moveText =""
text = font.render(column_moveText, True,BLACK, backgroundColor)
textRect = text.get_rect()
moveTextColor = WHITE
row_moveText = " "
active = False





def draw_window(moveText):
    WIN.fill(backgroundColor)
    for x in range(len(tabla)):
        c = 65
        n = 56
        WIN.blit(font.render(chr(c+x), True,BLACK, backgroundColor),pygame.Rect(175+(x*squareDim), 75, squareDim,squareDim))
        WIN.blit(font.render(chr(c+x), True,BLACK, backgroundColor),pygame.Rect(175+(x*squareDim),725, squareDim,squareDim))
        WIN.blit(font.render(chr(n-x) , True,BLACK, backgroundColor),pygame.Rect(125, 125+(x*squareDim), squareDim,squareDim))
        WIN.blit(font.render(chr(n-x) , True,BLACK, backgroundColor),pygame.Rect(775, 125+(x*squareDim), squareDim,squareDim))

        #pygame.draw.rect(WIN,WHITE,row_input_rect,2)
        #text_surface = font.render(moveText,True,(0,0,0))
        #WIN.blit(text_surface,(row_input_rect.x + 20 , row_input_rect.y + 10))

        pygame.draw.rect(WIN,WHITE,column_input_rect,2)
        text_surface = font.render(moveText,True,(0,0,0))
        WIN.blit(text_surface,(column_input_rect.x + 20 , column_input_rect.y + 10))

        column_input_rect.w = max(50,text_surface.get_width() + 5)
        for y in range(len(tabla)):
            
            #if tabla[x][y] == "-":
            squareColor = (255,255,255)
            pygame.draw.rect(WIN ,squareColor ,
            pygame.Rect(150+(y*squareDim),100+(x*squareDim) , squareDim,squareDim), 2)

        for x in range(len(tabla)):
            for y in range(len(tabla)):
                if tabla[x][y] == "X" and tabla[x+1][y] == "X":
                    squareColor = ORANGE
                    pygame.draw.rect(WIN ,squareColor ,
                    pygame.Rect(150+(y*squareDim)+7.5,100+(x*squareDim)+12.5 , squareDim-15 ,2*squareDim-25))
                if tabla[x][y] == "O" and tabla[x][y+1] == "O":
                    squareColor = BLACK
                    pygame.draw.rect(WIN ,squareColor ,
                    pygame.Rect(150+(y*squareDim)+12.5,100+(x*squareDim)+7.5 , 2*squareDim-25,squareDim-15))

    pygame.display.update()

def igrajPotez(moveText,player):

    validanPotez =  Domineering.PlayMove2(playerValue(player),(int(moveText[0]),moveText[1]),tabla)
    if not validanPotez:
        return False
    else :    
        print(player , not player)
        #player = not player
        print(moveText[0],moveText[1])
        return True


def playerValue(player):

    if player :
        return 'X'
    return 'O'    


def main():
    clock = pygame.time.Clock()
    run = True 
    moveText =""
    active = False
    player = True

    while(run):
        for event in pygame.event.get():
            draw_window(moveText)
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
                        if valid :
                            player =  not player
                            moveText = ""
                        else :
                            player = player

                        kraj = Domineering.GameOver(player)
                        print(kraj[0])
                        if kraj :
                            if not player : 
                                text_surface = GAMEOVER_FONT.render("X WINS",True,(0,0,0))
                                WIN.blit(text_surface,(column_input_rect.x + 20 , column_input_rect.y + 10))
                                print("X WINS")
                            else :
                                text_surface = GAMEOVER_FONT.render("O WINS",True,(0,0,0))
                                WIN.blit(text_surface,(column_input_rect.x + 20 , column_input_rect.y + 10))
                                print("O WINS")

                    else:
                        moveText+=event.unicode
     
            #draw_window(moveText)

    clock.tick(FPS) 
    pygame.quit()            


if __name__ == "__main__":
    main()

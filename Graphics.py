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
player = "X"

pygame.init()

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Domineering")
tabla= Domineering.CreateTable(8,8)
Domineering.PrintTable(tabla)
newPlayer = Domineering.PlayMove(player,(2, "G"),tabla)
Domineering.PlayMove(newPlayer,(4, "B"),tabla)


column_input_rect = pygame.Rect(460,25,50,35)
row_input_rect = pygame.Rect(385,25,50,35)
font = pygame.font.Font('freesansbold.ttf', 18)
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
            
            if tabla[x][y] == "-":
                squareColor = (255,255,255)
                pygame.draw.rect(WIN ,squareColor ,
                pygame.Rect(150+(y*squareDim),100+(x*squareDim) , squareDim,squareDim), 2)
            if tabla[x][y] == "X":
                squareColor = ORANGE
                pygame.draw.rect(WIN ,squareColor ,
                pygame.Rect(150+(y*squareDim),100+(x*squareDim) , squareDim,squareDim))
            if tabla[x][y] == "O":
                squareColor = BLACK
                pygame.draw.rect(WIN ,squareColor ,
                pygame.Rect(150+(y*squareDim),100+(x*squareDim) , squareDim,squareDim))

    pygame.display.update()

def igrajPotez(moveText):
    Domineering.PlayMove("X",(int(moveText[0]),moveText[1]),tabla)
    print(moveText[0],moveText[1])

def main():
    clock = pygame.time.Clock()
    run = True 
    moveText =""
    active = False
    while(run):
        for event in pygame.event.get():
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
                        igrajPotez(moveText)
                        moveText = ""
                    else:
                        moveText+=event.unicode
     
            draw_window(moveText)

    clock.tick(FPS) 
    pygame.quit()            


if __name__ == "__main__":
    main()

import copy
import Tabla

table = []
#player = "X"
#pc = False
#myPlayer = ""
#pcPlayer = ""

'''def FirstMove():
    answer = input("Do you want to play first?\n")
    yes = "yes"
    no = "no"
    if answer == yes:
        myPlayer1="X"
        pcPlayer1="O"
        print("1: me")
        print("2: pc")
        return (myPlayer1, pcPlayer1)
    elif answer == no:
        myPlayer1="O"
        pcPlayer1="X"
        print("1: pc")
        print("2: me")
        return (myPlayer1, pcPlayer1)
    else:
        print("Invalid input!")
        return False


def OpponentSelection():
    answer = input("Do you want to play against computer?\n")
    yes = "yes"
    no = "no"
    if answer == yes:
        pc = True
        players = FirstMove()
        return players
    elif answer == no:
        print("Your opponent is human")
        return ("-", "-")
    else:
        print("Invalid input!")'''


def CreateTable(size):

    if size == "Small" :
        x = 4 
    elif size == "Medium" :
        x = 6
    elif size == "Large" :
        x = 8


    table = list()
    for i in range(x):
        table.append(list())
        for j in range(x):
            table[i].append('-')
    
    return table
   

def GetLetterList(len):
    letterList = list()
    c=65
    for i in range(len):
        letterList.append(chr(c))
        c+=1
    
    retlist = ' '.join(str(item) for item in letterList)
    return retlist


def PrintTable(table):
    letterlist = GetLetterList(len(table))
    counter=len(table)
    print(" ", letterlist)
    for field in table:
        print(counter,' '.join(str(item) for item in field), counter)
        counter-=1
    print(" ", letterlist)


def IsValid(player, move, table):
    if move[0]<0 or move[0]> len(table)-1  or move[1]<0 or move[1]> len(table)-1:
        return False
    if player == "X":
        if move[0] == 0 :
            return False
        if table[move[0]][move[1]] == "-":
            if table[move[0]-1][move[1]] == "-":
                return True
    if player == "O":
        if move[1] > len(table)-2:
            return False
        if table[move[0]][move[1]] == "-":
            if table[move[0]][move[1]+1] == "-":
                return True
    return False


def PlayMove(player, unFormatedMove,table):
    move = DecodeMove(unFormatedMove, table)
    valid = IsValid(player, move,table)

    new_table = copy.deepcopy(table)

    if valid:
        if(player == "X"):
            new_table[move[0]][move[1]] = player
            new_table[move[0]-1][move[1]] = player
            #PrintTable(new_table)
            '''istheGameOver = GameOver(player, new_table)
            #print(istheGameOver)
            if istheGameOver[0] == False:
                return (True , new_table)
            else:
                print(istheGameOver[1], "Wins!")
                return (True , new_table)'''
            return new_table
        else:
            new_table[move[0]][move[1]] = player
            new_table[move[0]][move[1]+1] = player
            #PrintTable(new_table)
            '''istheGameOver = GameOver(player, new_table)
            #print(istheGameOver)
            if istheGameOver[0] == False:
                return (True , new_table)
            else:
                print(istheGameOver[1], "Wins!")
                return (True , new_table)'''
            return new_table
    else:
        return new_table


def DecodeMove(move,table):
    if move[0] > len(table) or move[0]<0:
        i = move[0]
    elif move[0] == len(table):
        i=0
    else:
        i =  abs(move[0]-len(table))
    j = ord(move[1])-65
    return (i, j)

def EncodeMove(field,table):

    moveX = abs(field[0]-len(table))
    moveY = chr(65 + field[1])
    #print(moveX , moveY)
    return (moveX , moveY)


def GameOver(player, table):
    if player == "X":
        for i in range(len(table)):
            for j in range(len(table)-1):
                if table[i][j] == '-' and table[i][j+1] == '-':
                    return (False, player)
    else:
        for i in range(len(table)-1):
            for j in range(len(table)):
                if table[i][j] == '-' and table[i+1][j] == '-':
                    return (False, player)
  
    return (True, player)

def possibleMoves(tabla , player):

    potezi = []
    #print(len(tabla))

    if player == "O":
        for i in range(len(tabla)):
            for j in range(len(tabla)-1):
                if tabla[i][j] == '-' and tabla[i][j+1] == '-':
                    valid = IsValid(player, (i,j),tabla)                   
                    if valid :
                        move = EncodeMove((i,j),tabla)
                        potezi.append(move)
                    
    elif player == "X":
        for i in range(1, len(tabla)):
            for j in range(len(tabla)):
                if tabla[i][j] == '-' and tabla[i-1][j] == '-':
                    valid = IsValid(player, (i,j),tabla)                   
                    if valid :
                        move = EncodeMove((i,j),tabla)
                        potezi.append(move)
                
    return potezi


def heurstic(player, table):
    h = 0

    if player == "X":
        for i in range(len(table)):
            for j in range(len(table)):
                if j == 0 or j == len(table)-1: # proveravamo granicni uslov tj da li je plocica 
                    if table[i][j] == "X":      # uz levu ili desnu stranu table
                        if j == 0:
                            if table[i][j+1] == "-":
                                h+=1
                        else:
                            if table[i][j-1] == "-":
                                 h+=1
                else:
                    if table[i][j] == "X":
                        if table[i][j+1] == "-":
                                h+=1
                        elif table[i][j+1] == "X":
                                 h+=1
                        if table[i][j-1] == "-":
                                h+=1
                        elif table[i][j-1] == "X":
                                 h+=1
    
    else:
        for i in range(len(table)):
            for j in range(len(table)):
                if i == 0 or i == len(table)-1: # proveravamo granicni uslov tj da li je plocica
                    if table[i][j] == "O":      # uz gornju ili donju stranu table
                        if i == 0:
                            if table[i+1][j] == "-":
                                h-=1
                        else:
                            if table[i-1][j] == "-":
                                 h-=1
                else:
                    if table[i][j] == "O":
                        if table[i+1][j] == "-":
                                h-=1
                        elif table[i+1][j] == "O":
                                 h-=1
                        if table[i-1][j] == "-":
                                h-=1
                        elif table[i-1][j] == "O":
                                 h-=1
    return h


def max_stanje(lsv):
    return max(lsv, key=lambda x: x[1])

def min_stanje(lsv):
    return min(lsv, key=lambda x: x[1])
   

def minimax(stanje, dubina, moj_potez, potez = None):

    igrac = "X" if moj_potez else "O"
    gameover = GameOverPC(igrac, stanje)
    if gameover[0] == True:
        return(potez, gameover[1]) 

    fja = max_stanje if moj_potez else min_stanje
    lp = possibleMoves(stanje, igrac)

    if dubina == 0:
        return (potez, heurstic(igrac, stanje))

    if lp is None or len(lp) == 0:
        return (potez, heurstic(igrac, stanje))

    return fja([minimax(PlayMove(igrac, x, stanje), dubina - 1, not moj_potez, x if potez is None else potez) for x in lp])
            

def GameOverPC(player, table):
    if player == "X":
        for i in range(len(table)):
            for j in range(len(table)-1):
                if table[i][j] == '-' and table[i][j+1] == '-':
                    return (False, 0)
    else:
        for i in range(len(table)-1):
            for j in range(len(table)):
                if table[i][j] == '-' and table[i+1][j] == '-':
                    return (False, 0)
    
    if player == "X":
        return (True, 10)
    else:
        return (True, -10)


def Valid(player, move, table):
    move = DecodeMove(move, table)
    valid = IsValid(player, move, table)
    if valid:
        return True
    return False


def Game():
    tableSize = input("Select one of these listed tables: Small, Medium, Large:")
    table = CreateTable(tableSize)

    PC = True if input("Do you want to play against computer?") == "yes" else False
    moj = True if input("Do you want to play first?") == "yes" else False
    igrac = "X"
    PrintTable(table)

    gameover = GameOverPC(igrac, table)

    while gameover[0] == False:
        if PC:
            if moj:
                move = list(input("It's your trun:"))
                move[0] = int(move[0])
                move = tuple(move)
                valid = Valid(igrac, move, table)
                table = PlayMove(igrac, move, table)
                if valid:
                    PrintTable(table)
                    igrac = "O" if igrac == "X" else "X"
                    moj = not moj
                    gameover = GameOver(igrac, table)
                else:
                    print("Not Valid!")
            else:
                print("PC is playing...")
                rez = minimax(table, 3, moj)
                naj = rez[0] if type(rez) is tuple else (0, 0)
                table = PlayMove(igrac, naj, table)
                PrintTable(table)
                igrac = "O" if igrac == "X" else "X"
                moj = not moj
                gameover = GameOver(igrac, table)
        
        else:
            if moj:
                move = list(input("Player1: It's your trun:"))
                move[0] = int(move[0])
                move = tuple(move)
                valid = Valid(igrac, move, table)
                table = PlayMove(igrac, move, table)
                if valid:
                    PrintTable(table)
                    igrac = "O" if igrac == "X" else "X"
                    moj = not moj
                    gameover = GameOver(igrac, table)
                else:
                    print("Not Valid!")
            else:
                move = list(input("Player2: It's your trun:"))
                move[0] = int(move[0])
                move = tuple(move)
                valid = Valid(igrac, move, table)
                table = PlayMove(igrac, move, table)
                if valid:
                    PrintTable(table)
                    igrac = "O" if igrac == "X" else "X"
                    moj = not moj
                    gameover = GameOver(igrac, table)
                else:
                    print("Not Valid!")
        
    print("The winner is: ", gameover[1])

Game()

# TESTING 
# =============================
#players = OpponentSelection()
#myPlayer = players[0]
#pcPlayer = players[1]
'''table = CreateTable("Small")
PrintTable(table)'''
'''novatablica = PlayMove("X", (1, "A"), table)
print(possibleMoves((novatablica[1]),"X"))
novatablica = PlayMove("X", (2, "B"), novatablica[1])
print(possibleMoves((novatablica[1]),"X"))
novatablica = PlayMove("X", (3, "C"), novatablica[1])
print(possibleMoves((novatablica[1]),"X"))'''

'''novatablica = PlayMove("O", (1, "A"), table)
print(possibleMoves((novatablica[1]),"O"))
novatablica = PlayMove("O", (2, "A"), novatablica[1])
print(possibleMoves((novatablica[1]),"O"))
novatablica = PlayMove("O", (3, "B"), novatablica[1])
print(possibleMoves((novatablica[1]),"O"))'''


# ova situacija je losa(vise nije, nadam se)
'''novatablica = PlayMove("X", (3, "A"), table)
novatablica = PlayMove("O", (2, "B"), novatablica[1])
novatablica = PlayMove("X", (2, "D"), novatablica[1])
novatablica = PlayMove("O", (1, "C"), novatablica[1])'''

'''novatablica = PlayMove("X", (3, "A"), table)
novatablica = PlayMove("O", (2, "B"), novatablica[1])
novatablica = PlayMove("X", (3, "C"), novatablica[1])
novatablica = PlayMove("O", (1, "C"), novatablica[1])


heur = heurstic("X", novatablica[1])
print("Heuristika je:", heur)'''
# =========================== ==




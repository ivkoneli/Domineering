import copy
import Tabla

table = []

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


def heuristic(player, table):
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


def heuristicMove(player, table, move):
    h = 0
    move = DecodeMove(move, table)

    if player == "X":
        if move[1] == 0 or move[1] == len(table)-1:
            if move[1] == 0:
                if table[move[0]][move[1]+1] == "-":
                    h+=1
                if table[move[0]-1][move[1]+1] == "-":
                    h+=1
            else:
                if table[move[0]][move[1]-1] == "-":
                    h+=1
                if table[move[0]-1][move[1]-1] == "-":
                    h+=1
        else:
            if table[move[0]][move[1]+1] == "-":
                h+=1
            if table[move[0]][move[1]-1] == "-":
                h+=1
            if table[move[0]-1][move[1]+1] == "-":
                h+=1
            if table[move[0]-1][move[1]-1] == "-":
                h+=1
    
    else:
        if move[0] == 0 or move[0] == len(table)-1:
            if move[0] == 0:
                if table[move[0]+1][move[1]] == "-":
                    h+=1
                if table[move[0]+1][move[1]+1] == "-":
                    h+=1
            else:
                if table[move[0]-1][move[1]] == "-":
                    h+=1
                if table[move[0]-1][move[1]+1] == "-":
                    h+=1
        else:
            if table[move[0]+1][move[1]] == "-":
                h+=1
            if table[move[0]-1][move[1]] == "-":
                h+=1
            if table[move[0]+1][move[1]+1] == "-":
                h+=1
            if table[move[0]-1][move[1]+1] == "-":
                h+=1

    if player == "X":
        return h+1
    else:
        return -1*h-1


'''def max_stanje(lsv):
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
        return (potez, heuristic(igrac, stanje, potez))

    if lp is None or len(lp) == 0:
        return (potez, heuristic(igrac, stanje, potez))

    return fja([minimax(PlayMove(igrac, x, stanje), dubina - 1, not moj_potez, x if potez is None else potez) for x in lp])'''
            

def max_value(table, dubina, parity, alpha, beta, move = None):

    if abs(GameOverPC(table)) == 10:
        return (move, GameOverPC(table))

    possible_moves = list(possibleMoves(table, "X"))

    if dubina == 0 or possible_moves is None or len(possible_moves) == 0:
        if parity == 0:
            return (move, heuristicMove("X", table, move))
        return (move, heuristicMove("O", table, move))
    else:
        for s in possible_moves:
            alpha = max(alpha,
                    min_value(PlayMove("X", s, table), dubina - 1, parity, alpha, beta, s if move is None else move),
                    key=lambda x: x[1])
            if alpha[1] >= beta[1]:
                return beta
    return alpha


def min_value(table, dubina, parity, alpha, beta, move = None):

    if abs(GameOverPC(table)) == 10:
        return (move, GameOverPC(table))

    possible_moves = list(possibleMoves(table, "O"))
    
    if dubina == 0 or possible_moves is None or len(possible_moves) == 0:
        if parity == 0:
            return (move, heuristicMove("O", table, move))
        return (move, heuristicMove("X", table, move))
    else:
        for s in possible_moves:
            beta = min(beta,
                    max_value(PlayMove("O", s, table), dubina - 1, parity, alpha, beta, s if move is None else move),
                    key=lambda x: x[1])
            if beta[1] <= alpha[1]:
                return alpha
    return beta


def minimax(table, dubina, moj_potez, alpha = (None, -100), beta = (None, 100)):
    parity = dubina % 2
    if moj_potez:
        return max_value(table, dubina, parity, alpha, beta)
    else:
        return min_value(table, dubina, parity, alpha, beta)


def GameOverPC(table):
    X=0
    O=0

    for i in range(len(table)-1):
        for j in range(len(table)):
            if table[i][j] == '-' and table[i+1][j] == '-':
                X+=1

    for i in range(len(table)):
        for j in range(len(table)-1):
            if table[i][j] == '-' and table[i][j+1] == '-':
                O+=1
 
    if X != 0 and O != 0:
        return 0
    elif X != 0:
        return 10
    else: 
        return -10


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
    myTurn = True if input("Do you want to play first?") == "yes" else False

    if myTurn:
        player = "X"
        myTurnPC = False
    else:
        player = "X"
        myTurnPC = True
    
    PrintTable(table)

    gameover = GameOverPC(table)

    while gameover == 0:
        if PC:
            if myTurn:
                move = list(input("It's your trun:"))
                move[0] = int(move[0])
                move = tuple(move)
                valid = Valid(player, move, table)
                table = PlayMove(player, move, table)
                if valid:
                    PrintTable(table)
                    player = "O" if player == "X" else "X"
                    myTurn = not myTurn
                    gameover = GameOverPC(table)
                else:
                    print("Not Valid!")
            else:
                print("PC is playing...")
                rez = minimax(table, 5, myTurnPC)
                naj = rez[0] if type(rez) is tuple else (0, 0)
                print(naj)
                table = PlayMove(player, naj, table)
                PrintTable(table)
                player = "O" if player == "X" else "X"
                myTurn = not myTurn
                gameover = GameOverPC(table)
        
        else:
            if myTurn:
                move = list(input("Player1: It's your trun:"))
                move[0] = int(move[0])
                move = tuple(move)
                valid = Valid(player, move, table)
                table = PlayMove(player, move, table)
                if valid:
                    PrintTable(table)
                    player = "O" if player == "X" else "X"
                    myTurn = not myTurn
                    gameover = GameOverPC(table)
                else:
                    print("Not Valid!")
            else:
                move = list(input("Player2: It's your trun:"))
                move[0] = int(move[0])
                move = tuple(move)
                valid = Valid(player, move, table)
                table = PlayMove(player, move, table)
                if valid:
                    PrintTable(table)
                    player = "O" if player == "X" else "X"
                    myTurn = not myTurn
                    gameover = GameOverPC(table)
                else:
                    print("Not Valid!")
        
    print("The winner is: ", "X" if gameover == 10 else "O")

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




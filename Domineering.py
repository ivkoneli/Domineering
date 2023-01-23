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
            return new_table
        else:
            new_table[move[0]][move[1]] = player
            new_table[move[0]][move[1]+1] = player
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
                    return False
    elif player == "O":
        for i in range(len(table)-1):
            for j in range(len(table)):
                if table[i][j] == '-' and table[i+1][j] == '-':
                    return False
  
    return True

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
                            elif table[i][j+1] == "X":
                                 h+=0.5
                            elif table[i][j+1] == "O":
                                h-=1
                        else:
                            if table[i][j-1] == "-":
                                h+=1
                            elif table[i][j-1] == "X":
                                h+=0.5
                            elif table[i][j-1] == "O":
                                h-=1
                else:
                    if table[i][j] == "X":
                        if table[i][j+1] == "-":
                                h+=1
                        elif table[i][j+1] == "X":
                                h+=0.5
                        elif table[i][j+1] == "O":
                                h-=1
                        if table[i][j-1] == "-":
                                h+=1
                        elif table[i][j-1] == "X":
                                h+=0.5
                        elif table[i][j-1] == "O":
                                h-=1
    
    else:
        for i in range(len(table)):
            for j in range(len(table)):
                if i == 0 or i == len(table)-1: # proveravamo granicni uslov tj da li je plocica
                    if table[i][j] == "O":      # uz gornju ili donju stranu table
                        if i == 0:
                            if table[i+1][j] == "-":
                                h+=1
                            elif table[i+1][j] == "O":
                                h+=0.5
                            elif table[i+1][j] == "X":
                                h-=1
                        else:
                            if table[i-1][j] == "-":
                                h+=1
                            elif table[i-1][j] == "O":
                                h+=0.5
                            elif table[i-1][j] == "X":
                                h-=1
                                
                else:
                    if table[i][j] == "O":
                        if table[i+1][j] == "-":
                                h+=1
                        elif table[i+1][j] == "O":
                                h+=0.5
                        elif table[i+1][j] == "X":
                                h-=1
                        if table[i-1][j] == "-":
                                h+=1
                        elif table[i-1][j] == "O":
                                h+=0.5
                        elif table[i-1][j] == "X":
                                h-=1
    if player == "X":
        return h
    else:
        return -1*h


def max_value(table, dubina, parity, alpha, beta, move = None):

    if abs(GameOverPC(table)) == 100:
        return (move, GameOverPC(table))

    possible_moves = list(possibleMoves(table, "X"))

    if dubina == 0 or possible_moves is None or len(possible_moves) == 0:
        if parity == 0:
            return (move, heuristic("X", table))
        return (move, heuristic("O", table))
    else:
        for s in possible_moves:
            alpha = max(alpha,
                    min_value(PlayMove("X", s, table), dubina - 1, parity, alpha, beta, s if move is None else move),
                    key=lambda x: x[1])
            if alpha[1] >= beta[1]:
                return beta
    return alpha


def min_value(table, dubina, parity, alpha, beta, move = None):

    if abs(GameOverPC(table)) == 100:
        return (move, GameOverPC(table))

    possible_moves = list(possibleMoves(table, "O"))
    

    if dubina == 0 or possible_moves is None or len(possible_moves) == 0:
        if parity == 0:
            return (move, heuristic("O", table))
        return (move, heuristic("X", table))
    else:
        for s in possible_moves:
            beta = min(beta,
                    max_value(PlayMove("O", s, table), dubina - 1, parity, alpha, beta, s if move is None else move),
                    key=lambda x: x[1])
            if beta[1] <= alpha[1]:
                return alpha
    return beta


def minimax(table, dubina, moj_potez, alpha = (None, -1000), beta = (None, 1000)):
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
        return 100
    else: 
        return -100


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
                rez = minimax(table, 4, myTurnPC)
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
        
    print("The winner is: ", "X" if gameover == 100 else "O")

#Game()





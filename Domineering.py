import copy

player = "X"
pc = False
table = []
myPlayer = ""
pcPlayer = ""

def FirstMove():
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
        print("Invalid input!")


def CreateTable(size):

    if size == "small" :
        x = 4 
    elif size == "medium" :
        x = 6
    elif size == "large" :
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


def IsValid(player, move,table):
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
            PrintTable(new_table)
            istheGameOver = GameOver(player, new_table)
            print(istheGameOver)
            if istheGameOver[0] == False:
                return (True , new_table)
            else:
                print(istheGameOver[1], "X Wins!")
                return (True , new_table)
        else:
            new_table[move[0]][move[1]] = player
            new_table[move[0]][move[1]+1] = player
            PrintTable(new_table)
            istheGameOver = GameOver(player, new_table)
            print(istheGameOver)
            if istheGameOver[0] == False:
                return (True , new_table)
            else:
                print(istheGameOver[1], "O Wins!")
                return (True , new_table)
    else:
        print("Not valid")
        return (False , new_table)



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
                if table[i][j] == '-' and table[i][j+1] == '-':
                    valid = IsValid(player, (i,j),tabla)                   
                    if valid :
                        move = EncodeMove((i,j),tabla)
                        potezi.append(move)
                        #potezi.append((i,j))
                    
    else:
        for i in range(len(tabla)-1):
            for j in range(len(tabla)):
                if table[i][j] == '-' and table[i+1][j] == '-':
                    valid = IsValid(player, (i,j),tabla)                   
                    if valid :
                        move = EncodeMove((i,j),tabla)
                        potezi.append(move)
                        #potezi.append((i,j))

    return potezi



# TESTING 
# =============================
#players = OpponentSelection()
#myPlayer = players[0]
#pcPlayer = players[1]
#table = CreateTable("medium")
#PrintTable(table)
#print(possibleMoves((table),"X"))
#novatablica = PlayMove("X", (1, "C"), table)
#print(possibleMoves((novatablica[1]),"X"))
#novatablica = PlayMove("O", (1, "A"), novatablica[1])
#print(possibleMoves((novatablica[1]),"O"))
#PlayMove("O", (2, "A"), table)
#PlayMove("O", (3, "A"), table)
# =============================






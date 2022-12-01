player = "X"

def FirstMove():
    print("Ko igra prvi?")

table = []
def CreateTable(x, y):
    table = list()
    for i in range(x):
        table.append(list())
        for j in range(y):
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
    if valid:
        if(player == "X"):
            table[move[0]][move[1]] = player
            table[move[0]-1][move[1]] = player
            PrintTable(table)
            return "O"
        else:
            table[move[0]][move[1]] = player
            table[move[0]][move[1]+1] = player
            PrintTable(table)
            return "X"
    else:
        print("Not valid")
        return False


def DecodeMove(move,table):
    if move[0] == len(table):
        i=0
    else:
        i =  abs(move[0]-len(table))
    j = ord(move[1])-65
    return (i, j)


def GameOver(player):
    if player == "O":
        for i in range(len(table)):
            for j in range(len(table)-1):
                if table[i][j] == '-' and table[i][j+1] == '-':
                    return False
    else:
        for i in range(len(table)-1):
            for j in range(len(table)):
                if table[i][j] == '-' and table[i+1][j] == '-':
                    return False

    return (True, player)

#table = CreateTable(8, 8)
#PrintTable(table)
#PlayMove("O", (4, "A"))
#PlayMove("X", (2, "G"))
#PlayMove("X", (2, "S"))







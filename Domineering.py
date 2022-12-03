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
            istheGameOver = GameOver(player)
            if istheGameOver == False:
                return "O"
            else:
                print(istheGameOver[1], "Wins!")
        else:
            table[move[0]][move[1]] = player
            table[move[0]][move[1]+1] = player
            PrintTable(table)
            istheGameOver = GameOver(player)
            if istheGameOver == False:
                return "X"
            else:
                print(istheGameOver[1], "Wins!")
    else:
        print("Not valid")
        return False


def DecodeMove(move,table):
    if move[0] > len(table) or move[0]<0:
        i = move[0]
    elif move[0] == len(table):
        i=0
    else:
        i =  abs(move[0]-len(table))
    j = ord(move[1])-65
    return (i, j)


def GameOver(player):
    if player == "X":
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


#players = OpponentSelection()
#myPlayer = players[0]
#pcPlayer = players[1]
#table = CreateTable(3, 3)
#PrintTable(table)
#PlayMove("O", (1, "A"), table)
#PlayMove("O", (2, "A"), table)
#PlayMove("O", (3, "A"), table)
#PlayMove("X", (1, "C"), table)







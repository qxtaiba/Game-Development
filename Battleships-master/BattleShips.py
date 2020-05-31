from random import randint
import time 
import os

#DEFINE CONSTANTS

numRows = 10
numCols = 10
shipLen = 4

InitalBoolStat = "FALSE"
SecondBoolStat = "FALSE"

intCounter = 1
hitCounter = 0

#CREATE HIDDEN AND VISIBLE MATRIX

hiddenBoardMatrix = []
boardMatrix=[]

os.system("clear")

#FILL HIDDEN BOARD 

for row in range(numRows):
    rowList=[]

    for col in range(numCols):
        rowList.append(" ")

    hiddenBoardMatrix.append(rowList)

#FILL VISIBLE BOARD 

for row in range(numRows):
    rowList=[]

    for col in range(numCols):
        rowList.append(" ")

    boardMatrix.append(rowList)

#ASSIGN SHIP LOCATION(S)

while InitalBoolStat == "FALSE":

    #ASSIGN RANDOM VARIABLE(S)

    shipOrient = randint(1,2)
    shipRow = randint(0, numRows-1)
    shipCol = randint(0, numCols-1)

    if (shipOrient == 1 and shipCol <= (numCols-shipLen)):
        InitalBoolStat = "TRUE"

        for i in range (0,shipLen):
            hiddenBoardMatrix[shipRow][shipCol+i]='1'

    elif (shipOrient == 2 and shipRow <= (numRows-shipLen)):
        InitalBoolStat = "TRUE"

        for j in range (0,shipLen):
            hiddenBoardMatrix[shipRow+j][shipCol]= '1'

#PRINT BOARD 

for cols in range(numCols):
    print ("   "+str(cols),  end=" ")

print("\n "+" ---+"*numCols)

for row in range(numRows):
    print(row, "|", end="")

    for col in range(numCols):
        print(boardMatrix[row][col],' | ', end='')

    print("\n "+" ---+"*numCols)

print ("\nWELCOME TO BATTLESHIP,LET'S GET STARTED! DO YOU THINK YOU CAN WIN?\n")

#GAME LOOP

while SecondBoolStat == "FALSE":

    print("\nROUND: ", intCounter)

    usGuessRow = (input("\nGUESS A ROW: "))
    usGuessColumn = (input("\nGUESS A COLUMN: "))

    #INPUT CHECK

    while not usGuessColumn.isdigit() or not usGuessRow.isdigit():
        os.system("clear")
        
        #PRITN BOARD 

        for cols in range(numCols):
            print ("   "+str(cols),  end=" ")
    
        print("\n "+" ---+"*numCols)
        
        for row in range(numRows):
            print(row, "|", end="")
            
            for col in range(numCols):
                print(boardMatrix[row][col],' | ', end='')
            
            print("\n "+" ---+"*numCols)

        print ("\nINVALID INPUT!")
        print("\nROUND: ", intCounter)

        usGuessRow = (input("\nGUESS A ROW: "))
        usGuessColumn = (input("\nGUESS A COLUMN: "))

        #INPUT CHECK

    while (int(usGuessColumn) < 0 or int(usGuessColumn) >9 or int(usGuessRow) <0 or int (usGuessRow) > 9):
        os.system("clear")
        
        #PRINT BOARD 

        for cols in range(numCols):
            print ("   "+str(cols),  end=" ")

        print("\n "+" ---+"*numCols)

        for row in range(numRows):
            print(row, "|", end="")
    
            for col in range(numCols):
                print(boardMatrix[row][col],' | ', end='')
            
            print("\n "+" ---+"*numCols)

        print ("\nINVALID INPUT!")
        print("\nROUND: ", intCounter)

        usGuessRow = (input("\nGUESS A ROW: "))
        usGuessColumn = (input("\nGUESS A COLUMN: "))

        #DOUBLE-SELECTION CHECK 

    if ((boardMatrix[int(usGuessRow)][int(usGuessColumn)] == '0')):
        os.system("clear")

        #PRINT BOARD

        for cols in range(numCols):
            print ("   "+str(cols),  end=" ")
            
        print("\n "+" ---+"*numCols)
            
        for row in range(numRows):
            print(row, "|", end="")

            for col in range(numCols):
                print(boardMatrix[row][col],' | ', end='')
                
            print("\n "+" ---+"*numCols)


        print ("\nYOU HAVE ALREADY MADE THIS SELECTION! ")

        #SUCCESFUL HIT CHECK

    elif ((hiddenBoardMatrix[int(usGuessRow)][int(usGuessColumn)] == '1')):
        os.system("clear")
        boardMatrix[int(usGuessRow)][int(usGuessColumn)] = 'X'
        hiddenBoardMatrix[int(usGuessRow)][int(usGuessColumn)] = 'X'


        #PRINT BOARD 

        for cols in range(numCols):
            print ("   "+str(cols),  end=" ")

        print("\n "+" ---+"*numCols)

        for row in range(numRows):
            print(row, "|", end="")

            for col in range(numCols):
                print(boardMatrix[row][col],' | ', end='')

            print("\n "+" ---+"*numCols)


        print ("\nNICE SHOT!")

        intCounter +=1
        hitCounter+=1

        #UNSUCCESFUL HIT CHECK

    elif ((boardMatrix[int(usGuessRow)][int(usGuessColumn)] == ' ')):
        os.system("clear")

        boardMatrix[int(usGuessRow)][int(usGuessColumn)] = '0'

        #PRINT BOARD
        for cols in range(numCols):
            print ("   "+str(cols),  end=" ")

        print("\n "+" ---+"*numCols)
                                         
        for row in range(numRows):
            print(row, "|", end="")

            for col in range(numCols):
                print(boardMatrix[row][col],' | ', end='')

            print("\n "+" ---+"*numCols)

        print ("\nBETTER LUCK NEXT TIME!")

        intCounter +=1


    if (hitCounter == shipLen):
        SecondBoolStat = "TRUE"

os.system("clear")

print ("CONGRATULATIONS, YOU WON!")

            

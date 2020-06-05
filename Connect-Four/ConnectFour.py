#NAME:QUTAIBA AL-NUAIMY
#NETID: QAN205
#DATE: 8/10/2018

#MODULE IMPORT

from random import randint
import time 
import os
import sys

#CREATE DYNAMIC CONNECTFOUR GRID

def createBoard(numRows,numCols, boardMatrix):

	for row in range(int(numRows)+1):
	    rowList=[]

	    for col in range(int(numCols)+1):
	        rowList.append(" ")

	    boardMatrix.append(rowList)

#PRINT DYNAMIC CONNECTFOUR GRID

def printBoard(numRows,numCols):

	for cols in range(int(numCols)):

		if (cols<10):
		   	print ("    "+str(cols+1),  end=" ")
		else:
			print ("   "+str(cols+1),  end=" ")

		
	print("\n "+"  ---+"*int(numCols))

	for row in range(int(numRows)):
		if row<9:
			print(row+1, " |", end="")
		else:
			print(row+1, "|", end="")

		for col in range(int(numCols)):
		    print(boardMatrix[row+1][col+1],' |  ', end='')

		print("\n "+"  ---+"*int(numCols))

#PRINT GAME/USER MENU

def printMenu(boolStat):


	while boolStat == True:

		usIn = '1'

		while boolStat == True and usIn.isdigit():

			#PRINT MENU

			print ("\n****************************")
			print ("\n#1 - PLAY CONNECT-FOUR\n")
			print ("#2 - HELP\n")
			print ("#3 - QUIT\n")
			print ("****************************")

			usIn = input ("\nCHOSE ONE OF THE OPTIONS ABOVE: ")

			os.system("clear")

			#EXIT LOOP AND CONTINUE PROGRAM 

			if usIn == '1':

				boolStat = False

			#HELP PAGE

			elif usIn == '2':

				print("\nIF YOU ARE LOOKING FOR A SIMPLE STRATEGY GAME THAT CAN BE PLAYED WITH JUST ABOUT ANYONE, INCLUDING YOUNG CHILDREN, CONNECT FOUR IS FOR YOU. CONNECT FOUR IS A SIMPLE GAME SIMILAR TO TIC-TAC-TOE. ONLY INSTEAD OF THREE IN A ROW, THE WINNER MUST CONNECT FOUR IN A ROW.")
				print("\nIT IS A TWO-PLAYER CONNECTION GAME IN WHICH THE PLAYERS FIRST CHOOSE A COLOR AND THEN TAKE TURNS DROPPING ONE COLORED DISC FROM THE TOP INTO A SEVEN-COLUMN, SIX-ROW VERTICALLY SUSPENDED GRID. THE PIECES FALL STRAIGHT DOWN, OCCUPYING THE LOWEST AVAILABLE SPACE WITHIN THE COLUMN. THE OBJECTIVE OF THE GAME IS TO BE THE FIRST TO FORM A HORIZONTAL, VERTICAL, OR DIAGONAL LINE OF FOUR OF ONE'S OWN DISCS. CONNECT FOUR IS A SOLVED GAME. THE FIRST PLAYER CAN ALWAYS WIN BY PLAYING THE RIGHT MOVES.”")

				exCom = input ("\nENTER 'c' TO CONTINUE: ")

				while exCom != 'c':
					exCom = input ("ENTER 'c' TO CONTINUE: ")	
				os.system("clear")

			#EXIT PROGRAM 

			elif usIn == '3':
				sys.exit(0)

#PLACE MARKER ON BOARD

def playTurn(usTurn, usSym, ):

	x = int(numRows)
	placed = False

	while not placed:

		#CHECK FOR EMPTY POSITION IN ROW X

		if boardMatrix[x][int(playOneCol)] == " ":

			#ADD CONNECTFOUR MARKER IF EMPTY (UNIQUE TO PLAYER)

			boardMatrix[x][int(playOneCol)] = usSym[usTurn]

			os.system("clear")

			printBoard(numRows,numCols)

			placed = True

		else:

			#DECREMENT ROW NUMBER

			x-=1

#CREATE GAME

def setUpGame(setUpBool,boardBool):

	while setUpBool == False:

		numPlayers = (input("HOW MANY PLAYERS WILL BE JOINING US TODAY? "))

		if numPlayers.isdigit():

			setUpBool = True

			numPlayers = int(numPlayers)

			os.system("clear")

		else: 

			os.system("clear")


	for x in range(1,int(numPlayers)+1):
		playList[x] = input("PLAYER "+ str(x) +", ENTER YOUR NAME: ")

		os.system("clear")

	os.system("clear")

	numRows = (input("TO CONTINUE, ENTER THE NUMBER OF ROWS/COLUMNS YOU WOULD LIKE TO PLAY WITH: "))
	os.system("clear")
	numCols = numRows

	while boardBool:
		try:

			if int(numRows)<5:

				os.system("clear")
				numRows = (input("TO CONTINUE, ENTER THE NUMBER OF ROWS YOU WOULD LIKE TO PLAY WITH: "))
				os.system("clear")
				numCols = numRows
			else:
				boardBool = False


		except ValueError:	

			os.system("clear")
			numRows = (input("TO CONTINUE, ENTER THE NUMBER OF ROWS YOU WOULD LIKE TO PLAY WITH: "))
			os.system("clear")
			numCols = numRows		



	os.system("clear")

	usTurn=randint(1,numPlayers)

	return numCols, numRows, usTurn, numPlayers

#CHECK FOR WIN

def winCheck(playList,usTurn):

	for y in range(int(numRows)+1):
	    for x in range(int(numCols) - 2):
	        if boardMatrix[x][y] == usSym[usTurn] and boardMatrix[x+1][y] == usSym[usTurn] and boardMatrix[x+2][y] == usSym[usTurn] and boardMatrix[x+3][y] == usSym[usTurn]:
	        	winChecks = True
	        	return winChecks

	    # check vertical spaces
	for x in range(int(numCols)+1):
	    for y in range(int(numRows) - 2):
	        if boardMatrix[x][y] == usSym[usTurn] and boardMatrix[x][y+1] == usSym[usTurn]and boardMatrix[x][y+2] == usSym[usTurn] and boardMatrix[x][y+3] == usSym[usTurn]:
	        	winChecks = True
	        	return winChecks
	        	print("hi")

	    # check / diagonal spaces
	for x in range(int(numCols) - 2):
	    for y in range(3, (int(numRows)+1)):
	        if boardMatrix[x][y] == usSym[usTurn] and boardMatrix[x+1][y-1] == usSym[usTurn] and boardMatrix[x+2][y-2] == usSym[usTurn] and boardMatrix[x+3][y-3] == usSym[usTurn]:
	        	winChecks = True
	        	return winChecks

	    # check \ diagonal spaces
	for x in range(int(numCols) - 2):
	    for y in range(int(numRows) - 2):
	        if boardMatrix[x][y] == usSym[usTurn] and boardMatrix[x+1][y+1] == usSym[usTurn] and boardMatrix[x+2][y+2] == usSym[usTurn] and boardMatrix[x+3][y+3] == usSym[usTurn]:
	        	winChecks = True
	        	return winChecks

#VARIABLE DECLERATION(S)

usSym = ['!','@','£','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']'] #INFINITELY EXTENDABLE
playList = {}
setUpBool = False
winChecks = False 
inPut = True
inputCheck = False
boolStat = True
boardMatrix=[]
boardBool = True

os.system("clear")

printMenu(boolStat)

numCols, numRows, usTurn, numPlayers = setUpGame(setUpBool,boardBool)

createBoard(numRows,numCols, boardMatrix)


printBoard(numRows,numCols) 


while not winChecks:

	#CYCLE THROUGH PLAYERS

	usTurn = ((usTurn)%numPlayers)+1	

	inputCheck = False

	print("\n"+playList[usTurn]+ ", YOU ARE THE "+usSym[usTurn]+". LET'S GO!")

	playOneCol = input("\nPICK A COLUMN: ")

	while inputCheck == False:

		try:

			#CHECK INPUT IS VALID (WITHIN RANGE)

			if 0 > int(playOneCol) or int(playOneCol) > int(numCols):
				os.system("clear")
				printBoard(numRows,numCols)
				print("\nINVALID INPUT, ", playList[usTurn])
				playOneCol = input("\nPICK A COLUMN: ")
			elif 0> int(playOneCol) or int(playOneCol) <= int(numCols):
				inputCheck =True

		except ValueError:
			os.system("clear")
			printBoard(numRows,numCols)
			print("\nINVALID INPUT, ", playList[usTurn])
			playOneCol = input("\nPICK A COLUMN: ")
	
	#CHECK IF TOP ROW IS EMPTY 

	while boardMatrix[1][int(playOneCol)] != " ":

		os.system("clear")
		printBoard(numRows,numCols)
		print("\nINVALID INPUT, ", playList[usTurn])
		playOneCol = input("\nPICK A COLUMN: ")

		try:

			#CHECK INPUT IS VALID (WITHIN RANGE)

			if 0 > int(playOneCol) or int(playOneCol) >= int(numCols):
				os.system("clear")
				printBoard(numRows,numCols)
				print("\nINVALID INPUT, ",playList[usTurn])
				playOneCol = input("\nPICK A COLUMN: ")
			elif 0> int(playOneCol) or int(playOneCol) <= int(numCols):
				inputCheck =True

		except ValueError:
			os.system("clear")
			printBoard(numRows,numCols)
			print("\nINVALID INPUT, PLAYER ",playList[usTurn])
			playOneCol = input("\nPICK A COLUMN: ")


	#PLAY THE USER'S SELECTION

	playTurn(usTurn,usSym)

	#CHECK IF USER WON

	winChecks = winCheck(playList,usTurn)

	if winChecks:
		print("\nCONGRATULATIONS "+playList[usTurn]+ ", YOU ARE THE WINNER!")
	
			
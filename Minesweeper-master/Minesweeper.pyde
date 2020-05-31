#EXTRA IMAGE CALLED mineRed has been added to the game file and included in my online submission

add_library('minim')
import os
player = Minim(this)
import random 
path = os.getcwd()

class Minesweeper:
    
    def __init__(self, numN, numMines, pixelSize = 52):
        
        self.numCol = numN
        self.numRow = numN
        self.numN = numN
        self.numMines = numMines
        self.boardWidth = self.numCol*pixelSize
        self.boardHeight = self.numRow*pixelSize
        self.pixelSize=pixelSize
        self.gameOver = False
        self.OfficialGameBoard = [] 
        self.mineList=[]
        self.endimg = loadImage(path+"/images/gameover.png")
        self.img = loadImage(path+"/images/0.png")
        self.dfltimg = loadImage(path+"/images/tile.png")

        #LIST TO CHECK SURROUNDING TILES
        self.positionList =  [[0,0],[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,0],[-1,1],[-1,-1]]
        self.tileNum = numN*numN
        
        #CREATE 1D LIST POPULATED WITH TILE OBJECTS
        for r in range (self.numN):
            for c in range (self.numN): 
                self.OfficialGameBoard.append(Tile(r,c))
                
        #RANDOMLY DISTRIBUTE MINES
        self.mineList = random.sample(self.OfficialGameBoard, self.numMines)
        
        #CHANGE TILE VALUES TO MINE
        for mine in self.mineList:
            mine.changeTileVal("mine")
            
        #ASSIGN NUMBERS TO TILES SURROUNDING MINES
        for tile in self.OfficialGameBoard:
            if (tile.tileVal != "mine"):
                cnt=0
                for aroundTile in self.positionList:
                    if self.tileCheck(tile.tileRow+aroundTile[0],tile.tileCol+aroundTile[1]) != False:
                        if self. tileCheck(tile.tileRow+aroundTile[0],tile.tileCol+aroundTile[1]).tileVal == "mine":
                            cnt = cnt + 1
                tile.tileVal = str(cnt)
                tile.update()
    
    #FUNCTION TO REVEAL SURROUNDING TILES
    def aroundTileReveal (self, mouseRow, mouseCol):
        
        #CHECK IF TILE IS REAL
        tempTile = self.tileCheck (mouseRow, mouseCol)
        
        if tempTile.tileHidden != False:
            tempTile.reveal()
            self.reduceTile() 

        if tempTile.tileVal != "mine":
            tempTile.reveal()
            for aroundTile in self.positionList:
                
                #CHECK IF TILE IS REAL
                if self.tileCheck(tempTile.tileRow+aroundTile[0],  tempTile.tileCol+aroundTile[1]) != False:
                  
                    #CHECK IF TILE IS NOT A MINE
                    if self.tileCheck( tempTile.tileRow+aroundTile[0],  tempTile.tileCol+aroundTile[1]).tileVal != "mine":
                        
                        #CHECK IF TILE IS HIDDEN
                        if self.tileCheck( tempTile.tileRow+aroundTile[0],  tempTile.tileCol+aroundTile[1]).tileHidden != False:
                            self.reduceTile()
                            self.tileCheck( tempTile.tileRow+aroundTile[0],  tempTile.tileCol+aroundTile[1]).tileHidden = False 
                            
                            #REPEAT IF SURROUNDING TILE(S) HAS VALUE 0
                            if (self.tileCheck(tempTile.tileRow+aroundTile[0], tempTile.tileCol+aroundTile[1])).tileVal == "0":
                                 self.aroundTileReveal(tempTile.tileRow, tempTile.tileCol)                                                            
        else:
             self.gameOver = True    
                                                                                                                                                                                
    #FUNCTION TO REDUCE CLOSED TILE NUMBER                             
    def reduceTile (self):

        #REDUCE TOTAL NUMBER OF CLOSED TILES BY ONE        
        self.tileNum= self.tileNum-1
        
    #FUNCTION TO CHECK IF TILE EXISTS                                    
    def  tileCheck(self, tileRow, tileCol):     
          
        for tile in self.OfficialGameBoard:
            if tile.tileRow == tileRow:
                if tile.tileCol == tileCol:
                    return tile
        return False
    
    #FUNCTION TO BE EXECUTED UPON CLICKING
    def clickCheck (self):
        
        if self.gameOver == False:
            if self.tileNum > self.numMines:

                mouseCol = mouseX//self.pixelSize
                mouseRow = mouseY//self.pixelSize
           
                self.aroundTileReveal(mouseRow,mouseCol)

            else:  
                for i in range (0,100000):
                    print ("CONGRATUALTIONS "*7)
                exit()
                                        
    def display(self):
        
        #DISPLAY ALL TILE OBJECTS IN TILE LIST
        for tile in self.OfficialGameBoard:
            tile.display()
        
        if self.gameOver == True:
            for tile in self.OfficialGameBoard:
                
                if tile.tileVal == "mine":
                    
                    #CHANGE VALUE TO DISPLAY MINE WITH RED BORDER
                    tile.tileVal = "mineRed"
                    tile.update()
                    tile.reveal()
                    tile.display()    
            image(self.endimg,0,0,self.pixelSize*self.numN,self.pixelSize*self.numN)                  
  

class Tile:
    
    def __init__ (self, tileRow, tileCol, tileVal = "tile", tileHidden = True, pixelSize = 52):
        
        self.tileRow = tileRow
        self.tileCol = tileCol
        self.tileVal = tileVal
        self.tileHidden = tileHidden
        self.pixelSize=pixelSize
        self.dfltimg = loadImage(path+"/images/tile.png")
        self.endimg = loadImage(path+"/images/gameover.png")
        self.img = loadImage(path+"/images/0.png")

    def changeTileVal (self, tileVal):
        
        self.tileVal = tileVal
        self.update()    
          
    def reveal(self):
        self.tileHidden = False
        
    def update(self):
        self.img = loadImage(path+"/images/"+str(self.tileVal)+".png")

    def display(self):
        
        if self.tileHidden != True:
            image(self.img,self.tileCol*self.pixelSize,self.tileRow*self.pixelSize,self.pixelSize,self.pixelSize)
        else:
            image(self.dfltimg ,self.tileCol*self.pixelSize,self.tileRow*self.pixelSize,self.pixelSize,self.pixelSize)
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
tileObj = Minesweeper(10,35)   
                
def setup():
    size(tileObj.numN*52, tileObj.numN*52)
    
def draw():
    background(0)
    tileObj.display()

def mouseClicked():
           
    tileObj.clickCheck()

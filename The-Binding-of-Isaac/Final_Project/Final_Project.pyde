
               ### Initialization ###


import os, math, time, random
path = os.getcwd()

s = 2 ## Scaling of all assets

                  ### Classes ###


class Game:
    def __init__(self,w,h):
        self.lost = False
        self.w = w
        self.h = h
        self.player = Player(100,100,26,"basePlayer.png",28,40)
        self.room = Room("wideBackground.png",96,96,960,640)
        self.keyHandler={"mvUP":False, "mvDOWN":False, "mvLEFT":False, "mvRIGHT":False, \
                         "shUP":False, "shDOWN":False, "shLEFT":False, "shRIGHT":False}
        self.tears = []
        self.tearCounter = 0
        self.enemies = []
        self.randomObstacles(6)
        self.randomEnemies(5)
###############
    
    def randomObstacles(self,n):
        for i in range(n):
            self.room.tiles.append(Tile("obstacle.png", random.randint(2,6), random.randint(2,12), False, False))
    
    def randomEnemies(self,n):
        for i in range(n):
            self.enemies.append(Enemy(random.randint(400, 800), random.randint(0,600),26,"basePlayerEnemy.png",28,40,1,2))
    
    def display(self):
        self.room.displayRoom()
        self.playerMovement()
        self.playerTears()
        self.player.display()
        self.updateTears()
        self.enemyMovement()
        self.checkLose()
        self.checkWin()
        
###############

    def checkWin(self):
        if len(self.enemies) == 0 and self.lost == False:
            for e in self.enemies:
                self.deleteEnemy(e.x, e.y)
            img = loadImage(path+"/images/win.png") ## Sprite image loading
            image(img, 350, 200)
    def checkLose(self):
        p = self.player
        
        if p.health <= 0:
            for e in self.enemies:
                self.deleteEnemy(e.x, e.y)
            img = loadImage(path+"/images/gameOver.png") ## Sprite image loading
            image(img, 150, 50)
            self.lost = True
            

    def playerMovement(self):
        
        ### Horizontal Input
        if self.collisionDetect(self.player):
            if self.keyHandler["mvLEFT"]:
                self.player.vx = -self.player.ms
            elif self.keyHandler["mvRIGHT"]:
                self.player.vx = self.player.ms
            else:
                self.player.vx = 0
            
            ### Vertical Input    
            
            if self.keyHandler["mvUP"]:
                self.player.vy = -self.player.ms
            elif self.keyHandler["mvDOWN"]:
                self.player.vy = self.player.ms
            else:
                self.player.vy = 0
    
            ### Diagonal Movement Check
            
            if self.player.vx !=0 and self.player.vy != 0:
                self.player.vx = self.player.vx / math.sqrt(2)
                self.player.vy = self.player.vy / math.sqrt(2)
    
            ### Movement Input
            
            self.player.x += self.player.vx
            self.player.y += self.player.vy


    def changeAttribute (attributeMod, modVal):
            if self.attributeMod == "fireMod":
                self.fr += modVal
            elif self.attributeMod == "speedMod":
                self.ms += modVal
            elif self.attributeMod == "healthMod":
                if (self.player.health <= 20 - modVal):
                    self.player.health+=modVal
                elif self.player.health < 20 and self.player.health > 20-modVal:
                    self.player.health+= 20 - self.player.health 
                    
            
###############

    def collisionDetect(self, c): ## c for Creature Class
        
        b = 1 # b for Bounce Frames
        m = 3.5 * s # Margin of error for detection
        
    ### Wall Detection ###
        
        if c.x < self.room.xmin:
            c.x = self.room.xmin + b
            return (False)
        if c.x > self.room.xmax - (c.w * c.s * s):
            c.x = self.room.xmax - (c.w * c.s * s) - b
            return (False)
        if c.y < self.room.ymin:
            c.y = self.room.ymin + b
            return (False)
        if c.y > self.room.ymax  - (c.h * c.s * s):
            c.y = self.room.ymax - (c.h * c.s * s) - b
            return (False)
    ## Non Passable Tile Detect
        for t in self.room.tiles:
            if not t.p:
                xmin = self.room.xmin + (32 * t.c * s)
                xmax = xmin + (32 * s)
                ymin = self.room.ymin + (32 * t.r * s)
                ymax = ymin + (26 * s)
                        
                ## Aproach from up
                if c.x + (c.w * s * c.s) > xmin + 10 and c.x < xmax - 10 and c.y + (c.h * s * c.s) > ymin + 10 and c.y < ymin + c.h:
                    c.y -= b
                    stroke(255,0,0)
                    ellipse(xmin, ymin, 2, 2)
                    return (False)
                ## Aproach from right
                if c.x > xmax - m and c.x < xmax and c.y + ((c.h-m) * s * c.s) > ymin and c.y < ymax - 10:
                    c.x += b
                    stroke(255,0,0)
                    ellipse(xmin, ymin, 2, 2)
                    return (False)
                ## Aproach from down
                if c.x + (c.w * s * c.s) > xmin and c.x < xmax and c.y > ymax - m and self.player.y < ymax:
                    c.y += b
                    stroke(255,0,0)
                    ellipse(xmin, ymin, 2, 2)
                    return (False)
                ## Aproach from left
                if c.x + (c.w * s * c.s) > xmin and c.x + (c.w * s * c.s) < xmin + 10 and c.y + (c.h * s * c.s) > ymin + 10 and c.y < ymax - 10:
                    c.x -= b
                    stroke(255,0,0)
                    ellipse(xmin, ymin, 2, 2)
                    return (False)
    
        return (True)
    
    def tearCollision(self, tear):
        xtear = tear.x + (16 * s)
        ytear = tear.y + (16 * s)
        c = self.player
        
        for t in self.room.tiles:
            if not t.p:
                xmin = self.room.xmin + (32 * t.c * s)
                xmax = xmin + (32 * s)
                ymin = self.room.ymin + (32 * t.r * s)
                ymax = ymin + (32 * s)
                
            if xtear > xmin and xtear < xmax and ytear > ymin and ytear < ymax:
                    return (True)
        if tear.p == True:
            for e in self.enemies:
                if xtear > e.x and xtear < e.x + (e.w * e.s * s) and ytear > e.y and ytear < e.y + (e.h * e.s * s):
                    e.health -= tear.damg
                    self.deleteTear(tear.id)
        else:
            if xtear > c.x and xtear < c.x + (c.w * c.s * s) and ytear > c.y and ytear < c.y + (c.h * c.s * s):
                c.health -= tear.damg
                self.deleteTear(tear.id)
                print (c.health)
                
                
    
    def playerTears(self):
        
        if self.player.cd == 0:
            if self.keyHandler["shLEFT"]:
                self.tears.append(Tear(self.tearCounter, True, self.player.x, self.player.y, self.player.d, self.player.rang, self.player.shsp, math.pi, "tearsGuidelines.png"))
                self.tearCounter += 1
                self.player.cd = self.player.fr
                self.player.shooting = True
            elif self.keyHandler["shRIGHT"]:
                self.tears.append(Tear(self.tearCounter, True, self.player.x, self.player.y, self.player.d, self.player.rang, self.player.shsp, 0, "tearsGuidelines.png"))
                self.tearCounter += 1
                self.player.cd = self.player.fr
                self.player.shooting = True
            elif self.keyHandler["shUP"]:
                self.tears.append(Tear(self.tearCounter, True, self.player.x, self.player.y, self.player.d, self.player.rang, self.player.shsp, (3*math.pi)/2, "tearsGuidelines.png"))
                self.tearCounter += 1
                self.player.cd = self.player.fr
                self.player.shooting = True
            elif self.keyHandler["shDOWN"]:
                self.tears.append(Tear(self.tearCounter, True, self.player.x, self.player.y, self.player.d, self.player.rang, self.player.shsp, math.pi/2, "tearsGuidelines.png"))
                self.tearCounter += 1
                self.player.cd = self.player.fr
                self.player.shooting = True
            else:
                self.player.display()

    def updateTears(self):
        
        self.tearCounter = self.tearCounter % 256
        
        for t in self.tears:
            if t.trvl >= t.rang: ## Checks for Tear's max range
                self.deleteTear(t.id)
            elif (self.room.xmin - (16 * s)) >= t.x or t.x >= (self.room.xmax - (16 * s)) or (self.room.ymin - (16 * s)) >= t.y or t.y >= (self.room.ymax - (16 * s)):
                self.deleteTear(t.id)
            elif self.tearCollision(t) == True:
                self.deleteTear(t.id)
            else:
                t.update()
                t.display()
    
    def deleteTear(self, id):
        counter = 0
        for t in self.tears:
            if t.id == id:
                del self.tears[counter]
                return (True)
            counter += 1
        return (False)
    
    def deleteEnemy(self, x, y):
        counter = 0
        for e in self.enemies:
            if e.x == x and e.y == y:
                del self.enemies[counter]
                return (True)
            counter += 1
        return (False)


    def enemyMovement(self):
            p = self.player
            for e in self.enemies:
                if e.health <= 0:
                    self.deleteEnemy(e.x, e.y)
                xdel = p.x - e.x
                ydel = p.y - e.y
                theta =  math.atan2(ydel,xdel)
                e.vx = e.ms * cos(theta)
                e.vy = e.ms * sin(theta)
                if e.cd <= 0:
                    self.tears.append(Tear(self.tearCounter, False, e.x, e.y, e.d, e.rang, e.shsp, theta, "tearsGuidelines.png"))
                    self.tearCounter += 1
                    e.cd = e.fr
                e.move()
                e.display()
                
    
################################################


class Creature:
    def __init__(self, x, y, r, img, w, h, s = 1, ms = 4, damg = 3, rang = 300, shSpeed = 6, fireRate = 16):
        self.x = x ## X-Coordinate position in game
        self.y = y ## Y-Coordinate position in game
        self.health = 10
        self.r = r ## Radius of Creature (used for collision detection)
        self.img = loadImage(path+"/images/sprites/"+img) ## Sprite image loading
        self.f = 0 ## current frame
        self.w = w ## native width of creature
        self.h = h ## native height of creature
        self.s = s ## size multiplier of creature
        self.vx = 0 # Speed on X axis
        self.vy = 0 # Speed on Y axis
        self.ms = ms # Movement Speed
        self.d = damg # Damage
        self.rang  = rang # Range
        self.shsp = shSpeed # Speed of projectile
        self.fr = fireRate # shots per minute
        self.cd = 0 ## Cooldown until next projectile can be shot. Related to Fire Rate
        self.dir = "D"  # Direction Creature is looking
        self.shooting = False # Bool if Shooting

## Controls Displaying Creature

    def display(self):
        
        self.update()
    
    ## Point
        stroke(255)
        ellipse(self.x, self.y, 1 , 1)
    
    ## Leg Movement Control    
        if self.vx != 0 or self.vy != 0:
            self.f = (self.f + 0.2) % 10 # The 10 is from there being 10 frames in sprite animation
        else:
            self.f = 0
            
        if math.fabs(self.vy) >= math.fabs(self.vx):
            image(self.img, self.x, self.y + (20 * self.s * s), 28 * s * self.s, 15 * s * self.s, 14 + (32 * int(self.f)), 80, 42 +(32 * int(self.f)), 95) ## Vertical Movement
        elif self.vx > 0:
            image(self.img, self.x, self.y + (20 * self.s * s), 28 * s * self.s, 15 * s * self.s, 14 + (32 * int(self.f)), 123, 42 +(32 * int(self.f)), 138) ## Horizontal Movement
        else:
            image(self.img, self.x, self.y + (20 * self.s * s), 28 * s * self.s, 15 * s * self.s, 42 + (32 * int(self.f)), 123, 14 +(32 * int(self.f)), 138) ## Horizontal Movement
            
        
    ## Head Movement Control
        if self.dir == "D":
            if not self.shooting:
                image(self.img, self.x, self.y, 28 * s * self.s, 26 * s * self.s, 14, 25, 42, 51) ## HEAD
            else:
                image(self.img, self.x, self.y, 28 * s * self.s, 26 * s * self.s, 54, 25, 82, 51)
        elif self.dir == "R":
            if not self.shooting:
                image(self.img, self.x, self.y, 28 * s * self.s, 26 * s * self.s, 94, 25, 122, 51) ## HEAD
            else:
                image(self.img, self.x, self.y, 28 * s * self.s, 26 * s * self.s, 134, 25, 162, 51)
        elif self.dir == "U":
            if not self.shooting:
                image(self.img, self.x, self.y, 28 * s * self.s, 26 * s * self.s, 174, 25, 202, 51) ## HEAD
            else:
                image(self.img, self.x, self.y, 28 * s * self.s, 26 * s * self.s, 214, 25, 242, 51)
        elif self.dir == "L":
            if not self.shooting:
                image(self.img, self.x, self.y, 28 * s * self.s, 26 * s * self.s, 254, 25, 282, 51) ## HEAD
            else:
                image(self.img, self.x, self.y, 28 * s * self.s, 26 * s * self.s, 294, 25, 322, 51)
        
    def update(self):
    
        
    ## Update Shooting Cooldwon
        if self.cd > 0:
            self.cd -= 0.3
            
            ## Update Shooting Booleon for Displaying
            if self.cd < (self.fr - 3):
                self.shooting = False
        elif self.cd < 0:
            self.cd = 0
    
        
    def move(self):
        
    ### Movement Input
            
        self.x += self.vx
        self.y += self.vy
        

################################################

class Tear:
    def __init__(self, ID, player, x, y, damage, rang, speed, theta, img):
        self.id = ID         ### Tear ID
        self.p = player      ### Booleon if player's tear
        self.x = x           ### x position
        self.y = y           ### y position
        self.damg = damage   ### Damage if tear hits
        self.rang = rang     ### Range of the tear
        self.trvl = 0        ### How far has the tear traveled
        self.sp = speed      ### Speed of Tear
        self.t = theta       ### Direction of the tear. Theta is defined same as radians
        self.img = loadImage(path+"/images/sprites/tears/"+img)
        self.s = int(damage / 0.8) ### Determines the size of sprite displayed. Number determines how it scales with damage
            
    
    def update(self):
        self.move()
        
    def move(self):
        self.x = self.x + (self.sp * math.cos(self.t))
        self.y = self.y + (self.sp * math.sin(self.t)) ### This is a subtractiom because our y axis increases as we go down the screen
        self.trvl += self.sp
        
    def display(self):
        image(self.img, self.x, self.y, 32 * s, 32 * s, 32 * (self.s - 1), 0, 32 * self.s, 32)
        

################################################


class Player(Creature):
    def __init__(self,x,y,r,img,w,h,s = 1):
        Creature.__init__(self,x,y,r,img,w,h,s)
        self.health = 20
        self.immune = False
        self.fr = 8
        self.ms = 5


################################################


class Room:
    def __init__(self, img, xmin, ymin, w, h):
        self.w = w
        self.h = h
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = self.xmin + self.w
        self.ymax = self.ymin + self.h
        self.img = loadImage(path+"/images/rooms/"+img) ## Sprite image loading
        self.tiles = [Tile("obstacle.png", 6, 6, False, False), Tile("obstacle.png", 4, 6, False, False), Tile("obstacle.png", 4, 4, False, False), Tile("obstacle.png", 6, 4, False, False)]
        
    def displayRoom(self):
        image(self.img,0,0)
        self.displayTiles()
        
    def displayTiles(self):
        for t in self.tiles:
            image(t.img, self.xmin + (32 * t.c * s), self.ymin + (32 * t.r * s), 32 * s, 32 * s)
        
###############################################

class Tile:
    def __init__(self, img, r, c, Passable, Hurt): 
        self.r = r # Row: Counted from 0 - 19
        self.c = c # Column: Counted 0 - 29
        self.img = loadImage(path+"/images/tiles/"+img) ## Sprite image loading
        self.p = Passable # Boolean if obstacle
        self.h = Hurt #If inflicts damage on whatever passes over it


###############################################

class Enemy(Creature):
    def _init_ (self, x, y, r,img, w, h, s = 1, ms = 3, damg = 1, rang = 300, shSpeed = 6, fireRate = 16):
        Creature.__init__(self,x,y,r,img,w,h,s, ms, damg, rang, shSpeed, fireRate)        ### Initialization variables ###
        self.h = 28
    
    def display(self):
        self.update()
    
    ## Point
        stroke(255)
        ellipse(self.x, self.y, 1 , 1)
    
    
    ## Head Movement Control
        if self.dir == "D":
            image(self.img, self.x, self.y, 28 * s * self.s, 26 * s * self.s, 14, 25, 42, 51) ## HEAD
        elif self.dir == "R":
            image(self.img, self.x, self.y, 28 * s * self.s, 26 * s * self.s, 94, 25, 122, 51) ## HEAD
        elif self.dir == "U":
            image(self.img, self.x, self.y, 28 * s * self.s, 26 * s * self.s, 174, 25, 202, 51) ## HEAD
        elif self.dir == "L":
            image(self.img, self.x, self.y, 28 * s * self.s, 26 * s * self.s, 254, 25, 282, 51) ## HEAD


class Item:
    def __init__(self,img,x,y,attributeMod,modVal):
        self.img = loadImage(path+"/images/items/"+img) ## Sprite image loading
        self.x=x
        self.y=y
        self.attributeMod = attributeMod
        self.modVal = modVal
    
    def display(self):
        self.img = loadImage(path+"/images/items/"+img) ## Sprite image loading
        
game = Game(1152,832)       


        ### Processing Setup and Display ###



def setup():
    size(game.w, game.h)  ## NOTE: For some reason, processing displays at 2x, so we need to keep this considered
    background(0)  ## Real Size: 1690 x 1330 (845 x 665 px)
    
def draw():
    game.display()


       ### INPUT MANAGER ###

def keyPressed():
    if not game.lost:
        if keyCode == 65:                          ### KEY CODE for A
            game.keyHandler["mvLEFT"] = True
        if keyCode == 68:                          ### KEY CODE for D
            game.keyHandler["mvRIGHT"] = True
        if keyCode == 87:                          ### KEY CODE for W
            game.keyHandler["mvUP"] = True
        if keyCode == 83:                          ### KEY CODE for S
            game.keyHandler["mvDOWN"] = True
        if keyCode == UP:                          ### KEY CODE for Arrowkey Up
            game.keyHandler["shUP"] = True
            game.player.dir = "U"
        if keyCode == DOWN:                          ### KEY CODE for Arrowkey Down
            game.keyHandler["shDOWN"] = True
            game.player.dir = "D"
        if keyCode == LEFT:                          ### KEY CODE for Arrowkey Left
            game.keyHandler["shLEFT"] = True
            game.player.dir = "L"
        if keyCode == RIGHT:                          ### KEY CODE for Arrowkey Right
            game.keyHandler["shRIGHT"] = True
            game.player.dir = "R"
        
def keyReleased():
    if not game.lost:
        if keyCode == 65:                          ### KEY CODE for A
            game.keyHandler["mvLEFT"] = False
        if keyCode == 68:                          ### KEY CODE for D
            game.keyHandler["mvRIGHT"] = False
        if keyCode == 87:                          ### KEY CODE for W
            game.keyHandler["mvUP"] = False
        if keyCode == 83:                          ### KEY CODE for S
            game.keyHandler["mvDOWN"] = False
        if keyCode == UP:                          ### KEY CODE for Arrowkey Up
            game.keyHandler["shUP"] = False
        if keyCode == DOWN:                          ### KEY CODE for Arrowkey Down
            game.keyHandler["shDOWN"] = False
        if keyCode == LEFT:                          ### KEY CODE for Arrowkey Left
            game.keyHandler["shLEFT"] = False
        if keyCode == RIGHT:                          ### KEY CODE for Arrowkey Right
            game.keyHandler["shRIGHT"] = False

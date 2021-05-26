
#-------------------------------------------------------------------------------
# Author: Mihail Dimitrov
# Created: 15/03/2021
#
# Course: HND Software Development - NESCOL
# Modul: OOP
#
# Tutor: Chrissie Nyssen
#-------------------------------------------------------------------------------


#error handler checking if all class files are loaded
try:
    #imports the classes
    from field import Field
    from player import Player
    from seekers import Seeker
    from snitch import Snitch
    from sounds import Sound
except:
  print("Missing Class file or files")


#import the dependancies 
import sys, pygame
import random
from pygame.locals import *
from pygame import mixer



field =  Field()
player = Player("^", 4, 1)
snitch = Snitch("@", 3, 1)
seeker1 = Seeker("$", 5, 2)
seeker2 = Seeker("$", 2, 5)


#initialisate the sound efects
pygame.mixer.init()
moveSound = pygame.mixer.Sound('Assets/move.wav')
winSound = pygame.mixer.Sound('Assets/win.wav')
lostSound = pygame.mixer.Sound('Assets/lost.wav')
gameOverSound = pygame.mixer.Sound('Assets/game-over.mp3')

#set up the display requirements and keep them in variables
FPS = 30                    
WINWIDTH = 800              
WINHEIGHT = 600             
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

#set up the size of each tile
TILEWIDTH = 32
TILEHEIGHT = 32
TILEFLOORHEIGHT = 32

#set up the colours and keep them in variables
RED = ( 210, 0 ,0)
WHITE = (255, 255, 255)
BACKGROUNDCOLOR = RED
TEXTCOLOR = WHITE


#call the images and save them in key value object
IMAGESDICT = {'field': pygame.image.load("Assets/field.gif"),
              'edge': pygame.image.load("Assets/edge.png"),
              'snitch': pygame.image.load("Assets/snitch.png"),
              'seeker': pygame.image.load("Assets/seeker.png"),
              'player': pygame.image.load("Assets/player.png")}

TILEMAPPING = { '#':IMAGESDICT['edge'],
                ' ':IMAGESDICT['field'],
                '@':IMAGESDICT['snitch'],
                '^':IMAGESDICT['player'],
                '$':IMAGESDICT['seeker']}

#pygame initialisation and set up

pygame.init()

    
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('Quiddich - Final Version')
BASICFONT = pygame.font.Font('Assets/Passion.ttf', 20)

#declare the game variables and assign the values
curentLevel = 1
curentPointsPlayer = 0
curentPointsSeekers  = 0
movesCounter = 10

#Next 4 functions are responsible for moving the Player on the key pressed event
def moveLeft():
    global curentPointsPlayer
    x = field.getCharAtPos(player.getRow(), player.getCol() - 1)#check the object on the left side of the Player
    if x == "#" or x=="$":# if it is wall or Seeker call the functions which move the Seekers randomly  
        randomObjectMove(seeker1)
        randomObjectMove(seeker2)
        if curentLevel >=2: #if the level is 2 or greater move the Snitch
            randomObjectMove(snitch)
    elif x == "@":#if the object is Snitch add 150 points to the Player result, play sound and go to next level
        curentPointsPlayer += 150
        winSound.play()
        moveLevel()
    else:#if there is no object clear the curent position and move the Player left, move the Seekers and Snitch randomly
        field.clearAtPos(player.getRow(), player.getCol())
        player.moveLeft()
        field.placeObj(player.getChar(), player.getRow(), player.getCol())
        randomObjectMove(seeker1)
        randomObjectMove(seeker2)
        if curentLevel >=2:
            randomObjectMove(snitch)

def moveRight():#same as the MoveRight() function but works for the right side
    global curentPointsPlayer
    x = field.getCharAtPos(player.getRow(), player.getCol() + 1)
    if x == "#" or x=="$":
        randomObjectMove(seeker1)
        randomObjectMove(seeker2)
        if curentLevel >=2:
            randomObjectMove(snitch)
    elif x == "@":
        curentPointsPlayer += 150
        winSound.play()
        moveLevel()
    else:
        field.clearAtPos(player.getRow(), player.getCol())
        player.moveRight()
        field.placeObj(player.getChar(), player.getRow(), player.getCol())
        randomObjectMove(seeker1)
        randomObjectMove(seeker2)
        if curentLevel >=2:
            randomObjectMove(snitch)

def moveUp():#same as the MoveRight() function but works for the upper side
    global curentPointsPlayer
    x = field.getCharAtPos(player.getRow()-1, player.getCol())
    if x == "#" or x=="$":
        randomObjectMove(seeker1)
        randomObjectMove(seeker2)
        if curentLevel >=2:
            randomObjectMove(snitch)
    elif x == "@":
        curentPointsPlayer += 150
        winSound.play()
        moveLevel()
    else:
        field.clearAtPos(player.getRow(), player.getCol())
        player.moveUp()
        field.placeObj(player.getChar(), player.getRow(), player.getCol())
        randomObjectMove(seeker1)
        randomObjectMove(seeker2)
        if curentLevel >=2:
            randomObjectMove(snitch)

def moveDown():#same as the MoveRight() function but works for the bottom side
    global curentPointsPlayer
    x = field.getCharAtPos(player.getRow()+1, player.getCol())
    if x == "#" or x=="$":
        randomObjectMove(seeker1)
        randomObjectMove(seeker2)
        if curentLevel >=2:
            randomObjectMove(snitch)
    elif x == "@":
        curentPointsPlayer += 150
        winSound.play()
        moveLevel()
    else:
        field.clearAtPos(player.getRow(), player.getCol())
        player.moveDown()
        field.placeObj(player.getChar(), player.getRow(), player.getCol())
        randomObjectMove(seeker1)
        randomObjectMove(seeker2)
        if curentLevel >=2:
            randomObjectMove(snitch)
        
#function takes objects as a property (Snitch or Seekers) responsible for moving them. Identical with the upper 4 functions
def randomObjectMove(obj):
    global curentPointsSeekers
    randomMove = random.randint(1, 4)#generate random number from 1 to 4 which corespondent to left, right, up, down
    y = " "
    
    if randomMove == 1:
        y = field.getCharAtPos(obj.getRow(), obj.getCol()-1)
        if y == "#" or y == "$" or y=="^":
            pass
        elif y == "@":
            curentPointsSeekers +=150
            lostSound.play()
            moveLevel()
        else:
            field.clearAtPos(obj.getRow(), obj.getCol())
            obj.moveLeft()
            field.placeObj(obj.getChar(), obj.getRow(), obj.getCol())
    elif randomMove == 2:
        y = field.getCharAtPos(obj.getRow(), obj.getCol()+1)
        if y == "#" or y == "$" or y=="^":
            pass
        elif y == "@":
            curentPointsSeekers +=150
            lostSound.play()
            moveLevel()
        else:
            field.clearAtPos(obj.getRow(), obj.getCol())
            obj.moveRight()
            field.placeObj(obj.getChar(), obj.getRow(), obj.getCol())
    elif randomMove == 3:
        y = field.getCharAtPos(obj.getRow()-1, obj.getCol())
        if y == "#" or y == "$" or y=="^":
            pass
        elif y == "@":
            curentPointsSeekers +=150
            lostSound.play()
            moveLevel()
        else:
            field.clearAtPos(obj.getRow(), obj.getCol())
            obj.moveUp()
            field.placeObj(obj.getChar(), obj.getRow(), obj.getCol())
    elif randomMove == 4:
        y = field.getCharAtPos(obj.getRow()+1, obj.getCol())
        if y == "#" or y == "$" or y=="^":
            pass
        elif y == "@":
            curentPointsSeekers +=150
            lostSound.play()
            moveLevel()
        else:
            field.clearAtPos(obj.getRow(), obj.getCol())
            obj.moveDown()
            field.placeObj(obj.getChar(), obj.getRow(), obj.getCol())
                



#function responsible for moving between levels. On call move to the next level depends on the curent level, reset the movesCounter, place the objects on the field
def moveLevel():
    global curentLevel, movesCounter
    if curentLevel == 1:
        field.goToLevel2()
        movesCounter = 10
        startPositions()
        curentLevel = 2
    elif curentLevel == 2:
        field.goToLevel3()
        movesCounter = 10
        startPositions()
        curentLevel = 3
    elif curentLevel == 3:
        field.goToLevel4()
        movesCounter = 10
        startPositions()
        curentLevel = 4
    elif curentLevel == 4:
        field.goToLevel5()
        movesCounter = 10
        startPositions()
        curentLevel = 5
    elif curentLevel == 5:#last level
        field.gameOver()
        curentLevel = 0
    

#function responsible for positioning the objects at the beginning of each level
def startPositions():
    player.setRow(4)
    player.setCol(1)
    field.placeObj("^",4,1) #player
    seeker1.setRow(5)
    seeker1.setCol(2)
    field.placeObj('$', 5,2) #seeker1
    seeker2.setRow(2)
    seeker2.setCol(5)
    field.placeObj('$', 2,5) #seeker2
    snitch.setRow(1)
    snitch.setCol(3)
    field.placeObj ('@',1,3) #snitch



#main function
def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, BASICFONT, curentLevel, movesCounter

    startPositions()
    
    drawMap(field)
    
    while True:#
        
        for event in pygame.event.get(): #loop which listen for the key pressed 
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    if movesCounter !=0:
                        movesCounter -=1
                    if curentLevel != 0 and movesCounter !=0:
                        moveRight()
                        moveSound.play()
                    else:
                        curentLevel = 0
                        gameOverSound.play()
                        field.gameOver()
                elif event.key == K_UP:
                    if movesCounter !=0:
                        movesCounter -=1
                    if curentLevel != 0 and movesCounter !=0:
                        moveUp()
                        moveSound.play()
                    else:
                        curentLevel = 0
                        gameOverSound.play()
                        field.gameOver()
                elif event.key == K_LEFT:
                    if movesCounter !=0:
                        movesCounter -=1
                    if curentLevel != 0 and movesCounter !=0: 
                        moveLeft()
                        moveSound.play()
                    else:
                        curentLevel = 0
                        gameOverSound.play()
                        field.gameOver()
                elif event.key == K_DOWN:
                    if movesCounter !=0:
                        movesCounter -=1
                    if curentLevel != 0 and movesCounter !=0:
                        moveDown()
                        moveSound.play()
                    else:
                        curentLevel = 0
                        gameOverSound.play()
                        field.gameOver()
                elif event.key == K_SPACE:
                    field.goToLevel1()
                    movesCounter = 10
                    startPositions()
                    curentLevel = 1
                else:
                    pass
            mapNeedsRedraw = True


        #set up the display 
        DISPLAYSURF.fill(BACKGROUNDCOLOR)
        if mapNeedsRedraw:
            mapSurf = drawMap(field)
            mapNeedsRedraw = False

        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)


        #display the text on the screen
        messageSurf = BASICFONT.render('Current level: %s' % curentLevel, True, TEXTCOLOR)
        messageRect = messageSurf.get_rect()
        messageRect.topleft = (20, 30)
        DISPLAYSURF.blit(messageSurf, messageRect)

        messageSurf = BASICFONT.render('Player points: %s' % curentPointsPlayer, True, TEXTCOLOR)
        messageRect = messageSurf.get_rect()
        messageRect.topleft = (20, 60)
        DISPLAYSURF.blit(messageSurf, messageRect)

        messageSurf = BASICFONT.render('Seekers points: %s' % curentPointsSeekers, True, TEXTCOLOR)
        messageRect = messageSurf.get_rect()
        messageRect.topleft = (20, 90)
        DISPLAYSURF.blit(messageSurf, messageRect)

        messageSurf = BASICFONT.render('Moves left: %s' % movesCounter, True, TEXTCOLOR)
        messageRect = messageSurf.get_rect()
        messageRect.topleft = (20, 120)
        DISPLAYSURF.blit(messageSurf, messageRect)

        if curentLevel == 0:
            messageSurf = BASICFONT.render('GAME OVER! Press SPACE for the begining', True, TEXTCOLOR)
            messageRect = messageSurf.get_rect()
            messageRect.topleft = (230, 60)
            DISPLAYSURF.blit(messageSurf, messageRect)
            
        else:
            messageSurf = BASICFONT.render('Press SPACE to start from Level 1', True, TEXTCOLOR)
            messageRect = messageSurf.get_rect()
            messageRect.topleft = (260, 500)
            DISPLAYSURF.blit(messageSurf, messageRect)

        DISPLAYSURF.blit(mapSurf, mapSurfRect)

        pygame.display.update()
        FPSCLOCK.tick()



#function which creates the displays and matches the tiles
def drawMap(field):
    mapSurfWidth = field.getWidth() * TILEWIDTH
    mapSurfHeight = field.getHeight() * TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BACKGROUNDCOLOR)
    for h in range(field.getHeight()):
        for w in range(field.getWidth()):
            thisTile = pygame.Rect((w * TILEWIDTH, h * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            if field.getCharAtPos(h, w) in TILEMAPPING:

                baseTile = TILEMAPPING[field.getCharAtPos(h,w)]

            mapSurf.blit(baseTile, thisTile)
    return mapSurf



#function which qiuts the game
def terminate():
    pygame.quit()
    sys.exit()



if __name__ == '__main__':
    main()

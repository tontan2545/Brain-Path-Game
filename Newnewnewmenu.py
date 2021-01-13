import pygame
import os
import sys
from pygame.locals import *
from random import*
from Level_Path import*

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Brain Path")

#colors
lime = (50,205,50)
seagreen = (46,139,87)
black = (0,0,0)
white = (255,255,255)
Black = (0,0,0)
White = (255,255,255)
pink = (153,0,153)
red = (255,0,0)
dark_green = (0,51,0)
grey = (160,160,160)
verylightpink = (255,192,203)
lightpink = (255,105,180)
darkpink = (199,21,133)
somewhatdarkpink = (255,20,147)

# IMAGE SIZE
twoXtwo = 300
threeXthree = 200

blockWidth = twoXtwo
blockHeight = twoXtwo

blockWidth3 = threeXthree
blockHeight3 = threeXthree

#---------Map-For-2x2-------------------------------------------
                     
# Block 1 2x2 
path = os.path.join("Map2x2/B1.png")
Bim1 = pygame.image.load( path )
Bim1 = pygame.transform.scale(Bim1, (twoXtwo,twoXtwo))

# Block 2 2x2 
path = os.path.join("Map2x2/B2.png")
Bim2 = pygame.image.load( path )
Bim2 = pygame.transform.scale(Bim2, (twoXtwo,twoXtwo))

# Block 3 2x2 
path = os.path.join("Map2x2/B3.png")
Bim3 = pygame.image.load( path )
Bim3 = pygame.transform.scale(Bim3, (twoXtwo,twoXtwo))

# ARROW/PLAYER 
path = os.path.join("Map2x2/arrow.png")
Aim1 = pygame.image.load( path )
Aim1 = pygame.transform.scale(Aim1, (twoXtwo,twoXtwo))

# Row And Column
blueAtRow = 0
blueAtColumn = 0

arrowAtRow = -1
arrowAtColumn = -1

# Level Data
currentLevel = 0
LevelData = LevelDataList [currentLevel]

NextLevel = False
#----------------------UI/Backgrounds-----------------------------------

#backgroundmenu
path = os.path.join("picture","menu.png")
menupic = pygame.image.load(path)
menupic = pygame.transform.scale(menupic,(1024,768))

#gamebackground
bpath = os.path.join("picture", "brains.png")
brainpic = pygame.image.load(bpath)
brainpic = pygame.transform.scale(brainpic, (1024,768))
#------------------------UI/Texts--------------------------------------

#title
fontObj = pygame.font.Font("zombiecontrol.ttf",150)
gameTitle = fontObj.render("BrainPath",True, lightpink)
titleRect = gameTitle.get_rect()
titleRect.center = (512, 200)

#titleshading
fontObj = pygame.font.Font("zombiecontrol.ttf",150)
gameTitleshade = fontObj.render("BrainPath",True, pink)
titleRectshade = gameTitleshade.get_rect()
titleRectshade.center = (517, 205)

#start button
fontObj = pygame.font.Font("zombiecontrol.ttf",64)
startText = fontObj.render("Start",True, white)
startRect = startText.get_rect()
startRect.center = (512, 420)

#start button shade
fontObj = pygame.font.Font("zombiecontrol.ttf",64)
startTextshade = fontObj.render("Start",True, somewhatdarkpink)
startRectshade = startTextshade.get_rect()
startRectshade.center = (517, 425)

#exit button
fontObj = pygame.font.Font("zombiecontrol.ttf",64)
exitText = fontObj.render("Exit",True, white)
exitRect = exitText.get_rect()
exitRect.center = (512, 570)
#exit button shade
fontObj = pygame.font.Font("zombiecontrol.ttf",64)
exitTextshade = fontObj.render("Exit",True, white)
exitRectshade = exitTextshade.get_rect()
exitRectshade.center = (517, 575) 
sceneNumber = 0
#Hunger
fontObj2 = pygame.font.Font("zombiecontrol.ttf", 32)
hungerText = fontObj2.render("Hunger", True, white)
hungerRect = hungerText.get_rect()
hungerRect.center = (135,46)
#P
wayObj = pygame.font.Font("zombiecontrol.ttf", 100)
wayText = wayObj.render("P", True, white)
wayRect = wayText.get_rect()
wayRect.center = (106,360)
#Z
zombObj = pygame.font.Font("zombiecontrol.ttf", 100)
zombText = zombObj.render("Z", True, white)
zombRect = zombText.get_rect()
zombRect.center = (918,360)
#tutorialorno
tutObj = pygame.font.Font("zombiecontrol.ttf", 55)
tutText = tutObj.render("Do you want to play the tutorial?", True, lightpink)
tutRect = tutText.get_rect()
tutRect.center = (512,300)
#tutorialornoshade
tutshadeObj = pygame.font.Font("zombiecontrol.ttf", 55)
tutshadeText = tutshadeObj.render("Do you want to play the tutorial?", True, pink)
tutshadeRect = tutshadeText.get_rect()
tutshadeRect.center = (517,305)
#yes
yesObj = pygame.font.Font("zombiecontrol.ttf", 50)
yesText = yesObj.render("Yes", True, white)
yesRect = yesText.get_rect()
yesRect.center = (270,420)
#yesshade
yesshadeObj = pygame.font.Font("zombiecontrol.ttf", 50)
yesshadeText = yesshadeObj.render("Yes", True,somewhatdarkpink)
yesshadeRect = yesshadeText.get_rect()
yesshadeRect.center = (275,425)
#noshade
noshadeObj = pygame.font.Font("zombiecontrol.ttf", 50)
noshadeText = noshadeObj.render("No", True, somewhatdarkpink)
noshadeRect = noshadeText.get_rect()
noshadeRect.center = (735,425)
#no
noObj = pygame.font.Font("zombiecontrol.ttf", 50)
noText = noObj.render("No", True, white)
noRect = noText.get_rect()
noRect.center = (730,420)
#pmode1
p1Obj = pygame.font.Font("zombiecontrol.ttf", 70)
p1Text = p1Obj.render('"P" is path mode', True, lightpink)
p1Rect = p1Text.get_rect()
p1Rect.center = (492,360)
#pmode1shade
p1shadeObj = pygame.font.Font("zombiecontrol.ttf", 70)
p1shadeText = p1shadeObj.render('"P" is path mode', True, pink)
p1shadeRect = p1shadeText.get_rect()
p1shadeRect.center = (492,360)
#pmode2
p2Obj = pygame.font.Font("zombiecontrol.ttf", 30)
p2Text = p2Obj.render("you will move the path using this mode", True, lightpink)
p2Rect = p2Text.get_rect()
p2Rect.center = (492,360)
#zmode
zObj = pygame.font.Font("zombiecontrol.ttf", 70)
zText = zObj.render('"Z" is zombie mode', True, lightpink)
zRect = zText.get_rect()
zRect.center = (492,360)
#zmodeshade
zshadeObj = pygame.font.Font("zombiecontrol.ttf", 70)
zshadeText = zshadeObj.render('"Z" is zombie mode', True, pink)
zshadeRect = zshadeText.get_rect()
zshadeRect.center = (492,360)
#zmode2
z2Obj = pygame.font.Font("zombiecontrol.ttf", 25)
z2Text = z2Obj.render("you will control the zombie body using this mode", True, lightpink)
z2Rect = z2Text.get_rect()
z2Rect.center = (492,360)
#wtxt
wObj = pygame.font.Font("zombiecontrol.ttf", 25)
wText = wObj.render("W - Up", True, lightpink)
wRect = wText.get_rect()
#atxt
aObj = pygame.font.Font("zombiecontrol.ttf", 25)
aText = aObj.render("A - Left", True, lightpink)
aRect = aText.get_rect()
#stxt
sObj = pygame.font.Font("zombiecontrol.ttf", 25)
sText = sObj.render("S - Down", True, lightpink)
sRect = sText.get_rect()
#dtxt
dObj = pygame.font.Font("zombiecontrol.ttf", 25)
dText = dObj.render("D - Right", True, lightpink)
dRect = dText.get_rect()
#qtxt
qObj = pygame.font.Font("zombiecontrol.ttf", 25)
qText = qObj.render("Q - switch between modes", True, lightpink)
qRect = qText.get_rect()
#KEYS
kObj = pygame.font.Font("zombiecontrol.ttf", 150)
kText = kObj.render("Controls", True, lightpink)
kRect = kText.get_rect()
#keysshade
kshadeObj = pygame.font.Font("zombiecontrol.ttf", 150)
kshadeText = kshadeObj.render("Controls", True, pink)
kshadeRect = kshadeText.get_rect()
#objective
oObj = pygame.font.Font("zombiecontrol.ttf", 30)
oText = oObj.render("Your objective is to led the zombie before he hungers to death", True, lightpink)
oRect = oText.get_rect()
#ready
readyObj = pygame.font.Font("zombiecontrol.ttf",80)
readyText = readyObj.render("Are you ready?", True, lightpink)
readyRect = readyText.get_rect()
#readyshade
readyshadeObj = pygame.font.Font("zombiecontrol.ttf",80)
readyshadeText = readyshadeObj.render("Are you ready?", True, pink)
readyshadeRect = readyshadeText.get_rect()
#play
playObj = pygame.font.Font("zombiecontrol.ttf",70)
playText = playObj.render("Yes", True, white)
playRect = playText.get_rect()
#playshade
playshadeObj = pygame.font.Font("zombiecontrol.ttf",70)
playshadeText = playshadeObj.render("Yes", True, somewhatdarkpink)
playshadeRect = playshadeText.get_rect()
#3
_3Obj = pygame.font.Font("zombiecontrol.ttf",128)
_3Text = _3Obj.render("3", True, white)
_3Rect = _3Text.get_rect()
#------------------------------UI/Var-----------------------------------------
gamestart = False
isholdstartbutton = False
tutorialstep = 1
positionxh = 210
path = True
zombie = False
hunger1 = 600
timecounter = 0
finTutorial = False
px = 106
py = 360
ptx = 512
p1ty = 300
p2ty = 400
zx = 918
zy = 360
ztx = 512
z1ty = 300
z2ty = 400
controlx = 512
controly = 350
objectivex = 512
objectivey = 384
playx = 512
playy = 300
gameEnd = False
numx = 512
numy = 384
timer = 0

playButton = 0

#main loop
while True:

    if sceneNumber == 0:
        gameDisplay.blit(menupic,(0,0))
        gameDisplay.blit(gameTitleshade, titleRectshade)
        gameDisplay.blit(gameTitle, titleRect)
        gameDisplay.blit(startTextshade, startRectshade)
        startButton = pygame.Rect(426,392,158,57)
        gameDisplay.blit(startText, startRect)
        gameDisplay.blit(exitTextshade, exitRectshade)
        gameDisplay.blit(exitText, exitRect)
        exitButton = pygame.Rect(453,543,158,57)
        pygame.display.update()

        mousePos = pygame.mouse.get_pos()
        if startButton.collidepoint(mousePos) == True:
            startText = fontObj.render("Start",True, verylightpink)
            startTextshade = fontObj.render("Start",True, somewhatdarkpink)
        elif exitButton.collidepoint(mousePos) == True:
            exitText = fontObj.render("Exit",True, verylightpink)
            exitTextshade = fontObj.render("Exit",True, somewhatdarkpink)
        else:
            startText = fontObj.render("Start",True, white)
            startTextshade = fontObj.render("Start",True, somewhatdarkpink)
            exitText = fontObj.render("Exit",True, white)
            exitTextshade = fontObj.render("Exit",True, somewhatdarkpink)
            
        #events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    if exitButton.collidepoint(mousePos) == True:
                        exitText = fontObj.render("Exit",True, pink)
                        exitTextshade = fontObj.render("Exit",True, seagreen)
                    if startButton.collidepoint(mousePos) == True:
                        startText = fontObj.render("Start",True, pink)
                        startTextshade = fontObj.render("Start",True, white)
            if event.type == MOUSEBUTTONUP:
                exitText = fontObj.render("Exit",True, white)
                startText = fontObj.render("Start",True, white)
                if event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    print(mousePos)
                    if startButton.collidepoint(mousePos) == True:
                        print("start")
                        sceneNumber +=1
                    if exitButton.collidepoint(mousePos) == True:
                        pygame.quit()
                        sys.exit()
    #tutorial game
    if sceneNumber == 1:
        gameDisplay.blit(brainpic,(0,0))
        pygame.draw.rect(gameDisplay, white, (212,84,600,600))
        if finTutorial == True:
            timecounter +=1            
            if timecounter >= 1:
                if hunger1 > 0:
                    hunger1 -= (600.0/(50.0*60))
                    timecounter = 0
                    positionxh = 210
        if hunger1 <= 0:
            positionxh = 2000
        if hunger1 >= 150:    
            pygame.draw.rect(gameDisplay, lime, (positionxh,30,hunger1,30))
            hungerText = fontObj2.render("Hunger", True, lime)
            gameDisplay.blit(hungerText, hungerRect)
        else:
            pygame.draw.rect(gameDisplay, red, (positionxh,30,hunger1,30))
            hungerText = fontObj2.render("Hunger", True, red)
            gameDisplay.blit(hungerText, hungerRect)
        if (path == True) and (zombie == False):
            pygame.draw.circle(gameDisplay, lightpink, (106,360), 80,0)
            wayText = wayObj.render("P", True, white)
            gameDisplay.blit(wayText, wayRect)
            pygame.draw.circle(gameDisplay, darkpink, (918,360), 80,0)
            gameDisplay.blit(zombText, zombRect)
            zombText = zombObj.render("Z", True, grey)
        elif (path == False) and (zombie == True):
            pygame.draw.circle(gameDisplay, darkpink, (106,360), 80,0)
            wayText = wayObj.render("P", True, grey)
            gameDisplay.blit(wayText, wayRect)
            pygame.draw.circle(gameDisplay, lightpink, (918,360), 80,0)
            gameDisplay.blit(zombText, zombRect)
            zombText = zombObj.render("Z", True, white)
        overlay = pygame.Surface((1024,768), pygame.SRCALPHA)
        overlay.fill((0,0,0,220))
        gameDisplay.blit(overlay, (0,0))
        gameDisplay.blit(tutshadeText,tutshadeRect)        
        gameDisplay.blit(tutText,tutRect)
        gameDisplay.blit(yesshadeText,yesshadeRect)
        gameDisplay.blit(yesText,yesRect)
        #yesbutton
        yesButton = pygame.Rect(225,390,90,55)
        #nobutton
        noButton = pygame.Rect(700,395,58,45)
        gameDisplay.blit(noshadeText,noshadeRect)
        gameDisplay.blit(noText,noRect)
        mousePos = pygame.mouse.get_pos()
        if yesButton.collidepoint(mousePos) == True:
            yesText = yesObj.render("Yes",True, verylightpink)
            yesshadeText = yesObj.render("Yes",True, somewhatdarkpink)
        elif noButton.collidepoint(mousePos) == True:
            noText = noObj.render("no",True, verylightpink)
            noshadeText = noObj.render("no",True, somewhatdarkpink)    
        else:
            yesText = yesObj.render("Yes",True,white)
            yesshadeText = yesObj.render("Yes",True,somewhatdarkpink)
            noText = noObj.render("no",True,white)
            noshadeText = noObj.render("no",True,somewhatdarkpink)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if finTutorial == False:
                if event.type == MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    print(mousePos)
                    if yesButton.collidepoint(mousePos) == True:
                        print("Start Tutorial")
                        sceneNumber += 1
                    elif noButton.collidepoint(mousePos) == True:
                        print("Start game right away")
                        sceneNumber += 2
            if finTutorial == True:
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        if (path == True) and (zombie == False):
                            path = False
                            zombie = True
                        elif (path == False) and (zombie == True):
                            path = True
                            zombie = False
                elif event.type == MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    print(mousePos)
    #tutorial                
    if sceneNumber == 2:
        gameDisplay.blit(brainpic,(0,0))
        pygame.draw.rect(gameDisplay, white, (212,84,600,600))
        timecounter +=1            
        if timecounter >= 1:
            if hunger1 > 0:
                hunger1 -= (600.0/(50.0*60))
                timecounter = 0
            positionxh = 210
            if hunger1 <= 0:
                positionxh = 2000
            if hunger1 >= 150:    
                pygame.draw.rect(gameDisplay, lime, (positionxh,30,hunger1,30))
                hungerText = fontObj2.render("Hunger", True, lime)
                gameDisplay.blit(hungerText, hungerRect)
            else:
                pygame.draw.rect(gameDisplay, red, (positionxh,30,hunger1,30))
                hungerText = fontObj2.render("Hunger", True, red)
                gameDisplay.blit(hungerText, hungerRect)
        if (path == True) and (zombie == False):
            pygame.draw.circle(gameDisplay, lightpink, (106,360), 80,0)
            wayText = wayObj.render("P", True, white)
            gameDisplay.blit(wayText, wayRect)
            pygame.draw.circle(gameDisplay, darkpink, (918,360), 80,0)
            gameDisplay.blit(zombText, zombRect)
            zombText = zombObj.render("Z", True, grey)
        elif (path == False) and (zombie == True):
            pygame.draw.circle(gameDisplay, darkpink, (106,360), 80,0)
            wayText = wayObj.render("P", True, grey)
            gameDisplay.blit(wayText, wayRect)
            pygame.draw.circle(gameDisplay, lightpink, (918,360), 80,0)
            gameDisplay.blit(zombText, zombRect)
            zombText = zombObj.render("Z", True, white)
        #Overlay    
        overlay = pygame.Surface((1024,768), pygame.SRCALPHA)
        overlay.fill((0,0,0,220))
        gameDisplay.blit(overlay, (0,0))
        if tutorialstep == 1:
            pygame.draw.circle(gameDisplay, lightpink, (px,py), 80,0)
            wayText = wayObj.render("P", True, white)
            gameDisplay.blit(wayText, wayRect)
            p1Rect.center = (ptx,p1ty)
            p1shadeRect.center = (ptx+5,p1ty+5)
            gameDisplay.blit(p1shadeText,p1shadeRect)
            gameDisplay.blit(p1Text, p1Rect)
            p2Rect.center = (ptx,p2ty)
            gameDisplay.blit(p2Text, p2Rect)
        if tutorialstep == 2:
            px = 2000
            py = 2000
            ptx = 2000
            pygame.draw.circle(gameDisplay, lightpink, (zx,zy), 80,0)
            zombText = zombObj.render("Z", True, white)
            gameDisplay.blit(zombText, zombRect)
            zshadeRect.center = (ztx+5,z1ty+5)
            gameDisplay.blit(zshadeText,zshadeRect)
            zRect.center = (ztx,z1ty)
            gameDisplay.blit(zText,zRect)
            z2Rect.center = (ztx,z2ty)
            gameDisplay.blit(z2Text,z2Rect)
        if tutorialstep == 3:
            zx = 2000
            zy = 2000
            ztx = 2000
            kRect.center = (controlx + 5, controly -120)
            kRect.center = (controlx,controly-125)
            gameDisplay.blit(kText,kRect)
            wRect.center = (controlx,controly+25)
            gameDisplay.blit(wText,wRect)
            aRect.center = (controlx,controly+75)
            gameDisplay.blit(aText,aRect)
            sRect.center = (controlx,controly+125)
            gameDisplay.blit(sText,sRect)
            dRect.center = (controlx,controly+175)
            gameDisplay.blit(dText,dRect)
            qRect.center = (controlx,controly+225)
            gameDisplay.blit(qText,qRect)
        if tutorialstep == 4:
            controlx = 2000
            oRect.center = (objectivex,objectivey)
            gameDisplay.blit(oText,oRect)
        if tutorialstep == 5:
            objectivex = 2000
            gameDisplay.blit(readyshadeText,readyshadeRect)
            gameDisplay.blit(readyText,readyRect)
            readyshadeRect.center = (playx+5,playy+5)
            readyRect.center = (playx,playy)
            playshadeRect.center = (playx+5, playy +155)
            gameDisplay.blit(playshadeText,playshadeRect)
            playRect.center = (playx, playy +150)
            gameDisplay.blit(playText,playRect)
            playButton = pygame.Rect(449,416,123,74)
            
            
            
        pygame.display.update()    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_q:
                    if (path == True) and (zombie == False):
                        path = False
                        zombie = True
                    elif (path == False) and (zombie == True):
                        path = True
                        zombie = False
                tutorialstep += 1         
            if event.type == MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                print(mousePos)
                if event.button != 4 and event.button != 5:
                    if tutorialstep < 5:
                        tutorialstep += 1
                        print("Click")
                    elif tutorialstep == 5 and playButton.collidepoint(mousePos) == True:
                        print("Next Game")
                        sceneNumber += 1    
    #first game, template
    if sceneNumber == 3:
        gameDisplay.blit(brainpic,(0,0))
        pygame.draw.rect(gameDisplay, white, (212,84,600,600))
        pygame.draw.circle(gameDisplay, lime, (106,360), 80,0)
        wayText = wayObj.render("P", True, white)
        gameDisplay.blit(wayText, wayRect)
        pygame.draw.circle(gameDisplay, dark_green, (918,360), 80,0)
        gameDisplay.blit(zombText, zombRect)
        zombText = zombObj.render("Z", True, grey)
        print(gamestart)
        if gamestart == False:
            gamestart = True
        if gamestart == True:
#--------------------------Game--------------------------------------------------------------------------        
            for row in range( 0 , 2 , 1 ) :
                for column in range( 0 , 2 , 1 ) :
                    # Draw the game level
                    if LevelData[ row ][ column ] == "B1" :
                        gameDisplay.blit( Bim1, ( (blockWidth * column)+ 212, (blockHeight * row)+84))
                    if LevelData [ row ] [ column ] == "B2":
                        gameDisplay.blit( Bim2, (( blockWidth * column)+ 212, (blockHeight * row)+84))
                    if LevelData[ row ] [ column ] == "B3":
                        gameDisplay.blit(Bim3, ((blockWidth * column) + 212, (blockHeight * row)+84))

                    elif LevelData[ row ][ column ] == "A1" :
                        if arrowAtRow == -1 and arrowAtColumn == -1:
                            arrowAtRow = row
                            arrowAtColumn = column 
                
            gameDisplay.blit( Aim1, ( (blockWidth * arrowAtColumn)+212, (blockHeight * arrowAtRow)+84))
#--------------------------------------------------------------------------------------------------------
            timecounter +=1            
            if timecounter >= 1:
                if hunger1 > 0:
                    hunger1 -= (600.0/(50.0*60))
                    timecounter = 0
                positionxh = 210
                if hunger1 <= 0:
                    positionxh = 2000
                if hunger1 >= 150:    
                    pygame.draw.rect(gameDisplay, lime, (positionxh,30,hunger1,30))
                    hungerText = fontObj2.render("Hunger", True, lime)
                    gameDisplay.blit(hungerText, hungerRect)
                else:
                    pygame.draw.rect(gameDisplay, red, (positionxh,30,hunger1,30))
                    hungerText = fontObj2.render("Hunger", True, red)
                    gameDisplay.blit(hungerText, hungerRect)
            if (path == True) and (zombie == False):
                pygame.draw.circle(gameDisplay, lime, (106,360), 80,0)
                wayText = wayObj.render("P", True, white)
                gameDisplay.blit(wayText, wayRect)
                pygame.draw.circle(gameDisplay, dark_green, (918,360), 80,0)
                gameDisplay.blit(zombText, zombRect)
                zombText = zombObj.render("Z", True, grey)
            elif (path == False) and (zombie == True):
                pygame.draw.circle(gameDisplay, dark_green, (106,360), 80,0)
                wayText = wayObj.render("P", True, grey)
                gameDisplay.blit(wayText, wayRect)
                pygame.draw.circle(gameDisplay, lime, (918,360), 80,0)
                gameDisplay.blit(zombText, zombRect)
                zombText = zombObj.render("Z", True, white)
        pygame.display.update()    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
#-------------------------------------------------------------------------------------------
                if gameEnd == False:     
                    if path == True:
                        if event.key == K_q:
                                path = False
                                zombie = True

                        if event.key == K_w:        
                            if arrowAtRow > 0:
                                temp = LevelData [arrowAtRow-1][arrowAtColumn]
                                LevelData [arrowAtRow-1][arrowAtColumn] = LevelData [arrowAtRow][arrowAtColumn]
                                LevelData [arrowAtRow][arrowAtColumn] = temp
                                arrowAtRow += -1
                                
                        if event.key == K_s :
                            if arrowAtRow < 600/blockWidth - 1:
                                temp = LevelData [arrowAtRow+1][arrowAtColumn]
                                LevelData [arrowAtRow+1][arrowAtColumn] = LevelData [arrowAtRow][arrowAtColumn]
                                LevelData [arrowAtRow][arrowAtColumn] = temp
                                arrowAtRow += 1
                                
                        if event.key == K_d :
                            if arrowAtColumn < 600/blockWidth - 1:
                                temp = LevelData [arrowAtRow][arrowAtColumn + 1]
                                LevelData [arrowAtRow][arrowAtColumn + 1] = LevelData [arrowAtRow][arrowAtColumn]
                                LevelData [arrowAtRow][arrowAtColumn] = temp
                                arrowAtColumn += 1
                            
                        if event.key == K_a :
                            if arrowAtColumn > 0 :
                                temp = LevelData [arrowAtRow][arrowAtColumn - 1]
                                LevelData [arrowAtRow][arrowAtColumn - 1] = LevelData [arrowAtRow][arrowAtColumn]
                                LevelData [arrowAtRow][arrowAtColumn] = temp
                                arrowAtColumn += -1                        
#-------------------------------------------------------------------------------------------


                    elif path == False:    
                        if event.key == K_q:
                            path = True
                            zombie = False
                            #...
            if event.type == MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                print(mousePos)      
                        
    fpsClock.tick(fps)
          

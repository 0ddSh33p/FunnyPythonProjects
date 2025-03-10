#calling the libraries pygame and math
import pygame
import sys
from pygame.locals import *

#initiate and disply the screen
pygame.init()
Displayscreen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Golf")

#define the color for each level, the score variable, the wall colliders list, and the new level bool.
levelColors = ((75, 255, 141), (70, 248, 170), (78, 240, 208), (0, 210, 242), (0, 105, 242), (49, 23, 194), (92, 11, 184), (181, 11, 184), (186, 11, 128), (196, 4, 46))
Score = 0

rWallList =[]
lWallList =[]
tWallList =[]
bWallList =[]
ramp = pygame.rect
height = 0
NEWLEVEL = True
MenuButton = pygame.rect

#creates a button used to go back to the menu, all the function does is draw a button that says menu
def menubutton(Color):
    global MenuButton
    MenuButton = pygame.draw.rect(Displayscreen, (255, 255, 255), (455, 440,120,50))
    font = pygame.font.Font("freesansbold.ttf",40)
    text = font.render("Menu", True, Color)
    textLocation = text.get_rect()
    textLocation.center = (513, 465)
    Displayscreen.blit(text, textLocation)
    return(MenuButton)

def InfoPage(): 
    #set the background color
    Displayscreen.fill((148, 233, 255))
    menubutton((148, 233, 255))
    pygame.display.flip()
    InfoTitle = pygame.font.Font('freesansbold.ttf',60)
    InfoText = pygame.font.Font('freesansbold.ttf',18)
    info = InfoTitle.render("Info", True, (255, 255, 255))
    information = ["Controlls:","Clicking escape in any level sends you to the main menu","Click to shoot the ball away from the mouse","Hitting the edge of the screen will send you to the opposite side","Just like in  golf, points are bad","the orange trapazoids are ramps","TRY YOUR BEST!"]
    Displayscreen.blit(info, (20,20))
    for each in range(len(information)):
        infobody = InfoText.render(information[each], True, (255, 255, 255))
        Displayscreen.blit(infobody, (20,each*25 +100))
    pygame.display.flip()

    while True:
        Events = pygame.event.get()
        for event in Events:
            if event.type == pygame.MOUSEBUTTONUP:
                if menubutton((148, 233, 255)).collidepoint(pygame.mouse.get_pos()):
                    DrawMainMenu()
                    LoopA()

def DrawMainMenu():
    #set the background color
    Displayscreen.fill((148, 233, 255))
    pygame.display.flip()
     #display the "PRO GOLF" text on screen
    title = pygame.font.Font('freesansbold.ttf', 64)
    text = title.render("Pro Golf", True, (255, 255, 255))
    textLocation = text.get_rect()
    textLocation.center = (175, 83)
    Displayscreen.blit(text, textLocation)
    #draw the hill with the golf hole in it
    pygame.draw.circle(Displayscreen, (10, 255, 20), (350, 850), 500, 0)
    pygame.draw.ellipse(Displayscreen, (0, 0, 0), (338, 360,30,15))
    pygame.draw.rect(Displayscreen, (160,160,160), (350,245,5,130))
    pygame.draw.polygon(Displayscreen, (255,0,0), [(320,260), (350,245), (350,275)])

#this is the loop for the level select screen, it is called to display the level selec screen
def LevelSelector():

#sets background color and the words "level select"
    on = 0
    Displayscreen.fill((148, 233, 255))
    pygame.display.flip()
    font = pygame.font.Font("freesansbold.ttf",50)
    text = font.render("Level Select", True, (255,255,255))
    textLocation = text.get_rect()
    textLocation.center = (175, 83)
    Displayscreen.blit(text, textLocation)
    LevelButtons = []

    #this creates the button used to return to the menu
    menubutton((148, 233, 255))

#these two loops create the 2 lines of butttons on the main menu, thei colors, locations and text.
    holefont = pygame.font.Font("freesansbold.ttf",18)
    for i in range(5):
        LevelButtons.append(pygame.draw.rect(Displayscreen, (255, 255, 255), (i * 115 + 25 , 150,90,120)))
        pygame.draw.rect(Displayscreen, levelColors[on], (i * 115 + 25 , 150,90,100))
        hole = holefont.render("Hole " + str(i +1), True, (0,0,0))
        Displayscreen.blit(hole, ((i * 115 + 25),253))
        on += 1
    for i in range(5):
        LevelButtons.append(pygame.draw.rect(Displayscreen, (255, 255, 255), (i * 115 + 25 , 310,90,120)))
        pygame.draw.rect(Displayscreen, levelColors[on], (i * 115 + 25 , 310,90,100))
        if i + 6 != 10:
            hole = holefont.render("Hole " + str(i +6), True, (0,0,0))
        else:
            hole = holefont.render("Bonus", True, (0,0,0))
        Displayscreen.blit(hole, ((i * 115 + 25),413))
        on += 1

        #loop checks if you click, then if the click was on a button, if it was do the thing that button does
    while True:
        Mouse_pos = pygame.mouse.get_pos()
        Events = pygame.event.get()
        for event in Events:
            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(len(LevelButtons)):
                    if LevelButtons[i].collidepoint(Mouse_pos[0], Mouse_pos[1]):
                        Level = "Level" + str((LevelButtons.index(LevelButtons[i]) + 1))
                        eval(Level + "()")
                if MenuButton.collidepoint(Mouse_pos[0], Mouse_pos[1]):
                    DrawMainMenu()
                    LoopA()
        pygame.display.update()


#Used for the buttons on the main menu, creates them and checks for clicks
def LoopA():
    Button1 = pygame.draw.rect(Displayscreen, (255,255,255), (50,130,140,42))
    Button3 = pygame.draw.rect(Displayscreen, (255,255,255), (50,180,140,42))
    Button2 = pygame.draw.rect(Displayscreen, (255,255,255), (50,230,140,42))
    buttonfont = pygame.font.Font('freesansbold.ttf', 44)
    start = buttonfont.render("Start", True, (148, 233, 255))
    info = buttonfont.render("Info", True, (148, 233, 255))
    end = buttonfont.render("Quit", True, (148, 233, 255))
    Displayscreen.blit(start, Button1)
    Displayscreen.blit(info, Button3)
    Displayscreen.blit(end, Button2)
    while True:
        Mouse_pos = pygame.mouse.get_pos()
        Events = pygame.event.get()
        for event in Events:
            if event.type == pygame.MOUSEBUTTONUP:
                if Button1.collidepoint(Mouse_pos[0], Mouse_pos[1]):
                    LevelSelector()
                if Button2.collidepoint(Mouse_pos[0], Mouse_pos[1]):
                    pygame.quit()
                    sys.exit()
                if Button3.collidepoint(Mouse_pos[0], Mouse_pos[1]):
                    InfoPage()

        pygame.display.update()

#used in the main loop for each level, this draws the ball to the screen as well as the level name, par, and current strokes. 
def Draw(BallPos, HolePos, par, stroke):
    global height
    font = pygame.font.Font('freesansbold.ttf', 30)
    par = font.render("Par " + str(par), True, (255, 255, 255))
    Stroke = font.render("Stroke  " + str(stroke), True, (255, 255, 255))
    Displayscreen.blit(par, (10,50))
    Displayscreen.blit(Stroke, (10,20))
    pygame.draw.circle(Displayscreen, (0,0,0), HolePos, 10)
    hole = pygame.draw.circle(Displayscreen, (0,0,0), HolePos, 2)
    pygame.draw.circle(Displayscreen, (100, 100, 100), (BallPos[0],BallPos[1]+(height*2)), 8.95+((height+0.1)/2))
    Ball = pygame.draw.circle(Displayscreen, (255, 255, 255), BallPos, 8.95+((height+0.1)/2))

#this loop is used to draw the walls, you put in how many and where they are, then it draws the walls and puts them on the collision list
def DrawRects(num,pos,endpos,scale,endscale, extraposx, extraposy):
    global NEWLEVEL
    global rWallList
    global lWallList
    global tWallList
    global bWallList
    global ramp
    rWallList = []
    lWallList = []
    tWallList = []
    bWallList = []
    #draw the walls
    for wall in range(int(num)):
        pygame.draw.rect(Displayscreen, (255,255,255), (pos[wall], endpos[wall], scale[wall], endscale[wall]))
        ramp = pygame.draw.polygon(Displayscreen, (255,140,90), ((extraposx,extraposy-17),(extraposx,extraposy),(extraposx+20,extraposy+13),(extraposx+20,extraposy-30)))
        
        Lwall = (pygame.draw.rect(Displayscreen, (255,255,255), (pos[wall], endpos[wall]+1, 5, endscale[wall]-2)))
        Rwall = (pygame.draw.rect(Displayscreen, (255,255,255), (pos[wall]+(scale[wall]-5), endpos[wall]+1, 5, endscale[wall]-2)))
        Twall = (pygame.draw.rect(Displayscreen, (255,255,255), (pos[wall], endpos[wall], scale[wall], 5)))
        Bwall = (pygame.draw.rect(Displayscreen, (255,255,255), (pos[wall], endpos[wall]+(endscale[wall]-5), scale[wall], 5)))
        
        #append them to the list
        rWallList.append(Rwall)
        lWallList.append(Lwall)
        tWallList.append(Twall)
        bWallList.append(Bwall)
        


#THE MAIN LOOP OF THE GAME. IT IS CALLED TO CREATE EACH LEVEL 
def Controlls(color,BallX, BallY, HoleX, HoleY, par, num,pos,endpos,scale,endscale, extrapos, extraposy):
    #Define any permenant variables used
    stroke = 0
    Dragging = False
    Displayscreen.fill(color)
    pygame.display.flip()
    BallPos = [BallX,BallY]
    HolePos = [HoleX, HoleY]
    Xdistance = 0
    Ydistance = 0
    Won = False
    Speed = 45
    stroke = 0
    global Score
    global rWallList
    global lWallList
    global tWallList
    global bWallList
    global ramp

    global height
    
    Collided = False
    cooldown = 40
    Bounce = 0
    Ball = pygame.draw.circle(Displayscreen, (255, 255, 255), BallPos, 9)
    DrawMenu = True
    global MenuButton 

    
    while Won == False:
        #this section is just so that the screen is drawn and updated every frame
        Collided = False
        Displayscreen.fill(color)
        DrawRects(num,pos,endpos,scale,endscale,extrapos,extraposy)
        Draw(BallPos, HolePos, par, stroke)
            
        pygame.draw.circle(Displayscreen, (0,0,0), HolePos, 10)
        hole = pygame.draw.circle(Displayscreen, (0,0,0), HolePos, 2)
        Ball = pygame.draw.circle(Displayscreen, (255, 255, 255), BallPos, 9)
        if height > 0:
            height -= 0.3

        #this checks if the ball collides with the hole, if it does then it ends the level
        if Ball.colliderect(hole) and height < 1:
            Score += stroke - par
            Won =True

         #when the user starts clicking it beigns a swing
        Events = pygame.event.get()
        for event in Events:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    DrawMainMenu()
                    LoopA()
                    return()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                Dragging  = True

                    
         #this loop is used when you take a swing
        while Dragging == True:
            if height > 0:
                height -= 0.3
            
        #this draws the screen each frame and sets a few temporary variables
            Collided = False
            Displayscreen.fill(color)
            DrawRects(num,pos,endpos,scale,endscale, extrapos,extraposy)
            
            Draw(BallPos, HolePos, par, stroke)
            pygame.draw.line(Displayscreen, (255,255,255), BallPos, pygame.mouse.get_pos(), 4)
            Events = pygame.event.get()

 #when you let got move the ball away from the point of contact/mouse
            for event in Events:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        DrawMainMenu()
                        LoopA()
                        return()
                
                (MX, MY) = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
#for the swing, add a point
                    stroke +=1

#calculate the distance and direction of travel
                    Ballvect = pygame.math.Vector2((BallPos[0],BallPos[1]))
                    DistX = ((MX - Ballvect.x) *3)
                    DistY = ((MY - Ballvect.y) *3)
                    Xdistance = abs(DistX)
                    Ydistance = abs(DistY)
                    Dragging = False
            pygame.display.update()

#after you de-click, move the ball the amount deterimed above
        while Xdistance > 1 and Ydistance > 1 and Won == False:
            tempx = BallPos[0]
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        DrawMainMenu()
                        LoopA()
                        return()
 #draw the creen
            DrawRects(num,pos,endpos,scale,endscale,extrapos,extraposy)
            Draw(BallPos, HolePos, par, stroke)

#makes the ball travel for the amount of time needed for the distance dragged.
            Xdistance -=Xdistance/10
            Ydistance -=Ydistance/10
            hole = pygame.draw.circle(Displayscreen, (0,0,0), HolePos, 2)
            Ball = pygame.draw.circle(Displayscreen, (255, 255, 255), BallPos, 9)

#check if the ball hits the hole, 
            if Ball.colliderect(hole) and height <1:
#if it is traveling slow enough, go in
                if abs(DistY/Speed) < 11 and abs(DistX/Speed) < 11:
                    Score += stroke - par
                    Won =True
 #if the ball is traveling too fast, have it skip over the hole
            elif Ball.colliderect(hole) and abs(DistX/Speed) > 11:
                DistX -= 1.3
            elif Ball.colliderect(hole) and abs(DistY/Speed) > 11:
                DistY -= 1.3

#reduce the speed each frame to make the motion more fluent
            DistX = DistX/1.078
            DistY = DistY/1.078
            pygame.time.delay(10)
            Draw(BallPos, HolePos, par, stroke)
#move the ball
            BallPos[0] -= DistX/Speed
            BallPos[1] -= DistY/Speed

 # set the collider check to check every cooldown milliseconds
            if pygame.time.get_ticks() > Bounce + cooldown:
                Collided = False

#wall physics, if it his a wall, deterime from what direction and reflect it over that axis.

            for i in range(len(rWallList)):
                if Ball.colliderect(rWallList[i]) and Collided == False and height < 1:
                    Bounce = pygame.time.get_ticks()
                    DistX = -DistX
                    BallPos[0] += 1*(Speed/6)
                    Collided = True

            for i in range(len(lWallList)):
                if Ball.colliderect(lWallList[i]) and Collided == False and height < 1:
                    Bounce = pygame.time.get_ticks()
                    DistX = -DistX
                    BallPos[0] -= 1*(Speed/6)
                    Collided = True

            for i in range(len(tWallList)):
                if Ball.colliderect(tWallList[i]) and Collided == False and height < 1:
                    Bounce = pygame.time.get_ticks()
                    DistY = -DistY
                    BallPos[1] -= 1*(Speed/6)
                    Collided = True

            for i in range(len(bWallList)):
                if Ball.colliderect(bWallList[i]) and Collided == False and height < 1:
                    Bounce = pygame.time.get_ticks()
                    DistY = -DistY
                    BallPos[1] += 1*(Speed/6)
                    Collided = True
            
            Gright = False
            if tempx < BallPos[0]:
                Gright = True

            if Ball.colliderect(ramp) and height <= 7 and Gright == True:
                height = 7
            if Ball.colliderect(ramp) and Gright == False and Collided == False:
                Bounce = pygame.time.get_ticks()
                DistX = -DistX
                BallPos[0] -= 1*(Speed/6)
                Collided = True
            if height > 0:
                height -= 0.3
                    
                    
#if the ball goes off screen, put it on the opposite side of the screen
            if BallPos[1] < 0:
                BallPos[1] = 500
            if BallPos[1] > 500:
                BallPos[1] = 0
            if BallPos[0] > 600:
                BallPos[0] = 0
            if BallPos[0] < 0:
                BallPos[0] = 600

#updateb the screen at a rate of once per ten milliseconds in each loop
            pygame.display.flip()
            pygame.time.delay(10)
            pygame.display.update()
            Displayscreen.fill(color)
        pygame.display.update()
        pygame.display.flip()        


#function the displays the text scrollin for each level name and the congradutations screen.
def TextAnim(text, BGcolor):
    #sets up the text
    if text == "win":
        print("true")
        scorefont = pygame.font.Font('freesansbold.ttf', 35)
        scoretext = scorefont.render("Points: " + str(Score), True, (255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 45)
        nametext = font.render("CONGRATULATIONS", True, (255, 255, 255))
        textLocation = nametext.get_rect()
        textLocation.center = (300, 0)
    else:
        font = pygame.font.Font('freesansbold.ttf', 45)
        nametext = font.render(str(text), True, (255, 255, 255))
        textLocation = nametext.get_rect()
        textLocation.center = (300, 0)
    #move the text from the top to the middle of the screen
    while True:
        # if the text has reached the desired position, end the screen
        if textLocation.y >= 200:
           pygame.time.delay(1000)
           return()
        else:
            #clear the screen and redraw the text lower on the page
            Displayscreen.fill(BGcolor)
            Displayscreen.blit(nametext, textLocation)
            if text == "win":
                Displayscreen.blit(scoretext, (textLocation.x,textLocation.y+40))
            textLocation.y += 2
            pygame.time.delay(10)
            pygame.display.flip()
            pygame.display.update()

# the level functions call the main controlls function to build each level.
def Level1():
    #new level is triggered
    global NEWLEVEL
    NEWLEVEL = True
    #triggers the text intro
    TextAnim("HOLE 1", levelColors[0])
    #plays the level
    Controlls((75, 255, 141), 150,200, 400,375, 3,3,(350,365,435),(345,395,345),(20,80,20),(70,20,70),(-50),-50)
    #once you win, display the congrats screen
    TextAnim("win", levelColors[0])
    #Move onto the next level
    Level2()
    
    #functions the same as the level one function but with diffrent parameters
def Level2():
    global NEWLEVEL
    NEWLEVEL = True
    TextAnim("HOLE 2", levelColors[1])
    Controlls(levelColors[1], 400,375, 100,300, 2, 1, (300,0),(0,0),(20,0),(500,0),(-50),-50)
    TextAnim("win",levelColors[1])       
    Level3()

#functions the same as the level one function but with diffrent parameters
def Level3():
    global NEWLEVEL
    NEWLEVEL = True
    TextAnim("HOLE 3",levelColors[2])
    Controlls(levelColors[2], 400,185, 300,450, 3, 4,(0,315,0,0),(200,200,0,480),(285,300,600,600),(300,300,170,20),(-50),-50)
    TextAnim("win",levelColors[2])           
    Level4()

#functions the same as the level one function but with diffrent parameters
def Level4():
    global NEWLEVEL
    NEWLEVEL = True
    TextAnim("HOLE 4",levelColors[3])       
    Controlls(levelColors[3], 100,400, 480,100,6, 6, (-10,0,0,590,195,395),(0,-5,490,0,100,0),(20,650,650,20,20,20),(550,20,20,550,500,400),(-50),-50)
    TextAnim("win",levelColors[3])        
    Level5()

#functions the same as the level one function but with diffrent parameters
def Level5():
    global NEWLEVEL
    NEWLEVEL = True
    TextAnim("HOLE 5",levelColors[4])       
    Controlls(levelColors[4], 225,250, 350,300,6,8,(175,175,250,300,300,375,300,375),(150,150,150,150,150,220,330,150),(20,75,20,20,95,20,75,20),(200,20,200,200,20,130,20,40),(-50),-50)
    TextAnim("win",levelColors[4])        
    Level6()

#functions the same as the level one function but with diffrent parameters
def Level6():
    global NEWLEVEL
    NEWLEVEL = True
    TextAnim("HOLE 6",levelColors[5])       
    Controlls(levelColors[5], 150,340 ,500, 260, 2, 5, (400,565,565,565,565),(0,0,285,225,285),(20,20,20,30,30),(510,245,240,20,20),(-50),-50)
    TextAnim("win",levelColors[5])        
    Level7()

#functions the same as the level one function but with diffrent parameters
def Level7():
    global NEWLEVEL
    NEWLEVEL = True
    TextAnim("HOLE 7",levelColors[6])       
    Controlls(levelColors[6], 450,250, 275,30, 3, 5, (240,300,315,330,240),(0,0,150,300,290),(20,20,20,20,90),(500,150,150,200,20),(-50),-50)
    TextAnim("win",levelColors[6])           
    Level8()

#functions the same as the level one function but with diffrent parameters
def Level8():
    global NEWLEVEL
    NEWLEVEL = True
    TextAnim("HOLE 8",levelColors[7])       
    Controlls(levelColors[7], 220,290, 350,290,1,4,(100,100,300,100),(200,380,200,200),(20,200,20,200),(200,20,200,20),250,300)
    TextAnim("win",levelColors[7])        
    Level9()

#functions the same as the level one function but with diffrent parameters
def Level9():
    global NEWLEVEL
    NEWLEVEL = True
    TextAnim("HOLE 9",levelColors[8])       
    Controlls(levelColors[8], 100,200, 430,330,2,4,(380,460,400,380),(300,300,360,280),(20,20,80,100),(80,80,20,20),300,330)
    TextAnim("win",levelColors[8])        
    Level10()

#functions the same as the level one function but with diffrent parameters
def Level10():
    global NEWLEVEL
    NEWLEVEL = True
    TextAnim("BONUS HOLE",levelColors[9])       
    Controlls(levelColors[9], 230,155, 250,290,9,9,(120,460,120,120,120,410,170,170,170), (120,120,380,170,170,170,330,220,220), (360,20,360,20,310,20,260,20,210),(20,260,20,210,20,160,20,110,20),(-50),-50)
    TextAnim("win",levelColors[9])        
    LevelSelector()

#calls themain menu and starts the program
DrawMainMenu()
LoopA()
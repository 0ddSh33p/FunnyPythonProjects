import pygame
from pygame.locals import QUIT
import random
import math

pygame.init()

width = 400
height = 400

Screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cool Boat')

speed = 1
speed2 = 3
locationChange = [0, 0]
global gravity
gravity = 8
Distance = 0.6

allWater = []
location = [0,0]
LastLok = []
size = [70,30]
ClickRange = 30
lightness = 3

Button = 0
Pressing = False;

class Water:

    color = (0, 0, 255)
    size = 7
    location = [200, 150]
    Num = 0
    LastLok = location

    def __init__(self, location):
        self.location = location
        self.Num = len(allWater)
        self.color = ((22,22,250))
        allWater.append(self)

    def draw(self):
        
        for droplet in range(len(allWater)):
            if droplet != self.Num:
                
                temp = allWater[droplet].location[0] - self.location[0]
                tempY = self.location[1] - allWater[droplet].location[1]

                XYDiff = ((abs(temp)**2) + (abs(tempY)**2))**0.5

                if abs(temp) < 1 and abs(tempY) < 1:
                    self.location = [self.location[0]+0.2,self.location[1]+random.randint(-1,1)]
                elif XYDiff < self.size * Distance:
                    self.location = [self.location[0] - (temp/abs(temp + 0.0001) * 3 * speed), self.location[1] - 2*speed]

            
        
        self.location = [self.location[0],self.location[1] + (0.3* gravity)]
        
        if self.location[1] > height:
            self.location = [(self.location[0]), (height)]
        if self.location[0] < 0:
            self.location = [self.size, (self.location[1])]
        elif self.location[0] > width:
            self.location = [(width - self.size), (self.location[1])]

        if self.LastLok != self.location[0]:
            pygame.draw.circle(Screen, self.color, self.location, self.size)

        self.LastLok = self.location


class boat():
    locationNormal = [location[0] + width/2, location[1] + height/2]

    def draw(self):

        self.locationNormal = [self.locationNormal[0],self.locationNormal[1] + gravity]
        
        for droplet in allWater:
            tempX = droplet.location[0] - (self.locationNormal[0] + size[0]/2)
            tempY = droplet.location[1] - (self.locationNormal[1] + size[1]/2)
            
            if abs(tempX) < size[0]/2 and abs(tempY) < size[1]/2:
                self.locationNormal = [self.locationNormal[0] + (tempX/abs(tempX + 0.0001) * -speed), self.locationNormal[1] - speed]
       
        self.locationNormal = [self.locationNormal[0] + locationChange[0], self.locationNormal[1] + locationChange[1]]
        if self.locationNormal[0] > width - size[0]:
            self.locationNormal[0] = width - size[0]
        elif self.locationNormal[0] < 0:
            self.locationNormal[0] = 0.1

        if self.locationNormal[1] > height - size[1]:
            self.locationNormal = [self.locationNormal[0],height - size[1]]
            
        pygame.draw.rect(Screen, (180,50,80), (self.locationNormal, size))
        #pygame.draw.polygon(Screen, (180,50,80), (points))

def fillWater(amount):
    for i in range(amount):
        Water([int(random.randint(0, width)), height])

def Spash():
    Pos = pygame.mouse.get_pos()
    if Button == 1:
        direct = -1
    else:
        direct = 1
        
    for droplet in allWater:

        DiffX = droplet.location[0] - Pos[0]
        DiffY = droplet.location[1] - Pos[1]
        if DiffX > 0:
            Flip = 1
        else:
            Flip = -1

        if ((abs(DiffX)**2) + (abs(DiffY)**2))**0.5 < ClickRange:
            droplet.location = [droplet.location[0] + ((abs(DiffX) - (ClickRange/2)) * Flip) , droplet.location[1] - ((abs(DiffX) - ClickRange) * (speed/2) * direct)]

Boat = boat()
fillWater(400)
while (1):
    Screen.fill((210, 230, 255))
    Boat.draw()
    for water in allWater:
        water.draw()
    
    if Pressing:
        Spash()

    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_d]:
        if locationChange[0] < 3*speed2:
            locationChange = [locationChange[0] + speed2*0.5, locationChange[1]]
    elif pressed[pygame.K_a]:
        if locationChange[0] >  -3*speed2:
            locationChange = [locationChange[0] - speed2*0.5, locationChange[1]]
    else:
        locationChange = [0,0]   
    

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            Button = event.button
            Pressing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            Pressing = False
        elif event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

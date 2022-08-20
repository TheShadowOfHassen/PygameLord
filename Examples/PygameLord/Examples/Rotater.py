#PygameLord

# The MIT License (MIT)
# Copyright © 2021 <NAthanael K. Stottlemyer>
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the “Software”), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


#A example showing the rotation program
#Imports
import PygameLord
from PygameLord.ColorConstants import*
import pygame
from pygame.locals import*
import random
import time
import sys
WINDOW_WIDTH = 400
WINDOW_HIGHT = 400
FPS = 60
Clock = pygame.time.Clock()

Screen =  pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT),0, 32)
Tank =  pygame.image.load('./Images/Tank.png')
Lazer =  pygame.image.load('./Images/Lazer.png')
position = (0,0)
pygame.display.set_caption('Rotation')
laztrue = False

        
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            PygameLord.quit()
        if event.type == MOUSEMOTION:
            position = event.pos
        angle = PygameLord.Motion.point_towards((200,200),position)
        rotimage = pygame.transform.rotate(Tank, -angle)

#Now a vector moving system... It will eventuly be turned into a tutorial


        if event.type == MOUSEBUTTONDOWN:
            lazer = Vector2 (200,200) #point A
            lazerdes =(event.pos[0], event.pos[1]) #point B
            area = Vector2(lazer[0] - lazerdes[0], lazer[1] - lazerdes[1])  #get the distance between
            incrament = area/10 #devide it
            laztrue = True

        
            
            
    Screen.fill(BRITISH_RACING_GREEN)
    if laztrue:
        angle = PygameLord.Motion.point_towards((200,200),position)
        rotimage2 = pygame.transform.rotate(Lazer, -angle)
        lazer -= incrament #subtract incriment from position.
        rect = Lazer.get_rect(center = (int(lazer[0]), int(lazer[1])))
        Screen.blit(rotimage2,rect)
    rect = rotimage.get_rect(center = (200,200))
    Screen.blit(rotimage,rect)
    pygame.display.update()
    Clock.tick(FPS)
    
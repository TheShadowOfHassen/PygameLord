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

#Imports
import pygame, os,math
from pygame.locals import*
pygame.init()
from pygame.math import Vector2
'''
A point towards program
'''
'''
point_towards(current_pos, point_pos)
current_pos: The pos which the thing to rotate is set
point_pos: The pos to point towards.
Note: the images when put into this ought to have the way you want pointing right.
'''
def point_towards(current_pos, point_pos):
    x1 = current_pos[0]
    y1 = current_pos[1]
    x2 = point_pos[0]
    y2 = point_pos[1]
    position1 = Vector2(current_pos)
    position =  point_pos -  position1
    radius, angle = position.as_polar()
    return(int(angle))
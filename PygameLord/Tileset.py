#PygameLord

'''
Copyright (c) 2022 TheShadowOfHassen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

#Images and the things related to it.
#Imports
import pygame, os
from pygame.locals import*
pygame.init()
#Tilesset
'''


Tileset(file, (width, height))
Tilset a single word, A tilesheet is a group of images stuck tgether found in the games of long ago, this class will store and split it when needed 
file: the file to load and store
width: The width of every single tile on the set 
hight: the highth of the tiles on the set they are in a tuple
'''

class Tilesheet:
    def __init__(self, file, space,):
        self.image = pygame.image.load(file) #load the file.
        self.width = space[0] #
        self.height = space[1]
        self.image_width, self.image_height = self.image.get_size() #Get the image size
        self.tile_table = []
        for self.tile_x in range(0, int(int(self.image_width)/int(self.width))): #Splitting it, basicly a loop and a bit of magic
            self.line = []
            self.tile_table.append(self.line)
            for self.tile_y in range(0, int(int(self.image_height)/int(self.height))):
                self.rect = (self.tile_x*self.width, self.tile_y*self.height, self.width, self.height)
                self.line.append(self.image.subsurface(self.rect))

    '''
    Get_Tile(self, x, y)
    Thus it returns the tiles to your use.
    x: X cordanince that starts with 0
    y: same as x but with the y cords
    '''
    def get_tile(self, space):
         for X, row in enumerate(self.tile_table):
            if X == space[0]:
                for Y, tile in enumerate(row):
                    if Y == space[1]:
                        return tile
                

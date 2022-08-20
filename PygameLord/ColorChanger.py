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
#Imports
import pygame
from pygame.locals import*
pygame.init()
'''
Color manipulation.

'''
'''
ChangeColor(image, color_to_change, color_change_into)

images: The image you wish to change
color_to_change: The color to change in RGB Value
color_to_change: The color that color_to_change is replaced with
'''
def ChangeColor(image, color_to_change, color_change_into):
    image_changed = image
    array = pygame.PixelArray(image_changed)
    array.replace(color_to_change, color_change_into, 0.06)
    del array
    return image_changed

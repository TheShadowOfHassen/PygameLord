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
version = '1.0.0'
import os, sys
#This is PygameLord so clearly pygame comes first.
try: 
    import pygame
except ModuleNotFoundError:
    raise Exception('Please Get Pygame 2.0')
if pygame.get_sdl_version() < (2, 0, 0):
    raise Exception('Please Get Pygame 2.0')
from pygame.locals import*
pygame.init() #We Init it already-yet you should probably run this also in your code
Path = os.path.dirname(os.path.realpath(__file__));
print('Greetings from PygameLord ' + version +'.')
'''
Pygame LORD or PygameLord stands for Pygame library of reusible duhickes
and is essinstialy a project that has a moduole of useful pygame and python tricks i have picked up over the years.
You can use these files as a module or alternitvly copy and paste them into your code under the MIT Lisense
'''


#Importing the sepreate parts
import PygameLord.ColorChanger #Color changing module.
import PygameLord.Tileset #Images Modules
import PygameLord.Load_Multiple_Images #Loading objects
import PygameLord.Display_Text#Font
import PygameLord.Surface# Surface stuff
import PygameLord.Motion#Motion
LORD  = pygame.image.load(Path + '/Resorces/PygameLord.png')
pygame.display.set_caption('PygameLord')
pygame.display.set_icon(LORD)

# exiting
def exit():
    pygame.quit()
    
def quit_game():
    pygame.quit()
    sys.exit()

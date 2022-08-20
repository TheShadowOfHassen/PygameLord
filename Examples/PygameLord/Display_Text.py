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
import pygame, os
from pygame.locals import*
pygame.init()
Path = os.path.dirname(os.path.realpath(__file__));
IBMFONT = pygame.font.Font(Path+'/Resorces/PxPlus_AmstradPC1512.ttf', 12 ) #Loading the defult font for PygameLord this font hass full ASCII potental

'''
display_text(text, font, surface, xpos,ypos, color)
text: Text to display
font: The font to display it with
surface: On wich to display thine text
xpos: The location of the top left corner of the text on the x cordanints
ypos The y positon of the top left corenr
color: the color of the text.
'''
def display_text(text, surface, xpos,ypos, color, font=IBMFONT):
    Font = IBMFONT
    #text rangling parts
    parttext = ''
    for s in text:
        if s == '\t': #Replace Tabs with four spaces...
            parttext += '    '
        else:
            parttext += s
    Text = parttext.split('\n')
    NewText = []
    for t in Text:
        if t != '\n':#Split the new lines up.
            NewText.append(t)
    y = 0
    for i in  NewText:
        FinalTextSurface = Font.render(i,1,color)
        FinalTextRect = FinalTextSurface.get_rect()
        y += FinalTextRect.height
        FinalTextRect.topleft =(int(xpos), y+ypos) #assign the text rect
        surface.blit(FinalTextSurface, FinalTextRect)

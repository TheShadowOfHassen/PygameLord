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
import pygame,os
from pygame.locals import*
pygame.init()
#Loading Objects
'''
Parse_Locations(file)
file: Your text file, use  a .txt
Like in python '#'s will be ignored
An Example

#Coment
./File/File
./File/Other File
...
'''
def Parse_Locations(file):
    file = open(file, 'r')#read the file
    lines = []
    folders = []
    for text_line in file:
        lines.append(text_line) #pull the files info
    file.close()#close it
    moding = []
    for i in lines:
        s =i.strip('\n')#split the lines up
        moding.append(s)
    for i in moding:
        if i  != '\n' and i[0] != '#': #ignore new lines or coments '#'
            folders.append(i)
    return folders


def Load_Images(paths,files):
    Images = []
    Image_Set = {}
    for path in paths:
        file = os.listdir(path)
    
        for Object in file: #loops through the parts
            for fileEnd  in files:
                if Object.endswith(fileEnd):
                    Images.append(os.path.join(path, Object))

    for image in Images:#appends them
        text = os.path.split(image)[-1]
        text = text.split('.')
        text = text[0]
        im = pygame.image.load(image)#Here's the defrence it loads them.
        Image_Set[text] = im
        
    return Image_Set

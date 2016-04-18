#python34

import random
from PIL import Image
import os, sys
import bisect
##from tkinter import *

RGB = [i for i in range(256) if i % 9 == 0]


tableau = []
pixelated = []

##fileName = filedialog.askopenfilename()

Alpha = ' abcdefghijklmnopqrstuvwxyz'

enIm = Image.open('etc.png')

##set bounds
width = enIm.size[0] - 1
height = enIm.size[1]

##for wpixel in range(width):
for hpixel in range(height):
    item = enIm.getpixel((0, hpixel))
    for i in item:
##        if i != 255: #remove this if statement to leave alpha values in tact
        tableau.append(i)

def decode(score, breakpoints=RGB, grades=Alpha):
    i = bisect.bisect(breakpoints, score)
    return grades[i-1]

decoded = [decode(score) for score in tableau]
decMsg = ''.join(decoded)
print(decMsg)

##print(len(tableau))

##this works for 'ribbons' only
##for i in range(height):
##    item = enIm.getpixel((0,i))
##    for i in item:
##        tableau.append(i)

##print(tableau)

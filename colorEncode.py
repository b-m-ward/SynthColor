#python34

import random
from PIL import Image
import os

RGB = [i for i in range(256) if i % 9 == 0]

#dave

encoded = []
tableau = []
pixelated = []

Alpha = ' abcdefghijklmnopqrstuvwxyz'

message = input('Provide a message: ')

for i in message:
    for x in Alpha:
        if i == x:
            encoded.append(Alpha.index(x)*9)

for i in encoded:
    tableau.append(random.randint(i, i+8))

def convert():
    while len(tableau) % 4 != 0:
        tableau.append(0)
##    print('Tableau is: ', tableau)

def pixelate():
    counter = 0
    for i in range(len(tableau)//4):
        pixel_set = (tableau[counter], tableau[counter+1], tableau[counter+2], tableau[counter+3])
##        print(pixel_set)
        pixelated.append(pixel_set)
        counter = counter + 4

convert()
pixelate()

#create canvas
canvas = Image.new('RGBA', (1, len(pixelated)))

for x in range(len(pixelated)):
    canvas.putpixel((0,x), pixelated[x])

file_name = input('Name your file: ')
canvas.save('Images/'+file_name + '.png')
print('Saving file ', file_name + '.png')
os.system("start Images/"+file_name+".png")

import random
from PIL import Image
import os, sys


class Encoder(object):
    def __init__(self):
        self.encoded = []
        self.tableau = []
        self.pixelated = []
        self.EncodedKeys = {}
        self.Alphabet = ' abcdefghijklmnopqrstuvwxyz'
        self.rgb = [i for i in range(256) if i % 9 == 0]

    # build out a dictionary for all the characters in self.Alphabet
    # and their corresponding rgb values
    def buildList(self):
        # loop over the alphabet provided and create an RGB value for each character
        byteValues = map(ord, self.Alphabet)
        for i in self.Alphabet:
            self.EncodedKeys[i] = byteValues[i]
            # store the byte value as int in dict


    # take a message from the user and encode it.
    def encode(self,msg):
        message = msg
        for i in message:
            for x in self.Alphabet:
                if i == x:
                    self.encoded.append(self.Alphabet.index(x)*9)

        for i in self.encoded:
            self.tableau.append(random.randint(i, i+8))
        self.convert()
        self.pixelate()

    def convert(self):
        while len(self.tableau) % 4 != 0:
            self.tableau.append(0)

    def pixelate(self):
        counter = 0
        for i in range(len(self.tableau)//4):
            pixel_set = (self.tableau[counter], self.tableau[counter+1], self.tableau[counter+2], self.tableau[counter+3])
            self.pixelated.append(pixel_set)
            counter = counter + 4

    def save(self):
        canvas = Image.new('RGBA', (1, len(self.pixelated)))
        for x in range(len(self.pixelated)):
            canvas.putpixel((0,x), self.pixelated[x])
        file_name = input('Name your file: ')
        canvas.save('Images/'+file_name + '.png')
        print('Saving file ', file_name + '.png')
        os.system("start Images/"+file_name+".png")

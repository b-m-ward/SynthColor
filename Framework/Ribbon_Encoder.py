import random
from PIL import Image
import os, sys
import datetime
import bisect
import math
import time

class Ribbon(object):
    """Encodes text into a one pixel wide horizontal ribbon"""
    def __init__(self):
        self.encoded = []
        self.tableau = []
        self.pixelated = []
        self.alpha = ' abcdefghijklmnopqrstuvwxyz'
        self.rgb = [i for i in range(256) if i % 9 == 0]
        self.translated = []

    # take input and encode it.
    def encode(self,msg):
        startTime = time.time()
        message = msg.lower()
        for i in message:
            for x in self.alpha:
                if i == x:
                    self.encoded.append(self.alpha.index(x)*9)
        for i in self.encoded:
            self.tableau.append(random.randint(i, i+8))
        self.convert()
        self.pixelate()
        endTime = time.time()
        print('Seconds passed: ', startTime - endTime)

    def convert(self):
        while len(self.tableau) % 4 != 0:
            self.tableau.append(0)

    def pixelate(self):
        counter = 0
        for i in range(len(self.tableau)//4):
            pixel_set = (self.tableau[counter], self.tableau[counter+1], self.tableau[counter+2], self.tableau[counter+3])
            self.pixelated.append(pixel_set)
            counter = counter + 4

    def open(self):
        startTime = time.time()
        item = open('../TestFiles/war.txt', mode='r')
        encoded = self.encoded
        for line in item:
            for x in line:
                if x == '\n':
                    self.encoded.append(0)
                for letter in self.alpha:
                    if x == letter:
                        self.encoded.append(self.alpha.index(x)*9)
        for i in self.encoded:
            self.tableau.append(random.randint(i, i+8))
        self.convert()
        self.pixelate()
        endTime = time.time()
        print('Seconds passed during open: ', endTime - startTime)

    def save(self): ##creates ribbons
        startTime = time.time()
        canvas = Image.new('RGBA', (1, len(self.pixelated)))
        for x in range(len(self.pixelated)):
            canvas.putpixel((0,x), self.pixelated[x])
        file_name = input('Save ribbon file: ')
        canvas.save('../Images/'+file_name + '.png')
        print('Saving file ', file_name + '.png')
        #os.system("start Images/"+file_name+".png")
        endTime = time.time()
        print('Time to save: ', endTime - startTime)

    def savecube(self): ##creates ribbons
        canvas = Image.new('RGBA', (len(self.pixelated), len(self.pixelated)))
        for x in range(len(self.pixelated)):
            for y in range(len(self.pixelated)):
                canvas.putpixel((y,x), self.pixelated[x])
        file_name = input('Save cube file: ')
        canvas.save('../Images/'+file_name + '.png')
        print('Saving file ', file_name + '.png')
        #os.system("start Images/"+file_name+".png")

    def decode(self):
        """Decode Function"""
        startTime = time.time()
        rgb = self.rgb
        alpha = self.alpha
        translated = self.translated
        pixelated = self.pixelated
        tableau = self.tableau
        fileToDecode = input('enter file name: ')
        enIm = Image.open("../Images/"+fileToDecode+".png")
        width = enIm.size[0] - 1
        height = enIm.size[1]
        for hpixel in range(height):
            item = enIm.getpixel((0, hpixel))
            for i in item:
        ##        if i != 255: #remove this if statement to leave alpha values in tact
                translated.append(i)
        def parse(score, breakpoints=rgb, grades=alpha):
            i = bisect.bisect(breakpoints, score)
            return grades[i-1]
        decoded = [parse(score) for score in translated]
        decMsg = ''.join(decoded)
        print(decMsg)
        endTime = time.time()
        print('Time to decode: ', endTime - startTime)

class lang(Ribbon):
    """Encodes by averaging each word into one pixel"""
    super.__init__
    def encodelang(msg):
        super.encode()

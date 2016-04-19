import random
from PIL import Image
import os, sys
import datetime
import bisect

class Encoder(object):
    def __init__(self):
        self.Encoded = [] # List holding the input message characters encoded to RGB values
        self.Pixels = [] # List of Tuples, each tuple representing a pixel for the final Image
        self.EncodedKeys = {} # DIctionary of Key(alphanumeric) Values(RGB representation) for encoding input... THE CIPHER
        self.Alphabet = ' abcdefghijklmnopqrstuvwxyz.,()-'
        self.fileName = str(datetime.date.today()) + "-" + str(random.randint(1,100)) + ".png"
        self.buildList()

    # build out a dictionary for all the characters in self.Alphabet and their corresponding rgb values
    def buildList(self):
        byteValues = list(map(ord, self.Alphabet))
        for i in self.Alphabet:
            self.EncodedKeys[i] = byteValues[self.Alphabet.index(i)]
            # TODO: could write a randomization algo here to make the byte value something based off of a key
            #ex self.EncodedKeys[i] = self.randomizeByte(byteValues[self.Alphabet.index(i)])

    # take a message from the user and encode it with the encoding keys.
    def encodeMessage(self,msg):
        for i in msg.lower():
            self.Encoded.append(self.EncodedKeys[i])

        # we break off the encoded values into tuples of 3 so the Encoded list needs x%3==0 to be true for pixel processing
        while(len(self.Encoded)%3 != 0):
            self.Encoded.append(255)

    def buildPixels(self):
        index = 0
        for i in range(len(self.Encoded)//3):
            self.Pixels.append((self.Encoded[i], self.Encoded[i+1], self.Encoded[i+2], 150))
            counter = index + 3

    def buildCanvasBlock(self):
        dimension = len(self.Pixels)
        self.canvas = Image.new('RGBA', (dimension,dimension))
        for x in range(dimension):
            for y in range(dimension):
                self.canvas.putpixel((x,y), self.Pixels[x])

    def buildCanvas(self):
        self.canvas = Image.new('RGBA', (1, len(self.Pixels)))
        for x in range(len(self.Pixels)):
            self.canvas.putpixel((0,x), self.Pixels[x])

    def open(self):
        item = open('testDoc.txt', mode='r')
        encoded = self.encoded
        for line in item:
            for x in line:
                if x == '/n'
                    print('found linebreak')
                for letter in self.alpha:
                    if x == letter:
                        self.encoded.append(self.alpha.index(x)*9)
        for i in self.encoded:
            self.tableau.append(random.randint(i, i+8))
        self.convert()
        self.pixelate()

    def save(self):
        print('Saving file ', self.fileName)
        self.canvas.save('Images/' + self.fileName)
        os.system("start Images/" + self.fileName)


    # def decode(self):
    #     rgb = self.rgb
    #     alpha = self.alpha
    #     tableau = []
    #     pixelated = self.pixelated
    #     fileToDecode = input('enter file name: ')
    #     enIm = Image.open("Images/"+fileToDecode+".png")
    #     width = enIm.size[0] - 1
    #     height = enIm.size[1]
    #     for hpixel in range(height):
    #         item = enIm.getpixel((0, hpixel))
    #         for i in item:
    #     ##        if i != 255: #remove this if statement to leave alpha values in tact
    #             tableau.append(i)
    #     def parse(score, breakpoints=rgb, grades=alpha):
    #         i = bisect.bisect(breakpoints, score)
    #         return grades[i-1]
    #     decoded = [parse(score) for score in tableau]
    #     decMsg = ''.join(decoded)
    #     print(decMsg)

import random
from PIL import Image
import os, sys
import datetime
import bisect
import math
import time
#test change

class Encoder(object):
    def __init__(self):
        self.Encoded = [] # List holding the input message characters encoded to RGB values
        self.Pixels = [] # List of Tuples, each tuple representing a pixel for the final Image
        self.EncodedKeys = {} # DIctionary of Key(alphanumeric) Values(RGB representation) for encoding input... THE CIPHER
        self.Alphabet = ' abcdefghijklmnopqrstuvwxyz.,()-:;?|1234567890![]*=/'
        self.fileName = str(datetime.date.today()) + "-" + str(random.randint(1,100)) + ".png"
        self.buildList()
        self.startTime = 0
        self.endTime = 0


    def startTimer(self):
        self.startTime = time.time()

    def stopTimer(self, msg):
        self.endTime = time.time()
        print('Time taken to ' + msg + ' : ' + str(self.endTime - self.startTime) + 's')

    # build out a dictionary for all the characters in self.Alphabet and their corresponding rgb values
    def buildList(self):
        byteValues = list(map(ord, self.Alphabet))
        for i in self.Alphabet:
            self.EncodedKeys[i] = byteValues[self.Alphabet.index(i)] - random.randint(0,100)
            # TODO: could write a randomization algo here to make the byte value something based off of a key
            #ex self.EncodedKeys[i] = self.randomizeByte(byteValues[self.Alphabet.index(i)])

    # take a message from the user and encode it with the encoding keys.
    def encodeMessage(self,msg):
        self.startTimer()
        for i in msg.lower():
            self.Encoded.append(self.EncodedKeys[i])

        # we break off the encoded values into tuples of 3 so the Encoded list needs x%3==0 to be true for pixel processing
        while(len(self.Encoded)%3 != 0):
            self.Encoded.append(0)
        self.stopTimer('encoding message')

    def buildPixels(self):
        self.startTimer()
        index = 0
        for i in range(len(self.Encoded)//3):
            self.Pixels.append((self.Encoded[i], self.Encoded[i+1], self.Encoded[i+2]))
            counter = index + 3
        self.stopTimer('builing pixels')

    def buildCanvasBlock(self):
        self.startTimer()
        xval = 0
        yval = 0
        dimension = math.ceil(math.sqrt(len(self.Pixels)))
        self.canvas = Image.new('RGB', (dimension,dimension))
        print('total pixels = ' + str(len(self.Pixels)))
        print('dimension : ' + str(dimension))
        for pixel in range(len(self.Pixels)):
            self.canvas.putpixel((xval,yval), self.Pixels[pixel])
            xval = xval + 1
            if(xval == dimension):
                yval = yval + 1
                xval = 0
                if(yval == dimension):
                    yval = 0
        self.stopTimer('builing canvas block')

    def buildCanvas(self):
        self.startTimer()
        self.canvas = Image.new('RGB', (1, len(self.Pixels)))
        for x in range(len(self.Pixels)):
            self.canvas.putpixel((0,x), self.Pixels[x])
        self.stopTimer('builing canvas block')

    def encodeFile(self, path):
        self.startTimer()
        item = open(path, mode='r')
        for line in item:
            for char in line.lower():
                if(char == "\n" or char == "'" or char == '"'):
                    continue
                self.Encoded.append(self.EncodedKeys[char])
        self.stopTimer('encoding file')

    def save(self):
        print('Saving file ', self.fileName)
        self.canvas.save('../Images/' + self.fileName)
        os.system("start ../Images/" + self.fileName)

    def savecube(self): ##creates ribbons
        length = len(self.Pixels)
        canvas = Image.new('RGBA', (length, length))
        for x in range(length):
            for y in range(length):
                canvas.putpixel((x,y), self.Pixels[x])
        canvas.save('../Images/'+self.fileName)
        print('Saved file ', self.fileName)

    # Given a value((R,G,B)) functions returns its characer from encoded keys
    # def getCharacterForValue(self, val):
        # for key in self.EncodedKeys():

    def decode(self):
        xval = 0
        yval = 0
        decodedList = []
        img = self.canvas
        for pixel in math.pow(i.size[1] , 2):
            pix = img.getpixel((xval,yval))
            #get the rgb values
            vals = (pix[0],pix[1],pix[2])
            for key in self.EncodedKeys():
                if self.EncodedKeys[key] == pix[0]:
                    decodedList.append(key)
                if self.EncodedKeys[key] == pix[1]:
                    decodedList.append(key)
                if self.EncodedKeys[key] == pix[2]:
                    decodedList.append(key)
            # go through the incerementation for indexers.
            xval = xval + 1
            if(xval == dimension):
                yval = yval + 1
                xval = 0
                if(yval == dimension):
                    yval = 0


    def decodeMessage(self, path):
        xval = 0
        yval = 0
        decodedList = []
        img = Image.open(path)
        for pixel in math.pow(i.size[1] , 2):
            pix = img.getpixel((xval,yval))
            #get the rgb values
            vals = (pix[0],pix[1],pix[2])
            for key in self.EncodedKeys():
                if self.EncodedKeys[key] == pix[0]:
                    decodedList.append(key)
                if self.EncodedKeys[key] == pix[1]:
                    decodedList.append(key)
                if self.EncodedKeys[key] == pix[2]:
                    decodedList.append(key)
            # go through the incerementation for indexers.
            xval = xval + 1
            if(xval == dimension):
                yval = yval + 1
                xval = 0
                if(yval == dimension):
                    yval = 0

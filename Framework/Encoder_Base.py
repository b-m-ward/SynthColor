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
        self.decodedList = []

    # Uitlity func for starting a timer
    def startTimer(self):
        self.startTime = time.time()

    # Stop the timer and print result
    def stopTimer(self, msg):
        self.endTime = time.time()
        print('Time taken to ' + msg + ' : ' + str(self.endTime - self.startTime) + 's')

    # Writes decoded output to the filesystem in application directory "OutputFiles"
    def writeOutputFile(self):
        self.startTimer()
        num = str(random.randint(1,100))
        fileName = "..\OutputFiles\DecodeOutput-" + num + ".txt"
        with open(fileName,'w') as text_file:
            text_file.write(''.join(self.decodedList))
        self.stopTimer('write output file - ' + str(num))

    # Build out a dictionary for all the characters in self.Alphabet and their corresponding rgb values
    def buildList(self):
        byteValues = list(map(ord, self.Alphabet))
        for i in self.Alphabet:
            self.EncodedKeys[i] = byteValues[self.Alphabet.index(i)]

        #build out an inverted dictionary for lookups
        self.InverseKeys = {v:k for k,v in self.EncodedKeys.items()}
            # TODO: could write a randomization algo here to make the byte value something based off of a key
            #ex self.EncodedKeys[i] = self.randomizeByte(byteValues[self.Alphabet.index(i)])

    # Build a list of pixels from the encoded message values
    def buildPixels(self):
        self.startTimer()
        counter = 0
        for i in range(len(self.Encoded)//3):
            self.Pixels.append((self.Encoded[counter], self.Encoded[counter+1], self.Encoded[counter+2]))
            counter = counter + 3
        self.stopTimer('builing pixels')

    # Builds out the image from encoded message
    def buildCanvas(self):
        self.startTimer()
        xval = 0
        yval = 0
        dimension = math.ceil(math.sqrt(len(self.Pixels)))
        self.canvas = Image.new('RGB', (dimension,dimension))
        # print('total pixels = ' + str(len(self.Pixels)))
        # print('dimension : ' + str(dimension))
        for pixel in range(len(self.Pixels)):
            self.canvas.putpixel((xval,yval), self.Pixels[pixel])
            xval = xval + 1
            if(xval == dimension):
                yval = yval + 1
                xval = 0
                if(yval == dimension):
                    yval = 0
        self.stopTimer('builing canvas block')

    # encode a file
    def encodeFile(self, path):
        self.startTimer()
        item = open(path, mode='r')
        for line in item:
            for char in line.lower():
                if(char == "\n" or char == "'" or char == '"'):
                    continue
                self.Encoded.append(self.EncodedKeys[char])
        self.stopTimer('encoding file')

    # Take a message from the user and encode it with the encoding keys.
    def encodeMessage(self,msg):
        self.startTimer()
        for i in msg.lower():
            self.Encoded.append(self.EncodedKeys[i])

        # we break off the encoded values into tuples of 3 so the Encoded list needs x%3==0
        while(len(self.Encoded)%3 != 0):
            self.Encoded.append(0)
        self.stopTimer('encode user input')

    def save(self):
        self.canvas.save('../Images/' + self.fileName)
        os.system("start ../Images/" + self.fileName)
        print('Saved file ', self.fileName)

    def savecube(self): ##creates ribbons
        length = len(self.Pixels)
        canvas = Image.new('RGBA', (length, length))
        for x in range(length):
            for y in range(length):
                canvas.putpixel((x,y), self.Pixels[x])
                print('Saved file ', self.fileName)
        canvas.save('../Images/'+self.fileName)

    # Decodes an image one pixel at a time based on the EncodedKeys
    def decodeMessage(self, path=None):
        xval = 0
        yval = 0
        self.decodedList = []
        self.startTimer()

        # if passed a path then decode the file otherwise assume we are decoding from memory
        if path is None:
            img = self.canvas
        else:
            img = Image.open(path)

        for pixel in range(int(math.pow(img.size[1] , 2))):
            #unpack the tuple into rgb values
            r,g,b = img.getpixel((xval,yval))

            # deffer processing if this pixel is a filler pixel
            if(r == 0 and g == 0 and b == 0):
                continue
            #self.decodedPixels.append((r,g,b)) # here temp for debuging
            if r in self.InverseKeys:
                self.decodedList.append(self.InverseKeys[r])
            if g in self.InverseKeys:
                self.decodedList.append(self.InverseKeys[g])
            if b in self.InverseKeys:
                self.decodedList.append(self.InverseKeys[b])

            # go through the incerementation for indexers.
            xval = xval + 1
            if(xval == int(img.size[0])):
                yval = yval + 1
                xval = 0
                if(yval == int(img.size[0])):
                    yval = 0
        self.stopTimer('decoding image from file')
        self.writeOutputFile()

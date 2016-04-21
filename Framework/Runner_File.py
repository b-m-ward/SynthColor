from Encoder_Base import Encoder
import sys

user_input = input('Enter a file to encode: ')
e = Encoder()
e.encodeFile('..\TestFiles\\' + user_input)
e.buildPixels()
e.buildCanvas()
e.save()

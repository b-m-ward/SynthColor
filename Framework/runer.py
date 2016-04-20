from ../Framework/testClass import Encoder, Ribbon, lang
e = Ribbon()
e.encode('some test message')
e.save()
e.decode()

f = lang()
f.encode('this is some test text to mess with words')
f.save()
f.decode()

g = Encoder()
g.open()
g.save()
g.decode()

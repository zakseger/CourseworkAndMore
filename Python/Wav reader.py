import wave,struct
from binascii import hexlify
f = wave.open('piano2.wav', 'r')

for i in range(5,10):
    frame = f.readframes(i)
    print(frame)
struct.unpack('<H',frame)



  

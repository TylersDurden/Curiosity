import numpy as np
import struct
import wave

sampleRate = 44100.0 # hertz
duration = 1.0 # seconds
frequency = 440.0 # hertz
obj = wave.open('sound.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
for i in range(99999):
   value = np.sin(i/frequency)*500 + np.sin(i/frequency*2)*300
   data = struct.pack('<h', value)
   obj.writeframesraw(data)
obj.close()


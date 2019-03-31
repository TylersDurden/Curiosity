import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import struct
import wave
import sys


def create_tone_sequence(obj):
   for i in range(10000):
      value = np.sin(i / 2) * 500 + np.sin(i / 3) * 500 + \
              np.sin(i / 4) * 400
      data = struct.pack('<h', value)
      obj.writeframesraw(data)
   for i in range(12000):
      value = np.sin(i / 5) * 500 + np.sin(i / 3) * 500 + \
              np.sin(i) * i / 3
      data = struct.pack('<h', value)
      obj.writeframesraw(data)
   for i in range(10000):
      value = np.sin(i) * 500 + np.sin(i / 2) * 400 + \
              np.sin(i / 4) * i
      data = struct.pack('<h', value)
      obj.writeframesraw(data)
   for i in range(15000):
      value = np.sin(i / 6) * 500 + np.sin(i / 3) * 300 + \
              np.sin(i / 4) * 700 / (i + 1)
      data = struct.pack('<h', value)
      obj.writeframesraw(data)
   for i in range(18000):
      value = np.sin(i * 4) * 500 / (i + 1) + np.sin(i / 3) * 300 + \
              np.sin(i / 4) * 420
      data = struct.pack('<h', value)
      obj.writeframesraw(data)
   for i in range(18000):
      value = np.sin(i * 4) * 500 / (i + 1) + np.sin(i / 3) * 300 + \
              np.sin(i / 4) * 420
      data = struct.pack('<h', value)
      obj.writeframesraw(data)


def linear_frequency_chirp(obj):
    f = 10
    for i in range(90000):
       f +=i
       value = np.sin((f)/1000) * 1000
       data = struct.pack('<h', value)
       obj.writeframesraw(data)
    return obj


def wobble(obj):
   for i in range(24000):
       value = np.sin(i+i*np.cos(i/400))*1000*(np.sin(i/300))
       data = struct.pack('<h', value)
       obj.writeframesraw(data)
   return obj


def analyze(file_name):
    data = {}
    audio = wave.open(file_name, 'r')
    sample_rate, aud = np.array(wavfile.read(file_name))
    n_frames = audio.getnframes()
    data['fr'] = sample_rate
    data['length'] = n_frames
    data['samp_size'] = audio.getsampwidth()
    data['nchan'] = audio.getnchannels()
    data['audio'] = aud
    data['name'] = file_name
    return data


def main():
    if 'demo' in sys.argv:
       sampleRate = 44100.0  # hertz
       duration = 1.0  # seconds
       frequency = 440.0  # hertz
       obj = wave.open('sound.wav', 'w')
       obj.setnchannels(1)  # mono
       obj.setsampwidth(2)
       obj.setframerate(sampleRate)
       create_tone_sequence(obj)
       create_tone_sequence(obj)
       obj.close()

    if 'load' in sys.argv:
       song = analyze(sys.argv[2])
       print np.array(song['audio']).shape
       plt.plot(song['audio'])
       plt.show()

    if 'f_chirp' in sys.argv:
        obj = wave.open('chirp.wav', 'w')
        obj.setnchannels(1)
        obj.setsampwidth(2)
        obj.setframerate(44100)
        linear_frequency_chirp(obj).close()

    if 'wub' in sys.argv:
         obj = wave.open('wobble.wav', 'w')
         obj.setnchannels(1)
         obj.setsampwidth(2)
         obj.setframerate(44100)
         wobble(obj).close()

if __name__ == '__main__':
   main()

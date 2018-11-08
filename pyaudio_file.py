import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
spf = wave.open('/home/pi/Desktop/c.wav' ,'r')

#Extract Raw Audio from Wav File
signal = spf.readframes(5001)
signal = np.fromstring(signal, 'Int16')


#If Stereo
#if spf.getnchannels() == 2:
 #   print 'Just mono files'
 #	 sys.exit(0)
f = open("array.txt", "w")
f.write(signal)
plt.figure(1)
plt.title('Signal Wave...')
plt.plot(signal)
plt.show()









B
B
B
A
A
A
A
A
A


""" Exercise 3 """

import numpy as np
import pandas as pd
import matplotlib.pylab as plt

# Part A

Data1 = pd.read_csv("Codes/data/piano.txt", sep=" ", header= None)
Data2 = pd.read_csv("Codes/data/trumpet.txt", sep=" ", header= None)

Data1 = np.squeeze(Data1)
Data2 = np.squeeze(Data2)

plt.plot(Data1)
plt.title("Piano waveform")
plt.xlabel("n")
plt.ylabel("Amplitude")
#plt.savefig("Q3_a_1.png")
plt.show()

plt.plot(Data2)
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title("Trumpet waveform")
#plt.savefig("Q3_a_2.png")
plt.show()

c_1 = np.fft.fft(Data1)
c_2 = np.fft.fft(Data2)

plt.plot(abs(c_1[0:10000])**2)
plt.xlabel("k")
plt.ylabel("|c_k|^2")
plt.title("FFT of Piano")
#plt.savefig("Q3_a_3.png")
plt.show()


plt.plot(abs(c_2[0:10000])**2)
plt.xlabel("k")
plt.ylabel("|c_k|^2")
plt.title("FFT of Trumpet")
#plt.savefig("Q3_a_4.png")
plt.show()

"""While observing the graph we can conclude that the trumpet plays at a higher frequency when compared to piano."""

# Part B

sampling = 44100

freq_1 = np.fft.fftfreq(len(Data1),d=1/sampling)
freq_2 = np.fft.fftfreq(len(Data2),d=1/sampling)

freq_max_1 = freq_1[np.argmax(abs(c_1[0:10000])**2)]
freq_max_2 = freq_2[np.argmax(abs(c_2[0:10000])**2)]

print(f"Frequency generating the maximum amplitude in piano is {freq_max_1}")
print(f"Frequency generating the maximum amplitude in trumpet is {freq_max_2}")

"""
Frequency generating the maximum amplitude in piano is 524.79 Hz
Frequency generating the maximum amplitude in trumpet is 1043.847 Hz

This is in accordance with the actual fact that the trumpets playes the C6 note (approx 1046 Hz) while pianos plays the C5 note
(approx 523 Hz)."""
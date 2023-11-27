""" Exercise 6 """

import numpy as np
import pandas as pd
import matplotlib.pylab as plt

def FFT(x):
    
    # We will use the Cooley-Tukey algorithm for computing the fft of a function.
    
    N = len(x) # Base case in the recursion
    if N == 1:
        return x
    
    even_fft = FFT(x[::2]) # x[::2] would return a new sequence consisting of the elements at indices 0, 2, 4, etc. of x
    odd_fft = FFT(x[1::2]) # x[1::2] would return a new sequence consisting of the elements at indices 1, 3, 5, etc. of x
    
    twiddle_odd_fft = [np.exp(-1j*(2*np.pi*k)/N)*odd_fft[k] for k in range(int(N/2))] # np.exp(-1j*(2*np.pi*k)/N) is called the twidle factor
    
    fft = []
    for e, t in zip(even_fft, twiddle_odd_fft): # zip function creates a list of 2-tuples
        fft.append(e + t)
    for e, t in zip(even_fft, twiddle_odd_fft):
        fft.append(e - t)
    
    return fft

Data = pd.read_csv("Codes/data/pitch.txt", sep=" ", header= None )
Data = np.array(np.squeeze(Data))

c_1 = FFT(Data)
c_2 = np.fft.fft(Data)

fig , ax = plt.subplots(2,1)    

ax[0].plot(abs(np.array(c_1)))
ax[0].set_title("FFT using the recursion algorithm")

fig.subplots_adjust(hspace=0.5)

ax[1].plot(abs(np.array(c_2)))
ax[1].set_title("FFT using the numpy library")

plt.savefig("Q6.png")
plt.show()

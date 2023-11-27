""" Exercise 15 """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("stm.txt", header=None, sep=' ')

plt.pcolormesh(data)
plt.colorbar()
plt.title('Measurements of the (111) surface of silicon')
plt.savefig('Q15.png')
plt.show()


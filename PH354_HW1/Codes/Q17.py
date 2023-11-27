""" Exercise 17 """

""" For a certain c we iteratively find z_n+1 using the relation z_n+1 = z_n**2 + c and z_0 = 0 + 0i. If the |z_n+1| <= 2 then 
    we consider it to be in the Mandelbrot set, else not. The number of iterations performed here is 100. """

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

"""N = 100"""
x = np.arange(-2,2+0.005,0.005)
y = np.arange(-2,2+0.005,0.005)

def absolute(z):
    return np.sqrt(z[0]**2 + z[1]**2)

Num_Iter = np.zeros([len(x),len(y)])

def Z(a,b):
    z = np.zeros(2)
    i = 0
    while i < 100:
        if absolute(z) > 2:
            iter = i
            break
        else: 
            z = [z[0]**2 - z[1]**2 + a, 2*z[0]*z[1] + b] 
            i += 1
    if i == 100:
        return [0,100]
    else:
        return [1,iter]
    

color = np.zeros([len(x),len(y)])

for j in range(0,len(x)):
    for k in range(0,len(y)):
        color[j][k] = Z(x[j],y[k])[0]
        Num_Iter[j][k] = Z(x[j],y[k])[1]

plt.pcolormesh(x,y,np.transpose(color),cmap= cm.gray)
plt.title('Mandelbrot Set')
plt.savefig('Q15_bw.png')
plt.show()

# Hot and Jet Schemes

plt.pcolormesh(x,y,np.transpose(Num_Iter),cmap= 'jet')
plt.title('Mandelbrot Set')
plt.savefig('Q15_jet.png')
plt.show()

plt.pcolormesh(x,y,np.transpose(Num_Iter),cmap= 'hot')
plt.title('Mandelbrot Set')
plt.savefig('Q15_hot.png')
plt.show()
""" Exercise 17 """

from scipy.constants import epsilon_0
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'.')
from res.Gauss_Quad import *

# Part A

def V(x,y):
    if np.sqrt((x-0.05)**2 + y**2) == 0 or np.sqrt((x+0.05)**2 + y**2) == 0:
        return np.nan
    else:
        return (1/(4*np.pi*epsilon_0))*(1/(np.sqrt((x-0.05)**2 + y**2)) - 1/(np.sqrt((x+0.05)**2 + y**2)))

x = np.linspace(-0.5,0.5,101)
y = np.linspace(-0.5,0.5,101)

map = np.zeros([len(x),len(y)]) 

for i in range(0,len(x)):
    for j in range(0,len(y)):
        map[i][j] = V(x[i],y[j])

plt.pcolormesh(x,y,map.transpose(),vmax=1/(4*np.pi*epsilon_0),vmin=-1/(4*np.pi*epsilon_0))
plt.title('Potential')
plt.xlabel('x (in m)')
plt.ylabel('y (in m)')
plt.colorbar()
#plt.savefig("Q17_1")
plt.show()

# Part B

def Field(V,x,y):
    
    dim_x,dim_y = len(x),len(y)

    E = np.zeros([dim_x,dim_y])
    Direction = np.zeros([dim_x,dim_y])

    for i in range(1,dim_x-1):
        for j in range(1,dim_y-1):
            dV_dx = (-V(x[i+1],y[j])+V(x[i-1],y[j]))/(2*(x[1]-x[0]))
            dV_dy = (-V(x[i],y[j+1])+V(x[i],y[j-1]))/(2*(y[1]-y[0]))
            E[i][j] = np.sqrt(dV_dx**2 + dV_dy**2)
            Direction[i][j] = np.arctan2(dV_dy,dV_dx)

    return E,Direction

E,Direction = Field(V,x,y)

plt.pcolormesh(E.transpose(),cmap='jet',vmax=1000*1/(4*np.pi*epsilon_0),vmin=0)
plt.title('Magnitude of the Electric Field')
plt.xlabel('x (in m)')
plt.ylabel('y (in m)')
plt.colorbar()
#plt.savefig("Q17_2")
plt.show()

plt.pcolormesh(Direction.transpose(),cmap='hsv')
plt.title('Direction of the Electric Field')
plt.xlabel('x (in m)')
plt.ylabel('y (in m)')
plt.colorbar()
#plt.savefig("Q17_3")
plt.show()

X,Y = np.meshgrid(x,y)

u = E.transpose()*(np.cos(Direction.transpose()))
v = E.transpose()*(np.sin(Direction.transpose()))

plt.streamplot(X,Y,u,v)
plt.title('Electric Field')
plt.xlabel('x (in m)')
plt.ylabel('y (in m)')
#plt.savefig('Q17_stream.png')
plt.show()

# Part C
L = 0.1

x1,w1 = gaussxwab(10,-L/2,L/2)
x2,w2 = gaussxwab(10,-L/2,L/2)

def Square_V(x,y):

    # Surface charge density
    def sigma(u,v):
        return 100*(np.sin((2*np.pi*u)/L))*(np.sin((2*np.pi*v)/L))

    val = 0
    for i in range(0,len(x1)):
        for j in range(0,len(x2)):
            val += w1[i]*w2[j]*(sigma(x1[i],x2[j])/(np.sqrt((x-x1[i])**2 + (y-x2[j])**2)))
    
    return val*1/(4*np.pi*epsilon_0)

new_potential = np.zeros([len(x),len(y)])

for i in range(0,len(x)):
    for j in range(0,len(y)):
        new_potential[i][j] = Square_V(x[i],y[j]) 

new_E,new_Direction = Field(Square_V,x,y)

plt.pcolormesh(new_potential.transpose(),vmax = 1/(4*np.pi*epsilon_0),vmin =-1/(4*np.pi*epsilon_0))
plt.title('Potential')
plt.xlabel('x (in m)')
plt.ylabel('y (in m)')
plt.colorbar()
#plt.savefig("Q17_4")
plt.show()

plt.pcolormesh(new_Direction.transpose(),cmap='hsv')
plt.title('Direction of the Electric Field')
plt.xlabel('x (in m)')
plt.ylabel('y (in m)')
plt.colorbar()
#plt.savefig("Q17_5")
plt.show()

plt.pcolormesh(new_E.transpose(),cmap='jet')
plt.title('Magnitude of the Electric Field')
plt.xlabel('x (in m)')
plt.ylabel('y (in m)')
plt.colorbar()
#plt.savefig("Q17_6")
plt.show()
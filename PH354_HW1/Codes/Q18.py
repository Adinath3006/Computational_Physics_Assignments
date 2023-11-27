""" Exercise 18 """

"""We use the line y = mx + c to fit the data where m and c are found out using the least squares method:

                    m = (E_xy - E_x*E_y)/(E_xx - E_x**2) and c = (E_xx*E_y - E_x*E_xy)/(E_xx - E_x**2) 
                    
                    E_x = (1/N)*sum(x_i) ; E_y = (1/N)*sum(y_i) ; E_xx = (1/N)*sum(x_i**2) ; E_xy = (1/N)*sum(x_i*y_i)"""

# Part A

import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import h

x = []
y = []

with open('millikan.txt','r') as data:
    plot = csv.reader(data,delimiter=' ')

    for rows in plot:
        x.append(float(rows[0]))
        y.append(float(rows[1]))

plt.scatter(x,y,c = 'red',marker='.')
plt.xlabel('Frequency in (Hertz)')
plt.ylabel('Voltage in (Volts)')
plt.title('Millikan Experiment')
plt.savefig("Q18_a.png")
plt.show()

# Part B

N = len(x)

E_x = (1/N)*sum(x)
E_y = (1/N)*sum(y)
E_xx = (1/N)*sum(np.power(x,2))
E_xy = (1/N)*sum(np.multiply(x,y))

m = (E_xy - E_x*E_y)/(E_xx - E_x**2)
c = (E_xx*E_y - E_x*E_xy)/(E_xx - E_x**2)

# Part C

x_fit = np.linspace(x[0],x[N-1],100)
y_fit = m*x_fit + c*(np.ones(len(x_fit)))

plt.scatter(x,y,c = 'red',marker='.')
plt.plot(x_fit,y_fit)
plt.xlabel('Frequency in (Hertz)')
plt.ylabel('Voltage in (Volts)')
plt.title('Millikan Experiment')

# Part D

"""Using the equation V = (h/e)*f - W where W is the work function of the metal, we can now find the value of the Planck's constant 
    using the slope of our linear fit V = m*f + c, this implies that h = m*e"""

e = 1.602e-19

h_exp = m*e

plt.text(0.56e15,2.5,"Experimentally obtained Planck's Constant: {:.3E} \n Literature valure of Planck's Constant: {:.3E} \n Percentage Error: {:.3f}".format(h_exp,h,(h_exp-h)*100/h),fontsize = 10)
plt.savefig("Q18_b.png")
plt.show()
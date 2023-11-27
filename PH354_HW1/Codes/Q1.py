""" Exercise 1 """

""" The formula for the time taken by the ball to reach the grounf is given as t = ((2*height)/g))**0.5 """

from scipy.constants import g

height = float(input("Enter the height of the tower (in m) : "))

time =  (2*height/g)**(0.5)

print("The time that the ball takes to reach the ground is (in sec) : {:0.3f}".format(time))

""" Thus the time that the ball takes to reach the ground is : 4.516 s """
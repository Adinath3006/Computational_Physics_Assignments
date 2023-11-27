""" Exercise 11 """
"""All the results and graphs of the following code can be found in 'Outputs and Derivation' and 'Plots and Animations' directories"""
import random
import matplotlib.pyplot as plt
import numpy as np

L = 101 # side of a square

x_plot = np.arange(-0.5, L+3)
y_plot = np.arange(-0.5, L+3)

def point_assign(dir,i,j):
    if dir == 1:
        return [i+1,j]
    elif dir == 2:
        return [i,j+1]
    elif dir == 3:
        return [i-1,j]
    else:
        return [i,j-1]
        
def modif_brownian():
    x_end = []
    y_end = []
    neighbour = []
    init_adjacent = [[ (L-1)/2+1, (L-1)/2],[ (L-1)/2-1, (L-1)/2],[(L-1)/2, (L-1)/2+1],[ (L-1)/2, (L-1)/2-1]]
    advance = 1
    while advance == 1:
        # Initializing the array which stores the position of particle
        i_pos,j_pos = (L-1)/2,(L-1)/2
        end = 0
        while end < 1:
        # Assign direction for the next point according to the current location
            if i_pos == 0:
                x_end.append(i_pos)
                y_end.append(j_pos)
                neighbour.append([i_pos,j_pos])
                end = 1
            elif i_pos == L-1:
                x_end.append(i_pos)
                y_end.append(j_pos)
                neighbour.append([i_pos,j_pos])
                end = 1
            else:
                if j_pos == 0:
                    x_end.append(i_pos)
                    y_end.append(j_pos)
                    neighbour.append([i_pos,j_pos])
                    end = 1
                elif j_pos == L-1:
                    x_end.append(i_pos)
                    y_end.append(j_pos)
                    neighbour.append([i_pos,j_pos])
                    end = 1
                else:
                    if not neighbour:
                        dir = random.choice([1,2,3,4])
                        move = point_assign(dir,i_pos,j_pos)
                        i_pos = move[0]
                        j_pos = move[1]
                    else:
                        next_move = [[i_pos+1,j_pos],[i_pos-1,j_pos],[i_pos,j_pos+1],[i_pos,j_pos-1]]
                        for k in range(4):
                            if next_move[k] in neighbour:
                                proceed = 0
                                break
                            else:
                                proceed = 1
                        if proceed == 0:
                            x_end.append(i_pos)
                            y_end.append(j_pos)
                            neighbour.append([i_pos,j_pos])
                            end = 1
                        else:
                            dir = random.choice([1,2,3,4])
                            move = point_assign(dir,i_pos,j_pos)
                            i_pos = move[0]
                            j_pos = move[1]
            for k in range(4):
                if init_adjacent[k] in neighbour:
                    advance = 0
                    x_end.append((L-1)/2)
                    y_end.append((L-1)/2)
                    break
                else:
                    advance = 1
    plt.scatter(x_end,y_end,marker='.',c=range(len(x_end)))
    plt.xlim(-0.6, L-0.4)
    plt.ylim(-0.6, L-0.4)
    plt.title("DLA using brownian motion")
    plt.vlines(x_plot, ymin = -0.6, ymax = L+4, color = 'blue', linewidth = 0.2)
    plt.hlines(y_plot, xmin = -0.6, xmax = L+4, color = 'blue', linewidth = 0.2)
    plt.colorbar()
    plt.show()
            
modif_brownian()

def DLA():
    
    import math
    anchors = []
    anchors.append([(L-1)/2,(L-1)/2])
    x_end = []
    x_end.append((L-1)/2)
    y_end = []
    y_end.append((L-1)/2)
    x_circle = []
    y_circle = []
    R = range(1,int(L/2)+1)
    r = 1
    while r < L/4:
        theta = random.uniform(0,2*np.pi)
        x_curve = r*np.cos(theta) + (L-1)/2
        y_curve = r*np.sin(theta) + (L-1)/2
        # Choosing the closest point to the circle
        x_grid,y_grid = math.ceil(x_curve),math.ceil(y_curve)
        # Performing random walk with this point
        x_walk,y_walk = x_grid,y_grid
        end = 0
        while np.sqrt( (x_walk-(L-1)/2)**2 + (y_walk-(L-1)/2)**2 ) <= 2*r and end < 1:
            next_move = [[x_walk+1,y_walk],[x_walk-1,y_walk],[x_walk,y_walk+1],[x_walk,y_walk-1]]
            for k in range(4):
                if next_move[k] in anchors:
                    proceed = 0
                    break
                else:
                    proceed = 1
            if proceed == 0:    
                x_end.append(x_walk)
                y_end.append(y_walk)
                x_circle.append(x_grid)
                y_circle.append(y_grid)
                anchors.append([x_walk,y_walk])
                r += 1
                end = 1
            else:
                dir = random.choice([1,2,3,4])
                move = point_assign(dir,x_walk,y_walk)
                x_walk = move[0]
                y_walk = move[1]
    # Plotting the anchored points
    plt.scatter(x_end,y_end,marker='.',c=range(len(x_end)))
    plt.xlim(-0.6, L-0.4)
    plt.ylim(-0.6, L-0.4)
    plt.title("Original DLA algorithm implementation")
    plt.vlines(x_plot, ymin = -0.6, ymax = L+4, color = 'blue', linewidth = 0.2)
    plt.hlines(y_plot, xmin = -0.6, xmax = L+4, color = 'blue', linewidth = 0.2)
    plt.colorbar()
    plt.show()  
    # Plotting the selected points in the circle
    plt.scatter(x_circle,y_circle,marker='.',c='black')
    plt.xlim(-0.6, L-0.4)
    plt.ylim(-0.6, L-0.4)
    plt.title("Selected points from circles of varying radius")
    plt.vlines(x_plot, ymin = -0.6, ymax = L+4, color = 'blue', linewidth = 0.2)
    plt.hlines(y_plot, xmin = -0.6, xmax = L+4, color = 'blue', linewidth = 0.2)
    plt.show()          
        
DLA()        
        
    
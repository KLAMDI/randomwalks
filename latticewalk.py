##Note: this program was copied from the website https://introcs.cs.princeton.e
#du/python/14array/selfavoid.py.html.

import math
import numpy as np
import matplotlib.pyplot as plt
import random

def latticewalk(latsize, Nsteps):
    i = 0
    
    #A lattice array is created with all elements set to false
    lattice = np.array([[False for x in xrange(latsize)] for y in 
        xrange(latsize)])
        
    #The walk starts at the center of the lattice 
    x = latsize/2
    y = latsize/2
    xlist = []
    ylist = []
    
    #The walk must remain within the lattice
    while ((x > 0) and (x < latsize-1) and (y > 0) and (y < latsize-1) and 
    i <= Nsteps):
        
        #The current position is set to true
        lattice[x][y] = True
        xlist.append(x)
        ylist.append(y)
        
        #If the walk reaches a dead end, the simulation is terminated
        if (lattice[x-1][y] and lattice[x+1][y] and lattice[x][y-1] and 
        lattice[x][y+1]):
            break
        rand = random.randrange(1, 5)
        
        #The walk can only move to points that have not yet been occupied
        if   (rand == 1) and (not lattice[x+1][y]):
            x += 1
            i += 1
        elif (rand == 2) and (not lattice[x-1][y]):
            x -= 1
            i += 1
        elif (rand == 3) and (not lattice[x][y+1]):
            y += 1
            i += 1
        elif (rand == 4) and (not lattice[x][y-1]):
            y -= 1
            i += 1
    return (xlist, ylist)

rlist = latticewalk(100, 100)    
plt.figure(1)
plt.clf()
plt.plot(rlist[0], rlist[1], 'b', rlist[0][0], rlist[1][0], 'go')
plt.scatter(rlist[0], rlist[1])
plt.title('Lattice walk')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
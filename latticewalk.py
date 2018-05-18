##Note: this program was copied from the website https://introcs.cs.princeton.e
#du/python/14array/selfavoid.py.html.

import math
import numpy as np
import matplotlib.pyplot as plt
import random

l = 100
n = 10

def latticewalk(latsize, Nsteps):
    walkslist = []
    for attempt in range(0, 4*3**(Nsteps-1)):
        i = 0
        movelist = []
        
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
                movelist.append('r')
                i += 1
            elif (rand == 2) and (not lattice[x-1][y]):
                x -= 1
                movelist.append('l')
                i += 1
            elif (rand == 3) and (not lattice[x][y+1]):
                y += 1
                movelist.append('u')
                i += 1
            elif (rand == 4) and (not lattice[x][y-1]):
                y -= 1
                movelist.append('d')
                i += 1
        
        del movelist[-1]
        if movelist not in walkslist:        
            walkslist.append(movelist)
    return (xlist, ylist, len(walkslist))

rlist = latticewalk(l, n) 
print 'Approximate number of unique walk for %i steps: %i' % (n, rlist[2])
print 'Approximate connective constant: %f' % (rlist[2]**(1/float(n)))
plt.figure(1)
plt.clf()
plt.plot(rlist[0], rlist[1], 'b', rlist[0][0], rlist[1][0], 'go')
plt.scatter(rlist[0], rlist[1])
plt.title('Lattice walk')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
##Note: parts of this program were copied from the website 
#https://introcs.cs.princeton.edu/python/14array/selfavoid.py.html

import numpy as np
import matplotlib.pyplot as plt
import random

l = 100
n = 300
walkslist = []


#Do you wanna calculate a connective constant~?
calc_connective = False

#Set to true for a cool animation
#might not wanna do this if you're calculating the connective constant
anim = True

def walkCalc(latsize, Nsteps):
    i = 1
    movelist = []
    
    #A lattice array is created with all elements set to false
    lattice = np.array([[False for x in xrange(latsize+1)] for y in 
        xrange(latsize+1)])
        
    #The walk starts at the center of the lattice 
    x = latsize/2
    y = latsize/2
    xlist = []
    ylist = []
    
    #Creating edges of the box
    for j in range(0, latsize + 1):
        lattice[j][latsize] = True
        lattice[latsize][j] = True
        lattice[0][j] = True
        lattice[j][0] = True

    #The walk must remain within the lattice
    while i <= Nsteps:
        
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
        #and that aren't an edge
        if   (rand == 1) and (not lattice[x+1][y]):
            if x + 1 < latsize:
                x += 1
                movelist.append('r')
                i += 1
        elif (rand == 2) and (not lattice[x-1][y]):
            if x -1 > 0:
                x -= 1
                movelist.append('l')
                i += 1
        elif (rand == 3) and (not lattice[x][y+1]):
            if y + 1 < latsize:
                y += 1
                movelist.append('u')
                i += 1
        elif (rand == 4) and (not lattice[x][y-1]):
            if y -1 > 0:
                y -= 1
                movelist.append('d')
                i += 1      
        
        #Animation if you wanna
        if anim == True: 
            plt.figure(1)
            plt.clf()
            plt.plot(xlist, ylist)
            plt.draw()
            plt.pause(0.001)
        
    return(xlist, ylist, movelist)
        
def latticewalk(latsize, Nsteps, calcCC):
    if calcCC == True:
        for attempt in range(0, 4*3**(Nsteps-1)):
            results = walkCalc(latsize, Nsteps)
            if results[2] not in walkslist:        
                walkslist.append(results[2])
        return results + (len(walkslist),)
    else:
        return walkCalc(latsize, Nsteps) + (0,)

rlist = latticewalk(l, n, calc_connective) 
print 'Approximate number of unique walk for %i steps: %i' % (n, rlist[3])
print 'Approximate connective constant: %f' % (rlist[3]**(1/float(n)))
plt.figure(1)
plt.clf()
plt.plot(rlist[0], rlist[1], 'b', rlist[0][0], rlist[1][0], 'go')
plt.scatter(rlist[0], rlist[1])
plt.title('Lattice walk')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
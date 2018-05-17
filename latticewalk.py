import math
import numpy as np
import matplotlib.pyplot as plt
import random

def latticewalk(latsize, Nsteps):
    xlist = [latsize/2]
    ylist = [latsize/2]
    i = 0
    while i < Nsteps:
        rand = random.randrange(1, 5)
        if rand == 1:
            xlist.append(xlist[i] + 1)
            ylist.append(ylist[i])
            i+=1
        elif rand == 2:
            xlist.append(xlist[i] - 1)
            ylist.append(ylist[i])
            i+=1
        elif rand == 3:
            xlist.append(xlist[i])
            ylist.append(ylist[i] + 1)
            i+=1
        else:
            xlist.append(xlist[i])
            ylist.append(ylist[i] - 1)
            i+=1
    return (xlist, ylist)

rlist = latticewalk(100, 1000)    
plt.figure(1)
plt.clf()
plt.plot(rlist[0], rlist[1], 'b', rlist[0][0], rlist[1][0], 'go')
plt.title('Lattice walk')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
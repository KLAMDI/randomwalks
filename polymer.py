import math
import numpy as np
import matplotlib.pyplot as plt
import random

#The number of base pairs
N = 10

def constantwalk(N):
    crosslist = []
    rlist = []
    
    #This loop whil generate mutliple siumlations
    for i in range(0, 10000):    
        xnext = 0
        ynext = 0
        xlist = [0]
        ylist = [0]
        cross = 0
        
        #This loop generates the random walk
        for j in range(0, N):
            angle = 2*math.pi*random.random()
            xnext = math.cos(angle) + xlist[j]
            ynext = math.sin(angle) + ylist[j]
            if xnext == xlist[0] and ynext == ylist[0] and cross == 0:
                cross = j       
            xlist.append(xnext)
            ylist.append(ynext)
        crosslist.append(cross)
        
        #After every simulation the end-to-end distance is calculated
        r = math.sqrt((xlist[-1] - xlist[0])**2 + (ylist[-1] - ylist[0])**2)
        rlist.append(r)
        
    #The mean end-to-end distance is printed
    print np.mean(rlist)
        
    # plt.figure(1)
    # plt.clf()
    # plt.plot(xlist, ylist, 'b', xlist[0], ylist[0], 'go', xlist[-1], ylist[-1], 
    #     'ro')
    # plt.show()
    
constantwalk(N)
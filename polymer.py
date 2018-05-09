import math
import numpy as np
import matplotlib.pyplot as plt
import random

#The number of base pairs
N = 10
Nlist = [10, 50, 100, 500, 1000, 5000, 10000]
meanlist = []

def constantwalk(N):
    rlist = []
    
    #This loop will generate mutliple siumlations
    for i in range(0, 1000):  
        rcm = 0  
        xnext = 0
        ynext = 0
        xlist = [0]
        ylist = [0]
        
        #This loop generates the random walk
        for j in range(0, N):
            angle = 2*math.pi*random.random()
            xnext = math.cos(angle) + xlist[j]
            ynext = math.sin(angle) + ylist[j]     
            xlist.append(xnext)
            ylist.append(ynext)
            rcm += math.sqrt((xlist[-1] - xlist[0])**2 + (ylist[-1] - 
                ylist[0])**2)
        #After every simulation the end-to-end distance is calculated
        r = math.sqrt((xlist[-1] - xlist[0])**2 + (ylist[-1] - ylist[0])**2)
        rlist.append(r)
        
    #The mean end-to-end distance is printed
    return np.mean(rlist)

##A plot is generated of the end-to-end distance as a function of base pair 
#number
for i in Nlist:
    meanlist.append(constantwalk(i))
    
plt.figure(1)
plt.clf()
plt.plot(Nlist, meanlist, 'b')
plt.show()
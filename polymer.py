# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt
import random

#The number of base pairs
N = 10
Nlist = [10, 50, 100, 500, 1000, 5000, 10000]
rmeanlist = []
Rgmeanlist = []

##The following two functions will check if two line segments intersect based on 
#their oriëntation.
def ccw(Ax, Ay, Bx, By, Cx, Cy):
    return (Cy-Ay)*(Bx-Ax) > (By-Ay)*(Cx-Ax)
    
def intersect(x0, y0, x1, y1, xprev, yprev, xnext, ynext):
    return ccw(x0, y0, x1, y1, xprev, yprev) != ccw(x0, y0, x1, y1, xnext, 
        ynext) and ccw(xprev, yprev, xnext, ynext, x0, y0) != ccw(xprev, yprev, 
        xnext, ynext, x1, y1)

def constantwalk(N):
    rlist = []
    crosslist = []
    Rglist = []
    
    #This loop will generate multiple siumlations
    for i in range(0, 1000): 
        cross = 0 
        rcm = 0
        Rg = 0 
        xlist = [0]
        ylist = [0]
        
        #This loop generates the random walk
        for j in range(0, N):
            angle = 2*math.pi*random.random()
            xnext = math.cos(angle) + xlist[j]
            ynext = math.sin(angle) + ylist[j]     
            xlist.append(xnext)
            ylist.append(ynext)
            
            ##This statement checks if a base pair intersected with the first
            #base pair
            if cross == 0 and j > 1 and intersect(0, 0, xlist[1], ylist[1], 
            xlist[j], ylist[j], xnext, ynext) == True:
                cross = j + 1
            
            rcm += (1/float(N))*math.sqrt((xlist[-1])**2 + (ylist[-1])**2)
        
        for k in range(0, N):
            Rg += (1/N+1)*(math.sqrt(xlist[k]**2 + ylist[k]**2) - rcm)**2
        Rglist.append(Rg)
                
        #After every simulation the end-to-end distance is calculated
        r = math.sqrt((xlist[-1] - xlist[0])**2 + (ylist[-1] - ylist[0])**2)
        rlist.append(r)
        if cross > 0:
            crosslist.append(cross)
        
    #The mean end-to-end distance is printed
    return np.mean(rlist), np.mean(crosslist), np.mean(Rglist)
    
##A plot is generated of the end-to-end distance as a function of base pair 
#number
for i in Nlist:
    rmeanlist.append(constantwalk(i)[0])
    Rgmeanlist.append(constantwalk(i)[2])
    
plt.figure(1)
plt.clf()
plt.plot(Nlist, rmeanlist, 'b')
plt.title('End-to-end distance as a function of base pairs')
plt.xlabel('N')
plt.ylabel('r')

plt.figure(2)
plt.clf()
plt.plot(Nlist, Rgmeanlist, 'b')
plt.title('Radius of gyration as a function of base pairs')
plt.xlabel('N')
plt.ylabel('$R_{g}$')
plt.show()
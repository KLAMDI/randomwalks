# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt
import random
import time

starttime = time.time()

##The following two functions will check if two line segments intersect based on 
#their oriëntation.
def ccw(Ax, Ay, Bx, By, Cx, Cy):
    return (Cy-Ay)*(Bx-Ax) > (By-Ay)*(Cx-Ax)
    
def intersect(x0, y0, x1, y1, xprev, yprev, xnext, ynext):
    return ccw(x0, y0, x1, y1, xprev, yprev) != ccw(x0, y0, x1, y1, xnext, 
        ynext) and ccw(xprev, yprev, xnext, ynext, x0, y0) != ccw(xprev, yprev, 
        xnext, ynext, x1, y1)

#The starting variables and lists
N = 100
Nrot = 100
pdflist = []

def avoidingwalk(N, Nrot):
    j = 0
    xlist = [0]
    ylist = [0]
    dlist = []
    
    #First, generate a straight line 
    for n in range(0, N):
        xlist.append(n + 1)
        ylist.append(0)
    
    #This loop goes on untill the polymer has rotated Nrot times    
    while j <= Nrot - 1:
        
        #Choose a random pivot site
        pivot_site = int(random.random()*N)
        int_check = False
        
        #Seperate the part that is to be rotated
        xlistrot = np.array(xlist[pivot_site + 1:N + 1])
        ylistrot = np.array(ylist[pivot_site + 1:N + 1])
        
        #Perform a rotation on the line segment    
        angle = 2*math.pi*random.random()
        xlistrotnew = (math.cos(angle)*(xlistrot-xlist[pivot_site]) - 
            math.sin(angle)*(ylistrot-ylist[pivot_site]) + xlist[pivot_site]) 
        ylistrotnew = (math.sin(angle)*(xlistrot-xlist[pivot_site]) + 
            math.cos(angle)*(ylistrot-ylist[pivot_site]) + ylist[pivot_site]) 
        
        #Check if the new segment doesn't intersect with the original segment
        for f in range(1, N):
            if int_check == True:
                break
                
            #Special check for the segment starting from pivot site
            if intersect(xlist[f-1], ylist[f-1], xlist[f], ylist[f], 
                xlist[pivot_site], ylist[pivot_site], xlistrotnew[0], 
                ylistrotnew[0]) == True:
                int_check = True
                break
            for g in range(1, len(xlistrotnew)):
                if intersect(xlist[f-1], ylist[f-1], xlist[f], ylist[f], 
                xlistrotnew[g-1], ylistrotnew[g-1], xlistrotnew[g], 
                ylistrotnew[g]) == True:
                    int_check = True
                    break
                        
        if int_check == False:
            j += 1
            
            #The rotated segment is given the new coördinates
            del xlist[pivot_site + 1: N + 1]
            del ylist[pivot_site + 1: N + 1]
            xlist += xlistrotnew.tolist()
            ylist += ylistrotnew.tolist()
    
    #Calculation of the center of mass
    for i in range(0, N):
        dlist.append(math.sqrt(xlist[i]**2 + ylist[i]**2))
    rcm = np.sum(dlist)/len(dlist)

    return (xlist, ylist, rcm)   

#Computing the end-to-end distance 10000 times for the pdf 
rlist = avoidingwalk(N, Nrot)
for i in range(0, 10000):
    poslists = avoidingwalk(10, 10)
    pdflist.append(math.sqrt(poslists[0][-1]**2 + poslists[1][-1]**2))
       
print 'End-to-end distance: %f' %(math.sqrt(rlist[0][-1]**2 + rlist[1][-1]**2))
print 'Center of mass: %f' % (rlist[2])       
plt.figure(1)
plt.clf()
plt.scatter(rlist[0], rlist[1])
plt.plot(rlist[0], rlist[1], rlist[0][0], rlist[1][0], 'go')
plt.title('Self-avoiding random walk') 
plt.xlabel('x')
plt.ylabel('y')
    
plt.figure(2)
plt.clf()
plt.hist(pdflist, bins = np.arange(min(pdflist), max(pdflist) + 0.1, 0.1))
plt.title('Pdf of end-to-end distance')
plt.xlabel('r')
plt.ylabel('counts')
plt.show()

print 'Duration: %f seconds' % (time.time()-starttime)
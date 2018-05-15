import matplotlib.pyplot as plt
import random as rd
import math
import numpy as np

def ccw(Ax, Ay, Bx, By, Cx, Cy):
    return (Cy-Ay)*(Bx-Ax) > (By-Ay)*(Cx-Ax)
    
def intersect(x0, y0, x1, y1, xprev, yprev, xnext, ynext):
    return ccw(x0, y0, x1, y1, xprev, yprev) != ccw(x0, y0, x1, y1, xnext, 
        ynext) and ccw(xprev, yprev, xnext, ynext, x0, y0) != ccw(xprev, yprev, 
        xnext, ynext, x1, y1)

N = 100

xlist = [0]
ylist = [0]
for n in range(0, N):
    xlist.append(xlist[n] + 1)
    ylist.append(0)
 
for j in range(0, N):
    pivot_site = int(rd.random()*N)
    xlistrot = []
    ylistrot = []
    int_check = False
    
    for s in range(pivot_site, N+1):
        xlistrot.append(xlist[s])
        ylistrot.append(ylist[s])
    
    angle = 2*math.pi*rd.random()
    xlistrot = np.array(xlistrot)
    ylistrot = np.array(ylistrot)
    xlistrotnew = math.cos(angle)*xlistrot - math.sin(angle)*ylistrot
    ylistrotnew = math.sin(angle)*xlistrot + math.cos(angle)*ylistrot
    
    #Checks if rotation is done correctly
    # if xlistrotnew[len(xlistrot)-2] == (math.cos(angle)*xlistrot[len(xlistrot)-2] - math.sin(angle)*ylistrot[len(xlistrot)-2]):
    #     print 'yay'
    # else:
    #     print 'wtf'

    for n in range(0, len(xlistrot)-1):
        if int_check == False:
            for p in range(0, pivot_site):
                if intersect(xlist[p], ylist[p], xlist[p+1], ylist[p+1], xlistrotnew[n], ylistrotnew[n], xlistrotnew[n+1], ylistrotnew[n+1]):
                    int_check = True
                    # print '(%f, %f), (%f, %f)' % (xlist[p], ylist[p], xlist[p+1], ylist[p+1])
                    # print '(%f, %f), (%f, %f)' % (xlistrotnew[n], ylistrotnew[n], xlistrotnew[n+1], ylistrotnew[n+1])
                    break
                
                #Alternative method, doesn't yield better results
                # if (max(xlist[p],xlist[p+1]) < min(xlistrotnew[n],xlistrotnew[n+1])):
                #     break
                # else:
                #     A1 = (ylist[p]-ylist[p+1])/(xlist[p]-xlist[p+1]) # Pay attention to not divide by zero
                #     A2 = (ylistrotnew[n]-ylistrotnew[n+1])/(xlistrotnew[n]-xlistrotnew[n+1]) # Pay attention to not divide by zero
                #     b1 = ylist[p]-A1*xlist[p] 
                #     b2 = ylistrotnew[n]-A2*xlistrotnew[n]
                #     Xa = (b2 - b1) / (A1 - A2) # Once again, pay attention to not divide by zero
                #     
                #     if Xa < max(min(xlist[p],xlist[p+1]), min(xlistrotnew[n],xlistrotnew[n+1])) and Xa > min(max(xlist[p],xlist[p+1]), max(xlistrotnew[n],xlistrotnew[n+1])):
                #         break
                #     else:
                #         int_check == True

    if int_check == False:
        # print 'hello'
        for s in range(pivot_site, N + 1):
            xlist[s] = xlistrotnew[s-pivot_site]
            ylist[s] = ylistrotnew[s-pivot_site]

plt.close()        
plt.figure(1)
plt.plot(xlist, ylist)
# plt.plot([xlist[p],xlist[p+1]], [ylist[p], ylist[p+1]], 'g--')
# plt.plot([xlistrotnew[n], ylistrotnew[n]], [xlistrotnew[n+1], ylistrotnew[n+1]], 'r--')
plt.show()
import os
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt

n = 100
rep = 500
timerG = []
timerL = []
sumG = 0.0
sumL = 0.0

print("Generateur \n")

for k in range(rep) :
    timer = datetime.datetime.now()

    cnt = 0
    for (x,y,z) in ((a,b,c) for a in range(n) for b in range(n) for c in range(n) if a+b+c == n) :
        cnt += 1
    timerG.append( (datetime.datetime.now() - timer).total_seconds() )
    sumG += (datetime.datetime.now() - timer).total_seconds()
    #print("%-20s%-25s" %  ("If dedans : ", timer))

#timer = datetime.datetime.now()
#cnt = 0
#for (x,y,z) in ((a,b,c) for a in range(n) for b in range(n) for c in range(n)) :
#    if x+y+z == n :
#        cnt += 1
#print('Dehors : ', cnt)
#timer = datetime.datetime.now() - timer
#print("%-20s%-25s" %  ("If dehors : ", timer))

print("\nListes \n")

for k in range(rep) :
    timer = datetime.datetime.now()
    cnt = 0
    for (x,y,z) in [(a,b,c) for a in range(n) for b in range(n) for c in range(n) if a+b+c == n] :
        cnt += 1
    #print('Dedant : ', cnt)
    timerL.append( (datetime.datetime.now() - timer).total_seconds() )
    sumL += (datetime.datetime.now() - timer).total_seconds()
    #print("%-20s%-25s" %  ("If dedans : ", timer))

plt.scatter([1 for i in range(rep)], timerG, label='GENS')
plt.scatter([2 for i in range(rep)], timerG, label='LIST')
plt.show()

print('Gen : ', sumG)
print('List: ', sumL)
#timer = datetime.datetime.now()
#cnt = 0
#for (x,y,z) in [(a,b,c) for a in range(n) for b in range(n) for c in range(n)] :
#    if x+y+z == n :
#        cnt += 1
#print('Dehors : ', cnt)
#timer = datetime.datetime.now() - timer
#print("%-20s%-25s" %  ("If dehors : ", timer))
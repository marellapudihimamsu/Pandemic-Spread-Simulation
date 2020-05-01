# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 08:44:02 2020

@author: Dell
"""

import networkx as nx
import random as rand
import matplotlib.pyplot as pyp
from copy import deepcopy
import numpy as np
filepath='E:\\shapecontrol\\pandemic spread\\flush\\'
imgiter=0
n=rand.randint(75,100)
print(len(list(np.linspace(-100,100,n))))
p=[[]for adsffd in range(2) ]
#random input
p[0]=list(np.linspace(-100,100,n))    # X
p[1]=list(np.linspace(-100,100,n))   #
rand.shuffle(p[0])
rand.shuffle(p[1])
stepsize=3
pyp.plot(p[0],p[1],'k*',markersize="3")
pyp.title("input points "+str(n))
pyp.grid(color='r', linestyle='-', linewidth=0.5)
pyp.axis([-101, 101, -101, 101])
pyp.gca().set_aspect('equal', adjustable='box')
pyp.savefig(filepath+str(imgiter)+'.png')
imgiter+=1
pyp.show()
des=[0 for asdfgh in range(n)]
des[0]=1
finalpos=[[]for asdfgh in range(2)]
for i in range(n):
    finalpos[0].append(rand.randint(-100,100))
    finalpos[1].append(rand.randint(-100,100))
for dummy in range(1000):
    if(dummy%40==0):
        for i in range(n):
            finalpos[0][i]=(rand.randint(-100,100))
            finalpos[1][i]=(rand.randint(-100,100))
    for i in range(n):
        for j in range(n):
            if (( (p[0][i]-p[0][j])**2  +  (p[1][i]-p[1][j])**2  )**0.5  < 4)&(i!=j):
                des[i]=1
                des[j]=1 #epidemic spreads 
        x=p[0][i]-finalpos[0][i]
        y=p[1][i]-finalpos[1][i]
        val=( (      (x**2)  +  (y**2)             )**0.5)*(1/stepsize)
        x=x/val
        y=y/val
        #print(x,y,"x,y")
        p[0][i]=p[0][i]-(x)
        p[1][i]=p[1][i]-(y)    
    
    
    print("final points")
    # print(finalpos)
    for i in range(n):
        if(des[i]==0):
            pyp.plot(p[0][i],p[1][i],'k*',markersize="3")
        if(des[i]==1):
            pyp.plot(p[0][i],p[1][i],'r*',markersize="3")
    pyp.title("final points")
    pyp.grid(color='r', linestyle='-', linewidth=0.5)
    pyp.axis([-101,101,-101,101])
    pyp.gca().set_aspect('equal', adjustable='box')
    pyp.savefig(filepath+str(imgiter)+'.png')
    imgiter+=1
    pyp.show()

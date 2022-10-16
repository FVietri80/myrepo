#####Regressione Polinomiale

import  math as mt
import random

import matplotlib.pyplot  as plt

import numpy as np


xpoints = []
ypoints = []
for i in range(10) :
    xpoints.append(round(random.random(),1))

#print(xpoints)
for i in range(len(xpoints)):
    ypoints.append(round(mt.sin((2*mt.pi*xpoints[i])+random.uniform(0,1)),1))

print(ypoints)

plt.plot(xpoints,ypoints,'o',color = 'black')
plt.show()




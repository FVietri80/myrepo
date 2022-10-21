#####Regressione Polinomiale

import  math as mt
import random

import matplotlib.pyplot  as plt

import numpy as np


x = np.linspace(-2*np.pi,2*np.pi,100)

y =np.sin(x)

z = y =np.sin(x+np.random.uniform(-2*np.pi,2*np.pi))

plt.plot(x,y)
plt.plot(z,marker = 'o',color = 'red')
plt.show()

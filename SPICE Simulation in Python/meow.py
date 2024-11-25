import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def random_func(x,a,b):
  return a/((x**5)*(np.exp(b/x)-1))

with open("d1.txt") as f:
  li = [line.strip().split(',') for line in f.readlines()]

li
x=[float(i[0]) for i in li]
y=[float(i[1]) for i in li]

plt.plot(x,y)
plt.show()
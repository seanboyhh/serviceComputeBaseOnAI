'''
Created on Mar 30, 2021

@author: DingYang
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

#Time Complexity and coverage rate
 
x = [20,40,60,80]
y1= [0.20947,0.10399,0.07894,0.05404]
y2= [5.45146,3.91704,3.22271,1.83019]
y3= [56.82045,44.75310,30.00406,19.80401]
y4= [144.79084,115.49912,79.81753,50.50138]
y5= [1026.5975,888.7864,594.8155,282.1190]
plt.plot(x, y1, marker='o', mec='r', mfc='w',label='The number of subtasks is 4')
plt.plot(x, y2, marker='*', ms=10,label='The number of subtasks is 8')
plt.plot(x, y3, marker='s', ms=10,label='The number of subtasks is 12')
plt.plot(x, y4, marker='^', mec='r', mfc='w',label='The number of subtasks is 16')
plt.plot(x, y5, marker='v', mec='r', mfc='w',label='The number of subtasks is 20')
ax=plt.gca()
ax.yaxis.set_major_locator(MultipleLocator(60))
ax.set_ylim(bottom=0.)
plt.xticks(x)
plt.xlabel('coverage rate(percentage)')
plt.ylabel('Time complexity')
plt.legend(loc='upper right')
plt.show()

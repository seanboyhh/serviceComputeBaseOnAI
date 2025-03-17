'''
Created on Mar 30, 2021

@author: DingYang
'''

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
 
x = [2,4,6,8,10,12,14,16,18,20]
y1= [18.623,23.804,36.513,44.916,48.867,51.596,51.529,58.463,65.115,69.979]
y2=[0.028340,0.035786,0.052156,0.053987,0.055823,0.057389,0.059784,0.061465,0.067316,0.073837]
y2=[i*1000 for i in y2];
y3=[0.048990,0.051323,0.072334,0.072674,0.072563,0.079865,0.083707,0.086237,0.089654,0.092345]
y3=[i*1000 for i in y3]
y4= [45.560,48.970,71.823,72.481,73.652,76.673,78.875,81.768,86.387,89.124]
y5= [33.410,38.906,56.318,57.911,59.221,60.945,63.467,65.797,77.837,80.346] 


plt.plot(x, y1, marker='o', mec='r', mfc='w',label='IDPSO')
plt.plot(x, y2, marker='x', mec='r', mfc='w',label='FWPSO')
plt.plot(x, y3, marker='*', ms=10,label='OPSO')
plt.plot(x, y4, marker='v', mec='r', mfc='w',label='ZP-PSO')
plt.plot(x, y5, marker='s', mec='r', mfc='w',label='S-ABC')

ax=plt.gca()
ax.yaxis.set_major_locator(MultipleLocator(5))
plt.xticks(x)
plt.xlabel('Number of subtasks')
plt.ylabel('Optimality*1000')
plt.legend(loc='lower right')
plt.show()

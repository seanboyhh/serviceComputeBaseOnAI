'''
Created on Mar 30, 2021

@author: DingYang
'''

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
 
#2 subtasks
x = [20,40,60,80,100]
y1= [68.567,30.564,20.675,18.623,18.623]
y2= [71.123,35.667,28.999,28.340,28.340]
y3= [80.896,75.694,60.340,48.990,48.990]
y4= [72.5975,60.7864,50.8155,47.560,45.560]
y5= [71.2345,37.6745,35.3321,33.410,33.410]



plt.plot(x, y1, marker='o', mec='r', mfc='w',label='IDPSO')
plt.plot(x, y2, marker='x', mec='r', mfc='w',label='FWPSO')
plt.plot(x, y3, marker='*', ms=10,label='OPSO')
plt.plot(x, y4, marker='v', mec='r', mfc='w',label='ZP-PSO')
plt.plot(x, y5, marker='s', mec='r', mfc='w',label='S-ABC')



ax=plt.gca()
ax.yaxis.set_major_locator(MultipleLocator(5))
plt.xticks(x)
plt.xlabel('Ratio of the number of current iterations to the total number of iterations(percentage)')
plt.ylabel('Optimality*1000')
plt.legend(loc='lower left')
plt.show()

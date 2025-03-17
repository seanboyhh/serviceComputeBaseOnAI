'''
Created on Mar 30, 2021

@author: DingYang
'''

import matplotlib.pyplot as plt

# 8 subtasks
x = [20,40,60,80,100]
y1= [83.3555,77.7775,66.2509,54.6248,44.916]
y2= [84.123,78.345,70.234,60.678,53.987]
y3= [89.2332,85.1946,82.3442,78.7475,72.674]
y4= [88.5975,83.7864,80.8155,75.1190,72.481]
y5= [87.2345,80.6745,75.3321,65.6734,57.911]

plt.plot(x, y1, marker='o', mec='r', mfc='w',label='IDPSO')
plt.plot(x, y2, marker='x', mec='r', mfc='w',label='FWPSO')
plt.plot(x, y3, marker='*', ms=10,label='OPSO')
plt.plot(x, y4, marker='v', mec='r', mfc='w',label='ZP-PSO')
plt.plot(x, y5, marker='s', mec='r', mfc='w',label='S-ABC')

ax=plt.gca()
ax.yaxis.set_major_locator(plt.MultipleLocator(5))
plt.xticks(x)
plt.xlabel('Ratio of the number of current iterations to the total number of iterations(percentage)')
plt.ylabel('Optimality*1000')
plt.legend(loc='lower left')
plt.show()

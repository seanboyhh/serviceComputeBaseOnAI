'''
Created on Mar 30, 2021

@author: DingYang
'''

#14 subtasks
import matplotlib.pyplot as plt

x = [20,40,60,80,100]
y1= [92.3555,82.7775,73.2509,64.6248,51.529]
y2= [94.3555,85.7775,78.2509,68.6248,59.784]
y3= [110.1332,100.4946,95.4442,88.3475,83.707]
y4= [105.5975,95.7864,89.8155,79.1190,78.875]
y5= [100.2345,90.6745,88.3321,77.6734,63.467]

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

'''
Created on Mar 30, 2021

@author: DingYang
'''

#20 subtask
import matplotlib.pyplot as plt
 
x = [20,40,60,80,100]
y1= [97.8765,74.7977,72.3015,72.0916,69.9790]
y2= [99.8765,80.7977,78.3015,75.0916,73.837]
y3= [120.4590,110.6946,105.5412,98.5475,92.345]
y4= [110.2181,105.2571,100.4783,90.6083,89.1245]
y5= [105.2345,95.6745,90.3321,85.6734,80.3467]

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

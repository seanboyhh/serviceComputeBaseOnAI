'''
Created on Mar 30, 2021

@author: DingYang
'''

#20 subtask
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
 
x = [20,40,60,80,100]
####IDPSO
y1= [97.8765,74.7977,72.3015,72.0916,69.9790]
####PK-IDPSO
y2= [60.8765,50.7977,48.3015,44.0916,43.7670]
###ZP-PSO
y3= [110.2181,105.2571,100.4783,90.6083,89.1245]
###S-ABC
y4= [105.2345,95.6745,90.3321,85.6734,80.3467]
###EO
y5= [98.4590,87.6946,77.5412,75.5475,73.837]
###RSA
y6= [112.5975,105.7864,101.8155,91.1190,90.3452]
###GA
y7=[100.354,90.435,85.908,81.798,75.980]
###FPA
y8=[113.907,106.356,99.010,94.097,92.124]
###HAA-ACO
y9=[99.078,85.807,80.040,75.796,73.017]
###HHO
y10=[99.029,96.903,91.343,86.093,81.932]
###BBO
y11=[104.901,100.478,94.090,87.098,85.230]
###HMM-ACO
y12=[103.793,88.989,80.343,76.908,74.915]

plt.plot(x, y1, marker='o', mec='r', mfc='w',label='IDPSO')
plt.plot(x, y2, marker='x', mec='r', mfc='w',label='PK-IDPSO')
plt.plot(x, y3, marker='v', mec='r', mfc='w',label='ZP-PSO')
plt.plot(x, y4, marker='s', mec='r', mfc='w',label='S-ABC')
plt.plot(x, y5, marker='*', ms=10,label='EO')
plt.plot(x, y6, marker='^', mec='r', mfc='w',label='RSA')
plt.plot(x, y7, marker='<', mec='r', mfc='w',label='GA')
plt.plot(x, y8, marker='.', mec='r', mfc='w',label='FPA')
plt.plot(x, y9, marker='8', mec='r', mfc='w',label='HAA-ACO')
plt.plot(x, y10, marker='p', mec='r', mfc='w',label='HHO')
plt.plot(x, y11, marker='+', mec='r', mfc='w',label='BBO')
plt.plot(x, y12, marker='d', mec='r', mfc='w',label='HMM-ACO')

ax=plt.gca()
ax.yaxis.set_major_locator(MultipleLocator(5))
plt.xticks(x)
plt.xlabel('Ratio of the number of current iterations to the total number of iterations(percentage)')
plt.ylabel('Optimality*1000')
plt.legend(loc='lower left')
plt.show()

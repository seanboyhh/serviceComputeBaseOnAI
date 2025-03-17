'''
Created on Mar 30, 2021

@author: DingYang
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
 
#2 subtasks
x = [20,40,60,80,100]
####IDPSO
y1= [70.567,30.564,20.675,18.623,18.623]
####PK-IDPSO
y2= [48.123,24.667,18.999,15.802,15.802]
###ZP-PSO
y3= [72.5975,60.7864,50.8155,45.560,45.560]
###S-ABC
y4= [71.2345,50.6745,40.3321,33.410,33.410]
###EO
y5= [70.896,35.694,30.340,28.340,28.332]
###RSA
y6= [78.2181,62.2571,52.4783,48.990,48.990]
###GA
y7=[70.345,40.543,37.908,32.698,32.698]
###FPA
y8=[71.375,50.132,48.223,47.215,47.215]
###HAA-ACO
y9=[71.003,34.310,30.131,25.332,25.332]
###HHO
y10=[71.021,37.713,36.337,35.403,35.403]
###BBO
y11=[72.314,43.013,39.011,38.192,38.192]
###HMM-ACO
y12=[73.112,35.123,33.901,31.709,31.709]

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

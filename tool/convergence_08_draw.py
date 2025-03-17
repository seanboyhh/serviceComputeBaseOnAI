'''
Created on Mar 30, 2021

@author: DingYang
'''

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
# 8 subtasks
x = [20,40,60,80,100]
####IDPSO
y1= [83.3555,77.7775,66.2509,54.6248,44.916]
####PK-IDPSO
y2= [50.123,45.345,40.234,35.678,28.045]
###ZP-PSO
y3= [88.5975,83.7864,80.8155,75.1190,72.481]
###S-ABC
y4= [87.2345,80.6745,75.3321,65.6734,57.911]
###EO
y5= [84.2332,78.1946,68.3442,58.7475,53.967]
###RSA
y6=[90.2181,85.2571,81.4783,72.674,72.674]
###GA
y7=[87.132,79.654,73.354,63.890,57.954]
###FPA
y8=[92.091,81.132,79.313,75.092,74.091]
###HAA-ACO
y9=[84.201,78.012,67.331,57.125,46.785]
###HHO
y10=[85.331,78.679,70.378,60.903,59.802]
###BBO
y11=[87.565,80.393,74.309,64.224,61.023]
###HMM-ACO
y12=[86.380,79.309,71.203,63.089,55.907]

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

'''
Created on Mar 30, 2021

@author: DingYang
'''

#14 subtasks
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

x = [20,40,60,80,100]
####IDPSO
y1= [92.3555,82.7775,73.2509,64.6248,51.596]
####PK-IDPSO
y2= [55.3555,50.7775,40.2509,38.6248,33.113]
###ZP-PSO
y3= [105.5975,95.7864,89.8155,79.1190,78.875]
###S-ABC
y4= [100.2345,90.6745,88.3321,77.6734,63.467]
###EO
y5= [96.1332,87.4946,75.4442,68.3475,59.684]
###RSA
y6= [105.2181,100.2571,89.4783,85.6083,83.707]
###GA
y7=[98.453,90.145,85.717,77.891,61.908]
###FPA
y8=[104.301,101.234,90.343,85.104,83.987]
###HAA-ACO
y9=[95.232,85.970,75.104,67.909,54.323]
###HHO
y10=[97.231,88.950,84.090,78.013,64.890]
###BBO
y11=[103.201,93.203,87.220,78.340,75.907]
###HMM-ACO
y12=[98.232,91.125,85.770,77.671,67.170]

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

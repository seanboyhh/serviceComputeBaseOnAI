'''
Created on Mar 30, 2021

@author: DingYang
'''

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
 
x = [2,4,6,8,10,12,14,16,18,20]
#IDPSO
y1= [18.623,23.804,36.513,44.916,48.867,51.596,53.529,58.463,65.115,69.979]
#PK-IDPSO
y2=[15.802,18.921,22.951,28.045,30.260,32.034,33.113,36.682,42.794,43.767]
#ZP-PSO
y3= [45.560,48.970,71.823,72.481,73.652,76.673,78.875,81.768,86.387,89.124]
#S-ABC
y4= [33.410,38.906,56.318,57.911,59.221,60.945,63.467,65.797,77.837,80.346] 
#EO
y5= [0.028431,0.033876,0.043113,0.047873,0.051238,0.053893,0.057847,0.059321,0.066234,0.072826]
y5=[i*1000 for i in y5];
#RSA
y6= [0.046875,0.051211,0.071944,0.073264,0.072656,0.080675,0.083764,0.085241,0.089243,0.091223]
y6=[i*1000 for i in y6];
#GA
y7=[0.032141,0.035908,0.045832,0.051897,0.053132, 0.057456, 0.059241,0.061836, 0.065664,0.075980]
y7=[i*1000 for i in y7];
#FPA
y8=[0.047215,0.053143,0.061901,0.074091,0.075983,0.08128,0.083987,0.087012,0.089193,0.092124]
y8=[i*1000 for i in y8]
#HAA-ACO
y9=[0.025332,0.028477,0.039453,0.046785,0.050274,0.052011,0.054323,0.059112,0.065901,0.073017]
y9=[i*1000 for i in y9]
#HHO
y10=[0.035403,0.039129,0.045865,0.059802,0.061971,0.062998,0.064890,0.067131,0.075924,0.081932]
y10=[i*1000 for i in y10]
#BBO
y11=[0.038192,0.043817,0.057098,0.061023,0.065911,0.071905,0.075907,0.078809,0.081287,0.085230]
y11=[i*1000 for i in y11]
#HMM-ACO
y12=[0.031709,0.041890,0.047075,0.055907,0.061703,0.064763,0.067170,0.069971,0.071378,0.074915]
y12=[i*1000 for i in y12]
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
plt.xlabel('Number of subtasks')
plt.ylabel('Optimality*1000')
plt.legend(loc='upper left')
plt.show()

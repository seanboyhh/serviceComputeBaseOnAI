'''
Created on Mar 30, 2021

@author: DingYang
'''

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
# Time Complexity
x = [4,8,12,16,20]
y1= [0.1062,8.7725,85.2681,246.0475,1408.9678]
y2= [22.9272,4.7119,51.3869,134.8976,783.9279]
y3= [0.1865,8.6554,80.2145,233.9001,1189.7903]
y4= [0.1806,8.2336,79.3367,220.9077,1120.9087]
y5= [0.1803,8.5641,83.6251,247.9567,1383.6095]
y6= [0.1673,9.0231,77.6733,213.7613,1047.5762]
y7=[0.1723, 8.6324, 83.7531, 241.9763, 1127.8721]
y8=[0.1801,8.1987,78.8907,218.9081,1117.8019]
y9=[0.1875,8.6172,82.9704,243.7750,1301.2047]
y10=[0.1713,8.1902,77.9017,217.5210,1103.9132]
y11=[0.1807,8.6135,81.2103,230.1192,1192.3671]
y12=[0.1890,8.9734,88.6729,251.5436,1479.8019]

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
ax.yaxis.set_major_locator(MultipleLocator(70))
ax.set_ylim(bottom=0.)
plt.xticks(x)
plt.xlabel('Number of subtasks')
plt.ylabel('Time complexity')
plt.legend(loc='upper left')
plt.show()

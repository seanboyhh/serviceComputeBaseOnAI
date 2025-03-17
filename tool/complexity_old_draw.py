'''
Created on Mar 30, 2021

@author: DingYang
'''
import matplotlib.pyplot as plt

# Time Complexity
x = [2,4,6,8,10,12,14,16,18,20]
y1= [0.0301,0.1794,0.9987,8.2725,30.4751,79.2681,149.3201, 220.0475,493.1813,1198.967]
y2= [0.0311,0.1935,1.1265,9.2365,40.3354,99.3213,190.8931,265.3461,601.3267,1438.8960]
y3= [0.0289,0.165,0.8976,7.9348,28.6791,75.2387,140.8879,201.9341,460.5609,1003.8976]
y4= [0.0356,0.1865,1.0031,8.6554,33.5643,80.2145,160.3576,233.9001,540.2231,1289.7903]
y5= [0.0303,0.1806,1.0024,8.4436,32.6574,81.3367,157.9017,231.9077,518.7039,1220.9087]

plt.plot(x, y1, marker='o', mec='r', mfc='w',label='IDPSO') 
plt.plot(x, y2, marker='x', mec='r', mfc='w',label='FWPSO')
plt.plot(x, y3, marker='*',  ms=10,label='OPSO')
plt.plot(x, y4, marker='v', mec='r', mfc='w',label='ZP-PSO')
plt.plot(x, y5, marker='s', mec='r', mfc='w',label='S-ABC')
ax=plt.gca()
ax.yaxis.set_major_locator(plt.MultipleLocator(60))
ax.set_ylim(bottom=0.)
plt.xticks(x)
plt.xlabel('Number of subtasks')
plt.ylabel('Time complexity')
plt.legend(loc='upper left')
plt.show()

import matplotlib.pyplot as plt
import csv
import numpy as np
import scipy.stats

min_level = -75
max_level = -72

x = []

with open('2402.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((float(row[0])))

mean = np.mean(x)
result = scipy.stats.describe(x, ddof=1, bias=False)
print(result)

#plt.hist(x, bins=np.linspace(result.minmax[0], result.minmax[1], num=100))#[-100,-95,-90,-85,-80,-75,-70,-65,-60,-55,-50,-45,-40,-35,-30,-25,-20,-15,-10,-5,0])
plt.hist(x, bins=np.linspace(min_level, max_level, num=100))#[-100,-95,-90,-85,-80,-75,-70,-65,-60,-55,-50,-45,-40,-35,-30,-25,-20,-15,-10,-5,0])
plt.xlabel('Level (dBm)')
plt.ylabel('Occurrence')
plt.title('Histogram from channel\n')
#plt.legend()
plt.show()
import matplotlib.pyplot as plt
import csv

x = []

with open('9022.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((float(row[0])))

plt.hist(x, bins=[-100,-95,-90,-85,-80,-75,-70,-65,-60,-55,-50,-45,-40,-35,-30,-25,-20,-15,-10,-5,0])
plt.xlabel('Level (dBm)')
plt.ylabel('Frequency')
plt.title('Histogram from channel\n')
#plt.legend()
plt.show()
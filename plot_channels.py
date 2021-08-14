import matplotlib.pyplot as plt
import csv

x = []
y = []
freq_label = []
color_array = []

good_level = -75
medium_level = -65

with open('meas.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append((120 - abs(float(row[1]))))
        if (float(row[1]) < good_level) :
                color_array.append('green')
        elif (float(row[1]) > good_level and float(row[1]) < medium_level) :
                color_array.append('yellow')
        else :
                color_array.append('red')

print(color_array)

freq_label = x
plt.bar(x, y, bottom=-120, tick_label=freq_label, width=0.8, color=color_array)
plt.ylim(top=0)
plt.xlabel('Channel')
plt.ylabel('dBm')
plt.title('Power Level from measured channels\nBluetooth')
#plt.legend()
plt.show()
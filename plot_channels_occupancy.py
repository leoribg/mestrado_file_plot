import matplotlib.pyplot as plt
import csv

x = []
y = []
freq_label = []
color_array = []

with open('meas.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[2]))
        if (int(row[2]) < 5) :
                color_array.append('green')
        elif (int(row[2]) > 5 and int(row[2]) < 40) :
                color_array.append('yellow')
        else :
                color_array.append('red')

print(color_array)

freq_label = x
plt.bar(x, y, bottom=0, tick_label=freq_label, width=0.8, color=color_array)
plt.ylim(top=100)
plt.xlabel('Channel')
plt.ylabel('%')
plt.title('Occupancy from measured channels\nWi-SUN')
#plt.legend()
plt.show()
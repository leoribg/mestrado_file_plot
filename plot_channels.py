import matplotlib.pyplot as plt
import csv

x = []
y = []
freq_label = []
color_array = []

with open('plot_data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append((120 - abs(int(row[1]))))
        if int(row[1]) < -90 :
                color_array.append('green')
        else :
                color_array.append('red')

print(color_array)

freq_label = x
plt.bar(x, y, bottom=-120, tick_label=freq_label, width=0.8, color=color_array)
plt.xlabel('Frequency')
plt.ylabel('dBm')
plt.title('Power Level from measured channels\nWi-SUN')
#plt.legend()
plt.show()
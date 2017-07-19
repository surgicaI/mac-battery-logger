import os
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
data_dir = dir_path + '/.data/'
files = os.listdir(data_dir)
file_name = sorted(files)[-1]

x = []
y = []
with open(data_dir + file_name, 'r') as handle:
    for line in handle:
        data = line.split()
        x.append(data[0])
        y.append(data[1])

plt.plot(x,y)
plt.show()

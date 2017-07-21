#! /usr/bin/env python3
import os, math, sys
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
data_dir = dir_path + '/.data/'
files = os.listdir(data_dir)

x = []
y = []
MUL = 25
num_days = int(sys.argv[1]) if len(sys.argv) > 1 else 1
for index, file_name in enumerate(files[-1*num_days:]):
    factor = MUL * index
    with open(data_dir + file_name, 'r') as handle:
        for line in handle:
            data = line.split()
            time_sec = int(data[0])
            time_hrs = math.floor(time_sec / 3600)
            time_mins = (time_sec % 3600) / 60
            scaling_factor = 60
            time = time_hrs + (float(time_mins) / scaling_factor) + factor
            x.append(time)
            y.append(data[1])

plt.plot(x,y)
plt.show()

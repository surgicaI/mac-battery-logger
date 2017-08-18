from datetime import datetime
from subprocess import Popen, PIPE, STDOUT
from threading import Timer
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
data_dir = dir_path + '/.data/'
INTERVAL_SECS = 5
prev_battery_percentage = ''

def collect_data():
    global prev_battery_percentage
    current_time = map(int, datetime.now().time().isoformat(timespec='seconds').split(':'))
    current_time = sum([x*y for x,y in zip(current_time, reversed([60**i for i in range(3)]))])
    file_name = map(str, datetime.now().date().timetuple()[:3])
    file_name = map(lambda x: '0'+x if len(x) < 2 else x, file_name)
    file_name = '-'.join(file_name)

    battery_info = Popen(['pmset', '-g', 'batt'], stdout=PIPE, stderr=STDOUT, encoding='utf8').communicate()[0]
    battery_percentage = battery_info.split('\n')[1].split('\t')[1]
    battery_percentage = battery_percentage[:battery_percentage.index('%')]
    if battery_percentage != prev_battery_percentage:
        prev_battery_percentage = battery_percentage
        data_point = '\t'.join(map(str, [current_time, battery_percentage]))

        with open(data_dir + file_name, 'a') as handle:
            handle.write(data_point + '\n')

    Timer(INTERVAL_SECS, collect_data).start()

if __name__ == '__main__':
    collect_data()

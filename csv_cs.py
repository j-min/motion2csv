"""
csv cubic splining

usage :: python csv_cs.py (inputfilename - optional) (outputfilename - optional)

default inputfilename = input.csv
"""

import numpy as np
from scipy.interpolate import CubicSpline
import sys

time_interval = 100

def main():

    if len(sys.argv) < 2:
        filename = "input.csv"
        outputfilename = "output.csv"
    else:
        filename = sys.argv[1][:]
        if len(sys.argv) == 3:
            outputfilename = sys.argv[2][:]
        else:
            outputfilename = filename.split('.')[0]+"_splined.csv"

    my_data = np.genfromtxt(filename, delimiter=',')
    times = []

    with open(filename) as f:
        lines = f.readlines()
        columnName = lines[0]

        for line in lines[1:]:
            time = line.split(',')[0].split('_')
            try:
                hour, min, sec, msec = map(int,time)
                totalmsec = ((((60 * hour) + min) * 60) + sec) * 1000 + msec
                times.append(totalmsec)
            except:
                pass

    t = np.array(times)                                      # t :: 시간축 데이터 (milisecond)
    xs = np.arange((t[0]) // time_interval * time_interval + time_interval, t[-1], time_interval)    # xs :: 100ms 단위의 시간축 데이터 (milisecond)
    res = []
    for skeleton in range(1,101):
        if skeleton % 4 == 0 :                               # State 값의 경우에는 정수 그대로 출력한다.
            # State값도 interpolation 하려면 그냥 이 if문 지워버리면 됨
            res.append(my_data[1:len(xs)+1,skeleton])
            continue

        cs = CubicSpline(t, my_data[1:, skeleton])
        res.append(cs(xs))

    result = np.array(res)
    result = np.transpose(result)

    with open(outputfilename, "w") as f:
        f.write(columnName)
        for i in range(len(result)):
            msec = xs[i] % 1000
            sec = xs[i] // 1000 % 60
            min = xs[i] // 1000 // 60 % 60
            hour = xs[i] // 1000 // 60 // 60
            f.write("%d_%d_%d_%d"%(hour, min, sec, msec)+',')
            f.write(",".join(map(str,result[i])))
            f.write("\n")

if __name__ == "__main__":
    main()


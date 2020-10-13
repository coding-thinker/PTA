# all accpeted

import sys

def format_time_stamp(time_stamp:str):
    l = sorted([int(i) for i in time_stamp.split(':')], reverse = 1)
    return sum([l[i] * 60**i for i in range(3)])

N = int(input())
minimum = sys.maxsize
maximum = -sys.maxsize
min_name = None
max_name = None

for _ in range(N):
    name, enter, leave = input().split()
    enter, leave = [format_time_stamp(i) for i in [enter, leave]]
    if enter < minimum:
        minimum = enter
        min_name = name
    if leave > maximum:
        maximum = leave
        max_name = name

print(min_name, max_name)
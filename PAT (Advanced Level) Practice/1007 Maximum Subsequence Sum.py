# all accepted

import sys

N = int(input())
inputing = [int(i) for i in input().split()]

flag = 0
sum_list = []

for i in range(len(inputing)):
    if inputing[i] > 0:
        flag = 1
    if flag != 1 and inputing[i] == 0:
        flag = 2
    
    if i == 0:
        sum_list.append(inputing[0])
    else:
        sum_list.append(sum_list[-1] + inputing[i])

if flag == 0:
    print(0, inputing[0], inputing[-1])
elif flag == 1:
    min = sys.maxsize
    max = -sys.maxsize
    min_index, max_index = None, None
    for i, each in enumerate(sum_list):
        if each > max:
            max = each
            max_index = i
    min_index = max_index - 1
    for i, each in enumerate(sum_list[:max_index]):
        if each < min:
            min = each
            min_index = i
    if min == sys.maxsize:
        min = 0
    if min_index == 0 and inputing[min_index] >0:
        print(sum(inputing[min_index:max_index+1]), inputing[min_index], inputing[max_index])
    else:
        print(max - min, inputing[min_index + 1], inputing[max_index])
else:
    print(0, 0, 0)



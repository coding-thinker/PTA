# all accepted

inputing = input().split()
num = int(inputing[0])
inputing.pop(0)

work_space = {i:0 for i in set(inputing)}
ok_set = []

if len(inputing) == len(set(inputing)):
    print(inputing[0])
else:
    for each in inputing:
        work_space[each] += 1
    for i, num in work_space.items():
        if num == 1:
            ok_set.append(i)
    for each in inputing:
        if each in ok_set:
            print(each)
            break
    else:
        print(None)
# all accepted

a, b = {}, {}
c = {}
for each in [a, b]:
    line = [float(i) for i in input().split()][1:]
    for i in range(len(line) // 2):
        each[int(line[i*2])] = line[i*2+1]

for i, num_0 in a.items():
    for j, num_1 in b.items():
        if i+j in c:
            c[i+j] += num_0 * num_1
        else:
            c[i+j] = num_0 * num_1

c = {i:j for i,j in c.items() if j != 0}
print(len(c), end='')
for each in sorted(list(c.keys()), reverse=1):
    if round(c[each],1) != 0:
        print(' %d %.1f' % (each, round(c[each],1)), end='')
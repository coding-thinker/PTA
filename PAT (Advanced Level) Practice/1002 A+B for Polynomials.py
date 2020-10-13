# all accepted

dictionary = {}
for _ in range(2):
    inputing = [float(i) for i in input().split()]
    for i in range(int(inputing[0])):
        powers = int(inputing[2*i+1])
        index = inputing[2*i+2]
        dictionary[powers] = dictionary.get(powers, 0) + index
output = ''
i = 0
for a, b in sorted(list(dictionary.items()), reverse=1):
    b = round(b, 1)
    if b:
        i += 1
        output += ' %d %.1f' % (a, b)
output = str(i) + output
print(output)

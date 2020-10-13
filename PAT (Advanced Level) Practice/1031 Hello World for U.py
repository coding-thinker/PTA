# all accepted

origin_str = input()
length = len(origin_str)

n1 = n3 = (length + 2) // 3
n2 = length - n1 - n3

for i in range(n1 - 1):
    print(origin_str[i] + " " * n2 + origin_str[length - i - 1])
i += 1
print(origin_str[i: length - i])
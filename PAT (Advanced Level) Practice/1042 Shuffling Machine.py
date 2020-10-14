# all accepted

deck = ['S%d' % i for i in range(1, 14)] + ['H%d' % i for i in range(1, 14)] + ['C%d' % i for i in range(1, 14)] + ['D%d' % i for i in range(1, 14)] + ['J1', 'J2']

N = int(input())
shuffle = [int(i) - 1 for i in input().split()]

for _ in range(N):
    temp = [None for i in range(54)]
    for i in range(len(shuffle)):
        temp[shuffle[i]] = deck[i]
    deck = temp[:]
for i, each in enumerate(deck):
    if i != len(deck) - 1:
        print(each, end = ' ')
    else:
        print(each)
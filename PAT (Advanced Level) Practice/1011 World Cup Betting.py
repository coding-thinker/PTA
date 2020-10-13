# all accepted

result = 1
strategy = []
names = {0: 'W', 1:'T', 2:'L'}
for _ in range(3):
    listing = [float(i) for i in input().split()]
    result *= max(listing)
    strategy.append(names[listing.index(max(listing))])
print(' '.join(strategy), round((result*0.65 - 1)*2, 2))
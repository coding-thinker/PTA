# This is the best version I can figure out with python
# Accepted on Cases 1-5 TLE on Case 6
# This algorithm is fine
# io takes too long time
# cpp version passes all cases, see in the same folder

from collections import deque

class Citys:
    def __init__(self, size):
        self.size = size
        self.paths = [[float('inf') for i in range(size)] for i in range(size)]
        self.teams = [0 for i in range(size)]
        self.src = -1
        self.dst = -1
        self.minimium = float('inf')
        self.mans = 0
        self.num = 0

    def set_teams(self):
        self.teams = [int(i) for i in input().split()]


    def set_path(self, times):
        for _ in range(times):
            a, b, v = [int(i) for i in input().split()]
            #self.paths[a][b] = v
            self.paths[b][a] = v


    def dfs(self, used, paths, mans):
        if (used and used[-1] == self.dst):
            if self.minimium > paths:
                self.num = 1
                self.minimium = paths
                self.mans = mans
            elif self.minimium == paths:
                self.num += 1
                if self.mans < mans:
                    self.mans = mans
            return
        else:
            if used:
                for each in set(range(self.size)) - set(used):
                    temp = self.paths[used[-1]][each] + paths
                    if temp == float('inf') or self.minimium < temp:
                        continue
                    if temp <= self.minimium:
                        used.append(each)
                        self.dfs(used, temp, mans + self.teams[each])
                        used.pop()
            else:
                used.append(self.src)
                self.dfs(used, paths , mans + self.teams[self.src])
                



n, m, a, b = [int(i) for i in input().split()]
city = Citys(n)
city.set_teams()


for _ in range(m):
    aa, bb, v = [int(i) for i in input().split()]
    city.paths[aa][bb] = v
    city.paths[bb][aa] = v
city.src = a
city.dst = b

city.dfs(deque(),0,0)

print('%d %d' % (city.num, city.mans))

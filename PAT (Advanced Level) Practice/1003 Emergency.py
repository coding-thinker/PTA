'''
As an emergency rescue team leader of a city, you are given a special map of your country. The map shows several scattered cities connected by some roads. Amount of rescue teams in each city and the length of each road between any pair of cities are marked on the map. When there is an emergency call to you from some other city, your job is to lead your men to the place as quickly as possible, and at the mean time, call up as many hands on the way as possible.

Input Specification:
Each input file contains one test case. For each test case, the first line contains 4 positive integers: N (≤500) - the number of cities (and the cities are numbered from 0 to N−1), M - the number of roads, C1​​  and C​2​​  - the cities that you are currently in and that you must save, respectively. The next line contains N integers, where the i-th integer is the number of rescue teams in the i-th city. Then M lines follow, each describes a road with three integers c​1​​ , c2​​  and L, which are the pair of cities connected by a road and the length of that road, respectively. It is guaranteed that there exists at least one path from C​1​​  to C2.

Output Specification:
For each test case, print in one line two numbers: the number of different shortest paths between C​1 and C​2​​ , and the maximum amount of rescue teams you can possibly gather. All the numbers in a line must be separated by exactly one space, and there is no extra space allowed at the end of a line.

Sample Input:
5 6 0 2
1 2 1 5 3
0 1 1
0 2 2
0 3 1
1 2 1
2 4 1
3 4 1
Sample Output:
2 4
'''



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

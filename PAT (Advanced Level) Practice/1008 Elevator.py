# all accpeted

class elevator():
    def __init__(self):
        self.floor = 0
        self.time = 0
    
    def move(self, target):
        if target < self.floor:
            self.time += 4*(self.floor - target) + 5
            self.floor = target
        elif target > self.floor:
            self.time += 6*(target - self.floor) + 5
            self.floor = target
        else:
            self.time += 5
            self.floor = target
            

E = elevator()
[E.move(int(i)) for i in input().split()[1:]]
print(E.time)
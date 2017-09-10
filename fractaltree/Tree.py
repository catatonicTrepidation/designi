import random
import math
import Branch

pi = math.pi

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

class Tree:
    def __init__(self, pos, lth=100, agl=0, curlrate=0, colors=[255,255,255,255]):
        self.pos = pos
        self.branches = [Branch.Branch(pos, lth, agl, curlrate, colors)]
        self.gen = 0

    def grow(self): #stub from previous project
        for i in range(2**self.gen - 1, 2**(self.gen+1) - 1):
            b = self.branches[i]
            self.branches.append(Branch.Branch(b.right_point(), b.lth * 0.5, b.agl + 90 + b.curlrate, b.curlrate, b.colors))
            self.branches.append(Branch.Branch(b.left_point(),  b.lth * 0.5, b.agl + 90 + b.curlrate, b.curlrate, b.colors))
        print("len of branches:",len(self.branches))
        self.gen += 1

    def inccolor(self, amt): #stub from previous project
        self.colors = ([0,0,0,255],[255,255,255,255])

    def saypos(self): #stub from previous project
        return str(self.pos[0]) + ", " + str(self.pos[1])

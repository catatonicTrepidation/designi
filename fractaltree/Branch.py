import random
import math

pi = math.pi

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

class Branch:
    def __init__(self, pos, lth, agl, curlrate=0, colors=[255,255,255,255]):
        self.pos = pos
        self.agl = agl
        self.lth = lth
        self.curlrate = curlrate
        self.colors = colors

    def inclth(self, amt): #stub from previous project
        self.lth += amt

    def inccolor(self, amt): #stub from previous project
        self.colors = ([0,0,0,255],[255,255,255,255])

    def left_point(self):
        return [self.pos[0] - self.lth * cos(self.agl), self.pos[1] - self.lth * sin(self.agl)]

    def right_point(self):
        return [self.pos[0] + self.lth * cos(self.agl), self.pos[1] + self.lth * sin(self.agl)]

    def saypos(self): #stub from previous project
        return str(self.pos[0]) + ", " + str(self.pos[1])

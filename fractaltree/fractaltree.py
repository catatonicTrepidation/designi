import random
import numpy
import math, colorsys
from PIL import Image, ImageDraw
import ImageSequence
import Image
#import images2gif
import imageio
import Branch
import Tree
import CurlyBranch
import copy

sequence = []

bgcolor = (35,30,30,100)

#Image's width and height
width, height = 800, 800
image = Image.new('RGB', (width, height), color=bgcolor)
draw = ImageDraw.Draw(image, 'RGBA')
pixels = image.load()

pi = math.pi
sin = math.sin
cos = math.cos
tan = math.tan
arcsin = math.asin
arccos = math.acos
arctan = math.atan
sqrt = math.sqrt
power = math.pow



inc_theta = 0.001
max_theta = 4 * pi


def tree(branches):
    image = Image.new('RGB', (width, height), color=bgcolor)
    draw = ImageDraw.Draw(image, 'RGBA')
    pixels = image.load()
    

    return image


def draw_tree(tree, draw):
    for i in range(2**tree.gen - 1, 2**(tree.gen+1) - 1):
            b = tree.branches[i]
            #print(tuple(b.left_point() + b.right_point()))
            draw.line(tuple(b.left_point() + b.right_point()), fill=tuple(b.colors), width=1)


#let's color it by int(ang/2pi), i.e. by sine "hump" 

iterations = 10
startingiter = 10

t1 = Tree.Tree([width/4, height/4], 200, 90, 0, [230,240,255,255])
t2 = Tree.Tree([3*width/4, 3*height/4], 200, 90, 0, [255,240,230,255])
curl1 = Tree.Tree([width/2, height/2], 200, 90, 15, [230,245,230,255])

for i in range(iterations):
    file_num = 0
    sequence.append(image.copy())
    draw_tree(t1, draw)
    t1.grow()
    draw_tree(t2, draw)
    t2.grow()
    draw_tree(curl1, draw)
    curl1.grow()
    #print(i)
    #file_num = i
    #image.save('../outputs/FractalTree GIF/fractaltree' + str(file_num) + '.png')

for j in reversed(range(len(sequence) - 1)):
    sequence.append(sequence[j].copy())
    #sequence.append(Image.new('RGB', (width, height), color=(7,0,2)))


sequence = [numpy.array(im) for im in sequence]
file_num = 4
imageio.mimsave('../outputs/FractalTree GIF/fractaltree' + str(file_num) + '.gif', sequence, duration=0.11)

#images2gif.writeGif('outputs/warpdim GIF/warpdim.gif', sequence, 2.0, True, False, 2)

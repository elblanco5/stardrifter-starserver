#!/usr/bin/python
import math
import random
from PIL import Image, ImageDraw

#useful for seeing the galaxy
drawgalaxy = True

n = 2500

def getcoordprob(x,y):
    """this uses a distance from center fall-off approach, this seems to
    generate more stars near the center as expected and fewer stars near the
    edges"""
    distance = (math.sqrt(x**2 + y**2)) # distance from center of galaxy
    maxd = (math.sqrt(n**2 + n**2)) #the maximum distance possible in the galactic grid
    reduction = ((maxd-distance)/maxd) #computes the drop-off probability
    if(distance != 0):
        return reduction/distance #normalizes to the size of the galactic grid

def generatestarlevel():
    """this generates the number of stars at a coordinate"""
    throw = random.randint(1,100)
    plist = [38,59,72,79,86,93,97,99,100] #some distribution
    if (throw < plist[0]):
        return 1
    elif (throw >= plist[0] and throw < plist[1]):
        return 2
    elif (throw >= plist[1] and throw < plist[2]):
        return 3
    elif (throw >= plist[2] and throw < plist[3]):
        return 4
    elif (throw >= plist[3] and throw < plist[4]):
        return 5
    elif (throw >= plist[4] and throw < plist[5]):
        return 6
    elif (throw >= plist[5] and throw < plist[6]):
        return 7
    elif (throw >= plist[6] and throw < plist[7]):
        return 8
    elif (throw >= plist[7] and throw <= plist[8]):
        return 9

def starcolor(star):
    """used for generating some kind of color for drawing"""
    color = {
            1:(79,129,189,0),
            2:(155,183,107,0),
            3:(196,213,64,0),
            4:(234,240,240,0),
            5:(255,255,100,0),
            6:(255,162,100,0),
            7:(255,80,100,0),
            8:(255,30,100,0),
            9:(255,0,100,0)
            }
    return color[star]

#sets the galactic grid to empty space
galaxy = [[0 for x in range(n+1)] for y in range(n+1)]

if (drawgalaxy == True):
    im = Image.new("RGB", (n*2,n*2))
    draw = ImageDraw.Draw(im)

systems = 0 # count the number of systems that have been created
starcount = 0 # count the number of stars

#run through all the coordinates in the galactic grid 0,0 is the center
for x in range(-n,n+1):
    for y in range(-n,n+1):

        r = random.random() #let's get some random number between 0,1

        # if the generated number is less than the computed probability in the
        # galactic grid, then a system should exist there
        if (r < getcoordprob(x,y)):
            stars = generatestarlevel() # how many stars should there be?
            galaxy[x][y]=stars

            if(drawgalaxy == True):
                draw.ellipse((x+n-stars,y+n-stars,x+n+stars,y+n+stars), fill=starcolor(stars))

            systems+=1
            starcount+=stars
        else:
            galaxy[x][y]=0

print systems
print starcount

if(drawgalaxy == True):
    del draw
    im.save("thing.png")

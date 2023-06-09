# File created by: Liam Newberry
from math import *
# calculate the velocities on a given maxvel and angle
def unit_cir(angle, max):
    # convert to degrees
    angle *= pi
    angle /= 180
    # unit circle alg 2 math
    xval = cos(angle)
    xval *= max
    yval = sin(angle)
    yval *= max
    return [xval,yval]

def is_touching(pos1, r1, pos2, r2):
    # use pythagorean theorum to see if two spriteas are touching
    x = abs(pos1[0] - pos2[0])
    y = abs(pos1[1] - pos2[1])
    x *= x
    y *= y
    hyp = sqrt(x+y)
    # finished pythag theorum
    # if the distance between < sum of radiuses
    if hyp <= r1 + r2:
        return True
    else:
        return False
    
def find_angle(pos1,pos2):
    # self.pos first
    x = pos1[0] - pos2[0]
    y = pos1[1] - pos2[1]
    # to keep from dividing by 0
    if x == 0:
        x += 0.000001
    angle = atan(y/x)
    angle /= pi
    angle *= 180
    if x > 0:
        angle += 90
    if x < 0:
        angle += 270
    return angle
    
def time_of_play(start, end):
    # used to calculate how long player was in game
    t = (end-start)/60
    minutes = int(t)
    minutes = str(minutes)
    seconds = int((t - int(minutes))*60)
    seconds = str(seconds)
    if len(seconds) == 1:
        seconds = "0" + seconds
    return str(minutes + ":" + seconds)
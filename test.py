from math import *
def unit_cir(angle, max):
    angle *= pi
    angle /= 180
    xval = cos(angle)
    xval *= max
    yval = sin(angle)
    yval *= max
    return [xval,yval]
angles = []

def list_maker(min,max,interval,list):
    while min <= max:
        list.append(min)
        min += interval
    return list
list_maker(10,360,10,angles)
player = (100,60) # 25
mob = (100,80) # 10
pr = 25
mr = 53/2

def is_touching(pos1, r1, pos2, r2):
    x = abs(pos1[0] - pos2[0])
    y = abs(pos1[1] - pos2[1])
    x *= x
    y *= y
    hyp = sqrt(x+y)
    if hyp <= r1 + r2:
        return True
    else:
        return False
print(is_touching(player,pr,mob,mr))
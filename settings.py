# File created by: Liam Newberry
import pygame as pg
# screen dimensions
WIDTH = 1200
HEIGHT = 900
# WIDTH = 1600
# HEIGHT = 1100
# player applied settings
PLAYER_ACC = 0.7
PLAYER_FRICTION = -0.03
PLAYER_JUMP = 20
PLAYER_GRAV = 0
PMAX_VEL = 25
PROT_SPEED = 10
P_IMMUNITY = 1200
PLAYER_RADIUS = 25
# mob applied settings
MOB_ACC = 2
MOB_FRICTION = -0.3
MOB_VEL_LIST = ["xvel", "yvel"]
MOB_SPAWN_LIST = ["top","bottom", "left", "right"]
MOB_CHARGE = ["pos", "neg"]
MOB_SMALL_IMG_LIST = ["1", "2", "3"]
MOB_S_X = 53
MOB_S_Y = 53
MOB_S_RADIUS = 26.5
# bullet applied settings
BMAX_VEL = 50
B_LEN = 7
# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
# screen refresh rate
FPS = 30
# variable for while loop
RUNNING = True
SCORE = 0
PAUSED = False
clk = False
# dimenstions of player image
player_x_len = 50
player_y_len = 100
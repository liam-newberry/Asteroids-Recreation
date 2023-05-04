# File created by: Liam Newberry
import pygame as pg
# screen refresh rate
FPS = 60
# screen dimensions
WIDTH = 1200
HEIGHT = 900
# WIDTH = 1600
# HEIGHT = 1100
# player applied settings
PLAYER_ACC = 0.8 * 30/FPS
PLAYER_FRICTION = -0.03 * 30/FPS
PMAX_VEL = 25 * 30/FPS
PROT_SPEED = 10 * 30/FPS
P_IMMUNITY = 1200
PLAYER_RADIUS = 25
# mob applied settings
MOB_VEL_LIST = ["xvel", "yvel"]
MOB_SPAWN_LIST = ["top","bottom", "left", "right"]
MOB_CHARGE = ["pos", "neg"]
MOB_SMALL_IMG_LIST = ["1", "2", "3"]
MOB_S_X = 53
MOB_S_Y = 53
MOB_S_RADIUS = 26.5
MOB_MAX_VEL = 6  * 30/FPS
MOB_MIN_VEL = 2  * 30/FPS
# bullet applied settings
BMAX_VEL = 25 * 30/FPS
B_LEN = 7
B_RADIUS = 4
# particle applied settings
PARL_WIDTH = 4
PARL_HEIGHT = 70
PARD_WIDTH = 7
PARD_HEIGHT = 7
PAR_MAX_VEL = 3 * 30/FPS
PAR_MAX_DIST = 20
# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
# variable for while loop
RUNNING = True
SCORE = 0
PAUSED = False
clk = False
# dimenstions of player image
player_x_len = 50
player_y_len = 100
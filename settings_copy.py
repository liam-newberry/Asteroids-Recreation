# File created by: Liam Newberry
import pygame as pg
# screen dimensions
WIDTH = 1200
HEIGHT = 900
# player applied settings
PLAYER_ACC = 0.7
PLAYER_FRICTION = -0.03
PLAYER_JUMP = 20
PLAYER_GRAV = 0
PMAX_VEL = 30
PROT_SPEED = 10
# mob applied settings
MOB_ACC = 2
MOB_FRICTION = -0.3
MOB_VEL_LIST = ["xvel", "yvel"]
MOB_SPAWN_LIST = ["top","bottom", "left", "right"]
MOB_CHARGE = ["pos", "neg"]
MOB_SMALL_IMG_LIST = ["1", "2", "3"]
MOB_S_X = 53
MOB_S_Y = 53
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
# Starting platforms
# PLATFORM_LIST = [[0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"],
#                  [WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (100,255,100), "bouncey"],
#                  [125, HEIGHT - 350, 100, 5, (200,100,50), "disappearing"],
#                  [700, 200, 100, 20, (200,200,200), "normal"],
#                  [175, 100, 50, 20, (200,200,200), "normal"]]
# PLATFORM_LIST = []
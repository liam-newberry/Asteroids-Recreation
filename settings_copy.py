# File created by: Liam Newberry
# screen refresh rate
FPS = 60
# screen dimensions
WIDTH = 1200
HEIGHT = 900
# game applied settings
MAIN_MUSIC_VOLUME = 100 / 100
MAIN_MUSIC_INTERVAL = 10
MAIN_MIN_MUSIC_BUFFER = 200
# player applied settings
PLAYER_ACC = 0.8 * 30/FPS
PLAYER_FRICTION = -0.03 * 30/FPS
PMAX_VEL = 25 * 30/FPS
PROT_SPEED = 10 * 30/FPS
P_IMMUNITY = 1200
PLAYER_RADIUS = 25
PTHRUST_VOLUME = 50 / 100
PFIRE_VOLUME = 40 / 100
# mob applied settings
MOB_VEL_LIST = ["xvel", "yvel"]
MOB_SPAWN_LIST = ["top","bottom", "left", "right"]
MOB_CHARGE = ["pos", "neg"]
MOB_SMALL_IMG_LIST = ["1", "2", "3"]
MOB_S_X = 53
MOB_S_Y = 53
MOB_S_RADIUS = MOB_S_X/2
MOB_S_MAX_VEL = 6  * 30/FPS
MOB_S_MIN_VEL = 2  * 30/FPS
MOB_S_ANI_NUM = 3
MOB_S_SCORE = 100
MOB_S_MAX_DIST = 60
MOB_M_X = 130
MOB_M_Y = 130
MOB_M_RADIUS = MOB_M_X/2
MOB_M_MAX_VEL = MOB_S_MAX_VEL*(2/3)  * 30/FPS
MOB_M_MIN_VEL = MOB_S_MIN_VEL*(2/3)  * 30/FPS
MOB_M_ANI_NUM = 5
MOB_M_SCORE = 50
MOB_M_MAX_DIST = 100
MOB_L_X = 190
MOB_L_Y = 190
MOB_L_RADIUS = MOB_L_X/2
MOB_L_MAX_VEL = MOB_S_MAX_VEL*(2/3)  * 30/FPS
MOB_L_MIN_VEL = MOB_S_MIN_VEL*(2/3)  * 30/FPS
MOB_L_ANI_NUM = 7
MOB_L_SCORE = 20
MOB_CRASH_VOLUME = 50 / 100
# invader applied settings
INVADER_S_MAX_VEL = 4
INVADER_L_MAX_VEL = 3
INVADER_S_Y_VEL = 2
INVADER_L_Y_VEL = 1.5
INVADER_S_RADIUS = 33
INVADER_L_RADIUS = 42
INVADER_S_SCORE = 200
INVADER_L_SCORE = 150
INVADER_VOLUME = 25 / 100
# bullet applied settings
B_SERIAL = 0
BMAX_VEL = 30 * 30/FPS
B_LEN = 7
B_RADIUS = 4
B_LIFETIME = 750
# particle applied settings
PARL_WIDTH = 4
PARL_HEIGHT = 70
PARD_WIDTH = 7
PARD_HEIGHT = 7
P_PAR_MAX_VEL = 3 * 30/FPS
P_PAR_MAX_DIST = 20
S_PAR_MAX_VEL = 3 * 30/FPS
M_PAR_MAX_VEL = 5 * 30/FPS
L_PAR_MAX_VEL = 7 * 30/FPS
S_PAR_MAX_DIST = 20
M_PAR_MAX_DIST = 60
L_PAR_MAX_DIST = 100
# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
GREEN = (0,255,0)
# variable for while loop
RUNNING = True
SCORE = 0
PAUSED = False
clk = False
# dimenstions of player image
player_x_len = 50
player_y_len = 100
# lists
MOB_ALL_VELS = [MOB_S_MAX_VEL, MOB_S_MIN_VEL,
                MOB_M_MAX_VEL, MOB_M_MIN_VEL,
                MOB_L_MAX_VEL, MOB_M_MIN_VEL,]
WAVES = [[4,0,0],
         [6,0,0],
         [4,0,1],
         [4,1,0],
         [6,1,1],
         [6,1,2],
         [6,2,2]]
# File created by: Liam Newberry
'''
Goals:
create a player that can rotate
let the player shoot asteroids (mobs)
create animations for mobs and players
add sound effects
get a high score from shooting asteroids
player can move through one edge and spawn at the other
create thrust (and animation)
let player bind own settings
add hostile mobs
'''
# import libs
import pygame as pg
import os
# import settings and sprites files
from settings_copy import *
from sprites_copy import *
# import sleep function
from time import sleep

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

# create game class in order to pass properties to the sprites file
class Game:
    # startup code
    def __init__(self):
        # init game window etc.
        # inits pygame and souns sytem
        pg.init()
        pg.mixer.init()
        # sets screen size
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # names the window
        pg.display.set_caption("Asteroids")
        # stores the clock class
        self.clock = pg.time.Clock()
        # used for while loop
        self.running = True
        self.keystate = pg.key.get_pressed()
    # sets up in game settings
    def new(self):
        # starting a new game
        self.score = 0
        # new place to store sprites
        self.all_sprites = pg.sprite.Group()
        # new place to store mobs
        self.enemies = pg.sprite.Group()
        # image used on Player
        p_image = pg.image.load(os.path.join(img_folder, "p2.png")).convert()
        p_image_rect = p_image.get_rect()
        pt_image = pg.image.load(os.path.join(img_folder, "thruster.png")).convert()
        pt_image_rect = pt_image.get_rect()
        pimgs = [p_image, p_image_rect]
        ptimgs = [pt_image, p_image_rect]
        # defines player with the image
        self.player = Player(self, pimgs, self.screen, "cont")
        self.playert = Player(self, ptimgs, self.screen, "thrust")
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # player added to sprites list
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.playert)
        
        # for plat in PLATFORM_LIST:
        #     p = Platform(*plat)
        #     self.all_sprites.add(p)
        #     self.platforms.add(p)
        # adds mobs to the screen
        s_asteroid1 = pg.image.load(os.path.join(img_folder, "s_asteroid1.png")).convert()
        s_asteroid2 = pg.image.load(os.path.join(img_folder, "s_asteroid2.png")).convert()
        s_asteroid3 = pg.image.load(os.path.join(img_folder, "s_asteroid3.png")).convert()
        s_asteroid_rect = s_asteroid1.get_rect()
        mimgs = [s_asteroid1,s_asteroid2,s_asteroid3,s_asteroid_rect]
        for i in range(0,10):
            rand_s_asteroid = choice(MOB_SMALL_IMG_LIST)
            if rand_s_asteroid == "1":
                s_asteroid = s_asteroid1
            elif rand_s_asteroid == "2":
                s_asteroid = s_asteroid2
            elif rand_s_asteroid == "3":
                s_asteroid = s_asteroid3
            m = Mob(s_asteroid,s_asteroid_rect)
            self.all_sprites.add(m)
            self.enemies.add(m)
        # starts all the import init functions 
        self.run()
    # def input(self):
        
    #     # if keystate[pg.K_0]:
    #     #     print(1)
    #     #     self.all_sprites.add(self.bullet1)
    #     pass
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    # detects anything that happens in the game
    def events(self):
        for event in pg.event.get():
            # if the app is quit, end the program
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            # if not keystate[pg.K_w]:
            
    # updates positions, events, and keeps tabs and updates everything
    def update(self):
        # updates the sprites
        self.all_sprites.update()
        # runs inbounds function in Player class
        self.player.inbounds()  
        # if not self.keystate[pg.K_w]:
        #     if self.player.timage.get_alpha() != 0:
        #         self.player.timage.set_alpha(0)
    #     if self.keystate[pg.K_w]:
    #         self.player.timage.set_alpha(255)
    #     else:
    #         # self.player.timage.set_alpha(0)
    #         pass
    # # all draw functions
    def draw(self):
        #make background black
        self.screen.fill(BLACK)
        # blit all the sprites
        self.all_sprites.draw(self.screen)
        # is this a method or a function? -- function
        # only refreshes the window
        pg.display.flip()
    # print text on the display
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        # draw the text
        self.screen.blit(text_surface, text_rect)
    # gets the coords of the cursor
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()
# ends the pg program
pg.quit()
# File created by: Liam Newberry
'''
Goals:
create a player that can rotate {}
let the player shoot asteroids
create animations for invaders and players
add sound effects
get a high score from shooting asteroids
player can move through one edge and spawn at the other {}
create thrust (and animation) {}
let player bind own settings
add invaders
'''
# import libs
import pygame as pg
import os
# import settings and sprites files
from settings import *
from sprites import *

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
        self.life_count = 3
        self.death = False
    # sets up in game settings
    def new(self):
        # starting a new game
        self.score = 0
        # new place to store sprites
        self.all_sprites = pg.sprite.Group()
        self.pbullets = []
        self.pbullets_active = []
        self.players = pg.sprite.Group()
        self.invaders = pg.sprite.Group()
        self.sasteroids = pg.sprite.Group()
        self.masteroids = pg.sprite.Group()
        self.lasteroids = pg.sprite.Group()
        # image used on Player
        # defines player with the image 
        s_asteroid1 = pg.image.load(os.path.join(img_folder, "s_asteroid1.png")).convert()
        s_asteroid2 = pg.image.load(os.path.join(img_folder, "s_asteroid2.png")).convert()
        s_asteroid3 = pg.image.load(os.path.join(img_folder, "s_asteroid3.png")).convert()
        s_asteroid_rect = s_asteroid1.get_rect()
        for i in range(0,10):
            rand_s_asteroid = choice(MOB_SMALL_IMG_LIST)
            if rand_s_asteroid == "1":
                s_asteroid = s_asteroid1
            elif rand_s_asteroid == "2":
                s_asteroid = s_asteroid2
            elif rand_s_asteroid == "3":
                s_asteroid = s_asteroid3
            sa = Small_Ast(s_asteroid,s_asteroid_rect,"small_ast", self)
            self.all_sprites.add(sa)
            self.sasteroids.add(sa)
        self.new_player()
        # starts all the import init functions 
        self.run()
    def new_player(self):
        p_image = pg.image.load(os.path.join(img_folder, "player.png")).convert()
        p_image_rect = p_image.get_rect()
        pt_image = pg.image.load(os.path.join(img_folder, "thruster.png")).convert()
        pimgs = [p_image, p_image_rect]
        ptimgs = [pt_image, p_image_rect]
        player = Player(self, pimgs, self.screen, "cont")
        playert = Player(self, ptimgs, self.screen, "thrust")
        self.player = player
        self.playert = playert
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.playert)
        self.players.add(self.player)
        self.players.add(self.playert)
        self.death = False
        self.player_life_img = pg.image.load(os.path.join(img_folder, "player_lives.png"))
        self.player_life_rect = self.player_life_img.get_rect()
        self.player_life_rect.x = 20
        self.player_life_rect.y = 50
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
    def p_death_ani(self):
        self.life_count-=1
        line_image = pg.image.load(os.path.join(img_folder, "line.png")).convert()
        line_image_rect = line_image.get_rect()
        dot_image = pg.image.load(os.path.join(img_folder, "dot.png")).convert()
        dot_image_rect = dot_image.get_rect()
        imgs = [line_image,line_image_rect,dot_image,dot_image_rect]
        for i in range(0,3):
            l = Particles(imgs,"line",self)
            self.all_sprites.add(l)
        for i in range(0,5):
            d = Particles(imgs,"dot",self)
            self.all_sprites.add(d)
        self.time_of_death = pg.time.get_ticks()
    # updates positions, events, and keeps tabs and updates everything
    def update(self):
        # updates the sprites
        self.all_sprites.update()
        now = pg.time.get_ticks()
        if self.life_count != 0 and len(self.players) == 0:
            if now - self.time_of_death >= 1400:
                self.new_player()
        if len(self.pbullets_active) > 4:
            self.pbullets_active.pop(0)
    def draw(self):
        #make background black
        self.screen.fill(BLACK)
        # blit all the sprites
        self.all_sprites.draw(self.screen)
        life_img1 = self.player_life_img
        life_img1.set_colorkey(BLACK)
        life_rect1 = self.player_life_rect
        life_img2 = self.player_life_img
        life_img2.set_colorkey(BLACK)
        life_rect2 = self.player_life_rect
        life_img3 = self.player_life_img
        life_img3.set_colorkey(BLACK)
        life_rect3 = self.player_life_rect
        if self.life_count >= 3:
            life_rect3.x = 110
            life_rect3.y = 80
            self.screen.blit(life_img3,life_rect3)
        if self.life_count >= 2:
            life_rect2.x = 60
            life_rect2.y = 80
            self.screen.blit(life_img2,life_rect2)
        if self.life_count >= 1:
            life_rect1.x = 10 
            life_rect1.y = 80
            self.screen.blit(life_img1,life_rect3)
        # is this a method or a function? -- function
        # only refreshes the window
        self.draw_text(str(self.score), "Hyperspace", 60, WHITE, 20,5,"topleft",True,False)
        pg.display.flip()
    # print text on the display
    def draw_text(self, text, font, size, color, x, y, align, bold, italicize):
        font_name = pg.font.match_font(font, bold, italicize)
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "topleft":
            text_rect.topleft = (x,y)
        elif align == "topright":
            text_rect.topright = (x,y)
        elif align == "center":
            text_rect.center = (x,y)
        elif align == "midtop":
            text_rect.midtop = (x,y)
        elif align == "midbottom":
            text_rect.midbottom = (x,y)
        elif align == "midleft":
            text_rect.midleft = (x,y)
        elif align == "midright":
            text_rect.midright = (x,y)
        elif align == "bottomleft":
            text_rect.bottomleft = (x,y)
        elif align == "bottomright":
            text_rect.bottomright = (x,y)
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
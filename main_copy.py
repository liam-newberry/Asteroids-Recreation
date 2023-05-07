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
from settings_copy import *
from sprites_copy import *

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")
sound_folder = os.path.join(game_folder, "sounds")
s_ast = os.path.join(img_folder, "s_ast")
m_ast = os.path.join(img_folder, "m_ast")
l_ast = os.path.join(img_folder, "l_ast")
particle_img = os.path.join(img_folder, "particles")
player_imgs = os.path.join(img_folder, "player")

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
        self.time_of_death = pg.time.get_ticks()
        self.player_life_img = pg.image.load(os.path.join(player_imgs, "player_lives.png"))
        self.player_life_rect = self.player_life_img.get_rect()
    # sets up in game settings
    def new(self):
        # starting a new game
        self.score = 0
        # new place to store sprites
        self.all_sprites = pg.sprite.Group()
        self.pbullets = []
        self.pbullet_group = pg.sprite.Group()
        self.pbullets_active = []
        self.players = pg.sprite.Group()
        self.invaders = pg.sprite.Group()
        self.asteroids = []
        self.near_death = []
        self.asteroids_copy = []
        self.mob_serial = 0
        self.last_sprite = -1000
        self.music_buffer = 1000
        self.last_played = 0
        self.beat1 = pg.mixer.Sound(os.path.join(sound_folder, "beat1.wav"))
        self.beat2 = pg.mixer.Sound(os.path.join(sound_folder, "beat2.wav"))
        self.beat = self.beat1
        # image used on Player
        # defines player with the image 
        self.new_player()
        self.large_ast_spawn(1)
        self.medium_ast_spawn(2)
        self.small_ast_spawn(4)
        self.run()
    def small_ast_spawn(self, number):
        s_asteroid1 = pg.image.load(os.path.join(s_ast, "s_asteroid1.png")).convert()
        s_asteroid2 = pg.image.load(os.path.join(s_ast, "s_asteroid2.png")).convert()
        s_asteroid3 = pg.image.load(os.path.join(s_ast, "s_asteroid3.png")).convert()
        s_asteroid4 = pg.image.load(os.path.join(s_ast, "s_asteroid4.png")).convert()
        s_asteroid_rect = s_asteroid1.get_rect()
        for i in range(0,number):
            rand_s_asteroid = randint(1,4)
            if rand_s_asteroid == 1:
                s_asteroid = s_asteroid1
            elif rand_s_asteroid == 2:
                s_asteroid = s_asteroid2
            elif rand_s_asteroid == 3:
                s_asteroid = s_asteroid3
            elif rand_s_asteroid == 4:
                s_asteroid = s_asteroid4
            sa = Ast(s_asteroid,s_asteroid_rect,"small_ast", self)
            self.all_sprites.add(sa)
    def medium_ast_spawn(self, number):
        m_asteroid1 = pg.image.load(os.path.join(m_ast, "m_asteroid1.png")).convert()
        m_asteroid2 = pg.image.load(os.path.join(m_ast, "m_asteroid2.png")).convert()
        m_asteroid3 = pg.image.load(os.path.join(m_ast, "m_asteroid3.png")).convert()
        m_asteroid4 = pg.image.load(os.path.join(m_ast, "m_asteroid4.png")).convert()
        m_asteroid_rect = m_asteroid1.get_rect()
        for i in range(0,number):
            rand_m_asteroid = randint(1,4)
            if rand_m_asteroid == 1:
                m_asteroid = m_asteroid1
            elif rand_m_asteroid == 2:
                m_asteroid = m_asteroid2
            elif rand_m_asteroid == 3:
                m_asteroid = m_asteroid3
            elif rand_m_asteroid == 4:
                m_asteroid = m_asteroid4
            ma = Ast(m_asteroid,m_asteroid_rect,"medium_ast", self)
            self.all_sprites.add(ma)
    def large_ast_spawn(self, number):
        l_asteroid1 = pg.image.load(os.path.join(l_ast, "l_asteroid1.png")).convert()
        l_asteroid2 = pg.image.load(os.path.join(l_ast, "l_asteroid2.png")).convert()
        l_asteroid3 = pg.image.load(os.path.join(l_ast, "l_asteroid3.png")).convert()
        l_asteroid4 = pg.image.load(os.path.join(l_ast, "l_asteroid4.png")).convert()
        l_asteroid_rect = l_asteroid1.get_rect()
        for i in range(0,number):
            rand_l_asteroid = randint(1,4)
            if rand_l_asteroid == 1:
                l_asteroid = l_asteroid1
            elif rand_l_asteroid == 2:
                l_asteroid = l_asteroid2
            elif rand_l_asteroid == 3:
                l_asteroid = l_asteroid3
            elif rand_l_asteroid == 4:
                l_asteroid = l_asteroid4
            la = Ast(l_asteroid,l_asteroid_rect,"large_ast", self)
            self.all_sprites.add(la)
    def new_player(self):
        p_image = pg.image.load(os.path.join(player_imgs, "player.png")).convert()
        p_image_rect = p_image.get_rect()
        pt_image = pg.image.load(os.path.join(player_imgs, "thruster.png")).convert()
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
        self.player_life_img = pg.image.load(os.path.join(player_imgs, "player_lives.png"))
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
        self.life_count -= 1
        line_image = pg.image.load(os.path.join(particle_img, "line.png")).convert()
        line_image_rect = line_image.get_rect()
        imgs = [line_image,line_image_rect,None,None]
        for i in range(0,3):
            l = Particles(imgs,"line",self,"player")
            self.all_sprites.add(l)
        self.time_of_death = pg.time.get_ticks()
    def ast_ani(self,number,size):
        dot_image = pg.image.load(os.path.join(particle_img, "dot.png")).convert()
        dot_image_rect = dot_image.get_rect()
        imgs = [None,None,dot_image,dot_image_rect]
        for i in range(0,number):
            d = Particles(imgs,"dot",self,"mob",size)
            self.all_sprites.add(d)
    def is_new_player(self):
        if self.life_count != 0 and len(self.players) == 0:
            if self.now - self.time_of_death >= 1400:
                self.new_player()
    def update_ast_list(self):
        for i in self.asteroids:
            if not i[3]:
                ind = self.asteroids.index(i)
                self.asteroids.pop(ind)
    def update_bullet_list(self):
        for bullet in self.pbullets_active:
            if self.now - bullet.birth > B_LIFETIME:
                self.pbullets_active.remove(bullet)
                break
    def main_music(self):
        if self.now - self.last_played >= self.music_buffer:
            self.beat.set_volume(MAIN_MUSIC_VOLUME)
            pg.mixer.Sound.play(self.beat)
            if self.beat == self.beat1:
                self.beat = self.beat2
            elif self.beat == self.beat2:
                self.beat = self.beat1
                if self.music_buffer > MAIN_MIN_MUSIC_BUFFER:
                    self.music_buffer -= MAIN_MUSIC_INTERVAL
            self.last_played = pg.time.get_ticks()
    # updates positions, events, and keeps tabs and updates everything
    def update(self):
        # updates the sprites
        self.all_sprites.update()
        self.now = pg.time.get_ticks()
        self.is_new_player()
        self.update_bullet_list()
        self.update_ast_list()
        self.main_music()
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
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
from title_screen import *
from end_screen import *
from math_funcs import *
# for getting date for highscores
from datetime import datetime
# for getting duration of a game
from time import mktime
from time import localtime
# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")
sound_folder = os.path.join(game_folder, "sounds")
s_ast = os.path.join(img_folder, "s_ast")
m_ast = os.path.join(img_folder, "m_ast")
l_ast = os.path.join(img_folder, "l_ast")
particle_img = os.path.join(img_folder, "particles")
player_imgs = os.path.join(img_folder, "player")
invader_imgs = os.path.join(img_folder, "invader")
title_imgs = os.path.join(img_folder, "title")
icon = pg.image.load(os.path.join(title_imgs, "icon.png"))
icon.set_colorkey(GREEN)

# create game class in order to pass properties to the sprites file
class Game:
    # startup code
    def __init__(self):
        # init game window etc.
        # inits pygame and sound system
        pg.init()
        pg.mixer.init()
        # sets screen size
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # names the window
        pg.display.set_caption("Asteroids")
        # window icon
        pg.display.set_icon(icon)
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
    def new(self):
        # resets all necessary class variables
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
        self.pbullets_fired = 0
        self.pbullets_hit = 0
        # to turn on sound
        self.sound = False
        # to turn on math visual
        self.math_vis = False
        if self.sound:
            self.beat1 = pg.mixer.Sound(os.path.join(sound_folder, "beat1.wav"))
            self.beat2 = pg.mixer.Sound(os.path.join(sound_folder, "beat2.wav"))
            self.beat = self.beat1
        # load all the images
        self.s_asteroid1 = pg.image.load(os.path.join(s_ast, "s_asteroid1.png")).convert()
        self.s_asteroid2 = pg.image.load(os.path.join(s_ast, "s_asteroid2.png")).convert()
        self.s_asteroid3 = pg.image.load(os.path.join(s_ast, "s_asteroid3.png")).convert()
        self.s_asteroid4 = pg.image.load(os.path.join(s_ast, "s_asteroid4.png")).convert()
        self.m_asteroid1 = pg.image.load(os.path.join(m_ast, "m_asteroid1.png")).convert()
        self.m_asteroid2 = pg.image.load(os.path.join(m_ast, "m_asteroid2.png")).convert()
        self.m_asteroid3 = pg.image.load(os.path.join(m_ast, "m_asteroid3.png")).convert()
        self.m_asteroid4 = pg.image.load(os.path.join(m_ast, "m_asteroid4.png")).convert()
        self.l_asteroid1 = pg.image.load(os.path.join(l_ast, "l_asteroid1.png")).convert()
        self.l_asteroid2 = pg.image.load(os.path.join(l_ast, "l_asteroid2.png")).convert()
        self.l_asteroid3 = pg.image.load(os.path.join(l_ast, "l_asteroid3.png")).convert()
        self.l_asteroid4 = pg.image.load(os.path.join(l_ast, "l_asteroid4.png")).convert()
        self.line_image = pg.image.load(os.path.join(particle_img, "line.png")).convert()
        self.dot_image = pg.image.load(os.path.join(particle_img, "dot.png")).convert()
        self.p_image = pg.image.load(os.path.join(player_imgs, "player.png")).convert()
        self.pt_image = pg.image.load(os.path.join(player_imgs, "thruster.png")).convert()
        self.puc_image = pg.image.load(os.path.join(player_imgs, "unit_circle.png")).convert()
        self.pd_image = pg.image.load(os.path.join(player_imgs, "direction.png")).convert()
        self.player_life_img = pg.image.load(os.path.join(player_imgs, "player_lives.png")).convert()
        self.large_inv_image = pg.image.load(os.path.join(invader_imgs, "invaderBig.png")).convert()
        self.small_inv_image = pg.image.load(os.path.join(invader_imgs, "invaderSmall.png")).convert()
        self.game_over = False
        self.check_player = True
        self.wave_count = 0
        # image used on Player
        # defines player with the image 
        self.new_player()
        # self.large_inv_spawn(1)
        # self.small_inv_spawn(1)
        # self.large_ast_spawn(4)
        #self.run()
    def small_ast_spawn(self, number, broken=False, pos=None):
        # spawns in small asteroids
        s_asteroid_rect = self.s_asteroid1.get_rect()
        for i in range(0,number):
            # get the random image that will be used
            rand_s_asteroid = randint(1,4)
            if rand_s_asteroid == 1:
                s_asteroid = self.s_asteroid1
            elif rand_s_asteroid == 2:
                s_asteroid = self.s_asteroid2
            elif rand_s_asteroid == 3:
                s_asteroid = self.s_asteroid3
            elif rand_s_asteroid == 4:
                s_asteroid = self.s_asteroid4
            # create a new instance
            sa = Ast(s_asteroid,s_asteroid_rect,"small_ast", self, broken, pos)
            self.all_sprites.add(sa)
    def medium_ast_spawn(self, number, broken=False, pos=None):
        # same as small_ast_spawn()
        m_asteroid_rect = self.m_asteroid1.get_rect()
        for i in range(0,number):
            rand_m_asteroid = randint(1,4)
            if rand_m_asteroid == 1:
                m_asteroid = self.m_asteroid1
            elif rand_m_asteroid == 2:
                m_asteroid = self.m_asteroid2
            elif rand_m_asteroid == 3:
                m_asteroid = self.m_asteroid3
            elif rand_m_asteroid == 4:
                m_asteroid = self.m_asteroid4
            ma = Ast(m_asteroid,m_asteroid_rect,"medium_ast", self, broken, pos)
            self.all_sprites.add(ma)
    def large_ast_spawn(self, number):
        # same as small_ast_spawn()
        l_asteroid_rect = self.l_asteroid1.get_rect()
        for i in range(0,number):
            rand_l_asteroid = randint(1,4)
            if rand_l_asteroid == 1:
                l_asteroid = self.l_asteroid1
            elif rand_l_asteroid == 2:
                l_asteroid =self. l_asteroid2
            elif rand_l_asteroid == 3:
                l_asteroid = self.l_asteroid3
            elif rand_l_asteroid == 4:
                l_asteroid = self.l_asteroid4
            la = Ast(l_asteroid,l_asteroid_rect,"large_ast", self)
            self.all_sprites.add(la)
    def small_inv_spawn(self, number):
        # spawns new invader
        s_inv_rect = self.small_inv_image.get_rect()
        # make all black transparent in image
        self.small_inv_image.set_colorkey(BLACK)
        imgs = [self.small_inv_image, s_inv_rect]
        for i in range(0,number):
            # create new instance
            si = Invader("small", imgs, self)
            self.all_sprites.add(si)
    def large_inv_spawn(self, number):
        # same as small inv_spawn
        l_inv_rect = self.large_inv_image.get_rect()
        self.large_inv_image.set_colorkey(BLACK)
        imgs = [self.large_inv_image, l_inv_rect]
        for i in range(0,number):
            li = Invader("large", imgs, self)
            self.all_sprites.add(li)
    def new_player(self):
        # all new player images, settings, types
        p_image_rect = self.p_image.get_rect()
        puc_image_rect = self.puc_image.get_rect()
        pimgs = [self.p_image, p_image_rect]
        ptimgs = [self.pt_image, p_image_rect]
        pucimgs = [self.puc_image, puc_image_rect]
        pdimgs = [self.pd_image, p_image_rect]
        player = Player(self, pimgs, self.screen, "cont")
        playert = Player(self, ptimgs, self.screen, "thrust")
        playeruc = Player(self, pucimgs, self.screen, "unit circle")
        playerd = Player(self, pdimgs, self.screen, "direction")
        self.player = player
        self.playert = playert
        self.playeruc = playeruc
        self.playerd = playerd
        # for math visual
        self.all_sprites.add(self.playeruc)
        # controlable player
        self.all_sprites.add(self.player)
        # thrust image
        self.all_sprites.add(self.playert)
        # more math visual
        self.all_sprites.add(self.playerd)
        self.players.add(self.playeruc)
        self.players.add(self.player)
        self.players.add(self.playert)
        self.players.add(self.playerd)
        self.death = False
        self.player_life_rect = self.player_life_img.get_rect()
        self.player_life_rect.x = 20
        self.player_life_rect.y = 50
    def run(self):
        # runs all necessary functions
        self.should_quit = False
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        # if loop should run end screen
        return self.should_quit
    # detects anything that happens in the game
    def events(self):
        # get all events
        for event in pg.event.get():
            # if the app is quit, end the program
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                self.should_quit = True
    def p_death_ani(self):
        # creates particles for where player dies
        self.life_count -= 1
        line_image_rect = self.line_image.get_rect()
        imgs = [self.line_image,line_image_rect,None,None]
        for i in range(0,3):
            # new instance of line particle
            l = Particles(imgs,"line",self,"player")
            self.all_sprites.add(l)
        self.time_of_death = pg.time.get_ticks()
    def ast_ani(self,number,size):
        # similar to p_death_ani()
        # spawns dots for asteroids and invaders when they die
        dot_image_rect = self.dot_image.get_rect()
        imgs = [None,None,self.dot_image,dot_image_rect]
        for i in range(0,number):
            d = Particles(imgs,"dot",self,"mob",size)
            self.all_sprites.add(d)
    def is_new_player(self):
        # create new player 1.4 seconds after player dies
        # if life count is not 0
        if self.life_count > 0 and len(self.players) == 0:
            if self.now - self.time_of_death >= 1400:
                self.new_player()
        elif self.life_count <= 0 and len(self.players) == 0:
            self.game_over = True
            self.game_over_time = self.now
            self.check_player = False
    def update_ast_list(self):
        # is the asteroid dead?
        for i in self.asteroids:
            if not i[3]:
                ind = self.asteroids.index(i)
                self.asteroids.pop(ind)
    def update_bullet_list(self):
        # should the bullet be dead?
        for bullet in self.pbullets_active:
            if self.now - bullet.birth > B_LIFETIME:
                self.pbullets_active.remove(bullet)
                break
    def main_music(self):
        # alternates between two beat sounds
        # speeds up over time
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
    def draw_math(self):
        # draw angles and vels for the player
        angle = self.player.rot
        angle += 90
        vels = unit_cir(angle, PMAX_VEL)
        xvel = vels[0]
        if abs(xvel) < 0.001:
            xvel = 0
        xvel = float(xvel)
        xvel = str(xvel)
        if len(xvel) < 5:
            xvel += "000"
        xvel = xvel[:5]
        yvel = vels[1]
        if abs(yvel) < 0.001:
            yvel = 0
        yvel = float(yvel)
        yvel = str(yvel)
        if len(yvel) < 5:
            yvel += "000"
        yvel = yvel[:5]
        if angle > 360:
            angle -= 360
        if len(str(angle)) < 5:
            angle = float(angle)
            angle = str(angle) + "000"
        angle = str(angle)
        angle = angle[:5]
        # angle
        self.draw_text(("angle = " + angle), "Hyperspace",
                        20, BLUE, WIDTH - 10, 10, "topright", True, False)
        # x velocity value
        self.draw_text(("cos(" + angle + ") x " + str(PMAX_VEL) + " = " + xvel), "Hyperspace",
                        20, RED, WIDTH - 310, 30, "topleft", True, False)
        # y velocity value
        self.draw_text(("sin(" + angle + ") x " + str(PMAX_VEL) + " = " + yvel), "Hyperspace",
                        20, GREEN, WIDTH - 310, 50, "topleft", True, False)
    def draw_life_count(self):
        # blit the images for how many lives the player has left
        life_img1 = self.player_life_img
        life_img1.set_colorkey(BLACK)
        life_rect1 = self.player_life_rect
        life_img2 = self.player_life_img
        life_img2.set_colorkey(BLACK)
        life_rect2 = self.player_life_rect
        life_img3 = self.player_life_img
        life_img3.set_colorkey(BLACK)
        life_rect3 = self.player_life_rect
        # if three lives
        if self.life_count >= 3:
            life_rect3.x = 110
            life_rect3.y = 80
            self.screen.blit(life_img3,life_rect3)
        # if two lives
        if self.life_count >= 2:
            life_rect2.x = 60
            life_rect2.y = 80
            self.screen.blit(life_img2,life_rect2)
        # if one life
        if self.life_count >= 1:
            life_rect1.x = 10 
            life_rect1.y = 80
            self.screen.blit(life_img1,life_rect3)
    def is_game_over(self):
        # game ends 1.3 secs after player loses last life
        if self.game_over and self.now - self.game_over_time >= 1300:
            if self.playing:
                self.playing = False
            self.running = False
    def new_wave(self):
        # if there are any asteroids or invaders on screen, no new wave
        new_wave = True
        for sprite in self.all_sprites:
            if "Ast" in str(type(sprite)) or "Invader" in str(type(sprite)):
                new_wave = False
                break
        # go to next wave from list in settings
        if new_wave:
            self.large_ast_spawn(WAVES[self.wave_count][0])
            self.small_inv_spawn(WAVES[self.wave_count][1])
            self.large_inv_spawn(WAVES[self.wave_count][2])
            if self.wave_count < len(WAVES):
                self.wave_count += 1
    def update(self):
        # update all the functions that need to be constantly checked
        self.now = pg.time.get_ticks()
        self.all_sprites.update()
        if self.check_player:
            self.is_new_player()
        self.update_bullet_list()
        self.update_ast_list()
        if self.sound:
            self.main_music()
        self.new_wave()
        self.is_game_over()
    def draw(self):
        # make background black
        self.screen.fill(BLACK)
        # blit all the sprites
        self.all_sprites.draw(self.screen)
        self.draw_life_count()
        if self.math_vis:
            self.draw_math()
        # is this a method or a function? -- function
        if self.game_over:
            self.draw_text("GAME OVER", "Hyperspace", 80, WHITE, 
                       WIDTH/2, HEIGHT/2, "center", True)
            self.sound = False 
        self.draw_text(str(self.score), "Hyperspace", 60, WHITE, 20,5,"topleft",True,False)
        pg.display.flip()
    # print text on the display
    def draw_text(self, text, font, size, color, x, y, align="topleft", bold=False, italicize=False):
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

# high scores for specific device
MAX_HIGH_SCORES = 10
high_scores = []
# name of high score document
path_to_high_scores = "asteroid_high_scores.csv"

def load_high_scores():
    lines = []
    # seperates different score sets by line
    try:
        with open(path_to_high_scores) as file:
            lines = file.read().splitlines()
    except:
        pass
    count = 0
    # seperate the name, date, score in each line
    for line in lines:
        line_list = line.split(',')
        if len(line_list) == 3:
            name = line_list[2]
            date = line_list[1]
            score = int(line_list[0])
            new_score = [score,date,name]
            high_scores.append(new_score)
            count += 1
            if count > MAX_HIGH_SCORES:
                break

def save_high_scores():
    # write new high scores in the document
    with open(path_to_high_scores,'w') as f:
        for score in high_scores:
            name = score[2]
            date = score[1]
            s = score[0]
            s = str(s)
            print(s + ',' + date + ',' + name, file=f)

def is_high_score(score):
    # if the score is 0, then it's not a high score
    if score == 0:
        return False
    count = 0
    for item in high_scores:
        count += 1
        # if the score is bigger than a score in our list, then it is a high score
        if score > item[0]:
            return True
    # if we don't have the max number of high scores yet, then this is a high score
    if count < MAX_HIGH_SCORES:
        return True
    # not a high score
    return False

def add_high_score(name,date,score):
    # create new high score and add to doc
    # all data for doc
    high_score = [score,date,name]
    inserted = False
    # find pos for the new high score
    for i in range(0,len(high_scores)):
        if score > high_scores[i][0]:
            high_scores.insert(i, high_score)
            inserted = True
            break
    if not inserted:
        high_scores.append(high_score)
    while len(high_scores) > MAX_HIGH_SCORES:
        high_scores.pop(-1)
    save_high_scores()

def game_loop():
    # loops for game, title, and end
    load_high_scores()
    # first is title
    while True:
        t = Title()
        t.new()
        should_quit = t.run()
        if should_quit:
            break
        # next is game
        g = Game()
        g.new()
        should_quit = g.run()
        # is there a new high score from this game
        if is_high_score(g.score):
            # need a way to get the player's name
            now = datetime.now()
            now = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
            add_high_score("PLAYER_NAME",now,g.score)
        if should_quit:
            break
        # new end screen
        e = End()
        e.new()
        should_quit = e.run()
        if should_quit:
            break
# call game loop
game_loop()
# end pygame
pg.quit()

# start_time = 1684291187.0
# end_time = start_time + 690
# print(time_of_play(start_time, end_time))
# import pygame stuff
import pygame as pg
from pygame.sprite import Sprite
# settings file
from settings_copy import *
# randint function
from random import randint
from random import choice
from random import uniform
# computer control
import os
from math import *
game_folder = os.path.dirname(__file__)
# for vel and acc
vec = pg.math.Vector2

# player class

class Player(Sprite):
    # starting attributes of player
    def __init__(self, game, img_folder, screen, typ):
        Sprite.__init__(self)
        # these are the properties
        # game class
        self.simg = img_folder[0]
        self.simg_rect = img_folder[1]
        self.simg.set_colorkey(BLACK)
        self.game = game
        self.image_orig = pg.transform.scale(self.simg, (50,100))
        orig = self.image_orig
        self.type = typ
        # how big p is
        self.image = pg.Surface((50,100))
        self.image.set_colorkey(BLACK)
        # self.timage.set_alpha(0)
        # p now has p image
        self.image.blit(self.simg, self.simg_rect)
        # self.timage.blit(self.timg, self.timg_rect)
        
        # p dimensions
        self.rect = self.image.get_rect()
        # where self prolclaimed center is
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.rect.center = (0,0)
        # where to spawn player
        self.pos = vec(WIDTH/2, HEIGHT/2 + player_y_len/2)
        self.pos_orig = self.pos
        if self.type == "cont":
            self.hitbox = pg.draw.circle(screen ,RED,self.pos,16)
        # starting velocity
        self.vel = vec(0,0)
        # starting acceleration
        self.acc = vec(0,0)
        self.cofric = 0.1
        # cannot jump
        self.canjump = False
        self.last_update = pg.time.get_ticks()
        self.rot = 0
        self.rot_speed = 0
    # gets user input that is then applied to p
    def input(self):
        # variable for when a key is pressed
        keystate = pg.key.get_pressed()
        # key_up = pg.KEYUP[pg.K_SPACE]
        # w moves up
        if keystate[pg.K_w]:
            x = [90,180,270,360]
            self.angle = self.rot
            self.angle += 90
            vels = unit_cir(self.angle, PMAX_VEL)
            xvel = vels[0]
            yvel = vels[1]
            # self.image.blit(self.timage,self.rect)
            print(1)
            if self.angle in x or abs(self.vel.x) <= abs(xvel) and abs(self.vel.y) <= abs(yvel):
                if abs(self.vel.x) <= PMAX_VEL and abs(self.vel.y) <= PMAX_VEL:
                    mx_acc = xvel/PMAX_VEL
                    mx_acc *= PLAYER_ACC
                    mx_acc *= 1
                    my_acc = yvel/PMAX_VEL
                    my_acc *= PLAYER_ACC
                    my_acc *= -1
                    self.acc.x = mx_acc
                    self.acc.y = my_acc
        else:
            # self.image.set_alpha(100)
            print(2)
        if keystate[pg.K_1]:
            if self.vel.y > -PMAX_VEL:
                self.acc.y = -PLAYER_ACC
        # a moves left
        if keystate[pg.K_2]:
            if self.vel.x > -PMAX_VEL:
                self.acc.x = -PLAYER_ACC
        # s moves down
        if keystate[pg.K_3]:
            if self.vel.y < PMAX_VEL:
                self.acc.y = PLAYER_ACC
        # d moves right
        if keystate[pg.K_4]:
            if self.vel.x < PMAX_VEL:
                self.acc.x = PLAYER_ACC
        # maybe controller in future?
        if keystate[pg.K_LEFT]:
            self.rot_speed = PROT_SPEED
            self.rotate()
        if keystate[pg.K_RIGHT]:
            self.rot_speed = -PROT_SPEED
            self.rotate()
        if keystate[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now - self.last_update > 30:
                b = Bullet(10)
                self.game.all_sprites.add(b)
                self.game.enemies.add(b)
        c = keystate[pg.CONTROLLER_AXIS_TRIGGERRIGHT]
        # testing stuff
    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 30:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pg.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            # self.image.set_alpha(0)
            
    def inbounds(self):
        # right
        if self.pos.x > WIDTH and self.vel.x > 0:
            self.pos.x = 0
            print("i am off the right side of the screen...")
        # left
        if self.pos.x < 0 and self.vel.x < 0:
            self.pos.x = WIDTH
            print("i am off the left side of the screen...")
        # bottom
        if self.pos.y > HEIGHT and self.vel.y > 0:
            self.pos.y = 0
            print("i am off the bottom of the screen")
        # top
        if self.pos.y < 0 and self.vel.y < 0:
            self.pos.y = HEIGHT
            if self.type == 'thrust':
                print("i am off the top of the screen...") 
    # when a player hits a mob...
    def mob_collide(self):
            # if a player hits a sprite in enemy list
            hits = pg.sprite.spritecollide(self, self.game.enemies, True)
            if hits:
                print("you collided with an enemy...")
                # self.game.score += 1
                # print(SCORE)
    # how player moves every second
    def update(self):
        # acceleration based on gravity
        self.acc = vec(0, PLAYER_GRAV)
        # maximum velocities
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.acc.y = self.vel.y * PLAYER_FRICTION
        # runs p input every second
        self.input()
        # velocity, position and origin
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        print(self.rect.center)
        self.rect.center = self.pos
        # self.timage.set_alpha(255)
        # self.image.blit(self.timage,self.timage.get_rect())
        # self.image.blit(self.image,self.image.get_rect())
        # self.self.timg
        # self.image.blit(self.image,self.timage.get_rect())
        

        #self.bullet.spawn(WIDTH/2, HEIGHT/2, -1)

# class for Mobs
class Mob(Sprite):
    # init the mobs initial settings and attributes
    def __init__(self, simg, simg_rect):
        Sprite.__init__(self)
        simg.set_colorkey(BLACK)
        self.image = pg.Surface((MOB_S_X,MOB_S_Y))
        self.image_orig = pg.transform.scale(simg,(MOB_S_X,MOB_S_Y))
        self.image.blit(simg, simg_rect)
        self.width = MOB_S_X
        self.height = MOB_S_Y
        # self.image = pg.Surface((self.width,self.height))
        self.rect = self.image.get_rect()
        # self.pos = vec(WIDTH/2, HEIGHT/2)
        # randomized velocity
        vel_choice = choice(MOB_VEL_LIST)
        mob_charge = choice(MOB_CHARGE)
        if vel_choice == "xvel":
            xvel = choice([-6,6])
            if mob_charge == "pos":
                yvel = uniform(2,6)
            elif mob_charge == "neg":
                yvel = uniform(-6,-2)
        elif vel_choice == "yvel":
            yvel = choice([-6,6])
            if mob_charge == "pos":
                xvel = uniform(2,6)
            elif mob_charge == "neg":
                xvel = uniform(-6,-2)
        self.vel = vec(xvel,yvel)
        spawn_choice = choice(MOB_SPAWN_LIST)
        if spawn_choice == "top":
            random_spawn = randint(0,WIDTH)
            self.pos = vec(random_spawn,0)
        elif spawn_choice == "bottom":
            random_spawn = randint(0,WIDTH)
            self.pos = vec(random_spawn,HEIGHT)
        elif spawn_choice == "left":
            random_spawn = randint(0,HEIGHT)
            self.pos = vec(0,random_spawn)
        elif spawn_choice == "right":
            random_spawn = randint(0,HEIGHT)
            self.pos = vec(WIDTH,random_spawn)
        self.acc = vec(100,100)
        self.cofric = 0.01
        self.last_update = pg.time.get_ticks()
        self.rotate()
    # this lets the mobs bounce around off the edges
    def inbounds(self):
        # right
        if self.pos.x > WIDTH and self.vel.x > 0:
            self.pos.x = 0
        # left
        if self.pos.x < 0 and self.vel.x < 0:
            self.pos.x = WIDTH
        # bottom
        if self.pos.y > HEIGHT and self.vel.y > 0:
            self.pos.y = 0
        # top
        if self.pos.y < 0 and self.vel.y < 0:
            self.pos.y = HEIGHT
    def rotate(self):
        new_image = pg.transform.rotate(self.image_orig, randint(0,360))
        old_center = self.rect.center
        self.image = new_image
        self.rect = self.image.get_rect()
        self.rect.center = old_center
    def update(self):
        # constantly run inbounds function
        self.inbounds()
        self.pos += self.vel
        self.rect.center = self.pos

# create a new platform class...

# class Platform(Sprite):
#     def __init__(self, x, y, width, height, color, variant):
#         Sprite.__init__(self)
#         self.width = width
#         self.height = height
#         self.image = pg.Surface((self.width,self.height))
#         self.color = color
#         self.image.fill(self.color)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.variant = variant

class Bullet(Sprite):
    def __init__(self,direction):
        Sprite.__init__(self)
        self.width = 7
        self.height = 7
        self.image = pg.Surface((self.width,self.height))
        self.color = WHITE
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.acc = vec(0,0)
        self.vel = vec(35,35)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.birth = pg.time.get_ticks()
    def inbounds(self):
        # right
        if self.pos.x > WIDTH and self.vel.x > 0:
            self.pos.x = 0
        # left
        if self.pos.x < 0 and self.vel.x < 0:
            self.pos.x = WIDTH
        # bottom
        if self.pos.y > HEIGHT and self.vel.y > 0:
            self.pos.y = 0
        # top
        if self.pos.y < 0 and self.vel.y < 0:
            self.pos.y = HEIGHT
    def update(self):
        # constantly run inbounds function
        self.inbounds()
        self.pos += self.vel
        self.rect.center = self.pos
        now = pg.time.get_ticks()
        if now - self.birth > 1000:
            self.kill()

def unit_cir(angle, max):
    angle *= pi
    angle /= 180
    xval = cos(angle)
    xval *= max
    yval = sin(angle)
    yval *= max
    return (xval,yval)
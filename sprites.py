# File created by: Liam Newberry
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
from time import sleep
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
        self.type = typ
        # how big p is
        self.image = pg.Surface((50,100))
        self.image.set_colorkey(BLACK)
        # player now has p image
        self.image.blit(self.simg, self.simg_rect)
        # p dimensions
        self.rect = self.image.get_rect()
        # where self proclaimed center is
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
        self.last_update = pg.time.get_ticks()
        self.rot = 0
        self.rot_speed = 0
        self.birth = pg.time.get_ticks()
    # gets user input that is then applied to p
    def input(self):
        # variable for when a key is pressed
        keystate = pg.key.get_pressed()
        # thrust
        if keystate[pg.K_w] or keystate[pg.K_UP]:
            x = [90,180,270,360]
            self.angle = self.rot
            self.angle += 90
            vels = unit_cir(self.angle, PMAX_VEL)
            xvel = vels[0]
            yvel = vels[1]
            if self.type == "thrust":
                alpha = self.image.get_alpha()
                if alpha == 0:
                    self.image.set_alpha(255)
                elif alpha == 255:
                    self.image.set_alpha(0)
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
            if self.type == "thrust":
                self.image.set_alpha(0)
            # pass
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
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.rot_speed = PROT_SPEED
            self.rotate()
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.rot_speed = -PROT_SPEED
            self.rotate()
        if keystate[pg.K_SPACE]:#or pg.MOUSEBUTTONUP:
            now = pg.time.get_ticks()
            if len(self.game.bullets) == 0 or now - self.game.bullets[0].birth > 200:
                angle = self.rot - 90
                direction = unit_cir(angle, BMAX_VEL)
                direction[0] *= -1
                position = [self.pos[0],self.pos[1]]
                location = unit_cir(angle, 36)
                location[0] *= -1
                position[0] += location[0]
                position[1] += location[1]
                b = Bullet(direction, position, self.game)
                self.game.all_sprites.add(b)
                self.game.bullets.append(b)
        c = keystate[pg.CONTROLLER_AXIS_TRIGGERRIGHT]
        # testing stuff
    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 30:
            alpha = self.image.get_alpha()
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pg.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.image.set_alpha(alpha)
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
            print("i am off the top of the screen...") 
    # when a player hits a mob...
    def mob_collide(self):
        now = pg.time.get_ticks()
        if now - self.birth >= P_IMMUNITY:
            for mob in self.game.enemies:
                if is_touching(self.pos,PLAYER_RADIUS,mob.pos,MOB_S_RADIUS):
                    mob.kill()
                    self.game.p_death_ani()
                    for player in self.game.players:
                        player.kill() 
        else:
            if self.type == "cont":
                if self.image.get_alpha() == 255:
                    self.image.set_alpha(0)
                    print(1)
                elif self.image.get_alpha() == 0:
                    self.image.set_alpha(255)
                    print(2)
    def update(self):
        # acceleration based on gravity
        self.acc = vec(0, PLAYER_GRAV)
        # maximum velocities
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.acc.y = self.vel.y * PLAYER_FRICTION
        # runs p input every second
        self.input()
        self.inbounds()
        self.mob_collide()
        # velocity, position and origin
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        if abs(self.vel.y) < 0.1:
            self.vel.y = 0

# class for Mobs
class Mob(Sprite):
    # init the mobs initial settings and attributes
    def __init__(self, simg, simg_rect, type):
        Sprite.__init__(self)
        self.type = type
        simg.set_colorkey(BLACK)
        self.image = pg.Surface((MOB_S_X,MOB_S_Y))
        self.image_orig = pg.transform.scale(simg,(MOB_S_X,MOB_S_Y))
        self.image.blit(simg, simg_rect)
        self.width = MOB_S_X
        self.height = MOB_S_Y
        self.rect = self.image.get_rect()
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

class Bullet(Sprite):
    def __init__(self,direction,location,game):
        Sprite.__init__(self)
        self.game = game
        self.width = B_LEN
        self.height = B_LEN
        self.image = pg.Surface((self.width,self.height))
        self.color = WHITE
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = B_LEN
        self.rect.y = B_LEN
        self.acc = vec(0,0)
        self.vel = vec(direction)
        self.pos = vec(location)
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
        if now - self.birth > 750:
            self.kill()
        if len(self.game.bullets) >= 2:
            self.game.bullets.pop(0)

class Particles(Sprite):
    def __init__(self, img_folder, type, game):
        Sprite.__init__(self)
        self.type = type
        self.rot = False
        self.game = game
        if self.type == "line":
            simg = img_folder[0]
            simg.set_colorkey(BLACK)
            simg_rect = img_folder[1]
            self.image_orig = pg.transform.scale(simg,((PARL_WIDTH,PARL_HEIGHT)))
            self.image = pg.Surface((PARL_WIDTH,PARL_HEIGHT))
        if self.type == "dot":
            simg = img_folder[2]
            simg.set_colorkey(BLACK)
            simg_rect = img_folder[3]
            self.image = pg.Surface((PARD_WIDTH,PARD_HEIGHT))
            self.image_orig = pg.transform.scale(simg,((PARD_WIDTH,PARD_HEIGHT)))
        self.image.blit(simg, simg_rect)
        self.rect = self.image.get_rect()
        p_pos = [game.player.pos[0], game.player.pos[1]]
        self.pos = (p_pos[0] + randint(-PAR_MAX_DIST,PAR_MAX_DIST),
                    p_pos[1] + randint(-PAR_MAX_DIST,PAR_MAX_DIST))
        self.vel = vec(uniform(-PAR_MAX_VEL,PAR_MAX_VEL),uniform(-PAR_MAX_VEL,PAR_MAX_VEL))
        self.rotate()
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
    def rotate(self):
        new_image = pg.transform.rotate(self.image_orig, randint(0,360))
        old_center = self.rect.center
        self.image = new_image
        self.rect = self.image.get_rect()
        self.rect.center = old_center
    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        self.inbounds()
        now = pg.time.get_ticks()
        if now - self.birth > 800:
            self.kill()

def unit_cir(angle, max):
    angle *= pi
    angle /= 180
    xval = cos(angle)
    xval *= max
    yval = sin(angle)
    yval *= max
    return [xval,yval]

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
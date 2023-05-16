# File created by: Liam Newberry
import pygame as pg
from sprites_copy import *
from settings_copy import *
from random import randint
import os

done = False

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")
s_ast = os.path.join(img_folder, "s_ast")
m_ast = os.path.join(img_folder, "m_ast")
l_ast = os.path.join(img_folder, "l_ast")
title_imgs = os.path.join(img_folder, "title")
icon = pg.image.load(os.path.join(title_imgs, "icon.png"))
icon.set_colorkey(GREEN)

class Title:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Asteroids")
        pg.display.set_icon(icon)
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        # starting a new game
        # new place to store sprites
        self.all_sprites = pg.sprite.Group()
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
        self.title_img = pg.image.load(os.path.join(title_imgs, "title screen.png"))
        self.title_img.set_colorkey(BLACK)
        self.title_rect = self.title_img.get_rect()
        self.title_rect.center = (WIDTH/2 , HEIGHT*1/3)
        # image used on Player
        # defines player with the image
        if True:
            self.mob_serial = 0
            self.sound = False
            self.asteroids = []
            self.pbullets_active = []
        self.ast_spawn(5)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pg.event.get():
            # if the app is quit, end the program
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                coords = self.get_mouse_now()
                if self.play_now_rect.collidepoint(coords):
                    if self.playing:
                        self.playing = False
                    self.running = False
                    from main_copy import new_game
                    from main_copy import t_init
                    t_init = False
                    new_game()
    def ast_spawn(self, number, broken=False, pos=None):
        for i in range(0,number):
            new_choice = randint(1,3)
            if new_choice == 1:
                img_rect = self.s_asteroid1.get_rect()
                size = "small_ast"
                rand_s_asteroid = randint(1,4)
                if rand_s_asteroid == 1:
                    img = self.s_asteroid1
                elif rand_s_asteroid == 2:
                    img = self.s_asteroid2
                elif rand_s_asteroid == 3:
                    img = self.s_asteroid3
                elif rand_s_asteroid == 4:
                    img = self.s_asteroid4
            elif new_choice == 2:
                img_rect = self.m_asteroid1.get_rect()
                size = "medium_ast"
                rand_m_asteroid = randint(1,4)
                if rand_m_asteroid == 1:
                    img = self.m_asteroid1
                elif rand_m_asteroid == 2:
                    img = self.m_asteroid2
                elif rand_m_asteroid == 3:
                    img = self.m_asteroid3
                elif rand_m_asteroid == 4:
                    img = self.m_asteroid4
            elif new_choice == 3:
                img_rect = self.l_asteroid1.get_rect()
                size = "large_ast"
                rand_l_asteroid = randint(1,4)
                if rand_l_asteroid == 1:
                    img = self.l_asteroid1
                elif rand_l_asteroid == 2:
                    img =self. l_asteroid2
                elif rand_l_asteroid == 3:
                    img = self.l_asteroid3
                elif rand_l_asteroid == 4:
                    img = self.l_asteroid4
            a = Ast(img,img_rect,size,self,broken,pos)
            self.all_sprites.add(a)
    def update(self):
        # updates the sprites
        self.now = pg.time.get_ticks()
        self.all_sprites.update()
    def draw(self):
        #make background black
        self.screen.fill(BLACK)
        # blit all the sprites
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.title_img, self.title_rect)
        self.play_now_rect = self.draw_text("PLAY GAME", "Hyperspace", 80, 
                                            WHITE, WIDTH/2, HEIGHT*2/3, "center", True)
        pg.display.flip()
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
        return text_rect
    # gets the coords of the cursor
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

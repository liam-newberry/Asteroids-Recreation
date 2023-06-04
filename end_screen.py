# File created by: Liam Newberry
import pygame as pg
from settings_copy import *
import os
from scores import *
from datetime import datetime

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")
s_ast = os.path.join(img_folder, "s_ast")
m_ast = os.path.join(img_folder, "m_ast")
l_ast = os.path.join(img_folder, "l_ast")
title_imgs = os.path.join(img_folder, "title")
end_imgs = os.path.join(img_folder, "end")
icon = pg.image.load(os.path.join(title_imgs, "icon.png"))
icon.set_colorkey(GREEN)

class End:
    def __init__(self, score):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Asteroids")
        pg.display.set_icon(icon)
        self.clock = pg.time.Clock()
        self.running = True
        self.score = score
    def new(self):
        self.cursor_image = pg.image.load(os.path.join(end_imgs, "cursor.png"))#.convert()
        self.cursor_rect = self.cursor_image.get_rect()
        self.got_name = False
        self.name = ""
        self.name_rect = self.draw_text(self.name, "Hyperspace", 80,
                                            WHITE, WIDTH/2, HEIGHT/2, "center", True)
        self.cursor_visible = True
        self.last_cursor_blink = 0
        if True:
            self.pressed_a = False
            self.pressed_b = False
            self.pressed_c = False
            self.pressed_d = False
            self.pressed_e = False
            self.pressed_f = False
            self.pressed_g = False
            self.pressed_h = False
            self.pressed_i = False
            self.pressed_j = False
            self.pressed_k = False
            self.pressed_l = False
            self.pressed_m = False
            self.pressed_n = False
            self.pressed_o = False
            self.pressed_p = False
            self.pressed_q = False
            self.pressed_r = False
            self.pressed_s = False
            self.pressed_t = False
            self.pressed_u = False
            self.pressed_v = False
            self.pressed_w = False
            self.pressed_x = False
            self.pressed_y = False
            self.pressed_z = False
            self.pressed_0 = False
            self.pressed_1 = False
            self.pressed_2 = False
            self.pressed_3 = False
            self.pressed_4 = False
            self.pressed_5 = False
            self.pressed_6 = False
            self.pressed_7 = False
            self.pressed_8 = False
            self.pressed_9 = False
            self.pressed_dash = False
            self.pressed__ = False
            self.pressed_period = False
            self.pressed_exclaim = False
            self.pressed_dollar = False
            self.pressed_lt = False
            self.pressed_gt = False
            self.pressed_space = False
            self.pressed_backspace = False
    def run(self):
        self.should_quit = False
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        return self.should_quit
    def events(self):
        for event in pg.event.get():
            # if the app is quit, end the program
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                self.should_quit = True
            if event.type == pg.MOUSEBUTTONDOWN:
                coords = self.get_mouse_now()
                # new game button pressed
                if self.new_game_rect.collidepoint(coords):
                    if self.playing:
                        self.playing = False
                    self.running = False
    def get_name(self):
        keystate = pg.key.get_pressed()
        if len(self.name) < 16:
            if not keystate[pg.K_a]:
                if self.pressed_a:
                    self.name += 'a'
                self.pressed_a = False
            else:
                self.pressed_a = True
            if not keystate[pg.K_b]:
                if self.pressed_b:
                    self.name += 'b'
                self.pressed_b = False
            else:
                self.pressed_b = True
            if not keystate[pg.K_c]:
                if self.pressed_c:
                    self.name += 'c'
                self.pressed_c = False
            else:
                self.pressed_c = True
            if not keystate[pg.K_d]:
                if self.pressed_d:
                    self.name += 'd'
                self.pressed_d = False
            else:
                self.pressed_d = True
            if not keystate[pg.K_e]:
                if self.pressed_e:
                    self.name += 'e'
                self.pressed_e = False
            else:
                self.pressed_e = True
            if not keystate[pg.K_f]:
                if self.pressed_f:
                    self.name += 'f'
                self.pressed_f = False
            else:
                self.pressed_f = True
            if not keystate[pg.K_g]:
                if self.pressed_g:
                    self.name += 'g'
                self.pressed_g = False
            else:
                self.pressed_g = True
            if not keystate[pg.K_h]:
                if self.pressed_h:
                    self.name += 'h'
                self.pressed_h = False
            else:
                self.pressed_h = True
            if not keystate[pg.K_i]:
                if self.pressed_i:
                    self.name += 'i'
                self.pressed_i = False
            else:
                self.pressed_i = True
            if not keystate[pg.K_j]:
                if self.pressed_j:
                    self.name += 'j'
                self.pressed_j = False
            else:
                self.pressed_j = True
            if not keystate[pg.K_k]:
                if self.pressed_k:
                    self.name += 'k'
                self.pressed_k = False
            else:
                self.pressed_k = True
            if not keystate[pg.K_l]:
                if self.pressed_l:
                    self.name += 'l'
                self.pressed_l = False
            else:
                self.pressed_l = True
            if not keystate[pg.K_m]:
                if self.pressed_m:
                    self.name += 'm'
                self.pressed_m = False
            else:
                self.pressed_m = True
            if not keystate[pg.K_n]:
                if self.pressed_n:
                    self.name += 'n'
                self.pressed_n = False
            else:
                self.pressed_n = True
            if not keystate[pg.K_o]:
                if self.pressed_o:
                    self.name += 'o'
                self.pressed_o = False
            else:
                self.pressed_o = True
            if not keystate[pg.K_p]:
                if self.pressed_p:
                    self.name += 'p'
                self.pressed_p = False
            else:
                self.pressed_p = True
            if not keystate[pg.K_q]:
                if self.pressed_q:
                    self.name += 'q'
                self.pressed_q = False
            else:
                self.pressed_q = True
            if not keystate[pg.K_r]:
                if self.pressed_r:
                    self.name += 'r'
                self.pressed_r = False
            else:
                self.pressed_r = True
            if not keystate[pg.K_s]:
                if self.pressed_s:
                    self.name += 's'
                self.pressed_s = False
            else:
                self.pressed_s = True
            if not keystate[pg.K_t]:
                if self.pressed_t:
                    self.name += 't'
                self.pressed_t = False
            else:
                self.pressed_t = True
            if not keystate[pg.K_u]:
                if self.pressed_u:
                    self.name += 'u'
                self.pressed_u = False
            else:
                self.pressed_u = True
            if not keystate[pg.K_v]:
                if self.pressed_v:
                    self.name += 'v'
                self.pressed_v = False
            else:
                self.pressed_v = True
            if not keystate[pg.K_w]:
                if self.pressed_w:
                    self.name += 'w'
                self.pressed_w = False
            else:
                self.pressed_w = True
            if not keystate[pg.K_x]:
                if self.pressed_x:
                    self.name += 'x'
                self.pressed_x = False
            else:
                self.pressed_x = True
            if not keystate[pg.K_y]:
                if self.pressed_y:
                    self.name += 'y'
                self.pressed_y = False
            else:
                self.pressed_y = True
            if not keystate[pg.K_z]:
                if self.pressed_z:
                    self.name += 'z'
                self.pressed_z = False
            else:
                self.pressed_z = True
            if not keystate[pg.K_0]:
                if self.pressed_0 and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += '0'
                self.pressed_0 = False
            else:
                self.pressed_0 = True
            if not keystate[pg.K_1]:
                if self.pressed_1 and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += '1'
                self.pressed_1 = False
            else:
                self.pressed_1 = True
            if not keystate[pg.K_2]:
                if self.pressed_2 and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += '2'
                self.pressed_2 = False
            else:
                self.pressed_2 = True
            if not keystate[pg.K_3]:
                if self.pressed_3 and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += '3'
                self.pressed_3 = False
            else:
                self.pressed_3 = True
            if not keystate[pg.K_4]:
                if self.pressed_4 and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += '4'
                self.pressed_4 = False
            else:
                self.pressed_4 = True
            if not keystate[pg.K_5]:
                if self.pressed_5 and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += '5'
                self.pressed_5 = False
            else:
                self.pressed_5 = True
            if not keystate[pg.K_6]:
                if self.pressed_6 and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += '6'
                self.pressed_6 = False
            else:
                self.pressed_6 = True
            if not keystate[pg.K_7]:
                if self.pressed_7 and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += '7'
                self.pressed_7 = False
            else:
                self.pressed_7 = True
            if not keystate[pg.K_8]:
                if self.pressed_8 and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += '8'
                self.pressed_8 = False
            else:
                self.pressed_8 = True
            if not keystate[pg.K_9]:
                if self.pressed_9 and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += '9'
                self.pressed_9 = False
            else:
                self.pressed_9 = True
            if not keystate[pg.K_MINUS]:
                if self.pressed_dash and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += '-'
                self.pressed_dash = False
            else:
                self.pressed_dash = True
            if not keystate[pg.K_MINUS] or not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                if self.pressed__:
                    self.name += '_'
                self.pressed__ = False
            elif keystate[pg.K_MINUS] and keystate[pg.K_LSHIFT] or keystate[pg.K_RSHIFT]:
                self.pressed__ = True
            if not keystate[pg.K_PERIOD]:
                if self.pressed_period and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += '.'
                self.pressed_period = False
            else:
                self.pressed_period = True
            if not keystate[pg.K_1] or not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                if self.pressed_exclaim:
                    self.name += '!'
                self.pressed_exclaim = False
            elif keystate[pg.K_1] and keystate[pg.K_LSHIFT] or keystate[pg.K_RSHIFT]:
                self.pressed_exclaim = True
            if not keystate[pg.K_4] or not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]: 
                if self.pressed_dollar:
                    self.name += '$' 
                self.pressed_dollar = False
            elif keystate[pg.K_4] and keystate[pg.K_LSHIFT] or keystate[pg.K_RSHIFT]:
                self.pressed_dollar = True
            if not keystate[pg.K_COMMA] or not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]: 
                if self.pressed_lt:
                    self.name += '<' 
                self.pressed_lt = False
            elif keystate[pg.K_COMMA] and keystate[pg.K_LSHIFT] or keystate[pg.K_RSHIFT]:
                self.pressed_lt = True
            if not keystate[pg.K_PERIOD] or not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]: 
                if self.pressed_gt:
                    self.name += '>' 
                self.pressed_gt = False
            elif keystate[pg.K_PERIOD] and keystate[pg.K_LSHIFT] or keystate[pg.K_RSHIFT]:
                self.pressed_gt = True
            if not keystate[pg.K_SPACE]:
                if self.pressed_space and len(self.name) > 0 and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name += ' '
                self.pressed_space = False
            else:
                self.pressed_space = True
        if len(self.name) > 0:
            if not keystate[pg.K_BACKSPACE]:
                if self.pressed_backspace and not keystate[pg.K_LSHIFT] and not keystate[pg.K_RSHIFT]:
                    self.name = self.name[:-1]
                self.pressed_backspace = False
            else:
                self.pressed_backspace = True
        if keystate[pg.K_RETURN] and len(self.name) > 0:
            self.name = self.name.upper()
            self.got_name = True
            self.add_score()
        # self.got_name = True
    def cursor_adjustments(self):
        self.cursor_rect.x = self.name_rect.midright[0]
        self.cursor_rect.y = HEIGHT/2
        self.cursor_rect.center = (self.cursor_rect.x, self.cursor_rect.y)
        if self.now - self.last_cursor_blink > 500:
            a = self.cursor_image.get_alpha()
            print(a)
            self.cursor_image.set_alpha(0)
            if self.cursor_image.get_alpha() == 255:
                self.cursor_image.set_alpha(0)
            elif self.cursor_image.get_alpha() == 0:
                self.cursor_image.set_alpha(255)
            self.last_cursor_blink = self.now
    def add_score(self):
        # is there a new high score from this game
        if is_high_score(self.score):
            # need a way to get the player's name
            now = datetime.now()
            today = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
            add_high_score(self.name, today, self.score)
    def update(self):
        # updates the sprites
        self.now = pg.time.get_ticks()
        if not self.got_name:
            self.get_name()
            self.cursor_adjustments()
    def draw(self):
        #make background black
        self.screen.fill(BLACK)
        # draw the new game button
        if not self.got_name:
            self.name_rect = self.draw_text(self.name, "Hyperspace", 80,
                                            WHITE, WIDTH/2, HEIGHT/2, "center", True)
            self.screen.blit(self.cursor_image, self.cursor_rect)
        if self.got_name:
            self.new_game_rect = self.draw_text("MAIN MENU", "Hyperspace", 80, 
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
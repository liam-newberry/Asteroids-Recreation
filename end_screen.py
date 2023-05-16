# File created by: Liam Newberry
import pygame as pg
from settings_copy import *
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")
s_ast = os.path.join(img_folder, "s_ast")
m_ast = os.path.join(img_folder, "m_ast")
l_ast = os.path.join(img_folder, "l_ast")
title_imgs = os.path.join(img_folder, "title")
icon = pg.image.load(os.path.join(title_imgs, "icon.png"))
icon.set_colorkey(GREEN)

class End:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Asteroids")
        pg.display.set_icon(icon)
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        #self.run()
        pass
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
                if self.new_game_rect.collidepoint(coords):
                    if self.playing:
                        self.playing = False
                    self.running = False
    def update(self):
        # updates the sprites
        self.now = pg.time.get_ticks()
    def draw(self):
        #make background black
        self.screen.fill(BLACK)
        # blit all the sprites
        self.new_game_rect = self.draw_text("NEW GAME", "Hyperspace", 80, 
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

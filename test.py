import pygame as pg
from pygame.sprite import Sprite
import os
from settings import *
from random import randint
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Asteroids")
clock = pg.time.Clock()
running = True
all_sprites = pg.sprite.Group()
playing = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            if playing:
                playing = False
            running = False
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()
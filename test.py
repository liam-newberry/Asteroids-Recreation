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
line_image = pg.image.load(os.path.join(img_folder, "line.png")).convert()
line_image_rect = line_image.get_rect()
class P(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((7,70))
        self.image_orig = pg.transform.scale(line_image,(7,70))
        self.image.blit(line_image,line_image_rect)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.rect.center = (0,0)
    def rotate(self):
        new_image = pg.transform.rotate(self.image_orig, randint(0,360))
        old_center = self.rect.center
        self.image = new_image
        self.rect = self.image.get_rect()
        self.rect.center = old_center
p = P()
all_sprites.add(p)
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
import os
import subprocess
try:
    import pygame, json, math, random, os
    from pygame.draw import line, rect
except ImportError:
    os.system('py3 -m pip install pygame')
from spritesheet import Spritesheet
from palette import Palette

pygame.init()
screenSize = [960, 736]
screen = pygame.display.set_mode(screenSize)


enemySheetSmall = Spritesheet("./assets/enemies_small.png")
enemySheetLarge = Spritesheet("./assets/enemies_large.png")

print(type(enemySheetSmall))
enemyCounts = [12,4]
enemySprites = enemySheetSmall.split(64, 64, 4, 64, enemyCounts[0])
print(enemySprites[0])

sprites = pygame.image.load("./assets/enemies_small.png").get_size()
print(type(sprites))
print(sprites)
print([int(sprites[0]/4), int(sprites[1]/64)])
import os
import pygame

dinbek_path = os.path.join('assets', 'dinbekbold.ttf')
FNT_SCORE = pygame.font.Font(dinbek_path, 24)
FNT_TITLE = pygame.font.Font(dinbek_path, 32)

SPR_BEAR = pygame.image.load(os.path.join('assets', 'bear.png'))
SPR_WALL = pygame.image.load(os.path.join('assets', 'wall.png'))
SPR_FIRE = pygame.image.load(os.path.join('assets', 'fire.png'))
SPR_STAR = pygame.image.load(os.path.join('assets', 'star.png'))
SPR_TEN = pygame.image.load(os.path.join('assets', 'ten.png'))

BG = pygame.image.load(os.path.join('assets', 'bg_scaled.png'))

SPR_TITLE = pygame.image.load(os.path.join('assets', 'title.png'))
SPR_GAME_OVER = pygame.image.load(os.path.join('assets', 'game_over.png'))

SND_BG = pygame.mixer.Sound(os.path.join('assets', 'bg.ogg'))
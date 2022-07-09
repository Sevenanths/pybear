import os
import pygame

FNT_ARIAL = pygame.font.SysFont('Arial', 24)

SPR_BEAR = pygame.image.load(os.path.join('assets', 'bear.png'))
SPR_WALL = pygame.image.load(os.path.join('assets', 'wall.png'))
SPR_FIRE = pygame.image.load(os.path.join('assets', 'fire.png'))
SPR_STAR = pygame.image.load(os.path.join('assets', 'star.png'))

BG = pygame.image.load(os.path.join('assets', 'bg_scaled.png'))
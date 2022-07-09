import pygame

WIDTH, HEIGHT = 800, 480

OBJECT_WIDTH = 32
OBJECT_HEIGHT = 32

BEAR_SPEED = 4
OBJECT_SPEED = 2

NUM_OBJECTS = 2

EV_BEAR_UP = pygame.USEREVENT + 1
EV_BEAR_DOWN = pygame.USEREVENT + 2
EV_BEAR_LEFT = pygame.USEREVENT + 3
EV_BEAR_RIGHT = pygame.USEREVENT + 4

FPS = 75
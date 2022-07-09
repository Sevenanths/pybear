import pygame
import random

from pybear.constants import *

from .bear_direction import ALL_DIRECTIONS, BearDirection

class Bear:
	def __init__(self):
		self.direction = random.choice(ALL_DIRECTIONS)
		self.rect = pygame.Rect((WIDTH // 2) - (OBJECT_WIDTH // 2),
						   		(HEIGHT // 2) - (OBJECT_HEIGHT // 2),
						   		OBJECT_WIDTH, OBJECT_HEIGHT)

	def read_key(self, key_event):
		if key_event == pygame.K_LEFT:
			self.direction = BearDirection.LEFT
		elif key_event == pygame.K_RIGHT:
			self.direction = BearDirection.RIGHT
		elif key_event == pygame.K_UP:
			self.direction = BearDirection.UP
		elif key_event == pygame.K_DOWN:
			self.direction = BearDirection.DOWN

	def move(self):
		if self.rect.x - BEAR_SPEED <= OBJECT_WIDTH:
			self.direction = BearDirection.RIGHT
		elif self.rect.x + BEAR_SPEED >= WIDTH - (OBJECT_WIDTH * 2):
			self.direction = BearDirection.LEFT
		elif self.rect.y - BEAR_SPEED <= OBJECT_HEIGHT:
			self.direction = BearDirection.DOWN
		elif self.rect.y + BEAR_SPEED >= HEIGHT - (OBJECT_HEIGHT * 2):
			self.direction = BearDirection.UP
	
		if self.direction == BearDirection.LEFT:
			self.rect.x -= BEAR_SPEED
		elif self.direction == BearDirection.RIGHT:
			self.rect.x += BEAR_SPEED
		elif self.direction == BearDirection.UP:
			self.rect.y -= BEAR_SPEED
		elif self.direction == BearDirection.DOWN:
			self.rect.y += BEAR_SPEED

def generate_random_coordinate(axis):
	if axis == "x":
		return random.randrange(OBJECT_WIDTH + 1,
								WIDTH - (2 * OBJECT_WIDTH))
	elif axis == "y":
		return random.randrange(OBJECT_HEIGHT + 1,
								HEIGHT - (2 * OBJECT_HEIGHT))
	else:
		return False
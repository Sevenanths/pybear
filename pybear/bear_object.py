import random
import pygame

from pybear.constants import *

from .object_direction import ALL_OBJECT_DIRECTIONS
from .object_direction import ObjectDirection

class BearObject:
	def __init__(self, object_type):
		self.type = object_type
		self.direction = random.choice(ALL_OBJECT_DIRECTIONS)
		self.rect = pygame.Rect(generate_random_coordinate("x"),
								generate_random_coordinate("y"),
								OBJECT_WIDTH, OBJECT_HEIGHT)

	def move(self):
		# Left wall collision
		if self.rect.x - OBJECT_SPEED <= OBJECT_WIDTH:
			if self.direction == ObjectDirection.UP_LEFT:
				self.direction = ObjectDirection.UP_RIGHT
			elif self.direction == ObjectDirection.DOWN_LEFT:
				self.direction = ObjectDirection.DOWN_RIGHT
		# Right wall collision
		elif self.rect.x + OBJECT_SPEED >= WIDTH - (OBJECT_WIDTH * 2):
			if self.direction == ObjectDirection.UP_RIGHT:
				self.direction = ObjectDirection.UP_LEFT
			elif self.direction == ObjectDirection.DOWN_RIGHT:
				self.direction = ObjectDirection.DOWN_LEFT
		# Top wall collision
		elif self.rect.y - OBJECT_SPEED <= OBJECT_HEIGHT:
			if self.direction == ObjectDirection.UP_LEFT:
				self.direction = ObjectDirection.DOWN_LEFT
			elif self.direction == ObjectDirection.UP_RIGHT:
				self.direction = ObjectDirection.DOWN_RIGHT
		elif self.rect.y + OBJECT_SPEED >= HEIGHT - (OBJECT_HEIGHT * 2):
			if self.direction == ObjectDirection.DOWN_LEFT:
				self.direction = ObjectDirection.UP_LEFT
			elif self.direction == ObjectDirection.DOWN_RIGHT:
				self.direction = ObjectDirection.UP_RIGHT
	
		if self.direction == ObjectDirection.UP_LEFT:
			self.rect.x -= OBJECT_SPEED
			self.rect.y -= OBJECT_SPEED
		elif self.direction == ObjectDirection.UP_RIGHT:
			self.rect.x += OBJECT_SPEED
			self.rect.y -= OBJECT_SPEED
		elif self.direction == ObjectDirection.DOWN_LEFT:
			self.rect.x -= OBJECT_SPEED
			self.rect.y += OBJECT_SPEED
		elif self.direction == ObjectDirection.DOWN_RIGHT:
			self.rect.x += OBJECT_SPEED
			self.rect.y += OBJECT_SPEED

def generate_random_coordinate(axis):
	if axis == "x":
		return random.randrange(OBJECT_WIDTH + 1,
								WIDTH - (2 * OBJECT_WIDTH))
	elif axis == "y":
		return random.randrange(OBJECT_HEIGHT + 1,
								HEIGHT - (2 * OBJECT_HEIGHT))
	else:
		return False
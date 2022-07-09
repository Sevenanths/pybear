# pybear
# by Anthe
# started on 2022-07-09

# -- Imports --
import pygame
import os
import random
pygame.font.init()
pygame.mixer.init()

from pybear.constants import *
from pybear.assets import *

from pybear.bear_direction import BearDirection, ALL_DIRECTIONS
from pybear.object_direction import ObjectDirection
from pybear.fire import Fire
from pybear.star import Star

# -- Constants --
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pybear")

# -- Functions --
def draw_window(obj_bear, objects):
	WIN.blit(BG, (0, 0))

	walls = []
	for x in range(25):
		# Top walls
		WIN.blit(SPR_WALL, (x * OBJECT_WIDTH, 0))
		# Bottom walls
		WIN.blit(SPR_WALL, (x * OBJECT_WIDTH, HEIGHT - OBJECT_HEIGHT))

	for y in range(1, 14):
		# Left walls
		WIN.blit(SPR_WALL, (0, y * OBJECT_HEIGHT))
		# Right walls
		WIN.blit(SPR_WALL, (WIDTH - OBJECT_WIDTH, y * OBJECT_HEIGHT))

	WIN.blit(SPR_BEAR, (obj_bear.x, obj_bear.y))

	for obj_object in objects:
		spr_object = SPR_FIRE if obj_object.type == "fire" else SPR_STAR
		WIN.blit(spr_object, (obj_object.rect.x, obj_object.rect.y))

	pygame.display.update()

def handle_bear_movement(key_event, obj_bear):
	if key_event == pygame.K_LEFT:
		pygame.event.post(pygame.event.Event(EV_BEAR_LEFT))
	elif key_event == pygame.K_RIGHT:
		pygame.event.post(pygame.event.Event(EV_BEAR_RIGHT))
	elif key_event == pygame.K_UP:
		pygame.event.post(pygame.event.Event(EV_BEAR_UP))
	elif key_event == pygame.K_DOWN:
		pygame.event.post(pygame.event.Event(EV_BEAR_DOWN))

def move_bear(bear_direction, obj_bear):
	if obj_bear.x - BEAR_SPEED <= OBJECT_WIDTH:
		bear_direction = BearDirection.RIGHT
		pygame.event.post(pygame.event.Event(EV_BEAR_RIGHT))
	elif obj_bear.x + BEAR_SPEED >= WIDTH - (OBJECT_WIDTH * 2):
		bear_direction = BearDirection.LEFT
		pygame.event.post(pygame.event.Event(EV_BEAR_LEFT))
	elif obj_bear.y - BEAR_SPEED <= OBJECT_HEIGHT:
		bear_direction = BearDirection.DOWN
		pygame.event.post(pygame.event.Event(EV_BEAR_DOWN))
	elif obj_bear.y + BEAR_SPEED >= HEIGHT - (OBJECT_HEIGHT * 2):
		bear_direction = BearDirection.UP
		pygame.event.post(pygame.event.Event(EV_BEAR_UP))

	if bear_direction == BearDirection.LEFT:
		obj_bear.x -= BEAR_SPEED
	elif bear_direction == BearDirection.RIGHT:
		obj_bear.x += BEAR_SPEED
	elif bear_direction == BearDirection.UP:
		obj_bear.y -= BEAR_SPEED
	elif bear_direction == BearDirection.DOWN:
		obj_bear.y += BEAR_SPEED

def main():
	obj_bear = pygame.Rect((WIDTH // 2) - (OBJECT_WIDTH // 2),
						   (HEIGHT // 2) - (OBJECT_HEIGHT // 2),
						   OBJECT_WIDTH, OBJECT_HEIGHT)

	objects = []
	for i in range(NUM_OBJECTS):
		fire = Fire()
		star = Star()

		objects.append(fire)
		objects.append(star)

	bear_direction = random.choice(ALL_DIRECTIONS)

	clock = pygame.time.Clock()
	run = True

	while run:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				handle_bear_movement(event.key, obj_bear)

			if event.type == EV_BEAR_UP:
				bear_direction = BearDirection.UP
			elif event.type == EV_BEAR_DOWN:
				bear_direction = BearDirection.DOWN
			elif event.type == EV_BEAR_LEFT:
				bear_direction = BearDirection.LEFT
			elif event.type == EV_BEAR_RIGHT:
				bear_direction = BearDirection.RIGHT

		for obj_object in objects:
			obj_object.move()

		move_bear(bear_direction, obj_bear)
		draw_window(obj_bear, objects)

	pygame.quit()

if __name__ == "__main__":
	main()
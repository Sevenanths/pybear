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
from pybear.bear import Bear

# -- Constants --
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pybear")

# -- Functions --
def draw_window(obj_bear, objects, score):
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

	WIN.blit(SPR_BEAR, (obj_bear.rect.x, obj_bear.rect.y))

	for obj_object in objects:
		spr_object = SPR_FIRE if obj_object.type == "fire" else SPR_STAR
		WIN.blit(spr_object, (obj_object.rect.x, obj_object.rect.y))

	score_text = FNT_ARIAL.render(str(score), 1, WHITE)
	score_outline = FNT_ARIAL.render(str(score), 1, BLACK)

	score_x = (WIDTH // 2) - (score_text.get_width() // 2)
	score_y = 2

	WIN.blit(score_outline, (score_x + 1, score_y + 1))
	WIN.blit(score_outline, (score_x - 1, score_y + 1))
	WIN.blit(score_outline, (score_x - 1, score_y - 1))
	WIN.blit(score_outline, (score_x + 1, score_y - 1))
	WIN.blit(score_text, (score_x, score_y))

	pygame.display.update()

def main():
	obj_bear = Bear()

	objects = []
	for i in range(NUM_OBJECTS):
		fire = Fire(obj_bear)
		star = Star(obj_bear)

		objects.append(fire)
		objects.append(star)

	score = 0

	clock = pygame.time.Clock()
	run = True

	while run:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				obj_bear.read_key(event.key)

			if event.type == EV_OBJECT_TOUCH:
				touched_object = event.dict["touched_object"]
				
				if touched_object.type == "star":
					score += SCORE_INCREASE
					new_object = Star(obj_bear)
				elif touched_object.type == "fire":
					score -= SCORE_INCREASE
					new_object = Fire(obj_bear)

				objects.remove(touched_object)
				objects.append(new_object)

		for obj_object in objects:
			obj_object.move()

		obj_bear.move()
		obj_bear.check_collision(objects)

		draw_window(obj_bear, objects, score)

	pygame.quit()

if __name__ == "__main__":
	main()
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

from pybear.game_modes import GameModes
from pybear.bear_direction import BearDirection, ALL_DIRECTIONS
from pybear.object_direction import ObjectDirection
from pybear.fire import Fire
from pybear.star import Star
from pybear.bear import Bear

# -- Constants --
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pybear by Anthe (2008-2022)")
pygame.display.set_icon(SPR_BEAR)

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

	score_text = FNT_SCORE.render(str(score), 1, WHITE)
	score_outline = FNT_SCORE.render(str(score), 1, BLACK)

	score_x = (WIDTH // 2) - (score_text.get_width() // 2)
	score_y = 2

	WIN.blit(score_outline, (score_x + 1, score_y + 1))
	WIN.blit(score_outline, (score_x - 1, score_y + 1))
	WIN.blit(score_outline, (score_x - 1, score_y - 1))
	WIN.blit(score_outline, (score_x + 1, score_y - 1))
	WIN.blit(score_text, (score_x, score_y))

	pygame.display.update()

def draw_title(show_text):
	WIN.blit(BG, (0, 0))

	WIN.blit(SPR_TITLE, (WIDTH // 2 - (SPR_TITLE.get_width() // 2),
						 HEIGHT // 2 - SPR_TITLE.get_height() // 2 - 20))

	if show_text:
		press_start_text = FNT_TITLE.render("Press ENTER to start", 1, WHITE)
		WIN.blit(press_start_text,
				 (WIDTH // 2 - press_start_text.get_width() / 2,
				 400))

	pygame.display.update()

def draw_game_over(show_text, score):
	WIN.blit(BG, (0, 0))

	WIN.blit(SPR_GAME_OVER, (WIDTH // 2 - (SPR_GAME_OVER.get_width() // 2),
						 	 HEIGHT // 2 - SPR_GAME_OVER.get_height() // 2 - 20))

	final_score_text = FNT_TITLE.render(f"Score: {score}", 1, WHITE)
	WIN.blit(final_score_text,
			 (WIDTH // 2 - final_score_text.get_width() / 2,
			 12))

	if show_text:
		press_start_text = FNT_TITLE.render("Press ENTER to restart", 1, WHITE)
		WIN.blit(press_start_text,
				 (WIDTH // 2 - press_start_text.get_width() / 2,
				 400))

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

	game_mode = GameModes.TITLE
	show_text = True

	pygame.time.set_timer(EV_HIDE_TEXT, 1000)

	while run:
		clock.tick(FPS)

		if game_mode == GameModes.TITLE:
			for event in pygame.event.get():
				if event.type == EV_HIDE_TEXT:
					show_text = not show_text
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						game_mode = GameModes.GAME
						SND_BG.play(-1)
						#pygame.time.set_timer(EV_HIDE_TEXT, 0)
				elif event.type == pygame.QUIT:
					run = False
					pygame.quit()
					return

			draw_title(show_text)
	
			continue
		elif game_mode == GameModes.GAME_OVER:
			for event in pygame.event.get():
				if event.type == EV_HIDE_TEXT:
					show_text = not show_text
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						run = False
						SND_BG.stop()
				elif event.type == pygame.QUIT:
					run = False
					pygame.quit()
					return

			draw_game_over(show_text, score)
	
		elif game_mode == GameModes.GAME:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					obj_bear.read_key(event.key)
				elif event.type == EV_OBJECT_TOUCH:
					touched_object = event.dict["touched_object"]
				
					if touched_object.type == "star":
						score += SCORE_INCREASE
						new_object = Star(obj_bear)
					elif touched_object.type == "fire":
						show_text = True
						game_mode = GameModes.GAME_OVER
						new_object = Fire(obj_bear)
		
					objects.remove(touched_object)
					objects.append(new_object)
				elif event.type == pygame.QUIT:
					run = False
					pygame.quit()
					return
		
			for obj_object in objects:
				obj_object.move()
		
			obj_bear.move()
			obj_bear.check_collision(objects)
		
			draw_window(obj_bear, objects, score)

	main()

if __name__ == "__main__":
	main()
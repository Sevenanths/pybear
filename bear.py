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
from pybear.ai_export import *

from ai_bear.model import Model
from ai_bear.predict_direction import predict_direction

# -- Constants --
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pybear by Anthe (2008-2022)")
pygame.display.set_icon(SPR_BEAR)

# -- Functions --
def draw_window(obj_bear, objects, score, ai_control):
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

	bear_sprite = SPR_BEAR if not ai_control else SPR_AI_BEAR

	WIN.blit(bear_sprite, (obj_bear.rect.x, obj_bear.rect.y))

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

def draw_title(show_text, ai_export, ai_control):
	WIN.blit(BG, (0, 0))

	WIN.blit(SPR_TITLE, (WIDTH // 2 - (SPR_TITLE.get_width() // 2),
						 HEIGHT // 2 - SPR_TITLE.get_height() // 2 - 20))

	if show_text:
		press_start_text = FNT_TITLE.render("Press ENTER to start", 1, WHITE)
		WIN.blit(press_start_text,
				 (WIDTH // 2 - press_start_text.get_width() / 2,
				 400))

	if ai_export:
		ai_text = FNT_SCORE.render("AI export enabled", 1, WHITE)
		WIN.blit(SPR_TEN, (10, 10))
		WIN.blit(ai_text, (48, 10))

	if ai_control:
		ai_text = FNT_SCORE.render("AI control enabled", 1, WHITE)
		WIN.blit(SPR_TEN, (10, 38))
		WIN.blit(ai_text, (48, 38))

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

ai_export = False
ai_control = False

model = Model(N_FEATURES)
model.load_state_dict(BEAR_MODEL)
model.eval()

SND_BG.play(-1)

def main():
	global ai_export
	global ai_control
	ai_control_OK = False

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
	feature_vectors = []

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
						#pygame.time.set_timer(EV_HIDE_TEXT, 0)
					elif event.key == pygame.K_a:
						ai_export = True
					elif event.key == pygame.K_TAB:
						ai_control = not ai_control
				elif event.type == pygame.QUIT:
					run = False
					pygame.quit()
					return

			draw_title(show_text, ai_export, ai_control)
	
			continue
		elif game_mode == GameModes.GAME_OVER:
			for event in pygame.event.get():
				if event.type == EV_HIDE_TEXT:
					show_text = not show_text
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						run = False
				elif event.type == pygame.QUIT:
					run = False
					pygame.quit()
					return

			draw_game_over(show_text, score)
	
		elif game_mode == GameModes.GAME:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if not ai_control:
						obj_bear.read_key(event.key)
				elif event.type == EV_OBJECT_TOUCH:
					touched_object = event.dict["touched_object"]
				
					if touched_object.type == "star":
						score += SCORE_INCREASE
						new_object = Star(obj_bear)
					elif touched_object.type == "fire":
						show_text = True
						game_mode = GameModes.GAME_OVER

						if ai_export:
							export_feature_vectors(feature_vectors)

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

			if ai_export or ai_control:
				feature_vector = get_feature_vector(obj_bear, objects)
				feature_vectors.append(feature_vector)

			if ai_control_OK:
				obj_bear.direction = predict_direction(model, feature_vectors)

			# Prune feature vectors if they need not be saved
			if not ai_export and ai_control:
				feature_vectors = feature_vectors[-2:]

			# AI control can only be enabled after two input frames
			ai_control_OK = True
		
			draw_window(obj_bear, objects, score, ai_control)

	main()

if __name__ == "__main__":
	main()
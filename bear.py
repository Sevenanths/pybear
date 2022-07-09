# pybear
# by Anthe
# started on 2022-07-09

# -- Imports --
import pygame
import os
import random
pygame.font.init()
pygame.mixer.init()

# -- Constants --
WIDTH, HEIGHT = 800, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pybear")

OBJECT_WIDTH = 32
OBJECT_HEIGHT = 32

BEAR_SPEED = 4

EV_BEAR_UP = pygame.USEREVENT + 1
EV_BEAR_DOWN = pygame.USEREVENT + 2
EV_BEAR_LEFT = pygame.USEREVENT + 3
EV_BEAR_RIGHT = pygame.USEREVENT + 4

FPS = 75

class Direction:
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4

# -- Assets --
SPR_BEAR = pygame.image.load(os.path.join('assets', 'bear.png'))
SPR_WALL = pygame.image.load(os.path.join('assets', 'wall.png'))

BG = pygame.image.load(os.path.join('assets', 'bg_scaled.png'))

# -- Functions --
def draw_window(obj_bear):
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
	if bear_direction == Direction.LEFT:
		obj_bear.x -= BEAR_SPEED
	elif bear_direction == Direction.RIGHT:
		obj_bear.x += BEAR_SPEED
	elif bear_direction == Direction.UP:
		obj_bear.y -= BEAR_SPEED
	elif bear_direction == Direction.DOWN:
		obj_bear.y += BEAR_SPEED

def main():
	obj_bear = pygame.Rect((WIDTH // 2) - (OBJECT_WIDTH // 2),
						   (HEIGHT // 2) - (OBJECT_HEIGHT // 2),
						   OBJECT_WIDTH, OBJECT_HEIGHT)

	bear_direction = random.choice([ Direction.UP, Direction.DOWN,
									 Direction.LEFT, Direction.RIGHT ])

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
				bear_direction = Direction.UP
			elif event.type == EV_BEAR_DOWN:
				bear_direction = Direction.DOWN
			elif event.type == EV_BEAR_LEFT:
				bear_direction = Direction.LEFT
			elif event.type == EV_BEAR_RIGHT:
				bear_direction = Direction.RIGHT

		move_bear(bear_direction, obj_bear)
		draw_window(obj_bear)

	pygame.quit()

if __name__ == "__main__":
	main()
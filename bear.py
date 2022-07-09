# pybear
# by Anthe
# started on 2022-07-09

# -- Imports --
import pygame
import os
pygame.font.init()
pygame.mixer.init()

# -- Constants --
WIDTH, HEIGHT = 800, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pybear")

OBJECT_WIDTH = 32
OBJECT_HEIGHT = 32

FPS = 60

# -- Assets --
SPR_BEAR = pygame.image.load(os.path.join('assets', 'bear.png'))
SPR_WALL = pygame.image.load(os.path.join('assets', 'wall.png'))

BG = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'bg.jpg')), (WIDTH, HEIGHT))

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
		print("left")
	elif key_event == pygame.K_RIGHT:
		print("right")
	elif key_event == pygame.K_UP:
		print("up")
	elif key_event == pygame.K_DOWN:
		print("down")

def main():
	obj_bear = pygame.Rect((WIDTH // 2) - (OBJECT_WIDTH // 2),
						   (HEIGHT // 2) - (OBJECT_HEIGHT // 2),
						   OBJECT_WIDTH, OBJECT_HEIGHT)

	clock = pygame.time.Clock()
	run = True

	while run:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				handle_bear_movement(event.key, obj_bear)

		draw_window(obj_bear)

	pygame.quit()

if __name__ == "__main__":
	main()
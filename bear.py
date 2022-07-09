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
SPR_WALL = pygame.image.load(os.path.join('assets', 'wall.png'))

BG = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'bg.jpg')), (WIDTH, HEIGHT))

# -- Functions --
def draw_window():
	WIN.blit(BG, (0, 0))

	pygame.display.update()

def main():
	run = True

	while run:
		clock = pygame.time.Clock()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw_window()

	pygame.quit()

if __name__ == "__main__":
	main()
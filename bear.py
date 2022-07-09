import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pybear")

FPS = 60

BG = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'bg.jpg')), (WIDTH, HEIGHT))

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
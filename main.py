import pygame
from pygame.locals import *

def main():
	pygame.init()
	running = True

	window_size = (1280, 720)
	window = pygame.display.set_mode(window_size)
	pygame.display.set_caption("MOMS")

	window.fill((150, 150, 150))

	while running:
		key_pressed_is = pygame.key.get_pressed()
		# Handle events
		if key_pressed_is[K_ESCAPE]: 
			running = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False




		pygame.display.update()

	pygame.quit()
	pass


if __name__ == "__main__":
	main()
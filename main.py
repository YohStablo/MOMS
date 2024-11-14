import os
import pygame
from pygame.locals import *

import json
from sidebar import Sidebar
from country import get_countries

#####   IDEAS   #####
# Information with sources in each country
# How tech works with detail of the 
# Make different maps by topics to be more clear
# Budget ??
# Ideology in different country ?
# Europeen overview ??? Europol ?
# News by countries ?
# Think about how to present the data ? Different maps
# Drop list / panel with details on each countries ?

def update_screen(window, sidebar, countries, window_size, mouse_pos):
	sidebar.width = window_size[0]*0.2
	sidebar.heightœ = window_size[1]

	for country in countries:
		country.draw_country(window)
		country.draw_border(window)
	for country in countries:
		if country.disp_name:
			country.draw_name(window)
	
	sidebar.draw(window)
	sidebar.draw_topics(window)

	pygame.display.update()

def main():
	background = pygame.image.load('background_2.png')
	background = pygame.transform.scale_by(background, 0.4)
	pygame.init()
	running = True

	info = pygame.display.Info()
	window_size = (info.current_w-10, info.current_h-50)
	old_window_size = (0, 0)
	window = pygame.display.set_mode(window_size)
	pygame.display.set_caption("MOMS")

	pygame.display.set_mode(window_size, RESIZABLE)


	countries = get_countries()

	bg_color = (6,66,115)

	sidebar = Sidebar(0.2*window_size[0], window_size[1], (0, 0))

	while running:

		info = pygame.display.Info()
		window_size = (info.current_w, info.current_h)
		

		window.fill(bg_color)

		key_pressed_is = pygame.key.get_pressed()
		# Handle events
		if key_pressed_is[K_ESCAPE]: 
			running = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

	
		if window_size != old_window_size:
			need_screen_update = True
			map_size = (window_size[0]*0.8, window_size[1])
			map_offset = (window_size[0]*0.2, 0)
			for country in countries:
				country.scale_country(map_size, map_offset)
				
		
		mouse_pos = pygame.mouse.get_pos()
		for country in countries:
			country.point_in_country(mouse_pos)
			if country.is_hover:
				need_screen_update = True

		if need_screen_update:
			update_screen(window, sidebar, countries, window_size, mouse_pos)
			need_screen_update = False
		old_window_size = window_size

		#####   DISPLAY BACKGROUND   #####
		# for x in range(0, window_size[0], background.get_width()):
		# 	for y in range(0, window_size[1], background.get_height()):
		# 		window.blit(background,(x,y))

		

	pygame.quit()
	pass





if __name__ == "__main__":
	main()
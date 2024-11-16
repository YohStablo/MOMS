import os
import pygame
from pygame.locals import *

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
	sidebar.height = window_size[1]

	for country in countries:
		country.draw_country(window)
		country.draw_border(window)
	for country in countries:
		if country.disp_name:
			country.draw_name(window)
	
	sidebar.draw(window)
	# sidebar.draw_topics(window)

	pygame.display.update()

def main():
	pygame.init()
	pygame.display.set_caption("MOMS")
	pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
	running = True


	info = pygame.display.Info()
	window_size = (info.current_w, info.current_h)
	old_window_size = (0, 0)

	window = pygame.display.set_mode(window_size, RESIZABLE)


	countries = get_countries()
	cpt = 0
	old_cpt = 0

	cpt_button = 0
	old_cpt_button = 0

	bg_color = (6,66,115)

	sidebar = Sidebar(0.2*window_size[0], window_size[1], (0, 0))
	sidebar.init_buttons()

	while running:
		mouse_pos = pygame.mouse.get_pos()

		info = pygame.display.Info()
		window_size = (info.current_w, info.current_h)
		

		sidebar.check_hover_buttons(mouse_pos)
		
		
		# Handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
			if event.type == pygame.MOUSEBUTTONDOWN: 
				for button in sidebar.buttons:
					if button.is_hover:
						button.is_clicked = True
						need_screen_update = True
					else:
						button.is_clicked = False
				if sidebar.return_button.is_hover:
					sidebar.return_button.is_clicked = True
					need_screen_update = True
				else:
					sidebar.return_button.is_clicked = False





		

	
		if window_size != old_window_size:
			need_new_window = False
			if window_size[0] < 1000:
				window_size = (1000, window_size[1])
				need_new_window = True
			if window_size[1] < 400:
				window_size = (window_size[0], 400)
				need_new_window = True
			if need_new_window:
				window = pygame.display.set_mode(window_size, RESIZABLE)

			need_screen_update = True


			map_size = (window_size[0]*0.8, window_size[1])
			map_offset = (window_size[0]*0.2, 0)
			sidebar.update_size(window_size)
			for country in countries:
				country.scale_country(map_size, map_offset)
		
		
		cpt = 0
		for i, country in enumerate(countries):
			country.point_in_country(mouse_pos)
			if country.is_hover:
				cpt += i+1
		if cpt != old_cpt:
			need_screen_update = True

		old_window_size = window_size
		old_cpt = cpt
		old_cpt_button = cpt_button

		if sidebar.change_state:
			need_screen_update = True
			sidebar.change_state = False

		#####   DISPLAY   ####
		if need_screen_update:
			window.fill(bg_color)
			update_screen(window, sidebar, countries, window_size, mouse_pos)
			need_screen_update = False

		if sidebar.ckeck_clicked_buttons():
			need_screen_update = True
		

	pygame.quit()
	pass





if __name__ == "__main__":
	main()
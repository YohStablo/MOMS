import os
import pygame
import webbrowser
from pygame.locals import *

from sidebar import Sidebar
from country import get_countries, set_democracy_score, init_states
from pop_card import Pop_card


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
		if country.draw_card:
			# country.update_card(window_size, sidebar.active_button_id + 1)
			country.pp_card.draw(window)

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
	set_democracy_score(countries)
	init_states(countries)


	bg_color = (6,66,115)

	sidebar = Sidebar(0.2*window_size[0], window_size[1], (0, 0))
	sidebar.init_objects()


	while running:
		mouse_pos = pygame.mouse.get_pos()

		info = pygame.display.Info()
		window_size = (info.current_w, info.current_h)
		
		sidebar.check_hover_clickables(mouse_pos)
		for country in countries:
			if country.pp_card.is_active:
				country.pp_card.check_is_hover(mouse_pos)
				country.pp_card.check_hover_links(mouse_pos)
		
		
		# Handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				
				sidebar.check_clicked_clickables()
				for country in countries:
					country.check_clicked()
					country.pp_card.check_clicked_links()
				
		

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
				country.pp_card.scale_card(window_size)
				
		old_window_size = window_size
		
		
		for country in countries:
			country.point_in_country(mouse_pos)
			if country.pp_card.change_state:
				country.pp_card.change_state = False
				need_screen_update = True

			if country.change_state:
				country.change_state = False
				need_screen_update = True



		if sidebar.change_state:
			for country in countries:
				country.update_card(window_size, sidebar.active_button_id + 1)
				country.pp_card.change_state = False
			need_screen_update = True
			sidebar.change_state = False

		#####   DISPLAY   ####
		if need_screen_update:
			window.fill(bg_color)
			update_screen(window, sidebar, countries, window_size, mouse_pos)
			need_screen_update = False

		sidebar.reset_clickables()
		

	pygame.quit()
	pass





if __name__ == "__main__":
	main()
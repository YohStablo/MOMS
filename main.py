import pygame
from pygame.locals import *

import json

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


class Country:
	def __init__(self, id:int, name:str, center_point:tuple, description:str, borders:list):
		self.id = id
		self.name = name
		self.pos = center_point
		self.description = description
		self.borders = borders
		self.is_hover = False
		self.color = (0, 0, 0)
		self.hover_color = (200, 200, 200)
		self.default_color = (50, 50, 50)
		self.border_color = (255, 255, 255)

	def draw_country(self, window):
		for border in self.borders:
			pygame.draw.polygon(window, self.color, border)
	
	def draw_border(self, window):
		for border in self.borders:
			for i in range(len(border)):
				pygame.draw.line(window, self.border_color, border[i], border[(i+1)%len(border)], 1)
	
	def draw_name(self, window):
		font = pygame.font.Font('freesansbold.ttf', 14)
		text = font.render(self.name, True, self.border_color)
		
		textRect = text.get_rect()
		textRect.center = self.pos
		
		window.blit(text, textRect)
	
	def point_in_country(self, pos):
		self.color = self.default_color
		for border in self.borders:
			self.is_hover = point_in_polygon(pos, border)
			if self.is_hover:
				self.color = self.hover_color
				break



# Renvoie si le point 'point' est dans de polygone ou à l'exterieur
def point_in_polygon(point, polygon) -> bool:
    x, y = point
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def main():
	pygame.init()
	running = True

	infoObject = pygame.display.Info()
	window_size = (infoObject.current_w, infoObject.current_h*0.9)
	window = pygame.display.set_mode(window_size)
	pygame.display.set_caption("MOMS")

	countries = get_countries(window_size)

	bg_color = (6,66,115)

	while running:
		window.fill(bg_color)

		key_pressed_is = pygame.key.get_pressed()
		# Handle events
		if key_pressed_is[K_ESCAPE]: 
			running = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		
		x, y = pygame.mouse.get_pos()

		for country in countries:
			country.point_in_country((x,y))
			country.draw_country(window)
			country.draw_border(window)
		for country in countries:
			country.draw_name(window)
			
		pygame.display.update()

	pygame.quit()
	pass


def transform_point(x, y, window_size):
	x_trans = (x + 27) * window_size[0] / (35 + 27)
	y_trans = (y - 33) * window_size[1] / (73 - 33)
	
	return x_trans, window_size[1] - y_trans


def get_countries(window_size):
	# Open and read the JSON file
	with open('world-administrative-boundaries.json', 'r') as file:
		data = json.load(file)

	countries = []
	country_id = 0
	for country in data:
		print(country["status"])
		if country["continent"] != 'Europe' or country["status"] != "Member State":
			continue
		

		shape = country["geo_shape"]
		geom = shape["geometry"]
		countries.append(Country(country_id, country["name"], transform_point(country["geo_point_2d"]["lon"], country["geo_point_2d"]["lat"], window_size), 'Description', []))

		if geom["type"] == "MultiPolygon":
			for poly in geom["coordinates"]:
				x = [p[0] for p in poly[0] if -40 < p[0] < 45 and 33 < p[1] < 73]
				y = [p[1] for p in poly[0] if -40 < p[0] < 45 and 33 < p[1] < 73]

				if len(x):
					if abs(max(x) - min(x)) > 0.5:
						if abs(max(y) - min(y)) > 0.5:
							countries[country_id].borders.append([transform_point(xi, yi, window_size) for xi, yi in zip(x, y)])

		else:
			x = [p[0] for p in geom["coordinates"][0] if -40 < p[0] < 45 and 33 < p[1] < 73]
			y = [p[1] for p in geom["coordinates"][0] if -40 < p[0] < 45 and 33 < p[1] < 73]
			
			if len(x):
				if abs(max(x) - min(x)) > 0.5:
					if abs(max(y) - min(y)) > 0.5:
						countries[country_id].borders.append([transform_point(xi, yi, window_size) for xi, yi in zip(x, y)])

		country_id += 1
	return countries



if __name__ == "__main__":
	main()
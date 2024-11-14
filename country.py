import pygame
import json
from util import point_in_polygon, transform_point

class Country:
	def __init__(self, id:int, name:str, center_point:tuple, description:str, borders:list):
		self.id = id
		self.name = name
		self.disp_name = False
		self.pos = center_point
		self.description = description
		self.borders = borders
		self.disp_country_borders = None
		self.disp_pos = None
		self.is_hover = False
		self.color = (0, 0, 0)
		self.hover_color = (200, 200, 200)
		self.default_color = (50, 50, 50)
		self.border_color = (255, 255, 255)
		
	def scale_country(self, map_size, map_offset):
		self.disp_pos = transform_point(self.pos, map_size, map_offset)
		self.disp_country_borders = []
		for i, border in enumerate(self.borders):
			self.disp_country_borders.append([])
			for p in border:
				transformed_point = transform_point(p, map_size, map_offset)
				self.disp_country_borders[i].append(transformed_point)
				
	

	def draw_country(self, window):
		for border in self.disp_country_borders:
			pygame.draw.polygon(window, self.color, border)
	
	def draw_border(self, window):
		for border in self.disp_country_borders:
			for i in range(len(border)):
				pygame.draw.line(window, self.border_color, border[i], border[(i+1)%len(border)], 1)
	
	def draw_name(self, window):
		font = pygame.font.Font('freesansbold.ttf', 14)
		text = font.render(self.name, True, (200, 100, 100))
		
		textRect = text.get_rect()
		textRect.center = self.disp_pos
		
		window.blit(text, textRect)
	
	def point_in_country(self, pos):
		self.color = self.default_color
		self.disp_name = False
		for border in self.disp_country_borders:
			self.is_hover = point_in_polygon(pos, border)
			if self.is_hover:
				self.color = self.hover_color
				self.disp_name = True
				break



def get_countries():
	# Open and read the JSON file
	with open('world-administrative-boundaries.json', 'r') as file:
		data = json.load(file)

	countries = []
	country_id = 0
	for country in data:
		# print(country["status"])
		if country["continent"] != 'Europe' or country["status"] != "Member State":
			continue
		

		shape = country["geo_shape"]
		geom = shape["geometry"]
		countries.append(Country(country_id, country["name"], (country["geo_point_2d"]["lon"], country["geo_point_2d"]["lat"]), 'Description', []))

		if geom["type"] == "MultiPolygon":
			for poly in geom["coordinates"]:
				x = [p[0] for p in poly[0] if -40 < p[0] < 45 and 33 < p[1] < 73]
				y = [p[1] for p in poly[0] if -40 < p[0] < 45 and 33 < p[1] < 73]

				if len(x):
					if abs(max(x) - min(x)) > 0.5:
						if abs(max(y) - min(y)) > 0.5:
							countries[country_id].borders.append([(xi, yi) for xi, yi in zip(x, y)])

		else:
			x = [p[0] for p in geom["coordinates"][0] if -40 < p[0] < 45 and 33 < p[1] < 73]
			y = [p[1] for p in geom["coordinates"][0] if -40 < p[0] < 45 and 33 < p[1] < 73]
			
			if len(x):
				if abs(max(x) - min(x)) > 0.5:
					if abs(max(y) - min(y)) > 0.5:
						countries[country_id].borders.append([(xi, yi) for xi, yi in zip(x, y)])

		country_id += 1
	return countries

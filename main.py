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


def main(polygons):
	pygame.init()
	running = True

	window_size = (1280, 720)
	window = pygame.display.set_mode(window_size)
	pygame.display.set_caption("MOMS")

	polys = [None for _ in range(len(polygons))]
	while running:
		hover_id = -1
		window.fill((150, 150, 150))

		key_pressed_is = pygame.key.get_pressed()
		# Handle events
		if key_pressed_is[K_ESCAPE]: 
			running = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		### Mouvement on the map
		if key_pressed_is[K_RIGHT]:
			x_offset -= 10
		if key_pressed_is[K_LEFT]:
			x_offset += 10
		if key_pressed_is[K_UP]:
			y_offset += 10
		if key_pressed_is[K_DOWN]:
			y_offset -= 10
		if key_pressed_is[K_r]:
			x_offset, y_offset = 0, 0

		
		x, y = pygame.mouse.get_pos()

		for i, poly in enumerate(polygons):
			result = point_in_polygon((x, y), poly)
			if result:
				hover_id = i
				break

		for i, poly in enumerate(polygons):
			color = (200, 200, 200)
			if i == hover_id:
				color = (255, 0, 0)
			polys[i] = pygame.draw.polygon(window, color, poly)

		pygame.display.update()

	pygame.quit()
	pass


def transform_point(x, y):
	# -27 to +35 	==> 0 to 1280
	# 33 to 73		==>	0 to 720
	x_trans = (x + 27) * 1280 / (35 + 27)
	y_trans = (y - 33) * 720 / (73 - 33)
	
	return x_trans, 720 - y_trans


def get_polygon():
	import matplotlib.pyplot as plt
	import numpy as np
	# Open and read the JSON file
	with open('world-administrative-boundaries.json', 'r') as file:
		data = json.load(file)

	polygon = []
	countries = {}

	for country in data:
		if country["continent"] != 'Europe':
			continue

		shape = country["geo_shape"]
		geom = shape["geometry"]
		# countries["name"]

		if geom["type"] == "MultiPolygon":
			for poly in geom["coordinates"]:
				x = [p[0] for p in poly[0] if -40 < p[0] < 45 and 33 < p[1] < 73]
				y = [p[1] for p in poly[0] if -40 < p[0] < 45 and 33 < p[1] < 73]

				if len(x):
					if abs(max(x) - min(x)) > 0.5:
						if abs(max(y) - min(y)) > 0.5:
							polygon.append([transform_point(xi, yi) for xi, yi in zip(x, y)])
							# plt.plot(x, y)

		else:
			x = [p[0] for p in geom["coordinates"][0] if -40 < p[0] < 45 and 33 < p[1] < 73]
			y = [p[1] for p in geom["coordinates"][0] if -40 < p[0] < 45 and 33 < p[1] < 73]
			
			if len(x):
				if abs(max(x) - min(x)) > 0.5:
					if abs(max(y) - min(y)) > 0.5:
						polygon.append([transform_point(xi, yi) for xi, yi in zip(x, y)])
						# plt.plot(x, y)
	# plt.show()
	return polygon



if __name__ == "__main__":
	polygon = get_polygon()
	main(polygon)
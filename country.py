import pygame
import json
from os import listdir
from util import point_in_polygon, transform_point
from pop_card import Pop_card

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
		self.color = (0, 170, 0)
		self.hover_color = (200, 200, 200)
		self.default_color = (0, 170, 0)
		self.border_color = (0, 0, 0)
		self.example_color = (255, 105, 97)
		self.pegasus_color = (50, 50, 50)
		self.in_pegasus_mode = False
		self.states = {
			'1': None,
			'2': None,
			'3': None,
			'4': None
			}

		self.democracy_score = "Not in EU"
		self.pp_card = Pop_card((0, 0), self.name, 0)
		self.pp_card.is_active = False

		self.is_clicked = False

		self.change_state = False

		
	def scale_country(self, map_size, map_offset):
		self.disp_pos = transform_point(self.pos, map_size, map_offset)
		self.disp_country_borders = []
		for i, border in enumerate(self.borders):
			self.disp_country_borders.append([])
			for p in border:
				transformed_point = transform_point(p, map_size, map_offset)
				self.disp_country_borders[i].append(transformed_point)
				
	

	def draw_country(self, window, state=0):
		for border in self.disp_country_borders:
			pygame.draw.polygon(window, self.color, border)
	
	def draw_border(self, window):
		for border in self.disp_country_borders:
			for i in range(len(border)):
				pygame.draw.line(window, self.border_color, border[i], border[(i+1)%len(border)], 1)
	
	def draw_name(self, window):
		font = pygame.font.Font('freesansbold.ttf', 18)
		text = font.render(f"{self.name}", True, (0, 0, 0))
		text2 = font.render(f"{self.democracy_score}", True, (0, 0, 0))
		
		textRect = text.get_rect()
		textRect.center = self.disp_pos
		textRect2 = text2.get_rect()
		textRect2.center = (self.disp_pos[0], self.disp_pos[1] + 15)
		
		window.blit(text, textRect)
		window.blit(text2, textRect2)
	
	def point_in_country(self, pos):
		self.color = self.default_color
		self.disp_name = False
		if not self.pp_card.keep_pp_card:
			self.draw_card = False
		old_is_hover = self.is_hover


		for border in self.disp_country_borders:
			self.is_hover = point_in_polygon(pos, border)
			if self.is_hover:				
				self.color = self.hover_color
				self.disp_name = True
				self.draw_card = True
				break
		
		if self.is_hover != old_is_hover:
			self.change_state = True
		
		if self.in_pegasus_mode:
			self.color = self.pegasus_color

	def check_clicked(self):
	
		if self.is_hover:
			if not self.is_clicked:
				self.change_state = True
			self.pp_card.keep_pp_card = True
			self.is_clicked = True
		else:
			if self.is_clicked:
				self.change_state = True
			if not self.pp_card.is_hover:
				self.pp_card.keep_pp_card = False
			self.is_clicked = False
		
	def update_card(self, window_size, topic:int):
		self.pp_card.is_active = False

		if topic < 1 or topic > 4:
			return
		
		KT = str(topic)		# converting topic id to key for self.states dictionnary
		if self.states[KT] is None:
			return

		path = self.states[KT]
		get_text = False

		n_links = 0
		with open(path, 'r') as f:
			file_topic = int(f.readline().strip().split('\t')[1])
			if file_topic != topic:
				return
			
			f.readline()
			id_country = int(f.readline().strip().split('\t')[1])
			if id_country != self.id:
				return
			
			links = []
			for line in f:

				if line[0] == '#':
					l = line.strip().split('\t')
					match l[0]:
						case '#_TEXT':
							get_text = True
						case '#_LINKS':
							n_links = int(l[1])

				elif get_text:
					text = line
					get_text = False

				elif (n_links > 0):
					links.append(line)
					n_links -= 1
				
		self.pp_card.window_size = window_size
		self.pp_card.init_description_and_links(text, links)
		self.pp_card.democracy_score = self.democracy_score
		self.pp_card.is_active = True
		if self.is_clicked:
			self.pp_card.keep_pp_card = True

			


	
				



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


def set_pegasus_color(countries):
	with open("pegasus_use.txt", 'r') as f:
		f.readline()
		for line in f:
			l = line.strip().split('\t')
			country_id = int(l[1])
			pegas_id = int(l[2])

			match pegas_id:
				case -1:
					countries[country_id].pegasus_color = (100, 100, 100)
				case 0:
					countries[country_id].pegasus_color = (255, 165, 10)
				case 1:
					countries[country_id].pegasus_color = (255, 100, 10)
				case 2:
					countries[country_id].pegasus_color = (255, 20, 10)


					




def set_democracy_score(countries):
	with open("democracy_score.txt", "r") as f:
		for line in f:
			l = line.strip().split(',')
			countries[int(l[0])].democracy_score = "DS : " + l[2] + "/10"
			countries[int(l[0])].default_color = (255 - 25.5*float(l[2]), int(25.5*float(l[2])), 0)

def init_states(countries:list, directory:str = "example/"):
	for filename in listdir(directory):
		path = directory + filename
		with open(path, 'r') as f:
			topic_id = 0
			country_id = None			
			for line in f:
				l = line.strip().split('\t')
				match l[0]:
					case '#_TOPIC':
						topic_id = l[1]
					case '#_COUNTRY':
						country_id = int(l[1])
			
			countries[country_id].states[topic_id] = path

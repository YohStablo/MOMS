from text_box import Text_box
from link import LinkURL
import util
import pygame

class Pop_card:
	def __init__(self, top_left_pos, window_size, country_name, dem_score):
		self.width = window_size[0] * 0.2
		self.height = window_size[1] * 0.5
		self.top_left_pos = top_left_pos
		self.color = (0, 0, 0)

		self.change_state = False
		self.window_size = window_size

		self.country_name = country_name
		self.democracy_score = dem_score

		self.description = ""
		self.links = []

		self.text_box = None

		self.keep_pp_card = False
		self.is_active = False
		self.is_hover = False

	def scale_card(self, window_size):

		self.window_size = window_size

		self.width = self.window_size[0] * 0.2
		self.height = self.window_size[1] * 0.5

		text_font = pygame.font.SysFont('freesans', min(int(20 * self.height/(945*0.5)), int(20 * self.width/384)))
		self.text_box = Text_box((self.top_left_pos[0] + self.width * 0.05, self.top_left_pos[1] + self.height * 0.25), self.width * 0.9, self.height * 0.6, ((50, 50, 50), (255, 255, 255)), self.description, text_font)
		self.text_box.is_active = True

		for i, link in enumerate(self.links):
			link.is_active = True
			if i < 3:
				link.top_left_pos = (self.top_left_pos[0] + (0.1 + 0.3*i)*self.width, self.top_left_pos[1] + 0.8 * self.height)
			elif i < 6:
				link.top_left_pos = (self.top_left_pos[0] + (0.1 + 0.3*(i-2))*self.width, self.top_left_pos[1] + 0.9 * self.height)

	def init_description_and_links(self, descrition:str, links:list):
		self.links = []

		self.width = self.window_size[0] * 0.2
		self.height = self.window_size[1] * 0.5

		text_font = pygame.font.SysFont('freesans', min(int(20 * self.height/(945*0.5)), int(20 * self.width/384)))
		self.text_box = Text_box((self.top_left_pos[0] + self.width * 0.05, self.top_left_pos[1] + self.height * 0.25), self.width * 0.9, self.height * 0.6, ((50, 50, 50), (255, 255, 255)), descrition, text_font)
		self.text_box.is_active = True

		for i, link in enumerate(links):
			link = LinkURL((0, 0), link, f"Link {i+1}", (100, 100, 255))
			link.is_active = True
			if i < 3:
				link.top_left_pos = (self.top_left_pos[0] + (0.1 + 0.3*i)*self.width, self.top_left_pos[1] + 0.8 * self.height)
			elif i < 6:
				link.top_left_pos = (self.top_left_pos[0] + (0.1 + 0.3*(i-2))*self.width, self.top_left_pos[1] + 0.9 * self.height)
			self.links.append(link)
		# print(self.links)

	def check_hover_links(self, mouse_pos):
		for link in self.links:
			link.check_is_hover(mouse_pos)
			if link.change_state:
				self.change_state = True
				link.change_state = False
				

	def check_clicked_links(self):
		for link in self.links:
			link.check_clicked()
			if link.change_state:
				self.change_state = True
				link.change_state = False
				
	
	def check_is_hover(self, mouse_pos):
		if self.is_active:
			p1 = self.top_left_pos
			p2 = (self.top_left_pos[0] + self.width, self.top_left_pos[1] + self.height)

			if util.point_in_box(mouse_pos, p1, p2):
				self.is_hover = True
				return

			self.is_hover = False

	def draw(self, window):
		if not self.is_active:
			return

		self.draw_backgroung(window)
		self.draw_country_ds(window)
		self.text_box.draw(window)

		if len(self.links) > 0:
			for link in self.links:
				link.draw(window)


	def draw_country_ds(self, window):
		font = pygame.font.Font('freesansbold.ttf', 16)

		country_name_text = font.render(f"{self.country_name}", True, (200, 200, 200))
		democracy_score_text = font.render(f"{self.democracy_score}", True, (200, 200, 200))
		description_text = font.render("Description", True, (200, 200, 200))
		
		country_name_text_rect = country_name_text.get_rect()
		democracy_score_text_rect = democracy_score_text.get_rect()
		description_text_rect = description_text.get_rect()

		country_name_text_rect.topleft = (self.top_left_pos[0] + 0.05 * self.width, self.top_left_pos[1] + 0.05 * self.height)
		democracy_score_text_rect.topright = (self.top_left_pos[0] + 0.95 * self.width, self.top_left_pos[1] + 0.05 * self.height)
		description_text_rect.topleft = (self.top_left_pos[0] + 0.05 * self.width, self.top_left_pos[1] + 0.15 * self.height)

		window.blit(country_name_text, country_name_text_rect)
		window.blit(democracy_score_text, democracy_score_text_rect)
		window.blit(description_text, description_text_rect)

	def draw_backgroung(self, window):
		rect = (self.top_left_pos[0], self.top_left_pos[1], self.width, self.height)
		pygame.draw.rect(window, (50, 50, 50), rect, 0, 2)

import pygame
from button import Button
from text_box import Text_box
from link import LinkURL

class Sidebar:
	def __init__(self, width, height, pos):
		self.width = width
		self.height = height
		self.pos = pos
		self.color = (0, 0, 0)

		self.change_state = False
		self.window_size = (width * 5, height)

		self.topics = {
			"Predictive analysis": "Predictive analysis in policing involves using historical crime data and AI algorithms to identify likely locations or individuals for future criminal activity. By analyzing patterns in past incidents, predictive tools help law enforcement to optimize resource allocation and pre-empt crime. This data-driven approach aims to enhance public safety but raises concerns about biases within the datasets used, as these may lead to disproportionate scrutiny of certain communities. The European Union has responded with stricter AI regulations, aiming to balance security interests and privacy concerns by limiting personal data use and ensuring that predictive technologies are employed responsibly. Civil rights groups caution that predictive policing can reinforce existing biases, potentially eroding trust between law enforcement and communities.",
			"Network and net surveillance" : "Network and web surveillance encompasses monitoring digital activity to combat crime and terrorism, often involving partnerships between governments and internet service providers. This type of surveillance allows law enforcement to track online communications, browsing histories, and social media activities. While intended to bolster national security, this invasive approach has sparked debates on privacy rights and government overreach. In response, the European Court of Human Rights has emphasized the need for legal safeguards to protect individuals from indiscriminate data collection. Advocates argue that surveillance must be transparent, with clear limitations on data access and storage to preserve citizens' right to online privacy.",
			"Intelligent video surveillance" : "Intelligent video surveillance uses AI-driven facial recognition and behavioral analysis to enhance public safety in real-time, typically through CCTV networks in public spaces. These systems can identify suspects, detect unusual behavior, and track individuals across multiple locations. While effective in managing large crowds and preventing crime, intelligent surveillance poses significant privacy challenges, especially when deployed without explicit public consent. Critics argue that the technology risks creating a surveillance state, where citizens are constantly monitored. European legislation has started to address these concerns by restricting certain high-risk uses of biometric data, aiming to balance security measures with fundamental rights.",
			"Electronic communications surveillance" : "Electronic communications surveillance involves intercepting and monitoring online and phone communications to track potential security threats. Often conducted by intelligence agencies, this form of surveillance can include real-time interception, metadata analysis, and monitoring encrypted communications. While effective in identifying criminal networks and terrorist activities, mass data collection raises serious privacy issues. Oversight bodies and human rights organizations have raised concerns about the balance of security and privacy, stressing the need for transparent and regulated surveillance practices. As European legal frameworks evolve, they increasingly demand that surveillance be proportionate, targeted, and subject to judicial oversight to prevent misuse and protect individual freedoms.",
			"Pegasus" : "Pegasus, spyware developed by Israel's NSO Group, infiltrates iOS and Android devices via “zero-click” attacks, requiring no user interaction. Discovered in 2016, it exploited a WhatsApp vulnerability in 2019 and later targeted iMessage. It can also be installed through wireless transceivers or physical access. Once installed, Pegasus provides full access to messages, contacts, photos, browsing history, and app data from platforms like WhatsApp, iMessage, and Telegram. It can activate cameras, microphones, and GPS for constant surveillance. NSO Group claims it is used by governments to combat crime, but reports reveal its misuse against journalists, activists, and political figures. Its stealth and ability to bypass detection raise privacy and human rights concerns. Blacklisted by the U.S., Pegasus faces lawsuits from Apple and Meta, highlighting ethical and legal issues."
			}
		
		link_color = (100, 100, 255)
		self.links = {
			"Predictive analysis": [
				LinkURL((0, 0), r"https://artificialintelligenceact.eu/ai-act-explorer/", "Link 1", link_color),
				LinkURL((0, 0), r"https://www.amnesty.eu/news/eu-ai-act-at-risk-as-european-parliament-may-legitimize-abusive-technologies/", "Link 2", link_color),
				LinkURL((0, 0), r"https://datajusticeproject.net/wp-content/uploads/2019/05/Report-Data-Driven-Policing-EU.pdf", "Link 3", link_color),
				LinkURL((0, 0), r"https://www.accessnow.org/press-release/ai-act-predictive-policing/", "Link 4", link_color),
				LinkURL((0, 0), r"https://www.mdpi.com/2076-0760/10/6/234", "Link 5", link_color),
			],
			"Network and net surveillance" : [
				LinkURL((0, 0), r"https://www.accessnow.org/press-release/ai-act-predictive-policing/", "Link 1", link_color),
				LinkURL((0, 0), r"https://www.mdpi.com/2076-0760/10/6/234", "Link 2", link_color),
			],
			"Intelligent video surveillance" : [
				LinkURL((0, 0), r"https://www.biometricupdate.com/202405/police-in-germany-using-live-facial-recognition", "Link 1", link_color),
				LinkURL((0, 0), r"https://ainowinstitute.org/wp-content/uploads/2023/09/regulatingbiometrics-fussey-murray.pdf", "Link 2", link_color)
			],
			"Electronic communications surveillance" : [
				LinkURL((0, 0), r"https://www.lemonde.fr/en/france/article/2023/07/06/france-set-to-allow-police-to-spy-through-phones_6044269_7.html", "Link 1", link_color),
				LinkURL((0, 0), r"https://edri.org/our-work/the-terrifying-expansion-of-swedens-state-surveillance/", "Link 2", link_color)
			],
			"Pegasus" : [
				LinkURL((0, 0), r"https://rm.coe.int/pegasus-and-similar-spyware-and-secret-state-surveillance/1680ac7f68", "Link 1", link_color),
				LinkURL((0, 0), r"https://www.europarl.europa.eu/RegData/etudes/ATAG/2023/747923/EPRS_ATA(2023)747923_EN.pdf", "Link 2", link_color),
				LinkURL((0, 0), r"https://www.coe.int/en/web/data-protection/-/pegasus-spyware-called-into-question-by-pace", "Link 3", link_color)
		    ]
			}
		
		self.keys = ["Predictive analysis", "Network and net surveillance", "Intelligent video surveillance", "Electronic communications surveillance", "Pegasus"]

		self.n_buttons = 5
		self.buttons = [None]*self.n_buttons
		self.back_button = None
		self.init_objects()



	def init_objects(self):

		self.active_button_id = -1

		# Back button
		button_colors = ((10, 20, 40), (80, 80, 80), (100, 100, 100), (255, 255, 255))
		button_font = pygame.font.Font('freesansbold.ttf', 14)
		center_pos = (0.8 * self.width, 0.9* self.height)
		width = 0.2*self.width
		height = 30
		self.back_button = Button(-1, center_pos, width, height, button_colors, "Back", button_font, False)

		# Text box
		top_left_pos = (self.width * 0.05, self.height * 0.15)
		text_box_colors = ((10, 20, 40), (255, 255, 255))
		text_box_font = pygame.font.SysFont('freesans', int(20 * self.height/1080))
		self.text_box = Text_box(top_left_pos, self.width * 0.9, self.height * 0.65, text_box_colors, "", text_box_font)


		# Buttons and links
		for i, key in enumerate(self.keys):
			# Buttons
			button_pos = (self.width // 2, self.height * ((i+1) / (self.n_buttons + 1)))
			self.buttons[i] = Button(i, button_pos, self.width*0.9, 50, button_colors, key, button_font)

			# Links
			for i, link in enumerate(self.links[key]):
				link.is_active = False
				if i < 3:
					link.top_left_pos = ((0.1 + 0.3*i)*self.width, 0.8 * self.height)
				elif i < 6:
					link.top_left_pos = ((0.1 + 0.3*(i-3))*self.width, 0.85 * self.height)



		

	def update_size(self, window_size):

		self.width = 0.2 * window_size[0]
		self.height = window_size[1]
		self.window_size = window_size

		if self.active_button_id != -1:
			# Text box size update
			self.text_box.text_font = pygame.font.SysFont('freesans', min(int(20 * self.height/945), int(20 * self.width/384)))
			self.text_box.top_left_pos = (self.width * 0.05, self.height * 0.1 + 40)
			self.text_box.width = self.width * 0.9
			self.text_box.height = self.height - 0.2 * self.height - 15

			# Active button size update
			self.buttons[self.active_button_id].width = self.width*0.9
			self.buttons[self.active_button_id].centre_pos = (self.width // 2, self.height * 0.1)

			# Back button size update
			self.back_button.centre_pos = (0.8 * self.width, 0.9* self.height)
			self.back_button.width = 0.2*self.width

			# Links size update
			for i, link in enumerate(self.links[self.keys[self.active_button_id]]):
				if i < 3:
					link.top_left_pos = ((0.1 + 0.3*i)*self.width, 0.8 * self.height)
				elif i < 6:
					link.top_left_pos = ((0.1 + 0.3*(i-3))*self.width, 0.85 * self.height)

		else:
			for i, button in enumerate(self.buttons):
				button.width = self.width*0.9
				button.centre_pos = (self.width // 2, self.height * ((i+1) / (self.n_buttons + 1)))
		





	def check_hover_clickables(self, mouse_pos): 
		# Topic button
		for button in self.buttons:
			button.check_is_hover(mouse_pos)
			if button.change_state:
				self.change_state = True 
				button.change_state = False

		# Back button
		self.back_button.check_is_hover(mouse_pos)
		if self.back_button.change_state:
			self.change_state = True
			self.back_button.change_state = False

		# Links
		for key in self.keys:
			for link in self.links[key]:
				link.check_is_hover(mouse_pos)
				if link.change_state:
					self.change_state = True
					link.change_state = False

	
	def check_clicked_clickables(self):
		# Topic button
		for button in self.buttons:
			button.check_clicked()
			if button.change_state:
				button.change_state = False
				self.change_state = True
			if button.is_clicked:
				self.active_button_id = button.id
				self.button_id_clicked()


		# Return button
		self.back_button.check_clicked()
		if self.back_button.change_state:
			self.back_button.change_state = False
			self.change_state = True
		if self.back_button.is_clicked:
			self.text_box.is_active = False
			self.init_objects()



		# Links
		for key in self.keys:
			for link in self.links[key]:
				link.check_clicked()
				if link.change_state:
					self.change_state = True
					link.change_state = False


	def reset_clickables(self):
		for button in self.buttons:
			if button.is_clicked:
				button.is_clicked = False
				self.change_state = True

		if self.back_button.is_clicked:
			self.back_button.is_active = False
			self.change_state = True
		

	def button_id_clicked(self):
		for i, key in enumerate(self.topics.keys()):
			if i == self.active_button_id:

				self.text_box.is_active = True
				self.text_box.text = self.topics[key]

				self.back_button.is_active = True

				for i, link in enumerate(self.links[key]):
					link.is_active = True

				# Put objects to right place
				self.update_size(self.window_size)

				continue
			self.buttons[i].is_active = False


		


	###   DISPLAY   ###
	def draw(self, window):
		rect = (self.pos[0], self.pos[1], self.width, self.height)
		pygame.draw.rect(window, self.color, rect)

		# self.draw_topics(window)
		self.draw_buttons(window)
		self.text_box.draw(window)
		self.back_button.draw(window)

		for key in self.links.keys():
			for link in self.links[key]:
				link.draw(window)


	def draw_topics(self, window):
		font = pygame.font.Font('freesansbold.ttf', 16)
		for i, topic in enumerate(self.topics.keys()):
			text = font.render(topic, True, (255, 255, 255))
			textRect = text.get_rect()
 
			textRect.center = (self.width // 2, self.height * ((i+1) / 6))

			window.blit(text, textRect)

	def draw_buttons(self, window):
		for button in self.buttons:
			button.draw(window)
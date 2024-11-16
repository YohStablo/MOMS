import pygame
from button import Button
from text_box import Text_box

class Sidebar:
    def __init__(self, width, height, pos):
        self.width = width
        self.height = height
        self.pos = pos
        self.color = (0, 0, 0)

        self.change_state = False

        self.topics = {
            "Predictive analysis": "Predictive analysis in policing involves using historical crime data and AI algorithms to identify likely locations or individuals for future criminal activity. By analyzing patterns in past incidents, predictive tools help law enforcement to optimize resource allocation and pre-empt crime. This data-driven approach aims to enhance public safety but raises concerns about biases within the datasets used, as these may lead to disproportionate scrutiny of certain communities. The European Union has responded with stricter AI regulations, aiming to balance security interests and privacy concerns by limiting personal data use and ensuring that predictive technologies are employed responsibly. Civil rights groups caution that predictive policing can reinforce existing biases, potentially eroding trust between law enforcement and communities.",
            "Network and net surveillance" : "Network and web surveillance encompasses monitoring digital activity to combat crime and terrorism, often involving partnerships between governments and internet service providers. This type of surveillance allows law enforcement to track online communications, browsing histories, and social media activities. While intended to bolster national security, this invasive approach has sparked debates on privacy rights and government overreach. In response, the European Court of Human Rights has emphasized the need for legal safeguards to protect individuals from indiscriminate data collection. Advocates argue that surveillance must be transparent, with clear limitations on data access and storage to preserve citizens' right to online privacy.",
            "Intelligent video surveillance" : "Intelligent video surveillance uses AI-driven facial recognition and behavioral analysis to enhance public safety in real-time, typically through CCTV networks in public spaces. These systems can identify suspects, detect unusual behavior, and track individuals across multiple locations. While effective in managing large crowds and preventing crime, intelligent surveillance poses significant privacy challenges, especially when deployed without explicit public consent. Critics argue that the technology risks creating a surveillance state, where citizens are constantly monitored. European legislation has started to address these concerns by restricting certain high-risk uses of biometric data, aiming to balance security measures with fundamental rights.",
            "Electronic communications surveillance" : "Electronic communications surveillance involves intercepting and monitoring online and phone communications to track potential security threats. Often conducted by intelligence agencies, this form of surveillance can include real-time interception, metadata analysis, and monitoring encrypted communications. While effective in identifying criminal networks and terrorist activities, mass data collection raises serious privacy issues. Oversight bodies and human rights organizations have raised concerns about the balance of security and privacy, stressing the need for transparent and regulated surveillance practices. As European legal frameworks evolve, they increasingly demand that surveillance be proportionate, targeted, and subject to judicial oversight to prevent misuse and protect individual freedoms.",
            "Pegasus" : ""}
        
        self.buttons = [None]*5
        self.return_button = None
        self.active_button_id = -1

        top_left_pos = (self.width * 0.05, self.height * 0.15)
        text_box_colors = ((10, 20, 40), (255, 255, 255))
        font = pygame.font.SysFont('freesans', int(20 * self.height/1080))
        self.text_box = Text_box(top_left_pos, self.width * 0.9, self.height * 0.65, text_box_colors, "", font)


    def init_buttons(self):
        button_colors = ((10, 20, 40), (80, 80, 80), (100, 100, 100), (255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 14)


        center_pos = (0.8 * self.width, 0.9* self.height)
        width = 0.2*self.width
        height = 30
        self.return_button = Button(center_pos, width, height, button_colors, "Back", font, False)

        for i, key in enumerate(self.topics.keys()):
            button_pos = (self.width // 2, self.height * ((i+1) / 6))
            self.buttons[i] = Button(button_pos, self.width*0.9, 50, button_colors, key, font)
        

    def update_size(self, window_size):

        self.width = 0.2 * window_size[0]
        self.height = window_size[1]
        print(self.height)


        if self.text_box.is_active:
            top_left_pos = (self.width * 0.05, self.height * 0.1 + 40)
            self.text_box.text_font = pygame.font.SysFont('freesans', int(20 * self.height/945))
            self.text_box.top_left_pos = top_left_pos
            self.text_box.width = self.width * 0.9
            self.text_box.height = self.height - 0.3 * self.height - 15

            self.buttons[self.active_button_id].width = self.width*0.9
            self.buttons[self.active_button_id].centre_pos = (self.width // 2, self.height * 0.1)
            center_pos = (0.8 * self.width, 0.9* self.height)
            width = 0.2*self.width
            self.return_button.centre_pos = center_pos
            self.return_button.width = width
        else:
            for i, button in enumerate(self.buttons):
                button.width = self.width*0.9
                button.centre_pos = (self.width // 2, self.height * ((i+1) / 6))
        





    def check_hover_buttons(self, mouse_pos): 
        self.return_button.check_is_hover(mouse_pos)
        if self.return_button.change_state:
            self.change_state = True
            self.return_button.change_state = False

        for button in self.buttons:
            button.check_is_hover(mouse_pos)
            if button.change_state:
                self.change_state = True 
                button.change_state = False

    
    def ckeck_clicked_buttons(self):
        for i, button in enumerate(self.buttons):
            if button.is_clicked:
                self.button_id_clicked(i)
                self.active_button_id = i
                button.is_clicked = False
                self.change_state = True

        if self.return_button.is_clicked:
            self.text_box.is_active = False
            self.return_button.is_active = False
            self.change_state = True
            self.init_buttons()

    def button_id_clicked(self, button_id):
        for i, key in enumerate(self.topics.keys()):
            if i == button_id:
                self.buttons[i].centre_pos = (self.width // 2, self.height * 0.1)
                self.text_box.is_active = True
                top_left_pos = (self.width * 0.05, self.height * 0.1 + 40)
                self.text_box.text_font = pygame.font.SysFont('freesans', int(20 * self.height/945))
                self.text_box.top_left_pos = top_left_pos
                self.text_box.width = self.width * 0.9
                self.text_box.height = self.height  - 0.3 * self.height - 15
                self.text_box.text = self.topics[key]

                self.return_button.is_active = True
                center_pos = (0.8 * self.width, 0.9* self.height)
                width = 0.2*self.width
                self.return_button.centre_pos = center_pos
                self.return_button.width = width

                continue
            self.buttons[i].is_active = False


        


    ###   DISPLAY   ###
    def draw(self, window):
        rect = (self.pos[0], self.pos[1], self.width, self.height)
        pygame.draw.rect(window, self.color, rect)

        # self.draw_topics(window)
        self.draw_buttons(window)
        self.text_box.draw(window)
        self.return_button.draw(window)

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
import pygame
from button import Button

class Sidebar:
    def __init__(self, width, height, pos):
        self.width = width
        self.height = height
        self.pos = pos
        self.color = (0, 0, 0)

        self.topics = {
            "Predictive analysis": "",
            "Network and net surveillance" : "",
            "Intelligent video surveillance" : "",
            "Electronic communications surveillance" : "",
            "Pegasus" : ""}
        
        self.buttons = [None]*5

    def update_size(self, window_size):

        self.width = 0.2 * window_size[0]
        self.height = window_size[1]

        for i, button in enumerate(self.buttons):
            button.width = self.width*0.9
            button.centre_pos = (self.width // 2, self.height * ((i+1) / 6))


    def init_buttons(self):
        button_colors = ((10, 20, 40), (80, 80, 80), (100, 100, 100), (255, 255, 255))

        for i, key in enumerate(self.topics.keys()):
            button_pos = (self.width // 2, self.height * ((i+1) / 6))
            font = pygame.font.Font('freesansbold.ttf', 14)
            text = key
            self.buttons[i] = Button(button_pos, self.width*0.9, 50, button_colors, text, font)


    def check_hover_buttons(self, mouse_pos):
        for button in self.buttons:
            if button.check_is_hover(mouse_pos):
                return True
        return False
    
    def ckeck_clicked_buttons(self):
        for button in self.buttons:
            if button.is_clicked:
                print("COUCOU !! :)")
                button.is_clicked = False
                return True
        return False


    ###   DISPLAY   ###
    def draw(self, window):
        rect = (self.pos[0], self.pos[1], self.width, self.height)
        pygame.draw.rect(window, self.color, rect)

        # self.draw_topics(window)
        self.draw_buttons(window)

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
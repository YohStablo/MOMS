import pygame

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

    
    def draw(self, window):
        rect = (self.pos[0], self.pos[1], self.width, self.height)
        pygame.draw.rect(window, self.color, rect)

    def draw_topics(self, window):
        font = pygame.font.Font('freesansbold.ttf', 16)
        for i, topic in enumerate(self.topics.keys()):
            text = font.render(topic, True, (255, 255, 255))
            textRect = text.get_rect()
 
            textRect.center = (self.width // 2, self.height * ((i+1) / 6))

            window.blit(text, textRect)
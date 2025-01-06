import pygame
import webbrowser


class LinkURL:
    def __init__(self, top_left_pos, link, text, text_color):
        self.top_left_pos = top_left_pos
        self.rect = None
        self.text = text
        self.link = link
        self.font = pygame.font.Font('freesansbold.ttf', 14)

        self.hover_color = (50, 0, 200)
        self.text_color = text_color
        self.clicked_color = (180, 0, 255)

        self.is_hover = False
        self.was_clicked = False
        self.change_state = False

        self.is_active = False
    

    def draw(self, window):
        if not self.is_active:
            return

        if self.was_clicked:
            color = self.clicked_color
        elif self.is_hover:
            color = self.hover_color
        else:
            color = self.text_color


        font_surface = self.font.render(self.text, True, color)
        self.rect = window.blit(font_surface, self.top_left_pos)


    def check_is_hover(self, mouse_pos):
        if not self.is_active:
            return
        
        if self.rect is not None:
            if self.rect.collidepoint(mouse_pos):
                if not self.is_hover:
                    self.change_state = True
                self.is_hover = True
            else:
                if self.is_hover:
                    self.change_state = True
                self.is_hover = False

    def check_clicked(self):
        if not self.is_active:
            return 
        
        if self.is_hover:
            self.was_clicked = True
            self.change_state = True
            webbrowser.open(self.link, 2)
    
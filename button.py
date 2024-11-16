import pygame
import util

class Button:
    def __init__(self, centre_pos, width, height, colors, text, text_font, is_active = True):
        self.centre_pos = centre_pos
        self.width = width
        self.height = height

        bg_color, hover_color, clicked_color, text_color = colors
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.clicked_color = clicked_color
        self.text_color = text_color

        self.text = text
        self.text_font = text_font

        self.is_hover = False
        self.is_clicked = False
        self.is_active = is_active
        self.change_state = False


    def check_is_hover(self, mouse_pos):
        if self.is_active:
            p1 = (self.centre_pos[0] - self.width/2, self.centre_pos[1] - self.height/2)
            p2 = (self.centre_pos[0] + self.width/2, self.centre_pos[1] + self.height/2)

            if util.point_in_box(mouse_pos, p1, p2):
                if not self.is_hover:
                    self.change_state = True

                self.is_hover = True
                return

            if self.is_hover:
                self.change_state = True

            self.is_hover = False       


    ###   DISPLAY   ###
    def draw(self, window):
        if self.is_active:
            self.draw_rect(window)
            self.write_text(window)

    def write_text(self, window):
        util.render_text_centered(self.text, self.text_font, self.text_color, self.centre_pos, window, self.width*0.9)

        # window.blit(text, textRect)

    def draw_rect(self, window):
        rect = (self.centre_pos[0] - self.width/2, self.centre_pos[1] - self.height/2, self.width, self.height)
        if self.is_clicked:
            color = self.clicked_color
        elif self.is_hover:
            color = self.hover_color
        else:
            color = self.bg_color
        pygame.draw.rect(window, color, rect, 0, 4)

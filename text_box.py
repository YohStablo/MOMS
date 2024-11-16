import pygame
import util

class Text_box:
    def __init__(self, top_left_pos, width, height, colors, text, text_font):
        self.top_left_pos = top_left_pos
        self.width = width
        self.height = height

        bg_color, text_color = colors
        self.bg_color = bg_color
        self.text_color = text_color

        self.text = text
        self.text_font = text_font

        self.is_active = False

    ###   DISPLAY   ###
    def draw(self, window):
        if self.is_active:
            self.draw_rect(window)
            self.write_text(window)

    def write_text(self, window):
        top_left_pos = (self.top_left_pos[0] + 0.05 * self.width, self.top_left_pos[1] + 0.1 * self.height)

        util.render_text_left(self.text, self.text_font, self.text_color, top_left_pos, window, self.width*0.9)

        # window.blit(text, textRect)

    def draw_rect(self, window):
        rect = (self.top_left_pos[0], self.top_left_pos[1], self.width, self.height)
        pygame.draw.rect(window, self.bg_color, rect, 0, 4)

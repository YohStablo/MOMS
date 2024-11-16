def point_in_box(p:tuple, p1:tuple, p2:tuple, error_offset:float = 1e-6):
	"""Check if the point 'p' is in the box defined by p1 and p2

	Args:
		p (tuple): Point to be checked
		p1 (tuple): First point
		p2 (tuple): Second point
		error_offset (float, optional): Error offset to overcome python binary error on float. Defaults to 1e-6.

	Returns:
		bool: If the point is in the box
	"""
	if p[0] > min(p1[0], p2[0]) - error_offset and p[0] < max(p2[0], p1[0]) + error_offset:
		if p[1] > min(p1[1], p2[1]) - error_offset and p[1] < max(p2[1], p1[1]) + error_offset:
			return True
	return False


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


def transform_point(pos, map_size, map_offset):
	x, y = pos
	x_trans = (x + 27) * map_size[0] / (35 + 27) + map_offset[0]
	y_trans = (y - 33) * map_size[1] / (73 - 33) + map_offset[1]
	
	return x_trans, map_size[1] - y_trans




###   DISPLAY TEXT   ###



def render_text_centered(text, font, colour, centre_pos, screen, allowed_width):
	# https://stackoverflow.com/questions/49432109/how-to-wrap-text-in-pygame-using-pygame-font-font
    # first, split the text into words

    x, y = centre_pos
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = - fh * len(lines)/2
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh



def render_text_left(text, font, colour, left_pos, screen, allowed_width):
	# https://stackoverflow.com/questions/49432109/how-to-wrap-text-in-pygame-using-pygame-font-font
    # first, split the text into words

    x, y = left_pos
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh*1.1
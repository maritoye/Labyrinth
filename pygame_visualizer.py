"""
Marit Øye Gjersdal
December 2020
"""

import pygame
import const


def get_display(height, width):
	"""
	Determines the size of the cells and the thickness of walls for the pygame visualizer.
	This will make cells in a small labyrinth large, and the cells will be smaller in a larger labyrinth.
	This is simply to fit the screen better, and to be able to visualize very large labyrinths without them becoming
	visually too large.
	:param height: int
	:param width: int
	:return: cell_size, height, width, margin, line - integers
	"""
	if (height < 40) and (width < 60):
		cell_size = 20
		height = height * cell_size
		width = width * cell_size
		margin = 50
		line = 3

	elif height > 200 or width > 350:
		cell_size = 2
		height = height * cell_size
		width = width * cell_size
		margin = 3
		line = 1

	elif height > 100 or width > 160:
		cell_size = 4
		height = height * cell_size
		width = width * cell_size
		margin = 5
		line = 1

	else:
		cell_size = 8
		height = height * cell_size
		width = width * cell_size
		margin = 5
		line = 2

	return cell_size, height, width, margin, line


def update(board, cell_size, margin, line, screen, wf, gbfs):
	"""
	Draws walls, path and visited cells on the pygame screen object.
	:param board: Board object
	:param cell_size: int - size of each cell
	:param margin: int - thickness or margin surrounding the labyrinth
	:param line: int - thickness of line separating the cells
	:param screen: pygame screen object
	:param wf: Boolean value - True if it should draw paths and visited cells from wall follower solver
	:param gbfs: Boolean value - True if it should draw paths and visited cells from greedy best first search solver
	"""
	screen.fill(const.cell_color)

	for y in range(board.get_height()):
		for x in range(board.get_width()):
			cell = board.get_cell(x, y)
			cell_rect = pygame.Rect(x*cell_size + margin, y*cell_size + margin, cell_size, cell_size)

			# set cell color if cell is visited by wall follower
			if wf and cell.get_visited_wf():
				pygame.draw.rect(screen, const.visited_color, cell_rect)

			# set cell color if cell is in the final path wall follower
			if wf and cell.get_path_wf():
				pygame.draw.rect(screen, const.path_color, cell_rect)

			# set cell color if cell is visited by path gbfs
			if gbfs and cell.get_visited_gbfs():
				pygame.draw.rect(screen, const.visited_color, cell_rect)

			# set cell color if cell is in the final path gbfs
			if gbfs and cell.get_path_gbfs():
				pygame.draw.rect(screen, const.path_color, cell_rect)

			# set north wall
			if cell.get_wall_n():
				pygame.draw.line(screen, const.wall_color, (x * cell_size + margin, y * cell_size + margin), ((x + 1) * cell_size + margin, y * cell_size + margin), line)

			# set south wall
			if cell.get_wall_s():
				pygame.draw.line(screen, const.wall_color, (x * cell_size + margin, (y + 1) * cell_size + margin), ((x + 1) * cell_size + margin, (y + 1) * cell_size + margin), line)

			# set west wall
			if cell.get_wall_w():
				pygame.draw.line(screen, const.wall_color, (x * cell_size + margin, y * cell_size + margin), (x * cell_size + margin, (y + 1) * cell_size + margin), line)

			# set east wall
			if cell.get_wall_e():
				pygame.draw.line(screen, const.wall_color, ((x + 1) * cell_size + margin, y * cell_size + margin), ((x + 1) * cell_size + margin, (y + 1) * cell_size + margin), line)


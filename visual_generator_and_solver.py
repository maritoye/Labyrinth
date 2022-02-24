"""
Marit Øye Gjersdal
December 2020
"""
import pygame
from board import Board
from greedy_bfs import solve_gbfs
from wallfollower import wallfollower
from pygame_visualizer import *
from time import perf_counter
from get_user_inputs import *
import const


def visual_generator_and_solver(gbfs, wf):
	"""
	Gets user inputs, initializes a pygame screen object, generates a labyrinth using user input values.
	Calls visual wall follower solver and/or visual greedy best first search solver if wf and/or gbfs are True
	Shows the pygame window (if pygame visualizer is set to true in const.py) and keeps window open until closed.
	:param gbfs: boolean value - True means labyrinth is to be solved using greedy best first search
	:param wf: Boolean value - True means labyrinth is to be solved using wall follower
	"""
	global cell_size, margin, line, screen

	# getting user inputs
	height, width = get_user_input_size()
	if wf or gbfs:
		start_x, start_y = get_user_input_start(height, width)

	# creating a pygame screen object
	cell_size, display_height, display_width, margin, line = get_display(height, width)
	pygame.init()
	screen = pygame.display.set_mode((display_width + margin * 2, display_height + margin * 2))
	screen.fill(const.cell_color)

	# generate labyrinth/board
	board = generator(width, height)

	# solving the labyrinth
	if wf: visual_wallfollower_solver(board, start_x, start_y, height, width)
	if gbfs: visual_gbfs_solver(board, start_x, start_y, height, width)

	if const.show_pygame_visualizer and gbfs and wf:
		print("\nThe pygame window visualizer has been deactivated due to choosing solving using both GBFS "
			  "and wall-follower. The solved labyrinths have been saved as images")
		pygame.quit()
		exit()

	# keeping pygame window open if activated in const.py
	elif const.show_pygame_visualizer:
		while True:
			update(board, cell_size, margin, line, screen, wf, gbfs)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					return
			pygame.display.update()


def visual_gbfs_solver(board, start_x, start_y, height, width):
	"""
	Solving using the greedy best first search solver. Calculates time spent to solve, and prints this
	along with statistics on how many cells were visited by the solver.
	Updates the pygame window to show the visited cells and the path, and saves the solved labyrinth to a jpeg file.
	:param board: Board object
	:param start_x: int
	:param start_y: int
	:param height: int
	:param width: int
	"""
	print("\nSolving labyrinth using greedy best first search.....")
	start_time_solver = perf_counter()

	solve_gbfs(board, start_x, start_y)
	screen.fill(const.cell_color)
	update(board, cell_size, margin, line, screen, wf=False, gbfs=True)
	pygame.image.save(screen, "labyrinth_solved_gbfs.jpeg")

	print("Labyrinth has been successfully solved and saved to file")
	solve_time = round(perf_counter() - start_time_solver, 2)
	print("Solving the labyrinth took " + str(solve_time) + " seconds")
	print("The solver visited " + str(board.get_visited_gbfs()) + " cells, which is " + str(round((
		board.get_visited_gbfs() / (height * width) * 100), 2)) + "% of the labyrinth")


def visual_wallfollower_solver(board, start_x, start_y, height, width):
	"""
	Solving using the wall following solver. Calculates time spent to solve, and prints this
	along with statistics on how many cells were visited by the solver.
	Updates the pygame window to show the visited cells and the path, and saves the solved labyrinth to a jpeg file.
	:param board: Board object
	:param start_x: int
	:param start_y: int
	:param height: int
	:param width: int
	"""
	print("\nSolving labyrinth using wall follower.....")
	start_time_solver = perf_counter()

	wallfollower(board, start_x, start_y)
	screen.fill(const.cell_color)
	update(board, cell_size, margin, line, screen, wf=True, gbfs=False)
	pygame.image.save(screen, "labyrinth_solved_wf.jpeg")

	print("Labyrinth has been successfully solved and saved to file")
	solve_time = round(perf_counter() - start_time_solver, 2)
	print("Solving the labyrinth took " + str(solve_time) + " seconds")
	print("The solver visited " + str(board.get_visited_wf()) + " cells, which is " + str(round((
		board.get_visited_wf() / (height * width) * 100), 2)) + "% of the labyrinth")


def generator(width, height):
	"""
	Creates a Board object (generating a labyrinth). Calculates time spent to generate, and prints this.
	Updates the pygame window to show the labyrinth, and saves the labyrinth to a jpeg file.
	:param width: int
	:param height: int
	:return: Board object
	"""
	print("\nGenerating labyrinth, stay tuned.....")
	start_time_generator = perf_counter()

	board = Board(width, height)
	update(board, cell_size, margin, line, screen, False, False)

	pygame.image.save(screen, "labyrinth_unsolved.jpeg")
	print("Labyrinth has been successfully generated and saved to file")
	generating_time = round(perf_counter() - start_time_generator, 2)
	print("Generating took " + str(generating_time) + " seconds")
	if const.show_pygame_visualizer: pygame.display.update()

	return board


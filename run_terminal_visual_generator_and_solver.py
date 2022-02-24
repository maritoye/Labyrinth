"""
Marit Øye Gjersdal
December 2020
"""

from greedy_bfs import solve_gbfs
from board import Board
from wallfollower import wallfollower
from get_user_inputs import *
from time import perf_counter


def main():
	print("Welcome to the labyrinth generator and solver!"
		  "\nSince you are running the terminal based visualizer, I recommend "
		  "sticking to generating labyrinths with width smaller than 50")

	while True:
		mode = get_mode()

		if mode == "1":
			run_terminal_visual(wf=False, gbfs=False)
		elif mode == "2":
			run_terminal_visual(wf=True, gbfs=False)
		elif mode == "3":
			run_terminal_visual(wf=False, gbfs=True)
		elif mode == "4":
			run_terminal_visual(wf=True, gbfs=True)
		elif mode == "x":
			print("Exiting the program")
			exit()
		else:
			print("Something went wrong :( \nPlease try running the program again")
			exit()


def run_terminal_visual(gbfs, wf):
	"""
	Gets user inputs, generates a labyrinth and calls visualize method to print it in terminal.
	If gbsf and/or wf are True it also calls the solver methods on the generated labyrinth.
	Calculates time spent to generate and solve, and prints this along with statistics on
	how many cells were visited by the solvers.
	:param gbfs: Boolean value - True means labyrinth is to be solved using greedy best first search
	:param wf: Boolean value - True means labyrinth is to be solved using wall follower
	"""
	height, width = get_user_input_size()

	if wf or gbfs:
		start_x, start_y = get_user_input_start(height, width)

	print("\nGenerating labyrinth, stay tuned.....")
	start_time_generator = perf_counter()

	board = Board(width, height)

	print("Labyrinth has been successfully generated")
	generating_time = round(perf_counter() - start_time_generator, 2)
	print("Generating took " + str(generating_time) + " seconds")
	visualize(board, gbfs=False, wf=False)
	print("\n")

	if wf:
		print("\nSolving labyrinth using wall follower.....")
		start_time_generator_wf = perf_counter()

		wallfollower(board, start_x, start_y)

		print("Labyrinth has been successfully solved")
		wf_time = round(perf_counter() - start_time_generator_wf, 2)
		print("Solving the labyrinth took " + str(wf_time) + " seconds")
		print("The solver visited " + str(board.get_visited_wf()) + " cells, which is " + str(round((
			board.get_visited_wf() / (height * width) * 100), 2)) + "% of the labyrinth")
		print("The '.' indicates visited cells, and the 'P' indicates cells in the path from start to goal ")
		visualize(board, gbfs=False, wf=True)
		print("\n")

	if gbfs:
		print("\nSolving labyrinth using greedy best first search.....")
		start_time_generator_gbfs = perf_counter()

		solve_gbfs(board, start_x, start_y)

		print("Labyrinth has been successfully solved")
		gbfs_time = round(perf_counter() - start_time_generator_gbfs, 2)
		print("Solving the labyrinth took " + str(gbfs_time) + " seconds")
		print("The solver visited " + str(board.get_visited_gbfs()) + " cells, which is " + str(round((
			board.get_visited_gbfs() / (height * width) * 100), 2)) + "% of the labyrinth")
		print("The '.' indicates visited cells, and the 'P' indicates cells in the path from start to goal ")
		visualize(board, gbfs=True, wf=False)
		print("\n")


def visualize(board, gbfs, wf):
	"""
	Terminal visualizer: creates a text based visualization of a labyrinth and prints it in terminal.
	:param board: an instance of Board (2d array of instances of Cell class)
	:param gbfs: Boolean value - True means the visualizer should include visited and path cells from
				greedy best first search results
	:param wf: Boolean value - True means the visualizer should include visited and path cells from
				wall follower results
	"""

	# create a blank board, as an array of strings
	for y in range((board.get_height() + 1) * 2):
		for x in range((board.get_width() + 1) * 2):
			lab = [["+"] * x for i in range(y)]

	# fill the array with walls, paths, visited and unvisited cells
	for y in range(board.get_height()):
		for x in range(board.get_width()):
			posx = ((x + 1) * 2) - 1
			posy = ((y + 1) * 2) - 1

			cell = board.get_cell(x, y)

			if gbfs and cell.get_path_gbfs():
				lab[posy][posx] = " P "
			elif gbfs and cell.get_visited_gbfs():
				lab[posy][posx] = " . "
			elif wf and cell.get_path_wf():
				lab[posy][posx] = " P "
			elif wf and cell.get_visited_wf():
				lab[posy][posx] = " . "
			else:
				lab[posy][posx] = "   "

			# set north wall, or blank
			if cell.get_wall_n():
				lab[posy - 1][posx] = "---"
			else:
				lab[posy - 1][posx] = "   "

			# set south wall, or blank
			if cell.get_wall_s():
				lab[posy + 1][posx] = "---"
			else:
				lab[posy + 1][posx] = "   "

			# set west wall, or blank
			if cell.get_wall_w():
				lab[posy][posx - 1] = "|"
			else:
				lab[posy][posx - 1] = " "

			# set east wall, or blank
			if cell.get_wall_e():
				lab[posy][posx + 1] = "|"
			else:
				lab[posy][posx + 1] = " "

	# put together strings for each row in the array, and print them
	for i in range(len(lab)):
		row = ""
		for j in range(len(lab[0])):
			row += lab[i][j]
		print(row)


if __name__ == '__main__':
	main()
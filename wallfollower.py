"""
Marit Øye Gjersdal
December 2020
"""

order = ["n", "e", "s", "w"]


def wallfollower(board, x, y):
	"""
	Solves a given board/labyrinth using the wall following principle.
	:param board: the Board to be solved
	:param x: int - start position x for search
	:param y: int - start position y for search
	"""
	start_cell = board.get_cell(x, y)
	start_cell.set_path_wf(True)
	start_cell.set_visited_wf(True, board)

	wall_direction = 0 # the current direction of wall we are trying to follow, an index in the order list
	solved = False
	current = start_cell

	while not solved:
		neighbor_x, neighbor_y, wall_direction = next_cell(current, wall_direction, board)

		# if neighbor is a previously visited cell, this could not have been the shortest path,
		# and will not be part of the solution
		if board.get_cell(neighbor_x, neighbor_y).get_path_wf():
			current.set_path_wf(False)

		current = board.get_cell(neighbor_x, neighbor_y) # set the neighbor as current
		current.set_visited_wf(True, board) # to mark the cell as visited
		current.set_path_wf(True) # to mark the cell as solution path

		# check if goal/solution was found, this will end the loop
		if current.get_solution():
			solved = True

	if solved:
		return True


def next_cell(current, dir, board):
	"""
	Finds a neighboring cell of the given cell, following the given direction and checking for neighbors
	in the order given by the order list
	:param current: Cell object
	:param dir: int - 0-3, to get direction index in the order list
	:param board: Board object
	:return: int, int, Cell object - x and y index of the neighbour, and the Cell object of the neighbour
	"""
	direction = dir
	new_direction = 0

	if order[direction] == "n":
		wall = current.get_wall_n()
		if wall:
			new_direction = direction+1 if direction < 3 else 0
			neighbor_x, neighbor_y, new_direction = next_cell(current,new_direction,board)
		elif not wall:
			neighbor_x, neighbor_y = current.get_x(), (current.get_y() - 1)
			new_direction = direction-1 if direction > 0 else 3
			return neighbor_x, neighbor_y, new_direction

	elif order[direction] == "e":
		wall = current.get_wall_e()
		if wall:
			new_direction = direction+1 if direction < 3 else 0
			neighbor_x, neighbor_y, new_direction = next_cell(current,new_direction,board)
		elif not wall:
			neighbor_x, neighbor_y = (current.get_x() + 1) , current.get_y()
			new_direction = direction-1 if direction > 0 else 3
			return neighbor_x, neighbor_y, new_direction

	elif order[direction] == "s":
		wall = current.get_wall_s()
		if wall:
			new_direction = direction+1 if direction < 3 else 0
			neighbor_x, neighbor_y, new_direction = next_cell(current,new_direction,board)
		elif not wall:
			neighbor_x, neighbor_y = current.get_x(), (current.get_y() + 1)
			new_direction = direction-1 if direction > 0 else 3
			return neighbor_x, neighbor_y, new_direction

	elif order[direction] == "w":
		wall = current.get_wall_w()
		if wall:
			new_direction = direction+1 if direction < 3 else 0
			neighbor_x, neighbor_y, new_direction = next_cell(current,new_direction,board)
		elif not wall:
			neighbor_x, neighbor_y = (current.get_x() - 1), current.get_y()
			new_direction = direction-1 if direction > 0 else 3
			return neighbor_x, neighbor_y, new_direction

	return neighbor_x, neighbor_y, new_direction


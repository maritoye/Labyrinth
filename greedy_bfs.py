"""
Marit Øye Gjersdal
December 2020
"""


def solve_gbfs(board, x, y):
	"""
	Solves a given board/labyrinth using greedy best first search.
	:param board: the Board to be solved
	:param x: int - start position x for search
	:param y: int - start position y for search
	"""
	start_cell = board.get_cell(x,y)
	open_cells = [] # child cells that have not been visited
	closed_cells = [] # cells that have been visited

	goal = board.get_solution()
	goal.set_manhattan(0)

	start_cell.set_manhattan(int(abs(goal.get_x() - start_cell.get_x())) + int(abs(goal.get_y() - start_cell.get_y())))
	start_cell.set_parent(start_cell)
	open_cells.append(start_cell)

	done = False

	while not done:
		if not open_cells:
			break
		current = open_cells.pop(0)
		current.set_visited_gbfs(True, board)
		closed_cells.append(current)
		if current.get_solution():
			break
		if build_children(board, current):
			for child in current.get_children():
				if child not in open_cells and child not in closed_cells:
					open_cells.append(child)
					child.set_manhattan(
						int(abs(goal.get_x() - current.get_x())) + int(abs(goal.get_y() - current.get_y())))

					sorted(open_cells, key=lambda node: node.get_manhattan()) # sorts the list by manhattan

	# Mark the cells in final path
	goal.set_path_gbfs(True)
	current = goal

	# Starts in the goal cell, and marks the cells parent as path cells until reaching start node.
	while not done:
		parent = current.get_parent()
		parent.set_path_gbfs(True)
		if (start_cell.get_x() == parent.get_x()) and (start_cell.get_y() == parent.get_y()):
			return True
		current = parent


def build_children(board, current):
	"""
	Finds all children of the current cell, and add them to the cells list of children.
	A child means a neighboring cell (a cell next to the current cell, without a wall between them).
	A cells parent cannot also be its child.
	:param board: Board object
	:param current: Cell object
	"""
	children = []
	parent = current.get_parent()

	if not current.get_solution():
		# north
		if not current.get_wall_n():
			child = board.get_cell(current.get_x(), current.get_y() - 1)
			if not ((child.get_x() == parent.get_x()) and (child.get_y() == parent.get_y())):
				children.append(child)
				child.set_parent(current)

		# south
		if not current.get_wall_s():
			child = board.get_cell(current.get_x(), current.get_y() + 1)
			if not ((child.get_x() == parent.get_x()) and (child.get_y() == parent.get_y())):
				children.append(child)
				child.set_parent(current)

		# east
		if not current.get_wall_e():
			child = board.get_cell(current.get_x()+1, current.get_y())
			if not ((child.get_x() == parent.get_x()) and (child.get_y() == parent.get_y())):
				children.append(child)
				child.set_parent(current)

		# west
		if not current.get_wall_w():
			child = board.get_cell(current.get_x()-1, current.get_y())
			if not ((child.get_x() == parent.get_x()) and (child.get_y() == parent.get_y())):
				children.append(child)
				child.set_parent(current)

	if children:
		current.set_children(children)
		return True
	return False

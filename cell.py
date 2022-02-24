"""
Marit Øye Gjersdal
December 2020
"""


class Cell:
	def __init__(self,x,y):
		self._posx = x
		self._posy = y

		self._north = False
		self._south = False
		self._west = False
		self._east = False
		self._solution = False

		# for solving the labyrinth using wall follower
		self._visited_wf = False
		self._path_wf = False

		# for solving the labyrinth using gbfs
		self._visited_gbfs = False
		self._path_gbfs = False
		self._manhattan = 0  # manhattan distance from this node to goal node
		self._parent = None
		self._children = []

	def set_wall_n(self, board, val):
		"""
		Set value for north wall of cell. Either True for wall, or False for no wall,
		will also set the south wall of the north neighboring cell (if any) to be the same value
		:param board: Board object
		:param val: Boolean - True for inserting wall, False for removing wall
		"""
		self._north = val
		if self._posy > 0:
			neighbor = board.get_cell(self._posx, self._posy-1)
			if not (neighbor.get_wall_s() == val):
				neighbor.set_wall_s(board, val)

	def set_wall_s(self, board, val):
		"""
		Set value for south wall of cell. Either True for wall, or False for no wall,
		will also set the north wall of the south neighboring cell (if any) to be the same value
		:param board: Board object
		:param val: Boolean - True for inserting wall, False for removing wall
		"""
		self._south = val
		if self._posy < board.get_height()-1:
			neighbor = board.get_cell(self._posx, self._posy+1)
			if not (neighbor.get_wall_n() == val):
				neighbor.set_wall_n(board, val)


	def set_wall_w(self, board, val):
		"""
		Set value for west wall of cell. Either True for wall, or False for no wall,
		will also set the east wall of the west neighboring cell (if any) to be the same value
		:param board: Board object
		:param val: Boolean - True for inserting wall, False for removing wall
		"""
		self._west = val
		if self._posx > 0:
			neighbor = board.get_cell(self._posx-1, self._posy)
			if not (neighbor.get_wall_e() == val):
				neighbor.set_wall_e(board, val)


	def set_wall_e(self, board, val):
		"""
		Set value for east wall of cell. Either True for wall, or False for no wall,
		will also set the west wall of the east neighboring cell (if any) to be the same value
		:param board: Board object
		:param val: Boolean - True for inserting wall, False for removing wall
		"""
		self._east = val
		if self._posx < board.get_width()-1:
			neighbor = board.get_cell(self._posx+1, self._posy)
			if not (neighbor.get_wall_w() == val):
				neighbor.set_wall_w(board, val)


	def set_visited_wf(self, value, board):
		"""
		Sets the visited status of cell, by wall follower solver.
		If value is set to True it also increases the total amount of visited cells (by wall follower) in the board
		:param value: Boolean - True for visited, False for not visited
		:param board: Board object
		"""
		if self._visited_wf != value:
			self._visited_wf = value
			if value:
				board.increase_visited_wf()

	def set_visited_gbfs(self, value, board):
		"""
		Sets the visited status of cell, by greedy best first search solver.
		If value is set to True it also increases the total amount of visited cells (by greedy bfs) in the board
		:param value: Boolean - True for visited, False for not visited
		:param board: Board object
		"""
		if self._visited_gbfs != value:
			self._visited_gbfs = value
			if value:
				board.increase_visited_gbfs()

	def set_path_wf(self, value):
		self._path_wf = value

	def set_path_gbfs(self, value):
		self._path_gbfs = value

	def set_solution(self, value):
		self._solution = value

	def set_manhattan(self, manhattan):
		self._manhattan = manhattan

	def set_parent(self, parent):
		self._parent = parent

	def set_children(self, children):
		self._children = children

	def get_wall_n(self):
		return self._north

	def get_wall_s(self):
		return self._south

	def get_wall_w(self):
		return self._west

	def get_wall_e(self):
		return self._east

	def get_y(self):
		return self._posy

	def get_x(self):
		return self._posx

	def get_path_wf(self):
		return self._path_wf

	def get_path_gbfs(self):
		return self._path_gbfs

	def get_visited_wf(self):
		return self._visited_wf

	def get_visited_gbfs(self):
		return self._visited_gbfs

	def get_solution(self):
		return self._solution

	def get_manhattan(self):
		return self._manhattan

	def get_parent(self):
		return self._parent

	def get_children(self):
		return self._children

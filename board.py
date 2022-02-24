"""
Marit Øye Gjersdal
December 2020
"""
"""
Board class
A board contains a 2d array of instances of Cell
The Board will upon initialization "split" itself by creating walls until it becomes a perfect labyrinth,
with one exit and only one solution from any position
"""
from cell import Cell
import random
import const


class Board:
	def __init__(self,x,y):
		self._board = [["c"] * x for i in range(y)]
		for i in range(x):
			for j in range(y):
				self._board[j][i] = Cell(i,j)

		self.create_walls()

		self.split_horizontal(0, 0, self.get_width()-1, self.get_height()-1)

		# For keeping count of how many cells have been visited when solving the labyrinth
		self._visited_wf = 0
		self._visited_gbfs = 0


	def create_walls(self):
		"""
		Creates the outer walls of the labyrinth, and chooses a random wall to put the exit on,
		then chooses a random cell along this wall to set as exit/goal
		"""
		exit_wall = random.randint(0, 3)
		exit_index = random.randint(0,self.get_width()-1) if ((exit_wall == 0) or (exit_wall == 1)) \
			else random.randint(0,self.get_height()-1)

		for ncell in range(len(self._board[0])):
			border_cell = self._board[0][ncell]
			border_cell.set_wall_n(self,True)
			if exit_wall == 0:
				if ncell==exit_index:
					border_cell.set_wall_n(self, False)
					border_cell.set_solution(True)
					self.solution = border_cell

		for scell in range(len(self._board[0])):
			border_cell = self._board[len(self._board)-1][scell]
			border_cell.set_wall_s(self,True)
			if exit_wall == 1:
				if scell==exit_index:
					border_cell.set_wall_s(self, False)
					border_cell.set_solution(True)
					self.solution = border_cell

		for wcell in range(len(self._board)):
			border_cell = self._board[wcell][0]
			border_cell.set_wall_w(self,True)
			if exit_wall == 2:
				if wcell==exit_index:
					border_cell.set_wall_w(self, False)
					border_cell.set_solution(True)
					self.solution = border_cell

		for ecell in range(len(self._board)):
			border_cell = self._board[ecell][len(self._board[0])-1]
			border_cell.set_wall_e(self, True)
			if exit_wall == 3:
				if ecell==exit_index:
					border_cell.set_wall_e(self, False)
					border_cell.set_solution(True)
					self.solution = border_cell


	def split_horizontal(self, fromx, fromy, tox, toy):
		"""
		Splits subset of board in two horizontally if height is two cells or larger, calls split_vertical
		for each of those boards. Inserts a wall at the split with one opening
		:param fromx: int - the subsets starting position x on the board
		:param fromy: int - the subsets starting position y on the board
		:param tox: int - the subsets ending position x on the board
		:param toy: int - the subsets ending position y on the board
		"""
		# breaks the recursive calling if the sub-board is size 1x1
		if (tox-fromx) < 1 and (toy-fromy) < 1:
			return

		elif (const.improved_recursive_generator
				and ((toy - fromy) > 0 and (tox - fromx) <= (toy - fromy)) or (toy - fromy) == 1) \
				or (not const.improved_recursive_generator and (toy - fromy) > 0):

			if (toy - fromy) > 0:
				split = random.randint(fromy+1, toy)
			else:
				split = toy

			if (tox - fromx) > 0:
				opening = random.randint(fromx, tox)
			else:
				opening = fromx

			for cell in range(fromx,tox+1):
				if cell != opening:
					self.get_cell(cell, split).set_wall_n(self, True)

			# call split_vertical for top board
			self.split_vertical(fromx, fromy, tox, split-1)

			# call split_vertical for bottom board
			self.split_vertical(fromx, split, tox, toy)

		# if grid is less than two cells high, go to split vertically
		elif tox-fromx > 2:
			self.split_vertical(fromx, fromy, tox, toy)


	def split_vertical(self, fromx, fromy, tox, toy):
		"""
		Splits subset of board in two vertically if width is two cells or larger, calls split_horizontal
		for each of those boards. Inserts a wall at the split with one opening
		:param fromx: int - the subsets starting position x on the board
		:param fromy: int - the subsets starting position y on the board
		:param tox: int - the subsets ending position x on the board
		:param toy: int - the subsets ending position y on the board
		"""
		# breaks the recursive calling if the sub-board is size 1x1
		if (tox - fromx) < 1 and (toy - fromy) < 1:
			return

		if (const.improved_recursive_generator
			  and ((tox-fromx) > 0 and (tox-fromx)>=(toy-fromy)) or (tox - fromx) == 1) \
				or (not const.improved_recursive_generator and (tox - fromx) > 0):

			if (tox - fromx) > 0:
				split = random.randint(fromx + 1, tox)
			else:
				split = tox

			if (toy - fromy) > 0:
				opening = random.randint(fromy, toy)
			else:
				opening = fromy

			for cell in range(fromy,toy+1):
				if cell != opening:
					self.get_cell(split,cell).set_wall_w(self, True)

			# call split_vertical for left board
			self.split_horizontal(fromx, fromy, split-1, toy)

			# call split_vertical for right board
			self.split_horizontal(split, fromy, tox, toy)

		# if grid is less than two cells high, go to split vertically
		elif toy-fromy > 2:
			self.split_horizontal(fromx, fromy, tox, toy)


	def increase_visited_wf(self):
		self._visited_wf+=1

	def increase_visited_gbfs(self):
		self._visited_gbfs+=1

	def get_cell(self,x,y):
		cell = self._board[y][x]
		return cell

	def get_solution(self):
		return self.solution

	def get_height(self):
		return len(self._board)

	def get_width(self):
		return len(self._board[0])

	def get_visited_wf(self):
		return self._visited_wf

	def get_visited_gbfs(self):
		return self._visited_gbfs
"""
Marit Øye Gjersdal
December 2020
"""

import const

menu = "\nChoose one of the following options: " \
	   "\n1 - Only generate a labyrinth " \
	   "\n2 - Generate a labyrinth and solve it using wall-follower" \
	   "\n3 - Generate a labyrinth and solve it using greedy best first search" \
	   "\n4 - Generate a labyrinth and solve it using both wall follower and greedy best first search" \
	   "\nx - Exit the program"
modes = ["1", "2", "3", "4", "x"]


def get_mode():
	"""
	Get the desired mode as input from user. The input must be in the modes list to be valid.
	:return: string - a mode from the "modes" list, as given by user input
	"""
	print(menu)
	mode = input("\nPlease enter the desired option: ")

	while mode not in modes:
		print("Input error: please enter a valid mode")
		mode = input("Enter the desired option: ")

	return mode

def get_user_input_size():
	"""
	Get user input for height and width. Checks for invalid inputs, such as negative inputs,
	inputs smaller than 3, and inputs that are not integers.
	:return: int ,int - the desired height and width of the labyrinth
	"""
	width = input("\nEnter the desired width of the labyrinth: ")
	height = input("Enter the desired height of the labyrinth: ")

	try:
		width = int(width)
		height = int(height)

		if width < 3:
			width = 10
			print("\nInput error: width was smaller than 3 or negative number, and has been set to 10" )

		elif width > const.max_size:
			width = const.max_size
			print("\nInput error: width was larger than maximum allowed size, and was set to " + str(const.max_size))

		if height < 3:
			height = 10
			print("\nInput error: height was smaller than 3 or negative number, and has been set to 10" )

		elif height > const.max_size:
			height = const.max_size
			print("\nInput error: height was larger than maximum allowed size, and was set to " + str(const.max_size))

	except:
		# If input was not an integer: set height and width to 100
		width = 100
		height = 100
		print("\nInput error: invalid input")
		print("The width and height of the labyrinth was set to 100")

	return height, width


def get_user_input_start(height, width):
	"""
	Get user input for start position x and start position y.
	Makes sure input is valid (invalid inputs are negative inputs and inputs that are not integers.)
	For start positions it checks that 0 <= x < width and 0 <= y < height
	:param: height: int
	:param: width: int
	:return: int ,int - the starting position x and y for solving the labyrinth
	"""
	start_x = input("\nHorizontal (x) position of start point when solving the labyrinth: ")
	start_y = input("Vertical (y) position of start point when solving the labyrinth: ")

	try:
		start_x = int(start_x) - 1
		start_y = int(start_y) - 1

		if start_x < 0:
			start_x = width//2
			print("\nInput error: x position was 0 or negative number, and has been set to " + start_x)

		elif start_x > width:
			start_x = width//2
			print("\nInput error: x position was larger than width, and was set to " + start_x)

		if start_y < 0:
			start_y = height//2
			print("\nInput error: y position was 0 or negative number, and has been set to " + start_y)

		elif start_y > height:
			start_y = height//2
			print("\nInput error: y position was larger than height, and was set to " + start_y)

	except:
		# If input was not an integer: set the starting position to center of labyrinth
		start_x = width//2
		start_y = height//2
		print("Input error: invalid input")
		print("The start position was set to the center of the labyrinth")

	return start_x, start_y
"""
Marit Øye Gjersdal
December 2020
"""

import visual_generator_and_solver as vis
from get_user_inputs import get_mode

def main():
	print("\nWelcome to the labyrinth generator and solver!")

	while True:
		mode = get_mode()

		if mode == "1":
			vis.visual_generator_and_solver(wf=False, gbfs=False)
		elif mode == "2":
			vis.visual_generator_and_solver(wf=True, gbfs=False)
		elif mode == "3":
			vis.visual_generator_and_solver(wf=False, gbfs=True)
		elif mode == "4":
			vis.visual_generator_and_solver(wf=True, gbfs=True)
		elif mode == "x":
			print("Exiting the program")
			exit()
		else:
			print("Something went wrong :( \nPlease try running the program again")
			exit()

		print("\nNote: Generating new labyrinths will result in overwriting the current image files. "
			  "\nPlease save the files in a different location before proceeding if you wish to keep them")


if __name__ == '__main__':
	main()
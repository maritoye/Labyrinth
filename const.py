"""
Marit Øye Gjersdal
December 2020
"""
"""
Constants used when running the program
Feel free to change these before running the program
"""
max_size = 1000 # The maximum size of a labyrinth in each direction

# Enable or disable the pygame window. Labyrinth will still be saved as image when running using pygame visualizer
# I highly suggest setting this to False when making labyrinths larger than 1000x1000 cells
show_pygame_visualizer = True

# Setting this to False will instead activate the basic recursive generator
improved_recursive_generator = True

# Colors for the pygame visualizer (and image files)
cell_color = (250, 250, 250) # white
wall_color = (0, 0, 0) # black
visited_color = (200, 200, 200) # grey
path_color = (100, 0, 100) # purple

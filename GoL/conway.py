"""
conway.py
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse, os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)


def plotInitialConfig(Lines, grid):
    """Plots the initial points into the grid"""
    for line in Lines:
        p = line.split()
        x = int(p[0])
        y = int(p[1])
        grid[x][y] = 1


def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0, 0, 255],
                       [255, 0, 255],
                       [0, 255, 255]])
    grid[i:i + 3, j:j + 3] = glider


def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    # TODO: Implement the rules of Conway's Game of Life
    for i in range(1, N-1, 1):
        for j in range(1, N-1, 1):
            # At each time step in the simulation, for each cell (i, j) in the grid, do the following:
            neighbors = grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1] + grid[i-1][j] + grid[i+1][j] + grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j+1]
            cell = grid[i][j]
            if cell == 1:
                if (neighbors < 2) or (neighbors > 3):
                    newGrid[i][j] = 0
            else:
                if neighbors == 3:
                    newGrid[i][j] = 1

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,


def heatmap(data, row_labels, col_labels, ax=None, **kwargs):
    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=False, bottom=True,
                   labeltop=False, labelbottom=True)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-70, ha="left",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1] + 1) - .5, minor=True)
    ax.set_yticks(np.arange(data.shape[0] + 1) - .5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im


# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    '''
        parser.add_argument("Path",
                        metavar='path',
                        type=str,
                        help='the path to initial configuration')
    '''

    # Get the input file with the initial configuration
    # configFile = os.path.basename(sys.argv[1])
    configFile = os.path.basename("Tile.txt")
    file1 = open(configFile, 'r')
    Lines = file1.readlines()

    # set grid size
    N = int(Lines[0].split()[0])

    # set animation update interval
    updateInterval = 10

    # declare grid
    # grid = np.array([])

    # populate grid with random on/off - more off than on
    # grid = randomGrid(N)
    # Uncomment lines to see the "glider" demo

    grid = np.zeros(N * N).reshape(N, N)

    # Plot the initial configuration points
    plotInitialConfig(Lines[1:], grid)

    fig, ax = plt.subplots()

    ax.set_xticks(np.arange(N))
    ax.set_yticks(np.arange(N))

    ax.set_title("Conway's Game of Life")
    im = heatmap(grid, range(0, N), range(N, 0), ax=ax, cmap="Wistia")

    # set up animation
    ani = animation.FuncAnimation(fig, update, fargs=(im, grid, N,), frames=30, interval=updateInterval, save_count=50)

    plt.show()


# call main
if __name__ == '__main__':
    main()

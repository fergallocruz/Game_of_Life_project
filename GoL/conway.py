"""
María Fernanda Gallo Cruz
Simulation & Visualization Class
Universidad Panamericana Campus Guadalajara
Computer Systems Engineering
conway.py
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse, os
import matplotlib.pyplot as plt
from matplotlib import animation

from report import *
from shapes import *

def plotInitialConfig(Lines, grid, h, w):
    """Plots the initial points into the grid"""
    for line in Lines:
        p = line.split()
        x = int(p[0])
        y = int(p[1])
        grid[x, y] = 1

def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    for s in counter:
        counter[s] = 0
    newGrid = grid
    # TODO: Implement the rules of Conway's Game of Life
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            if 0 < i < 29 and 0 < j < 29:
                total = int((grid[i, (j - 1)] +
                             grid[i, (j + 1)] +
                             grid[(i - 1), j] +
                             grid[(i + 1), j] +
                             grid[(i - 1), (j - 1)] +
                             grid[(i - 1), (j + 1)] +
                             grid[(i + 1), (j - 1)] +
                             grid[(i + 1), (j + 1)]))
                if grid[i, j] == 1:
                    if (total < 2) or (total > 3):
                        newGrid[i, j] = 0
                else:
                    if total == 3:
                        newGrid[i, j] = 1
            mat_4 = np.array(newGrid[i:i + 4, j:j + 4])
            mat_46 = np.array(newGrid[i:i + 4, j:j + 6])
            mat_5 = np.array(newGrid[i:i + 5, j:j + 5])
            mat_6 = np.array(newGrid[i:i + 6, j:j + 6])
            mat_56 = np.array(newGrid[i:i + 5, j:j + 6])
            mat_53 = np.array(newGrid[i:i + 5, j:j + 3])
            mat_35 = np.array(newGrid[i:i + 3, j:j + 5])
            mat_67 = np.array(newGrid[i:i + 6, j:j + 7])

            if mat_4.shape == (4, 4):
                isBlock = mat_4 == block
                if isBlock.all(): counter['Block'] += 1

            if mat_5.shape == (5, 5):
                isTub = mat_5 == tub
                isBoat = mat_5 == boat
                isGlider_1 = mat_5 == glider_1
                isGlider_2 = mat_5 == glider_2
                isGlider_3 = mat_5 == glider_3
                isGlider_4 = mat_5 == glider_4
                if isTub.all():  counter['Tub'] += 1
                if isBoat.all(): counter['Boat'] += 1
                if isGlider_1.all() or isGlider_2.all() or isGlider_3.all() or isGlider_4.all():
                    counter['Glider'] += 1

            if mat_6.shape == (6, 6):
                isToad_1 = mat_6 == toad_1
                isBeacon_1 = mat_6 == beacon_1
                isBeacon_2 = mat_6 == beacon_2
                isLoaf = mat_6 == loaf
                if isToad_1.all():  counter['Toad'] += 1
                if isBeacon_1.all() or isBeacon_2.all(): counter['Beacon'] += 1
                if isLoaf.all():  counter['Loaf'] += 1

            if mat_67.shape == (6, 7):
                isSpaceship_1 = mat_67 == spaceship_1
                isSpaceship_2 = mat_67 == spaceship_2
                isSpaceship_3 = mat_67 == spaceship_3
                isSpaceship_4 = mat_67 == spaceship_4
                if isSpaceship_1.all() or isSpaceship_2.all() or isSpaceship_3.all() or isSpaceship_4.all():
                    counter['Spaceship'] += 1

            if mat_46.shape == (4, 6):
                isToad_2 = mat_46 == toad_2
                if isToad_2.all(): counter['Toad'] += 1

            if mat_53.shape == (5, 3):
                isBlinker_1 = mat_53 == blinker_1
                if isBlinker_1.all(): counter['Blinker'] += 1
            elif mat_35.shape == (3, 5):
                isBlinker_2 = mat_35 == blinker_2
                if isBlinker_2.all(): counter['Blinker'] += 1

            if mat_56.shape == (5, 6):
                isBehive = mat_56 == behive
                if isBehive.all():
                    counter['Behive'] += 1
    print_report(frameNum)
    # print(blinker)
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,


def heatmap(data, ax=None, **kwargs):

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1] + 1) - .5, minor=True)
    ax.set_yticks(np.arange(data.shape[0] + 1) - .5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)

    return im


# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    parser.add_argument("Path",
                        metavar='path',
                        type=str,
                        help='the path to initial configuration')


    # Get the input file with the initial configuration
    configFile = os.path.basename(sys.argv[1])
    file1 = open(configFile, 'r')
    Lines = file1.readlines()

    # set grid size
    h = int(Lines[0].split()[0])
    w = int(Lines[0].split()[0])
    # set animation update interval
    updateInterval = 1

    # declare grid
    grid = np.zeros(h * w).reshape(h, w)

    # Plot the initial configuration points
    plotInitialConfig(Lines[1:], grid, h, w)

    fig, ax = plt.subplots()
    ax.set_title("Conway's Game of Life")
    im = heatmap(grid, ax=ax, cmap="coolwarm")

    # set up animation
    ani = animation.FuncAnimation(fig, update, fargs=(im, grid, 30), frames=15, interval=updateInterval, blit=False)
    plt.show()


# call main
if __name__ == '__main__':
    main()

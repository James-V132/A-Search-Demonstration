import random
import math
import time
import timeit


def make_man_maze(maze, x1, y1, x2, y2):
    man_maze = maze
    y = 0
    if y1 < y2:
        while y1 + y != y2:
            if man_maze[y1 + y][x1] != 2:
                man_maze[y1 + y][x1] = "|"
            y += 1
            posy = y1 + y
            posx = x1
    elif y1 > y2:
        while y1 - y != y2:
            if man_maze[y1 - y][x1] != 2:
                man_maze[y1 - y][x1] = "|"
            y += 1
            posy = y1 - y
            posx = x1
    else:
        posy = y1
        posx = x1

    #posx and posy save the position before modifying the x-direction to the goal position
    x = 0
    if posx < x2:
        while posx + x != x2:
            if man_maze[posy][posx + x] != 2:
                man_maze[posy][posx + x] = "-"
            x += 1
    elif posx > x2:
        while posx - x != x2:
            if man_maze[posy][posx - x] != 2:
                man_maze[posy][posx - x] = "-"
            x += 1
    return man_maze

def make_euc_maze(maze, x1, y1, x2, y2):
    euc_maze = list(maze)
    y = 0
    x = 0
    if y2 > y1:
        if x2 > x1:
            while x1 + x != x2 and y1 + y != y2:
                if euc_maze[y1 + y][x1 + x] != 2:
                    euc_maze[y1 + y][x1 + x] = "-"
                y += 1
                x += 1
            posx = x1 + x
            posy = y1 + y
            x = 0
            y = 0
            while posx + x != x2:
                euc_maze[posy][posx + x] = "-"
                x += 1
            while posy + y != y2:
                euc_maze[posy + y][posx] = "|"
                y += 1
        elif x2 < x1:
            while x1 - x != x2 and y1 + y != y2:
                if euc_maze[y1 + y][x1 - x] != 2:
                    euc_maze[y1 + y][x1 - x] = "-"
                y += 1
                x += 1
            posx = x1 - x
            posy = y1 + y
            x = 0
            y = 0
            while posx - x != x2:
                euc_maze[posy][posx - x] = "-"
                x += 1
            while posy + y != y2:
                euc_maze[posy + y][posx] = "|"
                y += 1
        else:
            if y2 > y1:
                while y1 + y != y2:
                    if euc_maze[y1 + y][x1] != 2:
                        euc_maze[y1 + y][x1] = "|"
                    y += 1
            elif y1 > y2:
                while y1 - y != y2:
                    if euc_maze[y1 - y][x1] != 2:
                        euc_maze[y1 - y][x1] = "|"
                    y += 1
    elif y2 < y1:
        if x2 > x1:
            while x1 + x != x2 and y1 - y != y2:
                if euc_maze[y1 - y][x1 + x] != 2:
                    euc_maze[y1 - y][x1 + x] = "-"
                y += 1
                x += 1
            posx = x1 + x
            posy = y1 - y
            x = 0
            y = 0
            while posx + x != x2:
                if euc_maze[posy][posx + x] != 2:
                    euc_maze[posy][posx + x] = "-"
                x += 1
            while posy - y != y2:
                if euc_maze[posy - y][posx] != 2:
                    euc_maze[posy - y][posx] = "|"
                y += 1
        elif x2 < x1:
            while x1 - x != x2 and y1 - y != y2:
                if euc_maze[y1 - y][x1 - x] != 2:
                    euc_maze[y1 - y][x1 - x] = "-"
                y += 1
                x += 1
            posx = x1 - x
            posy = y1 - y
            x = 0
            y = 0
            while posx - x != x2:
                if euc_maze[posy][posx - x] != 2:
                    euc_maze[posy][posx - x] = "-"
                x += 1
            while posy - y != y2:
                if euc_maze[posy - y][posx] != 2:
                    euc_maze[posy - y][posx] = "|"
                y += 1
        else:
            if y2 > y1:
                while y1 + y != y2:
                    if euc_maze[y1 + y][x1] != 2:
                        euc_maze[y1 + y][x1] = "|"
                    y += 1
            elif y1 > y2:
                while y1 - y != y2:
                    if euc_maze[y1 - y][x1] != 2:
                        euc_maze[y1 - y][x1] = "|"
                    y += 1
    else:
        if x2 > x1:
            while x1 + x != x2:
                if euc_maze[y1][x1 + x] != 2:
                    euc_maze[y1][x1 + x] = "-"
                x += 1
        elif x2 < x1:
            while x1 - x != x2:
                if euc_maze[y1][x1 - x] != 2:
                    euc_maze[y1][x1 - x] = "-"
                x += 1

    return euc_maze

def make_cheb_maze(maze, x1, y1, x2, y2):
    cheb_maze = maze
    if abs(y1 - y2) > abs(x1 - x2):
        y = 0
        if y1-y2 < 0:
            while y1 + y != y2+1:
                if cheb_maze[y1+y][x1] != 2 and cheb_maze[y1+y][x1] != 3:
                    cheb_maze[y1+y][x1] = "|"
                y += 1
        elif y1-y2 > 0:
            while y1 - y != y2-1:
                if cheb_maze[y1-y][x1] != 2 and cheb_maze[y1-y][x1] != 3:
                    cheb_maze[y1-y][x1] = "|"
                y +=1
    elif abs(y1 - y2) < abs(x1 - x2):
        x = 0
        if x1-x2 < 0:
            while x1 + x != x2 + 1:
                if cheb_maze[y1][x1+x] != 2 and cheb_maze[y1][x1+x] != 3:
                    cheb_maze[y1][x1+x] = "-"
                x += 1
        elif x1-x2 > 0:
            while x1 - x != x2 - 1:
                if cheb_maze[y1][x1-x] != 2 and cheb_maze[y1][x1-x] != 3:
                    cheb_maze[y1][x1-x] = "-"
                x += 1
    else:
        y = 0
        if y1 < y2:
            while y1 + y != y2 + 1:
                if cheb_maze[y1 + y][x1] != 2:
                    cheb_maze[y1 + y][x1] = "|"
                y += 1
        elif y1 > y2:
            while y1 - y != y2 - 1:
                if cheb_maze[y1 - y][x1] != 2:
                    cheb_maze[y1 - y][x1] = "|"
                y += 1
    return cheb_maze

def print_maze(maze): # Prints the maze at hand
    for i in range(5):
        print("-" * 30)
        for i2 in range(5):
            print("| ",maze[i][i2], " ", end="")
        print("|")
    print("-" * 30)

def reset_maze(maze): # Rests the modified maze to its original state
    for i in range(5):
        for i2 in range(5):
            if maze[i][i2] == "-" or maze[i][i2] == "|":
                maze[i][i2] = 0

def manhattan(x1, y1, x2, y2): # Calculates the Manhattan distance in the maze and returns the value
    print("Manhattan Distance:")
    return abs(x1 - x2) + abs(y1 - y2)

def euclidean(x1, y1, x2, y2): # Calculates the Euclidean distance in the maze and returns the value
    print("Euclidean Disntace: ")
    return round(math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)), 3)

def chebyshev(x1, y1, x2, y2): # Calculates the Chebyshev distance in the maze and returns the value
    print("Chebyshev Distance: ")
    return max(abs((x1 - x2)), abs((y1 - y2)))

def maze_maker(): #Generates the maze
    maze = []
    for i in range(5):
        maze_append = []
        for i in range(5):
            maze_append.append(0)
        maze.append(maze_append)
    return maze

def maze_plotter(maze):
    # Plots a starting point on the maze
    startx = random.randrange(0, 5)
    starty = random.randrange(0, 5)
    maze[starty][startx] = 2

    # Plots a goal point on the maze
    goalx = random.randrange(0, 5)
    goaly = random.randrange(0, 5)

    # Prevents the starting and goal point from being the same plot on the maze
    while startx == goalx and starty == goaly:
        goalx = random.randrange(0, 5)
        goaly = random.randrange(0, 5)

    maze[goaly][goalx] = 3

    return startx, starty, goalx, goaly

def main():

    maze = maze_maker()
    startx, starty, goalx, goaly = maze_plotter(maze)

    print_maze(maze)

    # Displays the starting and goal positions relative to the maze
    print()
    print("Starting Position: (", startx + 1, ",", abs(starty - 5), ")")
    print("Goal Position: (", goalx + 1, ",", abs(goaly - 5), ")")

    # Displays the Manhattan maze, number generated via this method, and time it took to calculate it
    print()
    start_time = timeit.default_timer()
    print(manhattan(startx, starty, goalx, goaly))
    end_time = timeit.default_timer()
    print("Elapsed Time:", end_time - start_time)

    man_maze = make_man_maze(maze, startx, starty, goalx, goaly)
    print_maze(man_maze)
    reset_maze(maze)

    # Displays the Euclidean maze, number generated via this method, and time it took to calculate it
    print()
    start_time = timeit.default_timer()
    print(euclidean(startx, starty, goalx, goaly))
    end_time = timeit.default_timer()
    print("Elapsed Time:", end_time - start_time)

    euc_maze = make_euc_maze(maze, startx, starty, goalx, goaly)
    print_maze(euc_maze)
    reset_maze(maze)

    # Displays the Chebyshev maze, number generated via this method, and time it took to calculate it
    print()
    start_time = timeit.default_timer()
    print(chebyshev(startx, starty, goalx, goaly))
    end_time = timeit.default_timer()
    print("Elapsed Time:", end_time - start_time)

    cheb_maze = make_cheb_maze(maze, startx, starty, goalx, goaly)
    print_maze(cheb_maze)

main()
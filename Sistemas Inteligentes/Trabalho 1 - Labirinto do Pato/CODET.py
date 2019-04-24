import numpy as np
import math
import sys

class Cell:
    def __init__(self, _i, _j):
        # posição
        self.i = _i
        self.j = _j

        # f, g, and h values for A *
        self.f = 0
        self.g = 0
        self.h = 0

        # Neighbors
        self.neighbors = []

        # Where did I come from?
        self.previous = None

        # AmIawall?
        self.wall = False

        self.neighbors = []








class Agent():
    def __init__(self):
        self.cell = None
        self.dir = 6


if __name__ == '__main__':

    def print_grid():
        for i in range(h):
            for j in range(w):
                if grid[i][j] == agent.cell:
                    print(2,end=' ')
                elif grid[i][j] == objective:
                    print(3,end=' ')
                elif grid[i][j].wall:
                    print(1,end=' ')
                else:
                    print(0, end=' ')
            print()

    def heuristic(a,b):
        return math.sqrt((a.i - b.i) ** 2 + (a.j - b.j) ** 2)



    def gheuristic(agent, neighbor):
        dist = heuristic(agent.cell, neighbor)

        if agent.cell.i < neighbor.i and agent.cell.j == neighbor.j:
            if agent.dir == 2:
                turn_effort = 1
            if agent.dir == 3 or agent.dir == 1:
                turn_effort = 2
            if agent.dir == 4 or agent.dir == 6:
                turn_effort = 3
            if agent.dir == 7 or agent.dir == 9:
                turn_effort = 4
            if agent.dir == 8:
                turn_effort = 5

        if agent.cell.i > neighbor.i and agent.cell.j == neighbor.j:
            if agent.dir == 2:
                turn_effort = 5
            if agent.dir == 3 or agent.dir == 1:
                turn_effort = 4
            if agent.dir == 4 or agent.dir == 6:
                turn_effort = 3
            if agent.dir == 7 or agent.dir == 9:
                turn_effort = 2
            if agent.dir == 8:
                turn_effort = 1

        if agent.cell.i == neighbor.i and agent.cell.j < neighbor.j:
            if agent.dir == 4:
                turn_effort = 5
            if agent.dir == 7 or agent.dir == 1:
                turn_effort = 4
            if agent.dir == 8 or agent.dir == 2:
                turn_effort = 3
            if agent.dir == 3 or agent.dir == 9:
                turn_effort = 2
            if agent.dir == 6:
                turn_effort = 1

        if agent.cell.i == neighbor.i and agent.cell.j > neighbor.j:
            if agent.dir == 4:
                turn_effort = 1
            if agent.dir == 7 or agent.dir == 1:
                turn_effort = 2
            if agent.dir == 8 or agent.dir == 2:
                turn_effort = 3
            if agent.dir == 3 or agent.dir == 9:
                turn_effort = 4
            if agent.dir == 6:
                turn_effort = 5

        if agent.cell.i > neighbor.i and agent.cell.j > neighbor.j:
            if agent.dir == 7:
                turn_effort = 1
            if agent.dir == 8 or agent.dir == 4:
                turn_effort = 2
            if agent.dir == 1 or agent.dir == 9:
                turn_effort = 3
            if agent.dir == 2 or agent.dir == 6:
                turn_effort = 4
            if agent.dir == 3:
                turn_effort = 5

        if agent.cell.i < neighbor.i and agent.cell.j < neighbor.j:
            if agent.dir == 7:
                turn_effort = 5
            if agent.dir == 8 or agent.dir == 4:
                turn_effort = 4
            if agent.dir == 1 or agent.dir == 9:
                turn_effort = 3
            if agent.dir == 2 or agent.dir == 6:
                turn_effort = 2
            if agent.dir == 3:
                turn_effort = 1

        if agent.cell.i > neighbor.i and agent.cell.j < neighbor.j:
            if agent.dir == 1:
                turn_effort = 1
            if agent.dir == 2 or agent.dir == 4:
                turn_effort = 2
            if agent.dir == 7 or agent.dir == 3:
                turn_effort = 3
            if agent.dir == 6 or agent.dir == 8:
                turn_effort = 4
            if agent.dir == 9:
                turn_effort = 5

        if agent.cell.i < neighbor.i and agent.cell.j > neighbor.j:
            if agent.dir == 1:
                turn_effort = 1
            if agent.dir == 2 or agent.dir == 4:
                turn_effort = 2
            if agent.dir == 7 or agent.dir == 3:
                turn_effort = 3
            if agent.dir == 6 or agent.dir == 8:
                turn_effort = 4
            if agent.dir == 9:
                turn_effort = 5

        return dist + turn_effort

    def niggas(cell):
        i = cell.i
        j = cell.j
        if i < h - 1:
            cell.neighbors.append(grid[i + 1][j])

        if i > 0:
            cell.neighbors.append(grid[i - 1][j])

        if j < w - 1:
            cell.neighbors.append(grid[i][j + 1])

        if j > 0:
            cell.neighbors.append(grid[i][j - 1])
        if i > 0 and j > 0:
            cell.neighbors.append(grid[i - 1][j - 1])

        if i < w - 1 and j > 0:
            cell.neighbors.append(grid[i + 1][j - 1])

        if i > 0 and j < h - 1:
            cell.neighbors.append(grid[i - 1][j + 1])

        if i < w - 1 and j < h - 1:
            cell.neighbors.append(grid[i + 1][j + 1])



    filename = 'Env.txt'
    file = open(filename, 'r')
    lines = file.read().splitlines()
    w = int(lines[0])
    h = int(lines[1])
    grid = [[0] * w for i in range(h)]
    agent = Agent()

    path = []

    openSet = []
    closedSet = []

    for i in range(h):
        for j in range(w):
            grid[i][j] = Cell(i,j)

    for i, line in enumerate(lines[2: 2 + h]):
        for j, row in enumerate(list(line)):
            if row == '*':
                grid[i][j].wall = True
            elif row == '>':
                objective = grid[i][j]
            elif row == 'x':
                agent.cell = grid[i][j]

    openSet.append(agent.cell)
    while 1:
        winner = 0
        agent.cell = min(openSet, key=lambda x: x.f)
        if agent.cell == objective:
            print("terminei")
            break


        openSet.remove(agent.cell)
        closedSet.append(agent.cell)

        niggas(agent.cell)

        neighbors = agent.cell.neighbors
        print('[', agent.cell.i, ',', agent.cell.j, ']')
        for neighbor in neighbors:
            if neighbor not in closedSet and not neighbor.wall:
                tempG = agent.cell.g + gheuristic(agent, neighbor)

                newPath = False
                if neighbor in openSet:
                    if tempG < neighbor.g:
                        neighbor.g = tempG
                        newPath = True

                else:
                    neighbor.g = tempG
                    newPath = True
                    openSet.append(neighbor)

                if newPath:
                    neighbor.h = heuristic(neighbor, objective)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = agent.cell

        # print()
        # print('OpenSet:')
        # # [print('[',x.i,',',x.j,']', end=' ') for x in openSet]
        # [print(x.f, end=' ') for x in openSet]
        # print()
        # print('ClosedSet:')
        # [print(x.f, end=' ') for x in closedSet]
        # # [print('[',x.i,',',x.j,']', end=' ') for x in closedSet]


    print_grid()


    temp = agent.cell
    path.append(temp)
    while (temp.previous):
        path.append(temp.previous)
        temp = temp.previous


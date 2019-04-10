from collections import deque

class Grid:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'r')
        self.lines = self.file.read().splitlines()
        self.w = int(self.lines[0])
        self.h = int(self.lines[1])
        self.grid = [[0] * self.w for i in range(self.h)]
        self.blacklisted_pos = []
        self.init_pos = None
        self.objective_pos = None

        for y, line in enumerate(reversed(self.lines[2: 2 + self.h])):
            for x, row in enumerate(list(line)):
                if row == '*':
                    self.grid[y][x] = 1
                    self.blacklisted_pos.append([y, x])
                elif row == '>':
                    self.grid[y][x] = 4
                    self.objective_pos = [y, x]
                elif row == 'x':
                    self.grid[y][x] = 3
                    self.init_pos = [y, x]
                else:
                    self.grid[y][x] = 0


class Agent:

    def __init__(self, pos, blacklisted_pos, objective_pos, w, h):
        self.pos = pos
        self.blacklisted_pos = blacklisted_pos
        self.w = w
        self.h = h
        self.objective_pos = objective_pos
        self.direction = 6
        self.directions = [6, 3, 2, 1, 4, 7, 8, 9]

    def checkpos(self, pos):
        if pos in self.blacklisted_pos:
            return 0
        if pos[0] < 0 or pos[0] >= self.h:
            return 0
        if pos[1] < 0 or pos[1] >= self.w:
            return 0
        else:
            return 1

    def turn(self, direction):
        if direction == 4:
            return self.directions[self.directions.index(self.direction)-1]
        elif direction == 6:
            return self.directions[(self.directions.index(self.direction) + 1) % len(self.directions)]

    def go(self, direction):
        old_pos = self.pos.copy()
        new_pos = self.pos.copy()
        if direction == 8:
            new_pos[0] += 1
        elif direction == 9:
            new_pos[1] += 1
            new_pos[0] += 1
        elif direction == 6:
            new_pos[1] += 1

        elif direction == 3:
            new_pos[1] += 1
            new_pos[0] -= 1

        elif direction == 2:
            new_pos[0] -= 1

        elif direction == 1:
            new_pos[1] -= 1
            new_pos[0] -= 1

        elif direction == 4:
            new_pos[1] -= 1

        elif direction == 7:
            new_pos[1] -= 1
            new_pos[0] += 1
        else:
            print("Wrong Input Try Again!")
            return old_pos
        if self.checkpos(new_pos) == 1:
            return new_pos
        else:
            return old_pos



def bsf():
    options = ['left', 'right', 'move']
    best_route = []
    frontier = deque()
    combo = agent.pos.copy()
    combo.append(agent.direction)
    frontier.append(combo)
    print(frontier)
    while len(frontier):
        agent.pos = frontier[0][0], frontier[0][1]
        agent.direction = frontier[0][2]
        for opt in options:
            if opt == 'left':
                combo[2] = agent.turn(4)
            elif opt == 'right':
                combo[2] = agent.turn(6)
            elif opt == 'move':
                combo[0],combo[1] =





if __name__ == '__main__':

    gridc = Grid('Env.txt')
    grid = gridc.grid

    for line in reversed(grid):
        print(line)

    agent = Agent(gridc.init_pos, gridc.blacklisted_pos, gridc.objective_pos, gridc.w, gridc.h)

    bsf()
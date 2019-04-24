

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

        for y, l in enumerate(reversed(self.lines[2: 2 + self.h])):
            for x, r in enumerate(list(l)):
                if r == '*':
                    self.grid[x][y] = 1
                    self.blacklisted_pos.append([x, y])
                elif r == '>':
                    self.grid[x][y] = 4
                    self.objective_pos = [x, y]
                elif r == 'x':
                    self.grid[x][y] = 3
                    self.init_pos = [x, y]
                else:
                    self.grid[x][y] = 0


class Agent:

    def __init__(self, pos, blacklisted_pos, objective_pos, w, h):
        self.pos = pos  # pos[x][y]
        self.blacklisted_pos = blacklisted_pos
        self.w = w
        self.h = h
        self.objective_pos = objective_pos
        self.direct = [6, 3, 2, 1, 4, 7, 8, 9]

    def checkpos(self, pos):
        if pos in self.blacklisted_pos:
            return 0
        if pos[0] < 0 or pos[0] >= self.w:
            return 0
        if pos[1] < 0 or pos[1] >= self.h:
            return 0
        else:
            return 1



if __name__ == '__main__':
    grido = Grid('Env.txt')
    grid = grido.grid


    print(grid[9][0])
    for x, line in enumerate(reversed(grid)):
        for y, row in enumerate(reversed(line)):
            print(grid[x][], end='')
        print()

    agent = Agent(grido.init_pos, grido.blacklisted_pos, grido.objective_pos, grido.w, grido.h)
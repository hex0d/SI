from collections import deque, defaultdict
from itertools import cycle


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

        '''for line in reversed(self.grid):

            print(line)'''

    def checkpos(self, pos):
        if pos in self.blacklisted_pos:
            return 0
        if pos[0] < 0 or pos[0] >= self.w:
            return 0
        if pos[1] < 0 or pos[1] >= self.h:
            return 0
        else:
            return 1


class Agent:

    def __init__(self, pos, blacklisted_pos, objective_pos, w, h):
        self.pos = pos  # pos[x][y]
        self.blacklisted_pos = blacklisted_pos
        self.w = w
        self.h = h
        self.objective_pos = objective_pos
        self.objective_pos.append(6)

    def checkpos(self, pos):
        if pos in self.blacklisted_pos:
            return 0
        if pos[0] < 0 or pos[0] >= self.h:
            return 0
        if pos[1] < 0 or pos[1] >= self.w:
            return 0
        else:
            return 1

    direct = [6,3,2,1,4,7,8,9]

    def ir(self,x):
        old_pos = self.pos.copy()
        new_pos = self.pos.copy()
        if x == "4":
            new_pos[2] = self.direct[(self.direct.index(new_pos[2])-1)]
        elif x == '6':
            new_pos[2] = self.direct[(self.direct.index(new_pos[2])+1) % len(self.direct)]
        elif x == '8':
            new_pos = self.irpara(str(new_pos[2]))
        else:
            print("Wrong Input Try Again!")
            return old_pos
        if self.checkpos(new_pos) == 1:
            return new_pos
        else:
            return old_pos





    def irpara(self, x):
        old_pos = self.pos.copy()
        new_pos = self.pos.copy()
        if x == 'N' or x == '8':
            new_pos[0] += 1
        elif x == 'NE' or x == '9':
            new_pos[1] += 1
            new_pos[0] += 1
        elif x == 'L' or x == '6':
            new_pos[1] += 1

        elif x == 'SE' or x == '3':
            new_pos[1] += 1
            new_pos[0] -= 1

        elif x == 'S' or x == '2':
            new_pos[0] -= 1

        elif x == 'SO' or x == '1':
            new_pos[1] -= 1
            new_pos[0] -= 1

        elif x == 'O' or x == '4':
            new_pos[1] -= 1

        elif x == 'NO' or x == '7':
            new_pos[1] -= 1
            new_pos[0] += 1
        else:
            print("Wrong Input Try Again!")
            return old_pos
        if self.checkpos(new_pos) == 1:
            return new_pos
        else:
            return old_pos


if __name__ == '__main__':

    gridc = Grid('Env.txt')
    grid = gridc.grid

    for line in reversed(grid):
        print(line)

    agent = Agent(gridc.init_pos, gridc.blacklisted_pos, gridc.objective_pos, gridc.w, gridc.h)

    directions = ['6', '4', '8']  # 6-> turn right / 4-> turn left / 8-> go into dir
    visited = []
    foundby = {}

    agent.pos.append(6)


    def bfs():
        best_route = []
        objective = agent.objective_pos
        objective = str(objective)
        frontier = deque()
        frontier.append(agent.pos)
        while len(frontier) > 0:
            agent.pos = frontier[0]
            for dire in directions:
                new_dir = agent.ir(dire)
                if new_dir != agent.pos and new_dir not in visited and new_dir not in agent.blacklisted_pos:
                    frontier.append(new_dir)
                    visited.append(new_dir)
                    foundby[str(new_dir)] = str(agent.pos)
            if agent.pos == agent.objective_pos:
                break

            print('Current:')
            print(agent.pos)
            print(frontier)
            visited.append(agent.pos)
            frontier.popleft()
        while objective != str(gridc.init_pos):
            objective = foundby[objective]
            best_route.append(objective)
        best_route.insert(0,agent.objective_pos)
        print("best path")
        print(best_route)

    def astar():
        print('Vamos Tentar')


    bfs()

'''    while 1:
        ipt = input('Direção')
        old_pos = agent.pos
        new_pos = agent.ir(ipt)
        agent.pos = new_pos
        grid[old_pos[0]][old_pos[1]] = 0
        grid[new_pos[0]][new_pos[1]] = 3
        for line in reversed(grid):
            print(line)'''
'''    if agent.pos == agent.objective_pos:
        print("you win!")
        break
'''



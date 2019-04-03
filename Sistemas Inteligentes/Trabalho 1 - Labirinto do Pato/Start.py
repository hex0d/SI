
class Agent:

    def __init__(self, pos, blacklisted_pos, w, h):
        self.pos = pos  # pos[x][y]
        self.blacklisted_pos = blacklisted_pos
        self.w = w
        self.h = h

    def checkpos(self, pos):
        if pos in self.blacklisted_pos:
            return 0
        if pos[0] < 0 or pos[0] >= self.w:
            return 0
        if pos[1] < 0 or pos[1] >= self.h:
            return 0
        else:
            return 1

    def get_pos(self):
        return self.pos

    def ir(self, x):
        old_pos = self.pos.copy()
        new_pos = self.pos.copy()
        if x == 'N':
            new_pos[1] += 1
        elif x == 'NE':
            new_pos[0] += 1
            new_pos[1] += 1
        elif x == 'L':
            new_pos[0] += 1

        elif x == 'SE':
            new_pos[0] += 1
            new_pos[1] -= 1

        elif x == 'S':
            new_pos[1] -= 1

        elif x == 'SO':
            new_pos[0] -= 1
            new_pos[1] -= 1

        elif x == 'O':
            new_pos[0] -= 1

        elif x == 'NO':
            new_pos[0] -= 1
            new_pos[1] += 1
        else:
            print("Wrong Input Try Again!")
            return old_pos
        if self.checkpos(new_pos) == 1:
            return new_pos
        else:
            return old_pos


class Grid:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'r')
        self.lines = self.file.readlines()
        self.w = int(self.lines[0])
        self.h = int(self.lines[1])
        self.lines_list = []
        for line in reversed(self.lines[2:2+self.h]):
            self.lines_list.append(list(line))
        self.start_pos = self.find_pos(self.lines_list, 'x')[0]
        self.blacklisted_pos = self.find_pos(self.lines_list, '*')
        self.objective_pos = self.find_pos(self.lines_list, '>')[0]

    @staticmethod
    def find_pos(my_list, item):
        places = []
        for i, x in enumerate(my_list):
            for j, y in enumerate(x):
                if y == item:
                    places.append([j, i])
        return places

    def print(self):
        for line in reversed(self.lines_list):
            for char in line:
                if char == '.':
                    print('O ', end='')
                elif char == '*':
                    print('X ', end='')
                elif char == '>':
                    print('T ', end='')
                elif char == 'x':
                    print('A ', end='')
                elif char == 'j':
                    print('J ', end='')
                else:
                    print(char, end='')


class AI:
    def __init__(self, grid):
        self.grid = grid




if __name__ == '__main__':

    grid = Grid('Env.txt')
    agent = Agent(grid.start_pos, grid.blacklisted_pos, grid.w, grid.h)


    while 1:
        grid.print()
        ipt = input('Direção')
        old_pos = agent.pos
        new_pos = agent.ir(ipt)
        agent.pos = new_pos
        grid.lines_list[old_pos[1]][old_pos[0]] = '.'
        grid.lines_list[new_pos[1]][new_pos[0]] = 'x'
        if agent.pos == grid.objective_pos:
            print("you win!")
            break

   a=   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        [0, 1, 4, 0, 0, 0, 1, 0, 1, 0]
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        [0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 0]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        [0, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3]



'''implementar
uma
busca
pouco
inteligente
(que ele mostrou na aula)

implemente
a - estrela'''
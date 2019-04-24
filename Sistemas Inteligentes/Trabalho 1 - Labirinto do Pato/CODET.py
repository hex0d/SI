# Esse algorítimo precisou ser feito de maneira diferente dos demais, eu não estava conseguindo pensar no grid invertido, portanto eu acabei fazendo com
# um orientação igual a de manipulação de amtrizer com y e x crescendo para sudeste
# Tive que recriar cada espaço do grid sendo uma cécula para guardar informações de f,g,h  e de deus vizinhos
# e mais alguma coisas foram feitas diferentes estão comentadas no código
#
#
# Tive alguns problemas para fazer esse, acabei escolhendo uma herística péssima e um modo de resolver o problema ficou bem abaixo do esperado, 
# para futuros projetos pretendo melhorar alguns quesitos de modularidade e encontrar soluções melhores pra alguns problemas que tive.
#
#
#
#


import numpy as np
import math
import sys

#Classe de célula, cada ponto no grid será uma célula
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




#Agente contendo a celula que esta presente e sua direção
class Agent():
    def __init__(self):
        self.cell = None
        self.dir = 6


if __name__ == '__main__':
    #função que printa o grid
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

    #calcula a distância entre a e b
    def heuristic(a,b):
        return math.sqrt((a.i - b.i) ** 2 + (a.j - b.j) ** 2)

    # Calcula a direção para qual o agente deve se virar para ir do bloco agente ao bloco neighbor
    def relative_pos(agent,neighbor):

        if agent.cell.i < neighbor.i and agent.cell.j == neighbor.j:
            return 2

        if agent.cell.i > neighbor.i and agent.cell.j == neighbor.j:
            return 8

        if agent.cell.i == neighbor.i and agent.cell.j < neighbor.j:
            return 6

        if agent.cell.i == neighbor.i and agent.cell.j > neighbor.j:
            return 4

        if agent.cell.i > neighbor.i and agent.cell.j > neighbor.j:
            return 7

        if agent.cell.i < neighbor.i and agent.cell.j < neighbor.j:
            return 3

        if agent.cell.i > neighbor.i and agent.cell.j < neighbor.j:
            return 9

        if agent.cell.i < neighbor.i and agent.cell.j > neighbor.j:
            return 1
        else:
            return 0




    #A eurística de G eu calculei a partir de o quão custoso é para ele se virar e andar até cada vizinho e a distancia do inicio até ele
    #e depois atribui a G da célula do vizinho
    def gheuristic(agent, neighbor):
        dist = heuristic(init_cell, neighbor)
        turn_effort = 0
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
                turn_effort = 5
            if agent.dir == 2 or agent.dir == 4:
                turn_effort = 4
            if agent.dir == 7 or agent.dir == 3:
                turn_effort = 3
            if agent.dir == 6 or agent.dir == 8:
                turn_effort = 2
            if agent.dir == 9:
                turn_effort = 1

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


    #Acha os vizinhos para a celula
    def neibos(cell):
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


    #inicialização
    filename = 'Env.txt'
    file = open(filename, 'r')
    lines = file.read().splitlines()
    w = int(lines[0])
    h = int(lines[1])
    grid = [[0] * w for i in range(h)]

    #agente
    agent = Agent()

    #caminho final
    path = []

    #lugares a visitar e ja visitados
    openSet = []
    closedSet = []

    #cria grid
    for i in range(h):
        for j in range(w):
            grid[i][j] = Cell(i,j)

    #pega dados a partir do arquivo
    for i, line in enumerate(lines[2: 2 + h]):
        for j, row in enumerate(list(line)):
            if row == '*':
                grid[i][j].wall = True
            elif row == '>':
                objective = grid[i][j]
            elif row == 'x':
                init_cell = grid[i][j]
                agent.cell = grid[i][j]

    #coemça a busca
    openSet.append(agent.cell)
    while 1:
        winner = min(openSet, key=lambda x: x.f) #acha o melhor f
        rp = relative_pos(agent, winner) #acha a posição relativa entre o melhor - lembrando que o calculo de esforço já está na heuristica
        agent.cell = winner #vai pra melhoor celula
        agent.dir = rp #se vira para a melhor celula
        if agent.cell == objective: #caso encontre o objetivo
            print("terminei")
            break


        openSet.remove(agent.cell)
        closedSet.append(agent.cell)

        neibos(agent.cell) #acha os vizinhos

        neighbors = agent.cell.neighbors 
        print('Visistando: ','[', agent.cell.i, ',', agent.cell.j, ']')
        
        #atualiza a melhor rota e os melhores valores para cara vizinho
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




    temp = agent.cell
    path.append(temp)
    while (temp.previous):
        path.append(temp.previous)
        temp = temp.previous
    print('Melhor Caminho: ')
    [print('[',x.i,',',x.j,']', end=' ') for x in path]


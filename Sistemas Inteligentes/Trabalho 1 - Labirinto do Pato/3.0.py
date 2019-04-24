# OBS: A Orientação da posição está como [y,x, dir] em que a direção é referente a qual lado ele está "olhando" Sendo que podem assumir valores:
# 1,2,3,6,9,8,7,4 - Sendo respectivamente para a direção que os numeros no Numpad(Teclado numérico) apontam: EX: 7 == NO , 8 == N , 3 == SE.
# o grid grece x e y para o nordeste
#

from collections import deque #import para conseguir retirar do começa da lista de maneira mais rápida
import math

class Agent:

    def __init__(self, pos, blacklisted_pos, objective_pos, w, h):

        self.pos = pos  # pos[y][x]

        self.blacklisted_pos = blacklisted_pos # Lista de Paredes

        self.w = w
        self.h = h

        self.objective_pos = objective_pos
        self.objective_pos.append(6)

    # método para checar se ele bateu em parede ou saiu dos limites
    def checkpos(self, pos):
        if pos in self.blacklisted_pos:
            return 0
        if pos[0] < 0 or pos[0] >= self.h:
            return 0
        if pos[1] < 0 or pos[1] >= self.w:
            return 0
        else:
            return 1

    direct = [6,3,2,1,4,7,8,9] # lista de todas as direções para qual ele pode apontar (Ver comentário no inicio do código)

    # método para girar o agente ou movê-lo para a direção apontada
    def ir(self,x):
        old_pos = self.pos.copy()
        new_pos = self.pos.copy()
        if x == '4':
            new_pos[2] = self.direct[(self.direct.index(new_pos[2])-1)]
        elif x == '6':
            new_pos[2] = self.direct[(self.direct.index(new_pos[2])+1) % len(self.direct)]
        elif x == '8':
            new_pos = self.irpara(str(new_pos[2]))
        else:
            print("Wrong Input Try Again!")
            print("Wrong Input Try Again!")
            return old_pos
        if self.checkpos(new_pos) == 1:
            return new_pos
        else:
            return old_pos

    # método para mover agente para a direção apontada
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


class Grid:
    def __init__(self, filename):

        #      construção do grid
        self.filename = filename
        self.file = open(self.filename, 'r')
        self.lines = self.file.read().splitlines()
        self.w = int(self.lines[0])
        self.h = int(self.lines[1])
        self.grid = [[0] * self.w for i in range(self.h)]

        # Lugares "Paredes"
        self.blacklisted_pos = []

        # Posição Inicial e Final
        self.init_pos = None
        self.objective_pos = None

        # Populando o grid
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


def bfs():  # Método de Busca em largura    
    best_route = [] #Guarda melhor rota 
    objective = agent.objective_pos 
    objective = str(objective)
    frontier = deque() 
    frontier.append(agent.pos) #fila 
    while len(frontier) > 0: 
        agent.pos = frontier[0]
        for dire in directions: # Testa todas as direções que pode tomar | Virar esquerda/direita - Ir pra frente
            new_dir = agent.ir(dire) 
            if new_dir != agent.pos and new_dir not in visited and new_dir not in agent.blacklisted_pos: #guarda a nova tripla de posição contendo (y,x,direcao) <Ler Sobre direção no começo do codigo>
                frontier.append(new_dir) #colcoa na fila
                visited.append(new_dir) #marca como visitado a posição nova
                foundby[str(new_dir)] = str(agent.pos) #indica quem é o "pai" dela
        if agent.pos == agent.objective_pos: #se chegar no objetivo para a execução
            break
        print()
        print('Current:') 
        print('Posição: ',str(agent.pos)) #printa a posição atual do agente [y,x,direcao] <Ler Sobre direção no começo do codigo>
        print("Fila: ", str(frontier)) #printa a fila a ser executada
        print()

        visited.append(agent.pos) # marca a posição que vai sair como visitado
        frontier.popleft() # tira a atual da fila

    # Quando terminar faz o Traceback do caminho encontrado como melhor - Formato: [y,x,direção]  <Ler Sobre direção no começo do codigo>
    while objective != str(gridc.init_pos):
        objective = foundby[objective]
        best_route.append(objective)
    best_route.insert(0,agent.objective_pos)
    print("Melhor Caminho:", str(best_route))
    print()








if __name__ == '__main__':

    gridc = Grid('Env.txt')
    grid = gridc.grid

    agent = Agent(gridc.init_pos, gridc.blacklisted_pos, gridc.objective_pos, gridc.w, gridc.h)

    directions = ['6', '4', '8']  # 6-> turn right / 4-> turn left / 8-> go into dir
    visited = []
    foundby = {}

    values_grid = [[0] * agent.w for i in range(agent.h)]

    agent.pos.append(6)


    bfs()


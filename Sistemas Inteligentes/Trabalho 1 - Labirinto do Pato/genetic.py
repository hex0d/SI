# OBS: A Orientação da posição está como (y,x, dir) em que a direção é referente a qual lado ele está "olhando" Sendo que podem assumir valores:
# 1,2,3,6,9,8,7,4 - Sendo respectivamente para a direção que os numeros no Numpad(Teclado numérico) apontam: EX: 7 == NO , 8 == N , 3 == SE.
# o grid grece x e y para o nordeste
# O Algorítimo consiste em criar uma população de agentes com tamanho "popsize" e gerar uma lista de movimentos de tamanho "lifespan"
# Após cada agente da população andar, é medido seu fitnes (Raw Distance - Distância entre o agente e o objetivo)
# Então são selecionados os "elite" % melhores para manterem iguais
# os "crossovered" % para serem cruzados os dados genéticos entre eles
# e por fim os "newcomers" % contendo um agente totalmente novo
# Após tudo isso ainda tem uma efeito de mutação aletório em que os "mutation_rate" % são modificados entre todos os agentes incluindo os elite
# as vezes com mutação alta e numero de população baixa o fitness pode reduzir

import math
import random



popsize = 100 # tamanho da população
lifespan = 15 # numero de movimentos
halfpop = popsize/2

# lista de todos movimentos possíveis
movment_pool = ['4','8','6']

# garanta que a soma de elite + crossovered + newcomers = 1, caso contrário a população cresce/decresce indefinidamente
elite = popsize * 0.05 # salva os 5% melhores
crossovered = popsize * 0.8 # 80% da população vai ser de crossover dos elites
newcomers = popsize * 0.15 # 15% da nova pop vai ser totalmente nova

# taxa de mutação
mutation_rate = 0.25 # 25%


# inicializa grid a partir do arquivo. (Igual de Busca "Burra")
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


class Agent:
    def __init__(self, pos, blacklisted_pos, objective_pos, w, h):

        self.completed = False # Se ele chegou ao objetivo ou não

        self.fitness = 0 # Quao adequado ao problema ele está

        self.dna = random.choices(movment_pool,k=lifespan) # cria vetor de comandos aleatório

        self.pos = pos  # pos[y][x]
        
        self.objective_pos = objective_pos # Posição do objetivo

        self.blacklisted_pos = blacklisted_pos # Lista de Paredes

        self.w = w
        self.h = h


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
            self.pos = old_pos
        if self.checkpos(new_pos) == 1:
            self.pos = new_pos
        else:
            self.pos = old_pos

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
    

    # método para calcular o fitness dele com base apenas na distancia
    def calc_fitness(self):
        dist = math.sqrt((self.pos[0] - self.objective_pos[0])**2+(self.pos[1] - self.objective_pos[1])**2)
        
        if dist:
            self.fitness = 1/dist
        else:
            self.fitness += 1 # se chegou no objetivo aumenta seu fitness
    
    # método que percorre a lista de comando movendo o agente pelo grid
    def move(self):
        for move in self.dna:
            if not self.pos == self.objective_pos:
                self.ir(move)
            else:
                self.completed = True

    







#classe de população crianto uma array de "popsize" agentes
class Population:
    def __init__(self, gridc):

        self.agents = []

        for _ in range(popsize):
            a = gridc.init_pos.copy()
            a.append(6)
            b = gridc.objective_pos.copy()
            b.append(6)
            self.agents.append(Agent(a, gridc.blacklisted_pos, b, gridc.w, gridc.h))
        
            
if __name__ == "__main__":

    def generate_dna():
        return random.choices(movment_pool,k=lifespan) # gera lista aleatória de movimentos

    # def crossover(parent1,parent2): # realzia o crossover pegando metade das informações dos pais
    #     newgenes = parent1.dna[:int(halfpop)] # pega a primeira metade
    #     newgenes.append(parent2.dna[int(halfpop):]) #pega e sengunda metade
    #     return newgenes
    
    def crossover(parent1, parent2): #realiza crossover pegando cada indice de mandeira aleatória de cada pai
        newgenes = []
        parentone = True
        for i in range(lifespan):
            parentone = bool(random.getrandbits(1))
            if parentone:
                newgenes.append( parent1.dna[i] )
            else:
                newgenes.append( parent2.dna[i] )
        return newgenes


    gridc = Grid('Env.txt')
    grid = gridc.grid

    pop = Population(gridc)

    champions = [] #agentes que conseguiram chegar no fim
    
    while 1:
        for agent in pop.agents: #faz cada agente se mover e calcular o fitness
            agent.move()
            agent.calc_fitness()
            if agent.fitness > 1:
                champions.append(agent)
            # print(agent.dna)
            # print(agent.pos)
            # print(agent.fitness)
        
        # print(pop.agents[0].dna)
        # print(pop.agents[0].pos)
        # print(pop.agents[0].fitness)

        def takeFitness(agent):
            return agent.fitness

        sorted_agents = sorted(pop.agents, key=takeFitness, reverse=True) # faz um sort por fitness com maior no i=0

        new_pop_agents = []
        a = gridc.init_pos.copy()
        a.append(6) #posição inicial de todos
        b = gridc.objective_pos.copy()
        b.append(6) #posição objetivo de todos

        # Mantém os elite
        for i in range(int(elite)):
            new_agent = Agent(a, gridc.blacklisted_pos, b, gridc.w, gridc.h)
            new_agent.dna = sorted_agents[i].dna
            new_agent.fitness = sorted_agents[i].fitness
            new_pop_agents.append(new_agent)
        # Gera novos a partir de crossover há 2 funções que podem ser comentadas e descomentadas
        for i in range(int(crossovered)):
            new_agent = Agent(a, gridc.blacklisted_pos, b, gridc.w, gridc.h)
            csv = crossover(sorted_agents[i],sorted_agents[i+2])
            new_agent.dna = csv
            new_pop_agents.append(new_agent)
        #gera novos agentes
        for _ in range(int(newcomers)):
            new_agent = Agent(a, gridc.blacklisted_pos, b, gridc.w, gridc.h)
            new_agent.dna = generate_dna()
            new_pop_agents.append(new_agent)
        # Mutação aleatórioa
        for agent in new_pop_agents:
            if random.random() < mutation_rate:
                agent.dna = generate_dna()
        

        pop.agents = new_pop_agents

       
        
        print("Best Fitness: ", str(sorted_agents[0].fitness))
        print("Best DNA:", str(sorted_agents[0].dna))
        print("Best Position:", str(sorted_agents[0].pos))
        print("Champions:", str(champions))
        print()
        input("Pressione Enter Para Iniciar a proxima geracao")








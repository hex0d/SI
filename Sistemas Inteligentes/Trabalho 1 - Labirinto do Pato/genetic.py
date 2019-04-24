import math
import random



popsize = 100 # tamanho da população
lifespan = 20 # numero de movimentos
halfpop = popsize/2
movment_pool = ['4','8','6']
elite = popsize * 0.15 # salva os 15% melhores
crossovered = popsize * 0.7 # 70% da população vai ser de crossover dos elites
newcomers = popsize * 0.15 # 15% da nova pop vai ser totalmente nova
mutation_rate = .15 # 15%

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
        self.completed = False
        self.fitness = 0
        self.dna = random.choices(movment_pool,k=lifespan)
        self.pos = pos  # pos[x][y]
        self.blacklisted_pos = blacklisted_pos
        self.w = w
        self.h = h
        self.objective_pos = objective_pos


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
    
    def calc_fitness(self):
        dist = math.sqrt((self.pos[0] - self.objective_pos[0])**2+(self.pos[1] - self.objective_pos[1])**2)
        
        if dist:
            self.fitness = 1/dist
        else:
            self.fitness = 10
    
    def move(self):
        for move in self.dna:
            if not self.pos == self.objective_pos:
                self.ir(move)

    







class Population:
    def __init__(self, gridc):

        self.agents = []

        for i in range(popsize):
            a = gridc.init_pos.copy()
            a.append(6)
            b = gridc.objective_pos.copy()
            b.append(6)
            self.agents.append(Agent(a, gridc.blacklisted_pos, b, gridc.w, gridc.h))
        
            
if __name__ == "__main__":

    def generate_dna():
        return random.choices(movment_pool,k=lifespan) # gera lista aleatória de movimentos

    def crossover(parent1,parent2):
        newgenes = parent1.dna[:int(halfpop)]
        newgenes.append(parent2.dna[int(halfpop):])
        return newgenes

    gridc = Grid('Env.txt')
    grid = gridc.grid

    pop = Population(gridc)
    
    while 1:
        for agent in pop.agents:
            agent.move()
            agent.calc_fitness()
            print(agent.pos)
            print(agent.fitness)

        def takeFitness(agent):
            return agent.fitness

        sorted_agents = sorted(pop.agents, key=takeFitness, reverse=True)

        new_pop_agents = []
        a = gridc.init_pos.copy()
        a.append(6)
        b = gridc.objective_pos.copy()
        b.append(6)
        for i in range(int(elite)):
            new_agent = Agent(a, gridc.blacklisted_pos, b, gridc.w, gridc.h)
            new_agent.dna = sorted_agents[i].dna
            new_pop_agents.append(new_agent)
        for i in range(int(crossovered)):
            new_agent = Agent(a, gridc.blacklisted_pos, b, gridc.w, gridc.h)
            csv = crossover(sorted_agents[i],sorted_agents[i+2])
            csv.pop()
            new_agent.dna = csv
            new_pop_agents.append(new_agent)
        for _ in range(int(newcomers)):
            new_agent = Agent(a, gridc.blacklisted_pos, b, gridc.w, gridc.h)
            new_agent.dna = generate_dna()
            new_pop_agents.append(new_agent)

        for agent in new_pop_agents:
            if random.random() < mutation_rate:
                agent.dna = generate_dna()
            print (agent.dna)
        


        pop.agents = new_pop_agents

       
        
        print("Best Fitness: ",str(sorted_agents[0].fitness))
        input("Pressione Enter Para Iniciar a proxima geracao")








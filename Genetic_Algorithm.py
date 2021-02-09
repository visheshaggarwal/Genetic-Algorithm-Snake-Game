from run_game_with_ml import *
from random import choice, randint

def cal_pop_fitness(pop):

    fitness = []
    score = []
    for i in range(pop.shape[0]):
        fit, sc = run_game_with_ml(display,clock,pop[i])
        print('fitness value of chromosome '+ str(i) +' :  ', fit, "score: ", sc)
        fitness.append(fit)
        score.append(sc)
    return np.array(fitness), np.array(score)

def select_mating_pool(pop, fitness, num_parents):
    
    # parents = np.empty((num_parents, pop.shape[1]))
    parents = []
    parents_fitness = []
    # print(pop[0, :])
    for parent_num in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents_fitness.append(np.max(fitness))
        
        parents.append(pop[max_fitness_idx, :])
        fitness[max_fitness_idx] = -99999999
    return np.array(parents), parents_fitness

def getParentIndex(cummFitness, random_value):
    i = -1
    for value in cummFitness:
        if value < random_value:
            i += 1
        else:
            return i

def uniformCrossover(parents, offspring_size, fitness):
    offspring = np.zeros(offspring_size)
    
    cummFitness = []
    cummFitness.append(fitness[0])
    for i in range(1,len(fitness)):
        cummFitness.append(cummFitness[i-1] + fitness[i])
    
    cummFitness = cummFitness/np.max(cummFitness)

    for k in range(offspring_size[0]): 
        
        random_value = random.uniform(0, 1)
        parent1_idx = getParentIndex(cummFitness, random_value)

        while True:
            random_value = random.uniform(0, 1)
            parent2_idx = getParentIndex(cummFitness, random_value)

            if parent1_idx != parent2_idx:
                for j in range(offspring_size[1]):
                    if random.uniform(0, 1) < 0.5:
                        offspring[k][j] = parents[parent1_idx][j]
                    else:
                        offspring[k][j] = parents[parent2_idx][j]
                break
    return offspring


def mutation(offspring_crossover):
    
    for idx in range(offspring_crossover.shape[0]):
        for _ in range(25):
            i = randint(0,offspring_crossover.shape[1]-1)

        random_value = np.random.choice(np.arange(-1,1,step=0.001),size=(1),replace=False)
        offspring_crossover[idx, i] = offspring_crossover[idx, i] + random_value

    return offspring_crossover
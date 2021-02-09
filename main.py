from Genetic_Algorithm import *
from Snake_Game import *
from test import *

# n_x -> no. of input units
# n_h -> no. of units in hidden layer 1
# n_h2 -> no. of units in hidden layer 2
# n_y -> no. of output units

# The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
sol_per_pop = 75
num_weights = n_x*n_h + n_h*n_y

# Defining the population size.
pop_size = (sol_per_pop,num_weights)
#Creating the initial population.

# new_population = np.random.choice(np.arange(-1,1,step=0.01),size=pop_size,replace=True)
new_population = load()

num_generations = 68

num_parents_mating = 20

for generation in range(num_generations):

    print('##############        GENERATION ' + str(12+generation)+ '  ###############' )
    
    fitness, score = cal_pop_fitness(new_population)
    print('#######  fittest chromosome in gneneration ' + str(12+generation) +' is having fitness value:  ', np.max(fitness))
    # # print(fitness)
    f = open("basicBarrier/uniformCrossover/gen_"+str(12+generation), 'w+')
    for weight in new_population:
        f.write("{}".format(weight))
    f.close()

    maxFitnessIndex = np.argmax(fitness)
    f = open("basicBarrier/uniformCrossover/gen_"+str(12+generation)+"_best", 'w+')
    f.write("{}, {}, {}, {}, {}".format(new_population[maxFitnessIndex], np.max(fitness), np.sum(fitness)/sol_per_pop, np.max(score), np.sum(score)/sol_per_pop))
    f.close()


    parents, parents_fitness = select_mating_pool(new_population, fitness, num_parents_mating)
    print(parents.shape)
    
    offspring_crossover = uniformCrossover(parents, (pop_size[0] - parents.shape[0], num_weights), parents_fitness)

    
    offspring_mutation = mutation(offspring_crossover)

    
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation


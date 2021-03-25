import random

def number_of_visited_positions(visited):
	result = 0
	for i in range(len(visited)):
		result += sum(visited[i])
	return result

def tournament_winner(population):
	participants = []
	for i in range(tournament_group_size):
		participants.append(population[random.randint(0, len(population)-1)])
	return max(participants, key=lambda x: x[1])[0]

def crossover_chromosomes(chromosome1, chromosome2):
	crossover_index = random.randint(0,path_length - 1)
	return chromosome1[:crossover_index] + chromosome2[crossover_index:], \
		chromosome2[:crossover_index] + chromosome1[crossover_index:]

def crossover_and_mutate_population(population):
	new_population = []
	for i in range(population_size // 2):
		chromosome1 = tournament_winner(population)
		chromosome2 = tournament_winner(population)
		for chromosome in crossover_chromosomes(chromosome1, chromosome2):
			chromosome = mutate_chromosome(chromosome)
			new_population.append((chromosome,check_fitness(chromosome)))
	return new_population

def mutate_chromosome(chromosome):
	if random.randint(0,1) == 1:
		mutation_index = random.randint(0,path_length - 1)
		chromosome = list(chromosome)
		chromosome[mutation_index] = move[random.randint(0,3)]
		chromosome = ''.join(chromosome)
	return chromosome

def check_fitness(chromosome):
	visited = [[0 for i in range(n)] for j in range(m)]
	position_y = 0
	position_x = 0
	visited[position_y][position_x] = 1
	for gene in chromosome:
		if 	gene == 'u':
			position_y -= 1
			if position_y >= 0:
				visited[position_y][position_x] = 1
			else:
				break
		elif gene == 'd':
			position_y += 1
			if position_y <= m-1:
				visited[position_y][position_x] = 1
			else:
				break
		elif gene == 'l':
			position_x -= 1
			if position_x >= 0:
				visited[position_y][position_x] = 1
			else:
				break
		elif gene == 'r':
			position_x += 1
			if position_x <= n-1:
				visited[position_y][position_x] = 1
			else:
				break

	return number_of_visited_positions(visited)


n, m = 5,5
move = ['u', 'd', 'l','r']
path_length = n * m - 1
fitness_value = path_length + 1
population_size = 10000
tournament_group_size = 2
population = []

for i in range(population_size):
	chromosome = ""
	for j in range(path_length):
		chromosome += move[random.randint(0,3)]
	population.append((chromosome,check_fitness(chromosome)))

for i in range(10**4):
	if max(population, key=lambda x: x[1])[1] == fitness_value:
		print("SOLUTION FOUND")
		print(max(population, key=lambda x: x[1])[0])
		break

	population = crossover_and_mutate_population(population)
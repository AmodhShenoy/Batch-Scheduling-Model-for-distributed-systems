import random
import math 

def get_time_vec(sol,etc):
	time_vec = [0 for _ in range(len(etc))]
	for i in range(len(sol)):
		time_vec[sol[i]] += etc[sol[i]][i]
	return time_vec

def makespan(sol):
	return max(get_time_vec(sol,etc))

def utilization(sol,etc):
	m = len(etc)
	time_vec = get_time_vec(sol,etc)
	mspan = max(time_vec)
	mpat = sum(time_vec)/m
	return mpat/mspan

def reset(pop):
	for i in pop:
			i.pop(-1)
	return pop

#for GA
def calcAndSort(pop,etc):
	for i in pop:
			i.append(makespan(i))
		
	pop.sort(key=lambda x:x[-1])
	return pop

def p(pop):
	for i in pop:
		print(i)

def GA(pop,etc):
	m = len(etc)
	n = len(etc[0])
	genes="01234"
	newgen=[]
	count=1

	while count!=len(newgen):
		newgen=[]
		
		#generation of makespan for each solution and then sorting(asc)
		pop=calcAndSort(pop,etc)

		#selection
		selected=math.ceil(len(pop)/2)
		pop=pop[:selected]

		pop=reset(pop)

		#crossover
		for _ in range(m*2):
			parent1=random.choice(pop)
			parent2=random.choice(pop)
			cp1=random.randint(0,n-1)
			cp2=random.randint(0,n-1)
			maxCp=max(cp1,cp2)
			minCp=min(cp1,cp2)
			child1=parent1[:minCp]+parent2[minCp:maxCp]+parent1[maxCp:]
			#mutation
			mpoint=random.randint(0,n-1)
			child1[mpoint]=int(random.choice(genes))
			child2=parent2[:minCp]+parent1[minCp:maxCp]+parent2[maxCp:]
			newgen.extend([child1,child2])

		select=len(newgen)-(count-1)
		newgen=newgen[:select]
		pop.extend(newgen)
		count+=1
	
	
	return pop[0]

def mkspn_sort(elem):
	return elem[-1]

def BFO(pop,etc):
	#Setting algorithm constraints
	m = len(etc)
	n = len(etc[0])
	S = len(pop)
	ned = 500	#no of elimination steps
	nc  = 10	#no of chemotaxis steps
	ped = 0.2	#probability of bacteria elimination

	for df in range(ned):
		for i in range(len(pop)):
			#tumble and move			
			for _ in range(nc):
				time_vec = get_time_vec(pop[i],etc)
				max_node = time_vec.index(max(time_vec))
				min_node = time_vec.index(min(time_vec))
				tasks = []
				for k in range(n):
					if pop[i][k] == max_node:
						tasks.append(k)

				tumbler = tasks[0]
				for t in tasks:
					if etc[max_node][t]<etc[max_node][tumbler]:
						tumbler = t
				pop[i][tumbler] = min_node
		pop.sort(key = makespan)

		#reproduce
		pop = pop[:int(math.ceil(len(pop)/2))] + pop[:int(math.ceil(len(pop)/2))]
		random.shuffle(pop)

		#eliminate and replace
		ct = int(len(pop)*ped)
		for _ in range(ct):
			pop.pop(int(random.random()*len(pop)))

		for _ in range(ct):
			l = []
			for _ in range(len(pop[0])):
				l.append(int(random.random()*m))
			pop.append(l)
	pop.sort(key=makespan)
	return pop[0][:-1]



def main():
	#loading the speed vector
	node_file = open('input/nodes')
	mips = list(map(float,node_file.read().strip().split(',')))
	m = len(mips)

	#loading the task sizes
	task_file = open('input/tasks')
	mi = list(map(float,task_file.read().strip().split(',')))
	n = len(mi)

	#generating the ETC Matrix
	global etc
	etc = [[0 for _ in range(n)] for _ in range(m)]
	for i in range(m):
		for j in range(n):
			etc[i][j] = mi[j]/mips[i]

	#generating population
	S = m*2
	pop = []
	for _ in range(S):
		l=[]
		for _ in range(n):
			l.append(int(random.random()*m))
		pop.append(l)

	pop.sort(key=makespan)
	print("Initial makespan:",makespan(pop[0]),"\n")
	#running BFO algorithm
	sol_bfo = BFO(pop,etc)
	print("Solution from BFO algorithm:")
	print(sol_bfo)
	print("Makespan:",makespan(sol_bfo))
	print("Utilization:",utilization(sol_bfo,etc),"\n")

	# #running GA algorithm
	sol_ga = GA(pop,etc)
	print("Solution from GA algorithm:")
	print(sol_ga)
	print("Makespan:",makespan(sol_ga))
	print("Utilization:",utilization(sol_ga,etc),"\n")

if __name__=='__main__':
	main()
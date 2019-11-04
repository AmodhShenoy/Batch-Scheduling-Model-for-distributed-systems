import random
import math 

def get_time_vec(sol,etc):
	time_vec = [0 for _ in range(len(etc))]
	for i in range(len(sol)):
		time_vec[sol[i]] += etc[sol[i]][i]
	return time_vec

def makespan(sol,etc):
	return max(get_time_vec(sol,etc))

def utilization(sol,etc):
	time_vec = get_time_vec(sol,etc)
	mspan = max(time_vec)
	mpat = sum(time_vec)/m
	return mpat/mspan

#for GA
def reset(pop):
	for i in pop:
			i.pop(-1)
	return pop

#for GA
def calcAndSort(pop,etc):
	for i in pop:
			i.append(makespan(i,etc))
		
	pop.sort(key=lambda x:x[-1])
	return pop

def p(pop):
	for i in pop:
		print(i)

def GA(pop,etc,n,m):
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
	
	pop[0].append(makespan(pop[0],etc))
	return pop[0]

def mkspn_sort(elem):
	return elem[-1]

def BFO(pop,etc):
	#Setting algorithm constraints
	m = len(etc)
	n = len(etc[0])
	S = len(pop)
	ned = 3 		#no of elimination steps
	nc  = 3			#no of chemotaxis steps
	ped = 0.5		#probability of bacteria elimination

	for _ in range(ned):
		
		for i in range(len(pop)):
			#tumble and move
			for _ in range(nc):
				print(pop[i])
				time_vec = get_time_vec(pop[i],etc)
				max_node = time_vec.index(max(time_vec))
				min_node = time_vec.index(min(time_vec))
				tasks = []
				for i in pop[i]:
					if i==max_node:
						tasks.append(i)
				tumbler = tasks[0]
				for t in tasks:
					if etc[max_node][t]<etc[max_node][tumbler]:
						tumbler = t
				pop[i][tumbler] = min_node
			pop[i].append(makespan(pop[i],etc))
		pop.sort(key=mkspn_sort)
		for i in range(len(pop)):
			pop[i].pop()

		#reproduce
		step = math.ceil(len(pop)/2)
		for i in range(step,len(pop)):
			pop[i] = pop[i-step]
		random.shuffle(pop)
		
		#eliminate and replace
		for _ in range(int(len(pop)*ped)):
			pop.pop(int(random.random()*len(pop)))
		for _ in range(int(len(pop)*ped)):
			l = []
			for _ in range(len(pop[0])):
				l.append(int(random.random()*m))

	for i in range(len(pop)):
		pop[i].append(makespan(pop[i],etc))

	pop.sort(key=mkspn_sort)
	return pop[0][:-1]



def main():
	#loading the speed vector
	node_file = open('nodes')
	mips = list(map(float,node_file.read().strip().split(',')))
	m = len(mips)

	#loading the task sizes
	task_file = open('tasks')
	mi = list(map(float,task_file.read().strip().split(',')))
	n = len(mi)

	#generating the ETC Matrix
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
			l.append(random.randint(0,m-1))
		pop.append(l)

	#running BFO algorithm
	#sol_bfo = BFO(pop,etc)
	#print("Solution from BFO algorithm:")
	#print(sol_bfo)
	#print("Makespan:",makespan(sol,etc))
	#print("Utilization:",utilization(sol,etc),"\n")

	#running GA algorithm
	sol_ga = GA(pop,etc,n,m)
	print("Solution from GA algorithm:")
	print(sol_ga,"\n")
	# print("Makespan:",makespan(sol,etc))
	# print("Utilization:",utilization(sol,etc),"\n")


	for i in pop:
		print(i)
	print("above is to be the pop at the end of main.\n")

if __name__=='__main__':
	main()
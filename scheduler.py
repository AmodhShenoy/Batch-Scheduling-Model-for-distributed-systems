import random

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

def GA(pop,n,m):
	pass

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
		
		
		#eliminate
		pass

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
			l.append(int(random.random()*m))
		pop.append(l)

	#running BFO algorithm
	sol_bfo = BFO(pop,etc)
	print("Solution from BFO algorithm:")
	print(sol_bfo)
	print("Makespan:",makespan(sol,etc))
	print("Utilization:",utilization(sol,etc),"\n")

	# #running GA algorithm
	# sol_ga = GA(pop,n,m)
	# print("Solution from GA algorithm:")
	# print(sol_ga)
	# print("Makespan:",makespan(sol,etc))
	# print("Utilization:",utilization(sol,etc),"\n")


	for i in pop:
		print(i)

if __name__=='__main__':
	main()
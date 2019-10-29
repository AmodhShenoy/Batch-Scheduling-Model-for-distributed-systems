import random

def makespan(sol,mips,mi,m):
	time_vec = [0 for _ in range(m)]
	for i in range(len(sol)):
		time_vec[sol[i]] += mi[i]/mips[sol[i]]
	return max(time_vec)

def utilization(sol,mips,mi,m):
	time_vec = [0 for _ in range(m)]
	for i in range(len(sol)):
		time_vec[sol[i]] += mi[i]/mips[sol[i]]
	mspan = max(time_vec)
	mpat = sum(time_vec)/m
	return mpat/mspan

def GA(pop,n,m):
	pass

def BFO(pop,n,m):
	#Setting algorithm constraints
	ned = 3 		#no of elimination steps
	nc  = 3			#no of chemotaxis steps
	ped = 0.5		#probability of bacteria elimination

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
	sol_bfo = BFO(pop,n,m)
	print("Solution from BFO algorithm:")
	print(sol_bfo)
	print("Makespan:",makespan(sol,mips,mi,m))
	print("Utilization:",utilization(sol,mips,mi,m),"\n")

	#running GA algorithm
	sol_ga = GA(pop,n,m)
	print("Solution from GA algorithm:")
	print(sol_ga)
	print("Makespan:",makespan(sol,mips,mi,m))
	print("Utilization:",utilization(sol,mips,mi,m),"\n")


	for i in pop:
		print(i)

if __name__=='__main__':
	main()
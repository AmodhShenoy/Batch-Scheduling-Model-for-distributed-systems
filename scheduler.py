import random
import math 

def get_time_vec(sol,etc):
	print(sol)
	time_vec = [0 for _ in range(len(etc))]
	for i in range(len(sol)):
		time_vec[sol[i]] += etc[sol[i]][i]
	return time_vec

def makespan(sol,etc):
	return max(get_time_vec(sol,etc))

def utilization(sol,etc):
	m = len(etc)
	time_vec = get_time_vec(sol,etc)
	mspan = max(time_vec)
	mpat = sum(time_vec)/m
	return mpat/mspan

def GA(pop,n,m):
	pass

def mkspn_sort(elem):
	return elem[-1]

def sort_pop(pop,etc):
	# print("Before sort:")
	# for i in range(len(pop)):
	# 	print(pop[i])
	for i in range(len(pop)):
		mkspn = makespan(pop[i],etc)
		pop[i].append(mkspn)
	pop.sort(key=mkspn_sort)
	for i in range(len(pop)):
		pop[i].pop()
	# print("After sort:")
	# for i in pop:
	# 	print(i)
	return pop


def BFO(pop,etc):
	#Setting algorithm constraints
	m = len(etc)
	n = len(etc[0])
	S = len(pop)
	ned = 30 		#no of elimination steps
	nc  = 30			#no of chemotaxis steps
	ped = 0.5		#probability of bacteria elimination

	for df in range(ned):
		print(df)
		#chemotaxis
		# print("Before chemotaxis")
		# for i in pop:
		# 	print(i)
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
		pop = sort_pop(pop,etc)
		print('----------------------------------')
	

		#reproduce
		pop = pop[:int(math.ceil(len(pop)/2))] + pop[:int(math.ceil(len(pop)/2))]
		for i in pop:
			print(i) 





		# step = math.ceil(len(pop)/2)
		# for i in range(step,len(pop)):
		# 	pop[i] = pop[i-step]
		# random.shuffle(pop)







	# 	print("Done reproducing")

	# 	#eliminate and replace
	# 	for _ in range(int(len(pop)*ped)):
	# 		pop.pop(int(random.random()*len(pop)))
	# 	for _ in range(int(len(pop)*ped)):
	# 		l = []
	# 		for _ in range(len(pop[0])):
	# 			l.append(int(random.random()*m))
	# 	print("Done eliminate")
	# for i in range(len(pop)):
	# 	pop[i].append(makespan(pop[i],etc))

	# pop.sort(key=mkspn_sort)
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
			l.append(int(random.random()*m))
		pop.append(l)

	#running BFO algorithm
	sol_bfo = BFO(pop,etc)
	print("Solution from BFO algorithm:")
	print(sol_bfo)
	print("Makespan:",makespan(sol_bfo,etc))
	print("Utilization:",utilization(sol_bfo,etc),"\n")

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
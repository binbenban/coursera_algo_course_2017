import random


def checkio():
	#read in each line and stores in a dictionary
	edges = get_edges()
	#print edges
	#print len(set([x[0] for x in edges] + [x[1] for x in edges])) 

	#keep doing while > 2 vertices
	while len(set([x[0] for x in edges] + [x[1] for x in edges ])) > 2:
		#pick a random edge to contract
		v1, v2, _ = edges[random.randint(0, len(edges)-1)]
		#print 'random edge:', v1, v2
		#replace all occurances of v2 with v1 in edges
		for index, (tv1, tv2, count) in enumerate(edges):
			#print 'processing:', tv1, tv2
			if tv1 == v2:
				tv1 = v1
			if tv2 == v2:
				tv2 = v1
			#print 'now becomes:', tv1, tv2
			edges[index] = (tv1, tv2, count)
			#print 'after an iteration:, edges:', edges
		#remove self loop
		edges = [x for x in edges if x[0] != x[1]]
	
	#print 'mincut...', len(edges)
	return len(edges)


def get_edges():
	edges = []
	fin = open('MinCut.txt', 'r')
	for line in fin:
		elems = [int(x) for x in line.split()]
		for x in elems[1:]:
			if (elems[0], x, 1) in edges or (x, elems[0], 1) in edges:
				pass
			else:
				edges.append((elems[0], x, 1))
	fin.close()
	return edges

def get_edges_temp():
	#return [(1,2,1),(1,3,1),(1,4,1),(2,3,1),(2,4,1),(3,4,1)]
	return [(1,2,1),(2,3,1),(3,4,1),(4,1,1)]


mincut = 10000
for t in range(0, 10):
	random.seed()
	mincut = min(mincut, checkio())
	print 'result:', mincut

print 'final:', mincut

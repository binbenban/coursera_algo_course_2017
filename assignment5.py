import heapq

def shortest_path(edges):
	#start from 1
	min_dist = {1:0}
	queue = []
	#push all 1's outgoing edges into queue
	for e in edges[1]:
		heapq.heappush(queue, (e[0], e[1], 1)) #length, v_target, v_source

	while queue:
		#get min from queue, 
		vt = heapq.heappop(queue)
		vt_new_dist = min_dist[vt[2]] + vt[0]
		if vt[1] not in min_dist or min_dist[vt[1]] > vt_new_dist:
			min_dist[vt[1]] = vt_new_dist
			#add vt[1] outgoing edges to queue
			for e in edges[vt[1]]:
				heapq.heappush(queue, (e[0], e[1], vt[1]))

	print ','.join([str(min_dist[x]) for x in [7,37,59,82,99,115,133,165,188,197] ])

def get_edges(fname):
	edges = {}	
	fin = open(fname, 'r')
	for line in fin:
		elements = line.split()
		#print elements
		v = int(elements.pop(0))
		edges[v] = []
		for an_edge in elements:
			edges[v].append((int(an_edge.split(',')[1]), int(an_edge.split(',')[0]))) 
	fin.close()
	#print edges
	return edges


edges = get_edges('dijkstraData.txt')
shortest_path(edges)
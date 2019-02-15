import simplejson

def scc_pass1(edges, all_vertices):
	#pass 1: read the edges as reversed
	visited = {}
	vertex_ordering = {}

	for v in sorted(all_vertices, reverse=True):
		if v not in visited:
			#DFS on v
			dfs(edges, v, visited, vertex_ordering)
	logme(vertex_ordering)
	logme(visited)
	logme('done pass 1')
	return vertex_ordering

def dfs(edges, v, visited, vertex_ordering):
	logme('dfs on:', v)
	if v not in visited:
		stack_to_explore = [v]
		while stack_to_explore:
			vertice = stack_to_explore[-1]
			logme('stack spit:', vertice)
			if vertice not in visited:
				visited[vertice] = 1
				logme('now visited =', visited)
				if vertice in edges:
					for other_vertex in edges.get(vertice):
						if other_vertex not in visited:
							stack_to_explore.append(other_vertex)
							logme('added to stack:', other_vertex)
			else: 
				#pop and assign ordering
				stack_to_explore.pop(-1)
				logme('removed from stack:', vertice)
				if vertice not in vertex_ordering: #
					vertex_ordering[vertice] = ordering
					global ordering
					ordering += 1
			logme('stack is now:', stack_to_explore)

def scc_pass2(edges, all_vertices):
	#now do DFS based on edges
	explored = {}
	top_10_scc_size = []

	for v in sorted(all_vertices, reverse=True):
		if v not in explored:
			scc_size = dfs2(edges, v, explored)
			top_10_scc_size.append(scc_size)
#	print 'leader values:', explored
	print sorted(top_10_scc_size, reverse=True)[:10]


def dfs2(edges, v, explored):
	scc_size = 0
#	print 'exploring', v
	if v not in explored:
		stack_to_explore = [v]
		while stack_to_explore:
			vertice = stack_to_explore.pop(-1)
			if vertice not in explored or True:
				explored[vertice] = v
				logme('vertice:', vertice, ' has leader:', v)
				scc_size += 1
				if vertice in edges:
					for other_vertex in edges[vertice]:
						if other_vertex not in explored:
							stack_to_explore.append(other_vertex)
	return scc_size

def get_edges_pass1(fname, edges, all_vertices):
	fin = open(fname, 'r')
	for line in fin:
		vto, vfrom = line.split()
		vfrom, vto = int(vfrom), int(vto)
		if vfrom not in edges:
			edges[vfrom] = [vto]
		else:
			edges[vfrom].append(vto)
		all_vertices.update([vfrom, vto])
	fin.close()
	print 'done reading file pass 1'

def get_edges_pass2(fname, edges, vertex_ordering):
	fin = open(fname, 'r')
	for line in fin:
		vfrom, vto = line.split()
		vfrom, vto = vertex_ordering[int(vfrom)], vertex_ordering[int(vto)]
		if vfrom not in edges:
			edges[vfrom] = [vto]
		else:
			edges[vfrom].append(vto)
	fin.close()
	print 'done reading file in pass 2'

def logme(*msg):
	if debug == True:
		print(msg)

debug = False
fname = 'scc.txt'
ordering = 1
leader = 1
edges = {}
all_vertices = set()

#pass 1
get_edges_pass1(fname, edges, all_vertices)
logme(edges)
print 'number of vertices:', len(all_vertices)
vertex_ordering = scc_pass1(edges, all_vertices)
logme('vertex ordering:', vertex_ordering)

#some analysis on the result
print 'size of ordering:', len(vertex_ordering)
print 'ordering key:', min(vertex_ordering.keys()), max(vertex_ordering.keys()), len(set(vertex_ordering.keys()))
print 'ordering value:', min(vertex_ordering.values()), max(vertex_ordering.values()), len(set(vertex_ordering.values()))

#pass 2
edges.clear()
get_edges_pass2(fname, edges, vertex_ordering)

scc_pass2(edges, all_vertices)



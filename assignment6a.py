def two_sum():
	nn = []

	#read file
	with open('2sum.txt', 'r') as fin:
		for line in fin:
			nn.append(int(line))

	target_vals = set()

	result = 0
	nn.sort()
	p1, p2 = 0, len(nn)-1
	while p1 < p2:
		if nn[p1] >= 0:
			break
		if nn[p2] <= 0:
			break
		if -10000 <= nn[p1] + nn[p2] <= 10000:
			if nn[p1] != nn[p2]:
				target_vals.add(nn[p1]+nn[p2])
			if nn[p1+1] < 0 and -10000 <= nn[p1+1] + nn[p2] <= 10000:
				if nn[p1+1] != nn[p2]:
					target_vals.add(nn[p1+1]+nn[p2])
			if nn[p2-1] > 0 and -10000 <= nn[p1] + nn[p2-1] <= 10000:
				if nn[p1] != nn[p2-1]:
					target_vals.add(nn[p1]+nn[p2-1])
			p1 += 1
			p2 -= 1
		else:
			if nn[p1] + nn[p2] < -10000:
				p1 += 1
			elif nn[p1] + nn[p2] > 10000:
				p2 -= 1

	print len(target_vals)




two_sum()
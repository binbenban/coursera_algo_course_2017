import heapq

def median_heaps():
	result = 0
	nums = []
	h1 = []
	h2 = []

	with open('Median.txt', 'r') as fin:
		for line in fin:
			nums.append(int(line))

	print len(set(nums))

	heapq.heappush(h1, min(nums[0:2]) * -1)
	heapq.heappush(h2, max(nums[0:2]))
	result += sum(nums[0:2])

	#print 'h1:', h1
	#print 'h2:', h2

	for x in nums[2:]:
		#print 'x:', x
		#push x to a heap
		f1, f2 = heapq.heappop(h1), heapq.heappop(h2)
		heapq.heappush(h1, f1)
		heapq.heappush(h2, f2)
		if x < f1*-1:
			heapq.heappush(h1, x*-1)
		else:
			heapq.heappush(h2, x)
		#print 'h1:', len(h1), sorted(h1, reverse=True)
		#print 'h2:', len(h2), sorted(h2)

		#check if need to re-arrange
		if len(h1)-2 >= len(h2):
			heapq.heappush(h2, -1*heapq.heappop(h1))
		elif len(h2)-2 >= len(h1):
			heapq.heappush(h1, -1*heapq.heappop(h2))
		#print 'rearranged h1:', len(h1), sorted(h1, reverse=True)
		#print 'rearranged h2:', len(h2), sorted(h2)

		#calculate median
		if len(h2) > len(h1):
			f1 = heapq.heappop(h2)
			#print 'median:', f1
			result += f1
			heapq.heappush(h2, f1)
		else:
			f1 = heapq.heappop(h1)
			#print 'median:', f1*-1
			result += f1*-1
			heapq.heappush(h1, f1)

	print result% 10000

def median_naive():
	nn = []
	result = 0
	with open('Median.txt', 'r') as fin:
		for line in fin:
			nn.append(int(line))
			nn.sort()
			#calculate
			if len(nn) % 2 == 0:
				#print 'median:', nn[len(nn)/2-1]
				result += nn[len(nn)/2-1]
			else:
				#print 'median:', nn[(len(nn)-1)/2]
				result += nn[(len(nn)-1)/2]
	print result %10000

median_heaps()
print '----'
median_naive()
#1213
num_comparisions = 0

def checkio():
	fin = open('quicksort.txt', 'r')
	nums = [int(line.replace('\n','')) for line in fin]
	fin.close()
	num_comp, nums_sorted = quicksort(nums)
	print num_comp
	print nums_sorted

def quicksort(ll):
	#base case
	#print 'procesing:', ll
	if len(ll) == 1 or len(ll) == 0:
		return 0, ll

	#recursive case	
	pivot_at = partition_last(ll)
	#print 'pivot_at:', pivot_at
	#print 'num:', len(ll)-1
	l_num, l_sorted = quicksort(ll[:pivot_at])
	r_num, r_sorted = quicksort(ll[pivot_at+1:])
	return len(ll)-1+l_num+r_num, l_sorted+r_sorted

def partition_first(ll):
	#print 'll, pivot', ll, pivot_at
	return partition_main(ll)

def partition_last(ll):
	#print 'll, pivot', ll, pivot_at
	ll[0], ll[-1] = ll[-1], ll[0]
	return partition_main(ll)

def partition_median(ll):
	#find median of three
	threesome = [(ll[0], 0), (ll[-1], len(ll)-1)]
	if len(ll) % 2 == 0:
		threesome.append((ll[max(0, len(ll)/2-1)], max(0, len(ll)/2-1)))
	else:
		threesome.append((ll[len(ll)/2], len(ll)/2))
	threesome.sort(key=lambda x: x[0])
	#print threesome
	pivot_at = threesome[1][1]
	#print pivot_at
	ll[0], ll[pivot_at] = ll[pivot_at], ll[0]
	return partition_main(ll)

def partition_main(ll):
	pivot = ll[0]
	i = 0 + 1
	for j in range(0+1, len(ll)):
		if ll[j] < pivot:
			ll[i], ll[j] = ll[j], ll[i]
			i += 1
	#put pivot element in place
	ll[0], ll[i-1] = ll[i-1], ll[0]
	return i-1

checkio()
#print partition_median([7,5,6,4])



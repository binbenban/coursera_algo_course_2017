def checkio():
	f = open('input.txt', 'r')
	ll = [int(l.replace('\n','')) for l in f]
	f.close()
	#print ll
	return num_inversion(ll)


def num_inversion(ll):
	#base case
	if len(ll) == 1:
		return 0, ll
	#recursive case
	left_inv, left_sorted = num_inversion(ll[:len(ll)/2])
	right_inv, right_sorted = num_inversion(ll[len(ll)/2:])
	#split inv based on left_sorted and right_sorted
	split_inv, merged = calc_split_inv(left_sorted, right_sorted)
	return left_inv+right_inv+split_inv, merged

def calc_split_inv(l, r):
	merged = []
	count = 0
	p1 = p2 = 0
	while p1 < len(l) and p2 < len(r):
		if l[p1] < r[p2]:
			merged.append(l[p1])
			p1 += 1
		else:
			merged.append(r[p2])
			count += len(l[p1:])
			p2 += 1
	if p1 >= len(l):
		merged += r[p2:]
	if p2 >= len(r):
		merged += l[p1:]
	return count, merged

#print calc_split_inv([6,5,4], [3,2,1])
print checkio()








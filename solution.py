def get_list():	
	n1 = raw_input()

	n1 = n1.strip().split(' ')[1:]
	l = []
	for x in n1:
		l.append(int(x))

	return l

def merge(l1, l2):
	n1 = len(l1)
	n2 = len(l2)
	s1 = 0
	s2 = 0

	l = []
	while(s1 < n1 or s2 < n2):
		if(s1 < n1 and (s2 >= n2 or l1[s1] < l2[s2])):
			l.append(l1[s1])
			s1+= 1
		else:
			l.append(l2[s2])
			s2+= 1

	return l

l1 = get_list()
l2 = get_list()
out = merge(l1, l2)

outlen = len(out)
print outlen,
for x in out:
	print x,
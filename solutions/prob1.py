def npb(n):
	c=0
	np=[]
	for i in range(2,n+1):
		if i not in np:
			c=c+1
			for j in range(i*i,n+1,i):
				np.append(j)
	return c
for l in tuple(open('../inputs/1.txt', 'r')):
	print>>open('../answers/1.txt', 'a'),npb(int(l))
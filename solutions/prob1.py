for l in tuple(open('../inputs/1.txt', 'r')):
	n=int(l)
	c=0
	np=[]
	for i in range(2,n+1):
		if i not in np:
			c=c+1
			for j in range(i*i,n+1,i):
				np.append(j)
	print>>open('../answers/1.txt', 'a'),c
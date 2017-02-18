for l in tuple(open('../inputs/1.txt', 'r')):
	n=int(l)
	c=0
	m=[]
	for i in range(2,n+1):
		if i not in m:
			c=c+1
			for j in range(i*i,n+1,i):
				m.append(j)
	print>>open('../answers/1.txt', 'a'),c
s=[w.strip() for w in open('../inputs/3.txt', 'r')]
ex=[]
def process(w):
	o=w
	p=[]
	while True:
		f=False
		for w1 in s:
			if o!=w1 and w.startswith(w1):
				f=True
				p.append(w1)
				w=w[len(w1):]
		if not f:
			break
	if len(p)>1:
		ex.append(o)
		ex.extend(p)	
for w in s:
	process(w)
for w in s:
	if w not in ex:
		print>>open('../answers/3.txt', 'a'),w
n={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19}
n1={"twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90}
n2={"hundred":100,"thousand":1000}

def test(w, c):
	for n0 in c:
		if w.startswith(n0):
			return n0
	return None

def process(w):
	r=0
	t=test(w,n1)
	if t:
		r=n1[t]
		w=w[len(t):]
		if w.startswith('-'):
			r=r+n[test(w[1:],n)]
	else:
		t=test(w,n)
		r=n[t]
		w=w[len(t):]
	for m in w.split(' '):
		t=test(m,n2)
		if t:
			r=r*n2[t]
	return r

for l in open('../inputs/6.txt', 'r'):
	i=0
	l=l.strip().replace(' and ', ', ')
	p=l.split(', ')
	for w in p:
		i=i+process(w)
	print>>open('../answers/6.txt', 'a'),i
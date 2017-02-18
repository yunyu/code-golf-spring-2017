from collections import deque
def p(t):
    t0=t.popleft()
    if t0=='+':
            return p(t)+p(t)
    elif t0=='-':
            return p(t)-p(t)
    elif t0=='*':
            return p(t)*p(t)
    elif t0=='/':
            return p(t)/p(t)
    else:
            return int(t0)

for l in open('../inputs/2.txt', 'r'):
    print>>open('../answers/2.txt', 'a'),p(deque(list(l.strip())))
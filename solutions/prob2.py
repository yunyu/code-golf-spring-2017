def run(a,b,o):
    print a,o,b
    z = 0
    if o == '+':
        z = a + b
    if o == '-':
        z = a - b
    if o == '*':
        z = a * b
    if o == '/':
        z = a / b
    return z

for n in tuple(open('../inputs/2.txt', 'r')):
    v = 0
    stack = []
    lst=[]
    for i, c in enumerate(n):
        if not c.isdigit():
            stack.append(c)
        else:
            c = ord(c) - 48
            if i+2 < len(n):
                if n[i+1].isdigit():
                    o = ord(n[i+1]) - 48
                    op = stack.pop()
                    v += run(o,c,op)
                else:
                    lst.append(c)
    stack.pop()
    print stack,lst
    while len(stack) > 0:
        v = run(lst.pop(), v, stack.pop())
    print v


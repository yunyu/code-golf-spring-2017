f = open("../answers/5.txt",'w')
def of(n):
    i=0
    while i<n:
        f.write(" ")
        i=i+1
def oe(v):
    f.write("\""+str(v)+"\">\n")
def op(v):
    f.write("<prime ")
    oe(v)
def ocp(v):
    f.write("<composite ")
    oe(v)
def cp():
    f.write("</prime>\n")
def ccp():
    f.write("</composite>\n")
def fact(v,ofs):
    hap = 0
    i = 0
    for i in range (2, v+1):
        if v % i == 0:
            of(ofs+2)
            op(i)
            of(ofs+2)
            cp()
            hap = 1
            break
    if hap == 1:
        of(ofs)
        ocp(v)
        fact(v / i, ofs + 2)
        of(ofs)
        ccp()
for n in tuple(open('../inputs/5.txt', 'r')):
    n = int(n)
    print n,":"
    fact(n, 0)
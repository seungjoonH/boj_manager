i,t=input,lambda:i().split(' is ')
p=[t()for _ in range(int(i()))]
c=[t()for _ in range(int(i()))]
g={}
for a,b in p:g[a]=b
def s(n,f):return n in g and f!=g[n]or s(g[n],f)
print('\n'.join(str(s(*a))[0]for a in c))

# #230